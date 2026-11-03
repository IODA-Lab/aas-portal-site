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
from html import escape
from itertools import groupby
from pathlib import Path
from urllib.parse import quote

SECTIONS = ("개발계획서", "가이던스", "AASX", "시뮬레이션", "참고자료")
AASX_NAME = re.compile(r"^[A-Z][A-Za-z0-9]*_v\d+\.\d+\.\d+(_\d{6}|_\d{8})?\.aasx$")

README = """# 한양대 AAS Archive

중소벤처기업부 「제조데이터 표준화 사업」의 참조모델 개발 과제에서 한양대학교가 만든 산출물을 장비별로 모은 저장소입니다.

## 과제 소개

이 사업은 중소 제조기업의 공장·기업 간 디지털 연결을 촉진하기 위해, 국제표준 AAS(Asset Administration Shell, IEC 63278)를 바탕으로 핵심 장비의 데이터 표준 참조모델과 가이던스를 개발해 제조 현장에 보급합니다. AAS는 장비 같은 제조자산의 정보를 디지털로 표현하고 관리하기 위한 표준 모델입니다.

| 항목 | 내용 |
|---|---|
| 사업명 | 2026년 제조데이터 표준화 사업 |
| 사업기간 | 2026년 5월 18일 ~ 2027년 2월 28일 |
| 수행 체계 | 주식회사 엣지크로스(주관), 한양대학교, 주식회사 엑센솔루션 |
| 개발 목표 | 장비 70종의 참조모델과 가이던스 |

## 산출물

| 산출물 | 내용 |
|---|---|
| 개발계획서 | 장비별 참조모델의 개발 범위와 구성을 정리한 문서 |
| 가이던스 | 기업이 참조모델을 활용할 수 있도록 설명한 문서 |
| AASX | AAS 파일 형식으로 만든 장비별 참조모델 |
| 시뮬레이션 | 참조모델의 활용을 보여 주는 시뮬레이션 코드, 실행 안내, 영상 링크 |
| 참고자료 | 작성에 참고한 카탈로그, 표준, 기술 문서 링크 |

## 장비별 자료

{table}

## 도구

{tools}
"""

TOOLS = {
    "semantic-id-search": "ECLASS Semantic ID 검색 도구",
    "plan2aasx": "개발계획서→AASX 변환 도구",
}


def equipment_stem(folder):
    """폴더 이름을 파일 이름용 장비명으로 바꾼다. 예: '디스크 탈수기(DISCFILTER)' -> '디스크탈수기'"""
    return re.sub(r"\([^)]*\)|[\s·･]", "", folder)


def link(label, path):
    return f'<a href="{quote(path, safe="/")}">{escape(label)}</a>'


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
    headers = ("장비군", "장비", "작성자")
    rows =["<table>", "<thead><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr></thead>", "<tbody>"]
    # 같은 장비군은 첫 칸을 rowspan으로 병합한다. Markdown 표는 병합이 안 되어 HTML 표를 쓴다.
    for group, members in groupby(sorted(equipment.items()), key=lambda kv: kv[0][0]):
        members = list(members)
        for i, ((_, name), _sections) in enumerate(members):
            cells = [link(name, f"equipment/{group}/{name}"), escape(authors.get(name) or "-")]
            first =f'<td rowspan="{len(members)}">{escape(group)}</td>' if i == 0 else ""
            rows.append("<tr>" + first + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
    rows += ["</tbody>", "</table>"]
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
