# -*- coding: utf-8 -*-
"""plan2aasx 원커맨드 오케스트레이터: 장비개발계획서 → AASX + 검증 리포트.

    계획서(.hwp/.hwpx) ─[변환]→ .hwpx ─[parse]→ 매핑표(JSON, 읽어 낸 내용 확인용)
                       ─[generate]→ AASX(.aasx/.json/.xml) ─[validate]→ 리포트(md/json)

사용:
    python run.py <계획서.hwp|.hwpx> [출력폴더]
    (인자 없이 실행하면 파일 선택 창이 뜸 — .exe 배포용)

.hwp 입력은 한컴 오피스가 설치된 Windows에서 PowerShell COM으로 .hwpx 변환.
전부 코드(에이전트 없음). basyx 필요.
"""
import os, sys, json, subprocess, tempfile, re, time, datetime, traceback

try:  # 콘솔 인코딩 무관하게 한글/기호 출력 안전
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import parse_plan
import generate_aasx
import validate_aasx


def hwp_to_hwpx(hwp_path, out_hwpx):
    """한컴 COM(PowerShell)으로 HWP→HWPX 변환. 성공 시 out_hwpx 경로 반환."""
    ps = f"""
$ErrorActionPreference='Stop'
$h=New-Object -ComObject HWPFrame.HwpObject
$h.RegisterModule("FilePathCheckDLL","FilePathCheckerModule") | Out-Null
$h.Open('{hwp_path}','HWP','forceopen:true') | Out-Null
$h.SaveAs('{out_hwpx}','HWPX','') | Out-Null
$h.Clear(1); $h.Quit()
Write-Host 'OK'
"""
    tf = tempfile.NamedTemporaryFile("w", suffix=".ps1", delete=False, encoding="utf-8-sig")
    tf.write(ps); tf.close()
    # GUI(windowed) 실행 시 파워셸 콘솔 창이 깜빡이지 않도록 숨김.
    _flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", tf.name],
                           capture_output=True, text=True, timeout=180, creationflags=_flags)
    finally:
        try: os.remove(tf.name)
        except OSError: pass
    if not os.path.exists(out_hwpx):
        raise RuntimeError("HWP→HWPX 변환 실패(한컴 오피스 설치 필요). "
                           + (r.stderr or r.stdout or "")[:300])
    return out_hwpx


def find_plan_image(plan_path):
    """계획서 옆에서 장비 대표 이미지를 결정론적으로 탐색.
    관례 파일명 우선순위: 장비이미지.* > productimage.* > <계획서이름>.* (png/jpg/jpeg).
    계획서 안의 그림은 다이어그램/로고와 구분이 어려워 자동 추출하지 않는다(엉뚱한 그림 방지)."""
    d = os.path.dirname(plan_path)
    stem = os.path.splitext(os.path.basename(plan_path))[0]
    names = ["장비이미지", "productimage", "product_image", stem]
    for base in names:
        for ext in (".png", ".jpg", ".jpeg"):
            p = os.path.join(d, base + ext)
            if os.path.exists(p):
                return p
    return None


# 계획서 옆에 첨부가 없을 때 넣는 공통 예시 파일(templates/defaults, 장비 이름 없이 '예시'라고 적힌 파일).
# 2026-10-28 사용자 결정: 계획서에 표가 없는 공통 서브모델(Nameplate, HandoverDocumentation)은 기본으로 채운다.
# 만드는 법: deliverable_builder/make_attachments.py <폴더> --generic
DEFAULT_ATTACHMENTS = {"marking": "marking_example.png", "handover": "operation_manual_example.pdf"}


def find_plan_attachments(plan_path, use_defaults=True):
    """계획서 옆의 첨부 파일을 관례 파일명으로 탐색. 계획서 옆 파일이 항상 우선이다.
      marking : Nameplate 인증 마킹 이미지(MarkingFile)      — 인증마크.*, marking_example.*, markingfile.*
      handover: Handover 문서 파일(DigitalFiles 첫 파일)     — 운영매뉴얼.*, operation_manual_example.*, handover_document.*
    없으면 공통 예시 파일(DEFAULT_ATTACHMENTS)을 쓰고 그 역할을 out["defaults"]에 적는다(use_defaults=False면 None)."""
    d = os.path.dirname(plan_path)
    roles = {
        "marking": (["인증마크", "인증마크_예시", "marking_example", "markingfile"], (".png", ".jpg", ".jpeg", ".svg")),
        "handover": (["운영매뉴얼", "운영매뉴얼_예시", "operation_manual_example", "handover_document"], (".pdf", ".html", ".htm")),
    }
    out = {"defaults": []}
    for role, (bases, exts) in roles.items():
        out[role] = None
        for base in bases:
            hit = next((os.path.join(d, base + e) for e in exts if os.path.exists(os.path.join(d, base + e))), None)
            if hit:
                out[role] = hit
                break
        if out[role] is None and use_defaults:
            p = generate_aasx._res(os.path.join("templates", "defaults", DEFAULT_ATTACHMENTS[role]))
            if os.path.exists(p):
                out[role] = p
                out["defaults"].append(role)
    return out


TOOL_VERSION = "1.1"

def _safe(s):
    """파일명 안전화(금지문자 제거, 공백→_)."""
    return re.sub(r'[\\/:*?"<>|\r\n\t]+', '', str(s or '')).replace(' ', '_').strip('_')

def write_run_log(out_dir, log):
    """실행 로그를 '<장비명>_<담당자>_log.json' 으로 출력 폴더에 저장(성공·실패 공통, 수집용)."""
    eq = log.get("equipment", {})
    name = _safe(eq.get("name_ko") or eq.get("aas_name") or "Equipment")
    mgr = _safe(eq.get("manager") or "담당자미상")
    path = os.path.join(out_dir, f"{name}_{mgr}_log.json")
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(log, f, ensure_ascii=False, indent=2)
        return path
    except Exception:
        return None


def run(plan_path, out_dir=None, thumbnail=None, product_image=None, verbose=True):
    plan_path = os.path.abspath(plan_path)
    if not os.path.exists(plan_path):
        raise FileNotFoundError(plan_path)
    stem = os.path.splitext(os.path.basename(plan_path))[0]
    out_dir = os.path.abspath(out_dir or os.path.join(os.path.dirname(plan_path), stem + "_AAS"))
    os.makedirs(out_dir, exist_ok=True)
    ext = plan_path.lower().rsplit(".", 1)[-1]

    # 실행 로그(수집용) — 성공/실패 모두 기록
    log = {
        "tool": "plan2aasx", "tool_version": TOOL_VERSION,
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "input_plan": os.path.basename(plan_path),
        "output_folder": out_dir,
        "equipment": {"name_ko": "", "name_en": "", "manager": "", "aas_name": ""},
        "status": "error", "gate": None, "critical": None, "major": None, "minor": None,
        "submodels": {"count": None, "list": []}, "concept_descriptions": None,
        "needs_review": {"count": 0, "items": []}, "error": None, "duration_sec": None,
    }
    t0 = time.time()
    try:
        # 장비 대표 이미지: 명시 인자 우선, 없으면 계획서 옆 관례 파일 자동 탐색.
        if product_image is None:
            product_image = find_plan_image(plan_path)
        if verbose:
            print(f"      장비 이미지: {product_image if product_image else '(없음 - 계획서 옆에 장비이미지.png 두면 자동 포함)'}")
        attachments = find_plan_attachments(plan_path)
        if verbose:
            def _att(role, name, slot):
                p = attachments[role]
                if role in attachments["defaults"]:
                    return f"(기본 예시 파일 {os.path.basename(p)} 사용. 실제 파일이 있으면 계획서 옆에 {name}로 두세요)"
                return p or f"(없음 - 계획서 옆에 {name} 두면 {slot}에 연결)"
            print(f"      인증 마킹 이미지: {_att('marking', '인증마크.png', 'MarkingFile')}")
            print(f"      인계 문서 파일: {_att('handover', '운영매뉴얼.pdf', 'DigitalFiles')}")

        # 1) HWPX 확보
        if ext == "hwpx":
            hwpx = plan_path
        elif ext == "hwp":
            if verbose: print("[1/4] HWP → HWPX 변환(한컴)...")
            hwpx = hwp_to_hwpx(plan_path, os.path.join(out_dir, stem + ".hwpx"))
        else:
            raise ValueError("입력은 .hwp 또는 .hwpx 여야 합니다: " + plan_path)

        # 2) 파싱 → 매핑표(읽어 낸 내용 확인용)
        if verbose: print("[2/4] 계획서 파싱 → 매핑표...")
        mapping = parse_plan.parse_plan_hwpx(hwpx)
        if not mapping.get("submodels"):
            raise ValueError("계획서에서 서브모델 내용을 하나도 찾지 못했습니다. 장비개발계획서 양식이 맞는지 확인하세요.")
        eq = mapping.get("equipment", {})
        log["equipment"].update({"name_ko": eq.get("name_ko", ""), "name_en": eq.get("name_en", ""),
                                 "manager": eq.get("manager", ""), "aas_name": mapping.get("aas_name", "")})
        map_path = os.path.join(out_dir, "mapping.json")
        json.dump(mapping, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        if verbose:
            print(f"      장비: {eq.get('name_ko','')} | 담당자: {eq.get('manager','')} | 서브모델 {len(mapping['submodels'])}종")
            print(f"      매핑표(계획서에서 읽어 낸 내용, 확인용): {map_path}")

        # 3) 생성 (장비 이미지가 있으면 썸네일·ProductImages에 임베드)
        if verbose: print("[3/4] AASX 생성...")
        aasx, gen = generate_aasx.generate(mapping, out_dir, thumbnail=thumbnail or product_image,
                                           product_image=product_image, attachments=attachments,
                                           verbose=verbose)
        if gen.get("aas_name"): log["equipment"]["aas_name"] = gen["aas_name"]
        log["submodels"] = {"count": gen.get("submodels"), "list": gen.get("submodel_list", [])}
        log["concept_descriptions"] = gen.get("cds")
        nr = gen.get("needs_review") or []
        log["needs_review"] = {"count": len(nr), "items": nr}

        # 4) 검증
        if verbose: print("[4/4] 검증 리포트...")
        summary = validate_aasx.validate(aasx, needs_review=gen.get("needs_review"))
        log.update({"status": "success", "gate": summary["gate"], "critical": summary["critical"],
                    "major": summary["major"], "minor": summary["minor"]})
        if summary.get("concept_descriptions") is not None:
            log["concept_descriptions"] = summary["concept_descriptions"]

        log["duration_sec"] = round(time.time() - t0, 2)
        log_path = write_run_log(out_dir, log)

        if verbose:
            print("\n" + "=" * 60)
            print(f"  게이트: {summary['gate']}  (Critical {summary['critical']} · "
                  f"Major {summary['major']} · Minor {summary['minor']})")
            print(f"  AASX:   {aasx}")
            print(f"  리포트: {os.path.splitext(aasx)[0]}_validation.md")
            if log_path: print(f"  실행로그: {log_path}")
            if summary.get("needs_review"):
                print(f"  NEEDS_REVIEW(검토 필요) {len(summary['needs_review'])}건: 계획서를 고친 뒤 다시 변환하세요")
            print("  ※ 최종 KOSMO/IDTA 검증기 통과는 검증기로 직접 확인하세요.")
            print("=" * 60)
        return summary
    except Exception as e:
        # 실패도 로그로 남겨 수집(어느 장비에서 왜 실패했는지).
        log["status"] = "error"
        log["error"] = {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()}
        log["duration_sec"] = round(time.time() - t0, 2)
        lp = write_run_log(out_dir, log)
        if verbose and lp:
            print(f"  실행로그(실패 기록): {lp}")
        raise


def _pick_file():
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
        root = tk.Tk(); root.withdraw()
        p = filedialog.askopenfilename(title="장비개발계획서 선택",
                                       filetypes=[("한글 문서", "*.hwp *.hwpx"), ("모든 파일", "*.*")])
        return p, (root, messagebox, filedialog)
    except Exception:
        return None, None


def main():
    if len(sys.argv) > 1:
        plan = sys.argv[1]
        out = sys.argv[2] if len(sys.argv) > 2 else None
        img = sys.argv[3] if len(sys.argv) > 3 else None      # 선택: 장비 이미지 경로
        run(plan, out, product_image=img)
    else:
        plan, ui = _pick_file()
        if not plan:
            print("계획서 파일을 지정하세요:  run.py <계획서.hwp|.hwpx> [출력폴더] [장비이미지]")
            return
        img = None
        if ui:
            _, messagebox, filedialog = ui
            # 장비 대표 이미지 선택(선택 사항). 취소하면 계획서 옆 관례 파일 자동 탐색.
            img = filedialog.askopenfilename(
                title="장비 대표 이미지 선택 (없으면 취소)",
                filetypes=[("이미지", "*.png *.jpg *.jpeg"), ("모든 파일", "*.*")]) or None
        try:
            s = run(plan, None, product_image=img)
            if ui:
                _, messagebox, _ = ui
                messagebox.showinfo("plan2aasx 완료",
                    f"게이트: {s['gate']}\nCritical {s['critical']} · Major {s['major']} · Minor {s['minor']}\n\n"
                    f"출력 폴더를 확인하세요.")
        except Exception as e:
            if ui:
                _, messagebox, _ = ui
                messagebox.showerror("오류", str(e))
            else:
                print("오류:", e)


if __name__ == "__main__":
    main()
