#!/usr/bin/env python3
"""AASX를 읽어 장비 폴더의 README.md(장비 페이지)를 만든다.

사용법: python tools/archive-index/build_pages.py 장비이름 [장비이름 ...]
"""
import csv
import re
import subprocess
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from html import escape
from pathlib import Path
from urllib.parse import quote

from build_index import inquiry_link

HERE = Path(__file__).parent
ROOT = HERE.parents[1]
SECTIONS = ("개발계획서", "가이던스", "AASX")
PURPOSE = {
    "Nameplate": "장비를 식별하는 명판 정보",
    "DigitalNameplate": "장비를 식별하는 명판 정보",
    "HandoverDocumentation": "납품 시 함께 전달하는 문서 목록",
    "TechnicalData": "제조사가 제시하는 기술 사양",
    "OperationalData": "운전 중 변하는 장비 상태 값",
    "TimeSeries": "상태 값의 시간별 기록",
    "ProcessParameters": "제품·공정별 설정값",
    "PredictiveMaintenance": "예지정비 모델과 결과",
    "FunctionalSafety": "기능 안전 정보",
    "CarbonFootprint": "탄소 배출 정보",
}
VALUE_TYPE = {
    "string": "문자열", "anyURI": "URI", "boolean": "참/거짓", "date": "날짜", "dateTime": "일시", "time": "시각",
    "duration": "기간", "double": "실수", "float": "실수", "decimal": "실수", "byte": "정수", "short": "정수",
    "int": "정수", "integer": "정수", "long": "정수", "unsignedByte": "정수", "unsignedShort": "정수",
    "unsignedInt": "정수", "unsignedLong": "정수", "nonNegativeInteger": "정수", "positiveInteger": "정수",
}
KIND = {
    "multiLanguageProperty": "다국어", "file": "파일", "blob": "내장 데이터", "referenceElement": "참조",
    "relationshipElement": "관계", "annotatedRelationshipElement": "관계", "operation": "동작", "capability": "기능",
    "basicEventElement": "이벤트",
}
GROUPS = {"submodelElementCollection": ("묶음", "value"), "submodelElementList": ("목록", "value"), "entity": ("개체", "statements")}
ELEMENTS = {"property", "range", *KIND, *GROUPS}
PREFIXES = (("https://www.smart-factory.kr/ids/cd/", "sf:"), ("https://admin-shell.io/", "ai:"))
LEGEND = "의미 ID의 `sf:`는 `https://www.smart-factory.kr/ids/cd/`, `ai:`는 `https://admin-shell.io/`를 줄인 것입니다."


def pick(node):
    """다국어 값에서 한국어, 영어, 첫 번째 값 순으로 고른다."""
    if node is None:
        return ""
    texts = {(c.findtext("language") or "")[:2]: (c.findtext("text") or "").strip() for c in node}
    return texts.get("ko") or texts.get("en") or next(iter(texts.values()), "")


def load(path):
    with zipfile.ZipFile(path) as zf:
        name = next(n for n in zf.namelist() if n.endswith(".aas.xml"))
        root = ET.fromstring(zf.read(name))
    for e in root.iter():
        e.tag = e.tag.split("}", 1)[-1]
    concepts = {c.findtext("id"): c for c in root.findall("conceptDescriptions/conceptDescription")}
    return root.findall("submodels/submodel"), concepts


def semantic(e):
    return e.findtext("semanticId/keys/key/value") or ""


def children(e):
    """묶음·목록의 하위 요소, 서브모델의 최상위 요소를 돌려준다."""
    tag = "submodelElements" if e.tag == "submodel" else GROUPS[e.tag][1]
    box = e.find(tag)
    return [c for c in box if c.tag in ELEMENTS] if box is not None else []


def is_group(e):
    return e.tag in GROUPS


def count(e):
    return 1 + sum(count(c) for c in children(e)) if is_group(e) else 1


def clean(text, limit):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit - 1] + "…"
    return escape(text).replace("|", "&#124;")


def shown(text):
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)


def fold(text, cap, limit):
    """GitHub 표는 내용 폭만큼 늘어나므로, 화면 폭을 넘지 않게 정해진 폭에서 줄을 나눈다."""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > cap:
        text = text[:cap - 1] + "…"
    lines, current = [], ""
    for word in text.split(" "):
        parts = re.findall(r"[^/#_.:-]+[/#_.:-]*|[/#_.:-]+", word) if shown(word) > limit else [word]
        for i, part in enumerate(parts):
            glue = " " if current and i == 0 else ""
            if current and shown(current + glue + part) > limit:
                lines.append(current)
                current = part
            else:
                current += glue + part
    if current:
        lines.append(current)
    return "<br>".join(escape(line).replace("|", "&#124;") for line in lines)


def solid(text):
    """형식 칸의 한글이 글자마다 줄바꿈되지 않게 묶는다."""
    return "⁠".join(text)


def short_id(sid):
    for long, short in PREFIXES:
        if sid.startswith(long):
            return short + sid[len(long):]
    return sid


def form(e):
    if is_group(e):
        return f"{solid(GROUPS[e.tag][0])}&nbsp;({len(children(e))})"
    if e.tag in ("property", "range"):
        kind = solid(VALUE_TYPE.get((e.findtext("valueType") or "").split(":")[-1], e.findtext("valueType") or ""))
        return f"{kind}&nbsp;{solid('범위')}" if e.tag == "range" else kind
    return solid(KIND[e.tag])


def value(e):
    if e.tag == "property":
        return e.findtext("value") or ""
    if e.tag == "range":
        low, high = e.findtext("min") or "", e.findtext("max") or ""
        return f"{low} ~ {high}" if low or high else ""
    if e.tag == "multiLanguageProperty":
        return pick(e.find("value"))
    if e.tag == "file":
        return (e.findtext("value") or "").rsplit("/", 1)[-1]
    return ""


def row(e, depth, concepts):
    concept = concepts.get(semantic(e))
    spec = concept.find(".//dataSpecificationIec61360") if concept is not None else None
    described = pick(e.find("description")) or (pick(spec.find("definition")) if spec is not None else "")
    unit = (spec.findtext("unit") or "") if spec is not None else ""
    name = escape(e.findtext("idShort") or "(항목)")
    name = f"**{name}**" if is_group(e) else name
    sid = f"<br><sub>{fold(short_id(semantic(e)), 90, 50)}</sub>" if semantic(e) else ""
    sample = " ".join(x for x in (value(e), unit) if x)
    return f"| {'&ensp;' * depth * 2}{name} | {fold(described, 140, 40)}{sid} | {form(e)} | {fold(sample, 60, 20)} |"


def signature(e):
    stem = re.sub(r"_*\d+_*$", "", e.findtext("idShort") or "")
    return e.tag, stem, tuple(c.findtext("idShort") for c in children(e))


def rows(parent, depth, concepts, tally):
    """표의 행을 만든다. 같은 구성이 세 번 이상 반복되는 묶음은 첫 묶음만 쓴다."""
    items = children(parent)
    repeats = {}
    for e in items:
        if is_group(e) and children(e):
            repeats.setdefault(signature(e), []).append(e)
    out = []
    seen = set()
    for e in items:
        group = repeats.get(signature(e)) if is_group(e) and children(e) else None
        if group and len(group) >= 3 and signature(e) in seen:
            continue
        tally["shown"] += 1
        out.append(row(e, depth, concepts))
        if is_group(e):
            out += rows(e, depth + 1, concepts, tally)
        if group and len(group) >= 3:
            seen.add(signature(e))
            hidden = group[1:]
            skipped = sum(count(x) for x in hidden)
            tally["hidden"] += skipped
            tally["repeats"].append((signature(e)[1], len(group)))
            out.append(f"| {'&ensp;' * depth * 2}<sub>⋯ 같은 구성 {len(hidden)}개 더<br>(항목 {skipped}개 생략)</sub> | | | |")
    return out


def submodel_section(sm, concepts):
    tally = {"shown": 0, "hidden": 0, "repeats": []}
    body = rows(sm, 0, concepts, tally)
    assert tally["shown"] + tally["hidden"] == sum(count(c) for c in children(sm)), sm.findtext("idShort")
    records = sum(n for stem, n in tally["repeats"] if stem.lower().startswith("record"))
    others = sum(n - 1 for stem, n in tally["repeats"] if not stem.lower().startswith("record"))
    notes = ([f"예시 기록 {records}건"] if records else []) + ([f"같은 구성 {others}개 생략"] if others else [])
    total = f"{tally['shown']}개 ({', '.join(notes)})" if notes else f"{tally['shown']}개"
    name = sm.findtext("idShort")
    purpose = PURPOSE.get(name) or clean(pick(sm.find("description")), 60)
    head = "| 항목 | 설명 · 의미 ID | 형식 | 예시값 |\n|---|---|---|---|"
    block = (
        f"<details>\n<summary><b>{escape(name)}</b> · {purpose} · 항목 {total}</summary>\n\n"
        f"{head}\n" + "\n".join(body) + "\n\n</details>"
    )
    return f"| {escape(name)} | {purpose} |", block


def tracked():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True).stdout
    return out.decode("utf-8").split("\0")[:-1]


def table(name):
    with open(HERE / name, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def video_block(name):
    for v in table("videos.csv"):
        if v["장비"] == name:
            video = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([\w-]{11})", v["YouTube 주소"]).group(1)
            return (
                f'## 시뮬레이션 영상\n\n<a href="https://www.youtube.com/watch?v={video}">'
                f'<img src="https://img.youtube.com/vi/{video}/mqdefault.jpg" width="480" alt="{escape(name)} 시뮬레이션 영상"></a>'
            )
    return ""


def page(name, paths):
    folders = sorted({"/".join(p.split("/")[:3]) for p in paths if p.split("/")[:1] == ["equipment"] and len(p.split("/")) > 3 and p.split("/")[2] == name})
    assert len(folders) == 1, name
    base = folders[0]
    owner = next(r["담당자"] for r in table("authors.csv") if r["장비"] == name)
    links = []
    aasx = []
    for section in SECTIONS:
        files = [p for p in paths if p.startswith(f"{base}/{section}/") and not p.endswith(".gitkeep")]
        if section == "AASX":
            files = [p for p in files if p.endswith(".aasx")]
            aasx = files
        cell = " · ".join(f'[{escape(p.rsplit("/", 1)[1])}]({quote(p[len(base) + 1:])})' for p in files) or "준비 중"
        links.append(f"| {section} | {cell} |")

    parts = [
        f"# {escape(name)}",
        f"장비군: {escape(base.split('/')[1])} · 담당자: {inquiry_link(name, owner)} <sub>(이름을 누르면 문의 양식이 열립니다)</sub>",
    ]
    video = video_block(name)
    if video:
        parts.append(video)
    parts.append("## 자료\n\n| 구분 | 파일 |\n|---|---|\n" + "\n".join(links))
    if len(aasx) == 1:
        submodels, concepts = load(ROOT / aasx[0])
        sections = [submodel_section(sm, concepts) for sm in submodels]
        parts.append("## 서브모델\n\n| 서브모델 | 용도 |\n|---|---|\n" + "\n".join(s[0] for s in sections))
        parts.append(
            "## 프로퍼티\n\n서브모델 이름을 누르면 표가 펼쳐집니다. "
            "**표의 예시값은 참조모델 설명을 위한 값이며 실제 장비의 측정값이 아닙니다.** "
            + LEGEND + "\n\n" + "\n\n".join(s[1] for s in sections)
        )
    else:
        parts.append("## 서브모델\n\nAASX 준비 중입니다." if not aasx else "## 서브모델\n\nAASX 파일이 여러 개라 정본 확인 뒤 표시합니다.")
    return base, "\n\n".join(parts) + "\n"


def main():
    paths = tracked()
    for name in sys.argv[1:]:
        base, text = page(name, paths)
        (ROOT / base / "README.md").write_bytes(text.encode("utf-8"))
        print(base, len(text.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
