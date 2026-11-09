#!/usr/bin/env python3
"""장비 폴더의 README.md(장비 페이지)를 만든다.

사용법: python tools/archive-index/build_pages.py 장비이름 [장비이름 ...]
"""
import csv
import re
import subprocess
import sys
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


def pick(node):
    """다국어 값에서 한국어, 영어, 첫 번째 값 순으로 고른다."""
    if node is None:
        return ""
    texts = {(c.findtext("language") or "")[:2]: (c.findtext("text") or "").strip() for c in node}
    return texts.get("ko") or texts.get("en") or next(iter(texts.values()), "")


def load_submodels(path):
    with zipfile.ZipFile(path) as zf:
        name = next(n for n in zf.namelist() if n.endswith(".aas.xml"))
        root = ET.fromstring(zf.read(name))
    for e in root.iter():
        e.tag = e.tag.split("}", 1)[-1]
    return root.findall("submodels/submodel")


def submodel_row(sm):
    name = sm.findtext("idShort")
    purpose = PURPOSE.get(name) or escape(re.sub(r"\s+", " ", pick(sm.find("description")))[:60]).replace("|", "&#124;")
    return f"| {escape(name)} | {purpose} |"


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


def document_links(files, base):
    """PDF가 있으면 열람 링크를 앞세우고, 원본은 내려받기 링크로 둔다."""
    href = lambda p: quote(p[len(base) + 1:])
    pdfs = {p.rsplit(".", 1)[0]: p for p in files if p.lower().endswith(".pdf")}
    cells = []
    for p in files:
        stem = p.rsplit(".", 1)[0]
        if p.lower().endswith(".pdf"):
            if not any(q != p and q.rsplit(".", 1)[0] == stem for q in files):
                cells.append(f"[열람]({href(p)})")
        elif stem in pdfs:
            cells.append(f"[열람]({href(pdfs[stem])}) · [원본 내려받기]({href(p)})")
        else:
            cells.append(f'[{escape(p.rsplit("/", 1)[1])}]({href(p)})')
    return " · ".join(cells) or "준비 중"


def page(name, paths):
    folders = sorted({"/".join(p.split("/")[:3]) for p in paths if p.startswith("equipment/") and p.count("/") > 2 and p.split("/")[2] == name})
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
        links.append(f"| {section} | {document_links(files, base)} |")

    parts = [
        f"# {escape(name)}",
        f"장비군: {escape(base.split('/')[1])} · 담당자: {inquiry_link(name, owner)} <sub>(이름을 누르면 문의 양식이 열립니다)</sub>",
    ]
    video = video_block(name)
    if video:
        parts.append(video)
    parts.append("## 자료\n\nPDF는 내려받지 않고 GitHub에서 바로 볼 수 있습니다.\n\n| 구분 | 보기 |\n|---|---|\n" + "\n".join(links))
    if len(aasx) == 1:
        rows = "\n".join(submodel_row(sm) for sm in load_submodels(ROOT / aasx[0]))
        parts.append("## 서브모델\n\n| 서브모델 | 용도 |\n|---|---|\n" + rows)
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
