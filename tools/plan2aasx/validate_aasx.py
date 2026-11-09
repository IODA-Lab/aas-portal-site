# -*- coding: utf-8 -*-
"""Stage 3: 생성된 AASX를 다시 읽어 규칙 점검 → 리포트(md+json).

코드는 '보고'만 한다(의미를 고치지 않음). Critical 0이어야 게이트 통과.
점검 규칙(결정론적으로 확인 가능한 것):
  [C1] round-trip 재파싱(스키마) 성공
  [C2] AAS assetKind = Type
  [C3] 모든 Submodel.kind = Template
  [C4] 모든 요소 semanticId → ConceptDescription 존재(댕글링 없음, 공식 원본에도 CD가 없는 semanticId는 예외로 표시)
  [M1] 모든 IEC61360 CD에 영문 definition (AASc-3a-008)
  [M2] 측정형(*_MEASURE) CD에 단위 (AASc-3a-009)
  [M3] 표준 서브모델은 IDTA 표준 submodel semanticId 사용(자체정의 아님)
  [M4] SML 직속 원소는 id_short 없음 (AASd-120)
  [M5] 같은 부모 내 idShort 유일 (AASd-022)
  [M6] 공식 IDTA 템플릿 CD(id 일치)는 공식 배포 원본과 내용이 같음(선제검토 #68·#69)
  [M7] File 값(패키지 경로)이 가리키는 파일이 AASX 안에 실제로 있음
  [m1] 우리 공개 IRI(smart-factory.kr/ids)에 내부 equipment_id(EQ_xxx) 없음 (R-IRI-002)
  [m2] 서브모델 총 6종 이상(모델링가이드)
  [m3] 필수 File(카디널리티 One/OneToMany)에 값이 있음(선제검토 #64·#65)
최종 KOSMO/IDTA 검증기 통과는 사용자가 직접 확인(이 리포트는 사전 점검).
"""
import os, sys, json, re
from basyx.aas.adapter.aasx import AASXReader, DictSupplementaryFileContainer
from basyx.aas.model import (DictObjectStore, Submodel, ConceptDescription,
                             AssetAdministrationShell, SubmodelElementCollection as SMC,
                             SubmodelElementList as SML)
import basyx.aas.model as m

HERE = os.path.dirname(os.path.abspath(__file__))
def _res(rel):
    return os.path.join(getattr(sys, "_MEIPASS", HERE), rel)
IDTA_SEM = json.load(open(_res("idta_semantics.json"), encoding="utf-8"))["standard_submodels"]
STD_BY_IDSHORT = {info["sm_idShort"]: info for info in IDTA_SEM.values()}
STD_SEMIDS = {info["submodel_semanticId"] for info in IDTA_SEM.values()}


def _semid(el):
    s = getattr(el, "semantic_id", None)
    return s.key[0].value if (s and s.key) else None


def _iter(el):
    """el의 하위 요소 재귀 순회(자기 포함 X, 자식부터)."""
    kids = list(el.value) if isinstance(el, (SMC, SML)) else []
    for c in kids:
        yield c, el
        yield from _iter(c)


def validate(aasx_path, needs_review=None):
    R = []  # (rule, sev, ok, detail)
    def add(rule, sev, ok, detail=""):
        R.append({"rule": rule, "severity": sev, "ok": bool(ok), "detail": detail})

    # C1 round-trip
    store = DictObjectStore()
    fstore = DictSupplementaryFileContainer()
    try:
        with AASXReader(aasx_path) as r:
            r.read_into(object_store=store, file_store=fstore)
        add("C1 round-trip 재파싱", "Critical", True, f"{len(store)}객체")
    except Exception as e:
        add("C1 round-trip 재파싱", "Critical", False, f"{type(e).__name__}: {e}")
        return _finish(R, aasx_path, needs_review)

    aas_list = [o for o in store if isinstance(o, AssetAdministrationShell)]
    subs = [o for o in store if isinstance(o, Submodel)]
    cds = {o.id: o for o in store if isinstance(o, ConceptDescription)}

    # C2 assetKind=Type
    ak_ok = bool(aas_list) and all(a.asset_information.asset_kind == m.AssetKind.TYPE for a in aas_list)
    add("C2 assetKind=Type", "Critical", ak_ok,
        ", ".join(a.asset_information.asset_kind.name for a in aas_list) or "AAS 없음")

    # C3 kind=Template
    bad_kind = [s.id_short for s in subs if s.kind != m.ModellingKind.TEMPLATE]
    add("C3 Submodel.kind=Template", "Critical", not bad_kind,
        "모두 Template" if not bad_kind else f"위반: {bad_kind}")

    # C4 요소 semanticId → CD 존재
    refs = {}
    for s in subs:
        for e in s.submodel_element:
            for el, _ in [(e, None)] + list(_iter(e)):
                sid = _semid(el)
                if sid: refs.setdefault(sid, getattr(el, "id_short", None))
                if isinstance(el, SML) and getattr(el, "semantic_id_list_element", None) and el.semantic_id_list_element.key:
                    refs.setdefault(el.semantic_id_list_element.key[0].value, "listElement")
    dangling = [sid for sid in refs if sid not in cds]
    try:                                   # 공식 템플릿 원본에도 그 id의 CD가 없는 semanticId는 원본 그대로 둔 예외(선제검토 #77)
        from generate_aasx import official_no_cd
        gaps = official_no_cd()
    except Exception:
        gaps = {}
    exc = [sid for sid in dangling if sid in gaps]
    real = [sid for sid in dangling if sid not in gaps]
    add("C4 요소 semanticId→CD 존재", "Critical", not real,
        ("댕글링 없음" if not real else f"CD 없는 참조 {len(real)}: {real[:5]}")
        + (f" · 공식 원본에도 CD가 없는 semanticId {len(exc)}개는 원본 그대로(예외: "
           + ", ".join(str(gaps[s][1] or s) for s in exc) + ")" if exc else ""))

    # M1/M2 CD 정의·단위
    no_def, meas_no_unit = [], []
    for cd in cds.values():
        for eds in (cd.embedded_data_specifications or []):
            c = eds.data_specification_content
            if isinstance(c, m.DataSpecificationIEC61360):
                if not (c.definition and c.definition.get("en")):
                    no_def.append(cd.id_short)
                if c.data_type and c.data_type.name.endswith("MEASURE") and not c.unit:
                    meas_no_unit.append(cd.id_short)
    add("M1 CD 영문 definition", "Major", not no_def,
        "모두 있음" if not no_def else f"누락 {len(no_def)}: {no_def[:5]}")
    add("M2 측정형 CD 단위", "Major", not meas_no_unit,
        "모두 있음" if not meas_no_unit else f"단위없는 측정형 {len(meas_no_unit)}: {meas_no_unit[:5]}")

    # M3 표준 서브모델은 IDTA semanticId, 자체제작은 smart-factory (KOSMO 인식/제외 기준)
    m3_bad = []
    for s in subs:
        info = STD_BY_IDSHORT.get(s.id_short)
        sid = _semid(s) or ""
        if info:
            if sid != info["submodel_semanticId"]: m3_bad.append(f"{s.id_short}(표준인데 {sid[:40]})")
        elif not sid.startswith("https://www.smart-factory.kr/ids/sm/"):
            m3_bad.append(f"{s.id_short}(자체인데 {sid[:40]})")
    add("M3 서브모델 semanticId(표준=IDTA/자체=smart-factory)", "Major", not m3_bad,
        "준수" if not m3_bad else f"{m3_bad}")

    # M4 SML 원소 id_short None (basyx는 재파싱 시 'generated_submodel_list_hack_*' placeholder를 붙임 → 무시)
    m4_bad = []
    for s in subs:
        for e in s.submodel_element:
            for el, parent in _iter(e):
                ish = getattr(el, "id_short", None)
                if isinstance(parent, SML) and ish is not None and not ish.startswith("generated_submodel_list_hack_"):
                    m4_bad.append(ish)
    add("M4 SML 원소 id_short 없음", "Major", not m4_bad,
        "정상(파일상 id_short 없음)" if not m4_bad else f"id_short 가진 SML원소 {len(m4_bad)}: {m4_bad[:5]}")

    # M5 같은 부모 idShort 유일
    m5_bad = []
    def check_unique(container_name, elems):
        seen = set()
        for el in elems:
            ish = getattr(el, "id_short", None)
            if ish is None: continue
            if ish in seen: m5_bad.append(f"{container_name}/{ish}")
            seen.add(ish)
    for s in subs:
        check_unique(s.id_short, list(s.submodel_element))
        for e in s.submodel_element:
            for el, _ in [(e, None)] + list(_iter(e)):
                if isinstance(el, (SMC, SML)):
                    check_unique(getattr(el, "id_short", "?"), list(el.value))
    add("M5 같은 부모 idShort 유일", "Major", not m5_bad,
        "유일" if not m5_bad else f"중복 {len(m5_bad)}: {m5_bad[:5]}")

    # m1 우리 IRI에 EQ_ 없음
    eq_hits = []
    for s in subs:
        for uri in [s.id, _semid(s)]:
            if uri and "smart-factory.kr/ids" in uri and re.search(r"EQ_\w+", uri):
                eq_hits.append(uri)
    add("m1 공개IRI에 equipment_id 없음", "Minor", not eq_hits,
        "정상" if not eq_hits else f"EQ_ 포함: {eq_hits[:3]}")

    # m2 서브모델 6종 이상
    add("m2 서브모델 6종 이상", "Minor", len(subs) >= 6, f"{len(subs)}종")

    # M6 공식 템플릿 CD = 공식 배포 원본(내용 동일)
    try:
        from generate_aasx import _load_official_cds
        from basyx.aas.adapter.json import AASToJsonEncoder
        off = _load_official_cds()
        def _norm(x):
            # valueList는 메타모델상 집합(순서 무의미)이라 basyx가 순서를 보존하지 않는다 → 정렬해 비교
            if isinstance(x, dict):
                return {k: (sorted((_norm(i) for i in v), key=lambda i: json.dumps(i, sort_keys=True))
                            if k == "valueReferencePairs" and isinstance(v, list) else _norm(v))
                        for k, v in x.items()}
            if isinstance(x, list):
                return [_norm(i) for i in x]
            return x
        def js(o):
            return _norm(json.loads(json.dumps(o, cls=AASToJsonEncoder)))
        hit, diff = 0, []
        for cid, cd in cds.items():
            if cid in off:
                hit += 1
                if js(cd) != js(off[cid][0]):
                    diff.append(cd.id_short or cid)
        add("M6 공식 템플릿 CD 원본 일치", "Major", not diff,
            f"공식 CD {hit}개 원본과 같음" if not diff else f"원본과 다른 공식 CD {len(diff)}: {diff[:5]}")
    except Exception as e:
        add("M6 공식 템플릿 CD 원본 일치", "Major", False, f"비교 실패: {type(e).__name__}: {e}")

    # M7 File 경로 → 패키지 실파일 / m3 필수 File 값
    def card(el):
        for q in (getattr(el, "qualifier", None) or []):
            if "ardinal" in (q.type or ""):
                return str(q.value or "")
        return ""
    files_ok, files_bad, req_empty = 0, [], []
    for s in subs:
        for e in s.submodel_element:
            for el, _ in [(e, None)] + list(_iter(e)):
                if isinstance(el, m.File):
                    if el.value:
                        try:
                            present = el.value in fstore
                        except Exception:
                            present = False
                        if present: files_ok += 1
                        else: files_bad.append(el.value)
                    elif card(el) in ("One", "OneToMany", ""):
                        ish = el.id_short if (el.id_short and not el.id_short.startswith("generated_submodel_list_hack")) else "[0]"
                        req_empty.append(f"{s.id_short}/{ish}")
    add("M7 File 경로 → 패키지 실파일", "Major", not files_bad,
        f"참조 파일 {files_ok}개 모두 있음" if not files_bad else f"없는 파일 {files_bad[:5]}")
    add("m3 필수 File 값", "Minor", not req_empty,
        "필수 File 모두 파일 연결" if not req_empty else f"파일 없는 필수 File {len(req_empty)}: {req_empty[:5]}")

    return _finish(R, aasx_path, needs_review, store)


def _finish(R, aasx_path, needs_review, store=None):
    crit = sum(1 for x in R if x["severity"] == "Critical" and not x["ok"])
    maj = sum(1 for x in R if x["severity"] == "Major" and not x["ok"])
    mino = sum(1 for x in R if x["severity"] == "Minor" and not x["ok"])
    gate = "PASS" if crit == 0 else "FAIL"
    nsub = sum(1 for o in store if isinstance(o, Submodel)) if store else 0
    ncd = sum(1 for o in store if isinstance(o, ConceptDescription)) if store else 0
    summary = {"gate": gate, "critical": crit, "major": maj, "minor": mino,
               "submodels": nsub, "concept_descriptions": ncd,
               "needs_review": needs_review or [], "checks": R, "aasx": aasx_path}

    base = os.path.splitext(aasx_path)[0]
    with open(base + "_validation.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    L = []
    L.append(f"# AASX 사전 검증 리포트\n")
    L.append(f"- 대상: `{os.path.basename(aasx_path)}`")
    L.append(f"- 서브모델 {nsub}종 · ConceptDescription {ncd}개")
    L.append(f"- **게이트: {gate}** (Critical {crit} · Major {maj} · Minor {mino})")
    L.append(f"- ※ 이 리포트는 사전 점검입니다. 최종 KOSMO/IDTA 검증기 통과는 검증기로 직접 확인하세요.\n")
    L.append("| 규칙 | 심각도 | 결과 | 상세 |")
    L.append("|---|---|---|---|")
    for x in R:
        L.append(f"| {x['rule']} | {x['severity']} | {'✅ PASS' if x['ok'] else '❌ FAIL'} | {x['detail']} |")
    if needs_review:
        L.append(f"\n## NEEDS_REVIEW ({len(needs_review)}) — 사람 검토 필요(계획서를 고친 뒤 다시 변환)")
        for r in needs_review:
            L.append(f"- {r}")
    with open(base + "_validation.md", "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    return summary


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("사용: python validate_aasx.py <장비.aasx> [needs_review.json]")
    aasx = sys.argv[1]
    nr = None
    if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
        nr = json.load(open(sys.argv[2], encoding="utf-8"))
    s = validate(aasx, needs_review=nr)
    print(f"게이트: {s['gate']} | Critical {s['critical']} · Major {s['major']} · Minor {s['minor']}")
    for x in s["checks"]:
        print(f"  {'PASS' if x['ok'] else 'FAIL':4} [{x['severity'][:4]}] {x['rule']} - {x['detail'][:60]}")
    print("리포트:", os.path.splitext(aasx)[0] + "_validation.md")
