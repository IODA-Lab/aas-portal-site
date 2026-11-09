# -*- coding: utf-8 -*-
"""plan2aasx GUI - 장비개발계획서 -> 표준 AASX 자동 생성/검증(그래픽 인터페이스).

입력: 계획서(.hwp/.hwpx) / 장비 이미지(선택) / 출력 폴더(선택)
실행: [변환 시작] -> 진행 로그 실시간 표시 -> 게이트 결과(PASS/FAIL) 표시.
엔진은 run.py(파싱->생성->검증)를 그대로 사용한다.
"""
import os
import sys
import queue
import threading
import traceback

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run as engine


class _QueueWriter:
    """print() 출력을 큐로 보내는 stdout 대체(스레드->UI 전달용)."""
    def __init__(self, q):
        self.q = q
    def write(self, s):
        if s:
            self.q.put(("log", s))
    def flush(self):
        pass


class App:
    def __init__(self, root):
        self.root = root
        self.q = queue.Queue()
        self.running = False
        root.title("plan2aasx - 장비개발계획서 → AASX 변환/검증")
        root.geometry("820x600")
        root.minsize(720, 520)

        pad = {"padx": 8, "pady": 5}
        frm = ttk.Frame(root, padding=12)
        frm.pack(fill="both", expand=True)
        frm.columnconfigure(1, weight=1)

        # 1) 계획서
        ttk.Label(frm, text="장비개발계획서 (.hwp/.hwpx)").grid(row=0, column=0, sticky="w", **pad)
        self.plan_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.plan_var).grid(row=0, column=1, sticky="ew", **pad)
        ttk.Button(frm, text="찾아보기", command=self.browse_plan).grid(row=0, column=2, **pad)

        # 2) 장비 이미지(선택)
        ttk.Label(frm, text="장비 이미지 (선택)").grid(row=1, column=0, sticky="w", **pad)
        self.img_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.img_var).grid(row=1, column=1, sticky="ew", **pad)
        ttk.Button(frm, text="찾아보기", command=self.browse_img).grid(row=1, column=2, **pad)

        # 3) 출력 폴더(선택)
        ttk.Label(frm, text="출력 폴더 (선택)").grid(row=2, column=0, sticky="w", **pad)
        self.out_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.out_var).grid(row=2, column=1, sticky="ew", **pad)
        ttk.Button(frm, text="찾아보기", command=self.browse_out).grid(row=2, column=2, **pad)

        ttk.Label(frm, text="※ 이미지·출력폴더를 비우면: 이미지는 계획서 옆에서 자동 탐색, 출력은 계획서 옆 \"<이름>_AAS\" 폴더.",
                  foreground="#666").grid(row=3, column=0, columnspan=3, sticky="w", padx=8)

        # 실행 버튼 + 상태
        bar = ttk.Frame(frm)
        bar.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(10, 4))
        bar.columnconfigure(1, weight=1)
        self.run_btn = ttk.Button(bar, text="변환 시작", command=self.start)
        self.run_btn.grid(row=0, column=0, padx=(8, 12))
        self.status_var = tk.StringVar(value="대기 중")
        self.status_lbl = tk.Label(bar, textvariable=self.status_var, font=("Segoe UI", 11, "bold"),
                                   anchor="w")
        self.status_lbl.grid(row=0, column=1, sticky="ew")
        self.open_btn = ttk.Button(bar, text="출력 폴더 열기", command=self.open_out, state="disabled")
        self.open_btn.grid(row=0, column=2, padx=8)

        # 진행 로그
        ttk.Label(frm, text="변환 진행 로그").grid(row=5, column=0, sticky="w", padx=8)
        self.log = scrolledtext.ScrolledText(frm, height=18, wrap="word",
                                             font=("Consolas", 10), state="disabled",
                                             background="#111", foreground="#e0e0e0")
        self.log.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=8, pady=(2, 8))
        frm.rowconfigure(6, weight=1)
        self.log.tag_config("ok", foreground="#5ee08a")
        self.log.tag_config("err", foreground="#ff6b6b")
        self.log.tag_config("info", foreground="#7db4ff")

        self._last_out = None
        # 명령줄 인자로 계획서를 받으면 미리 채움
        if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
            self.plan_var.set(sys.argv[1])

        self.root.after(80, self.poll)

    # ---- 파일 선택 ----
    def browse_plan(self):
        p = filedialog.askopenfilename(title="장비개발계획서 선택",
                                       filetypes=[("한글 문서", "*.hwp *.hwpx"), ("모든 파일", "*.*")])
        if p:
            self.plan_var.set(p)

    def browse_img(self):
        p = filedialog.askopenfilename(title="장비 이미지 선택",
                                       filetypes=[("이미지", "*.png *.jpg *.jpeg"), ("모든 파일", "*.*")])
        if p:
            self.img_var.set(p)

    def browse_out(self):
        p = filedialog.askdirectory(title="출력 폴더 선택")
        if p:
            self.out_var.set(p)

    def open_out(self):
        if self._last_out and os.path.isdir(self._last_out):
            os.startfile(self._last_out)

    # ---- 로그 ----
    def _append(self, text, tag=None):
        self.log.configure(state="normal")
        self.log.insert("end", text, tag or ())
        self.log.see("end")
        self.log.configure(state="disabled")

    def poll(self):
        try:
            while True:
                kind, payload = self.q.get_nowait()
                if kind == "log":
                    self._append(payload)
                elif kind == "done":
                    self._on_done(payload)
                elif kind == "error":
                    self._append("\n[오류] " + payload + "\n", "err")
                    self.status_var.set("오류 발생 - 로그를 확인하세요")
                    self.status_lbl.configure(fg="#c0392b")
                    self._finish()
        except queue.Empty:
            pass
        self.root.after(80, self.poll)

    # ---- 실행 ----
    def start(self):
        if self.running:
            return
        plan = self.plan_var.get().strip().strip('"')
        if not plan or not os.path.exists(plan):
            self.status_var.set("계획서 파일을 먼저 선택하세요")
            self.status_lbl.configure(fg="#c0392b")
            return
        img = self.img_var.get().strip().strip('"') or None
        out = self.out_var.get().strip().strip('"') or None
        self.running = True
        self.run_btn.configure(state="disabled")
        self.open_btn.configure(state="disabled")
        self.status_var.set("변환 중...")
        self.status_lbl.configure(fg="#2c3e50")
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
        self._append("변환을 시작합니다...\n\n", "info")
        t = threading.Thread(target=self._worker, args=(plan, out, img), daemon=True)
        t.start()

    def _worker(self, plan, out, img):
        old_out, old_err = sys.stdout, sys.stderr
        w = _QueueWriter(self.q)
        sys.stdout = w
        sys.stderr = w
        try:
            summary = engine.run(plan, out, product_image=img, verbose=True)
            # 출력 폴더 계산(엔진과 동일 규칙)
            stem = os.path.splitext(os.path.basename(plan))[0]
            out_dir = os.path.abspath(out or os.path.join(os.path.dirname(os.path.abspath(plan)), stem + "_AAS"))
            self.q.put(("done", {"summary": summary, "out_dir": out_dir}))
        except Exception as e:
            self.q.put(("log", "\n" + traceback.format_exc()))
            self.q.put(("error", str(e)))
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def _on_done(self, payload):
        s = payload["summary"]
        self._last_out = payload["out_dir"]
        gate = s.get("gate", "?")
        crit = s.get("critical", "?"); maj = s.get("major", "?"); mnr = s.get("minor", "?")
        self._append("\n" + "=" * 60 + "\n", "info")
        if str(gate).upper() == "PASS":
            self._append(f"완료 - 게이트: PASS  (Critical {crit} · Major {maj} · Minor {mnr})\n", "ok")
            self.status_var.set(f"완료 · PASS (Critical {crit} · Major {maj} · Minor {mnr})")
            self.status_lbl.configure(fg="#1e8e4e")
        else:
            self._append(f"완료 - 게이트: {gate}  (Critical {crit} · Major {maj} · Minor {mnr})\n", "err")
            self.status_var.set(f"완료 · {gate} (Critical {crit})")
            self.status_lbl.configure(fg="#c0392b")
        nr = s.get("needs_review")
        if nr:
            self._append(f"NEEDS_REVIEW(검토 필요) {len(nr)}건: 계획서를 고친 뒤 다시 변환하세요(목록은 위 로그와 검증 리포트에 있음)\n", "info")
        self._append(f"출력 폴더: {self._last_out}\n", "info")
        self._append("※ 최종 KOSMO/IDTA 검증기 통과는 검증기로 직접 확인하세요.\n", "info")
        self.open_btn.configure(state="normal")
        self._finish()

    def _finish(self):
        self.running = False
        self.run_btn.configure(state="normal")


def main():
    root = tk.Tk()
    try:
        root.call("tk", "scaling", 1.2)
    except Exception:
        pass
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
