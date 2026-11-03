#!/usr/bin/env python3
"""저장소 파일 목록으로 최상위 README.md의 표를 다시 만든다.

사용법: python tools/archive-index/build_index.py [--check]
--check 는 README를 고치지 않고 폴더 구조와 파일명 규칙 위반만 출력한다.
"""
import csv
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

SECTIONS = ("개발계획서", "가이던스", "AASX", "시뮬레이션", "참고자료")
AASX_NAME = re.compile(r"^[A-Z][A-Za-z0-9]*_v\d+\.\d+\.\d+(_\d{6}|_\d{8})?\.aasx$")

README = """# 한양대 AAS Archive

산업 장비 70종의 AAS 참조모델과 개발계획서, 가이던스, 시뮬레이션, 참고자료를 장비별로 모은 저장소입니다.

## 폴더 구성

```text
equipment/<장비군>/<장비>/
  개발계획서/   참조모델 개발계획서
  가이던스/     AAS 활용 가이던스
  AASX/        AASX 모델과 UML 원본
  시뮬레이션/   코드, 실행 안내, 영상 링크
  참고자료/     카탈로그, 매뉴얼, 참고 링크
tools/          여러 장비에 함께 쓰는 도구
```

파일은 장비 폴더에만 저장합니다. 아래 표는 파일을 저장하지 않고 링크만 연결합니다.

## 장비별 자료

{table}

## 도구

{tools}

## 자료 추가

1. 저장소를 클론하고 자기 장비 폴더의 해당 폴더에 파일을 넣습니다.
2. 파일 이름은 `<장비명>_개발계획서`, `<장비명>_가이던스` 형식으로 맞춥니다. 장비명은 폴더 이름에서 공백, 가운뎃점, 괄호를 뺀 것입니다.
3. 커밋하고 올립니다. 이 표는 자동으로 갱신되므로 README를 고치지 않습니다.

zip과 영상 파일은 올리지 않습니다. 코드는 풀어서 올리고, 영상은 YouTube 링크를 `시뮬레이션/링크.md`에 적습니다. 검토 기록은 올리지 않습니다.
"""

TOOLS = {
    "semantic-id-search": "ECLASS Semantic ID 검색 도구",
    "plan2aasx": "개발계획서→AASX 변환 도구",
}


def equipment_stem(folder):
    """폴더 이름을 파일 이름용 장비명으로 바꾼다. 예: '디스크 탈수기(DISCFILTER)' -> '디스크탈수기'"""
    return re.sub(r"\([^)]*\)|[\s·･]", "", folder)


def link(label, path):
    return f"[{label}]({quote(path, safe='/')})"


def file_links(files):
    """파일 링크를 확장자 이름으로 만든다. 같은 확장자가 여럿이면 번호를 붙인다."""
    by_ext = defaultdict(list)
    for f in sorted(files):
        by_ext[Path(f).suffix.lstrip(".").upper()].append(f)
    out = []
    for ext, items in by_ext.items():
        for i, f in enumerate(items, 1):
            out.append(link(ext if len(items) == 1 else f"{ext} {i}", f))
    return " · ".join(out) or "-"


def load_equipment(paths):
    equipment = defaultdict(lambda: defaultdict(list))
    for p in paths:
        parts = p.split("/")
        if parts[0] == "equipment" and len(parts) >= 5 and parts[3] in SECTIONS:
            equipment[(parts[1], parts[2])][parts[3]].append(p)
    return equipment


def real_files(files):
    return [f for f in files if not f.endswith(".gitkeep")]


def render(paths, authors):
    equipment = load_equipment(paths)
    rows = ["| 장비군 | 장비 | 작성자 | 개발계획서 | 가이던스 | AASX | 시뮬레이션 | 참고자료 |", "|---|---|---|---|---|---|---|---|"]
    for (group, name), sections in sorted(equipment.items()):
        root = f"equipment/{group}/{name}"
        aasx = [f for f in real_files(sections["AASX"]) if f.endswith(".aasx")]
        rows.append("| " + " | ".join([
            group,
            link(name, root),
            authors.get(name) or "-",
            file_links(real_files(sections["개발계획서"])),
            file_links(real_files(sections["가이던스"])),
            file_links(aasx),
            link("폴더", f"{root}/시뮬레이션") if real_files(sections["시뮬레이션"]) else "-",
            link("폴더", f"{root}/참고자료") if real_files(sections["참고자료"]) else "-",
        ]) + " |")
    names = sorted({p.split("/")[1] for p in paths if p.startswith("tools/") and p.count("/") >= 2} - {"archive-index"})
    tools = ["| 도구 | 설명 |", "|---|---|"] + [f"| {link(n, 'tools/' + n)} | {TOOLS.get(n, '')} |" for n in names]
    return README.format(table="\n".join(rows), tools="\n".join(tools))


def check(paths):
    problems = []
    tops = {p.split("/")[0] for p in paths}
    problems += [f"최상위에 허용되지 않은 항목: {t}" for t in sorted(tops - {"README.md", "equipment", "tools", ".github", ".gitattributes", ".gitignore"})]
    for (group, name), sections in sorted(load_equipment(paths).items()):
        stem = equipment_stem(name)
        for s in SECTIONS:
            if not sections[s]:
                problems.append(f"{name}: {s} 폴더 없음")
        for section, word in (("개발계획서", "개발계획서"), ("가이던스", "가이던스")):
            for f in real_files(sections[section]):
                if Path(f).stem != f"{stem}_{word}":
                    problems.append(f"{name}: 파일명 규칙과 다름: {Path(f).name}")
        for f in real_files(sections["AASX"]):
            if f.endswith(".aasx") and not AASX_NAME.match(Path(f).name):
                problems.append(f"{name}: AASX 파일명 형식 확인: {Path(f).name}")
        for f in real_files(sum(sections.values(), [])):
            if f.lower().endswith((".zip", ".mp4")):
                problems.append(f"{name}: zip·영상 파일: {Path(f).name}")
    return problems


def main():
    root = Path(__file__).resolve().parents[2]
    out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True).stdout
    paths = out.decode("utf-8").split("\0")[:-1]
    if "--check" in sys.argv:
        problems = check(paths)
        sys.stdout.reconfigure(encoding="utf-8")
        print("\n".join(problems) or "문제 없음")
        return 1 if problems else 0
    with open(Path(__file__).with_name("authors.csv"), encoding="utf-8-sig", newline="") as f:
        authors = {r["장비"]: r["작성자"] for r in csv.DictReader(f)}
    (root / "README.md").write_text(render(paths, authors), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
