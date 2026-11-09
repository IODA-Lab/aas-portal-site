#!/usr/bin/env python3
"""장비 문의 양식으로 등록된 이슈를 그 장비의 담당자에게 지정한다.

GitHub Actions의 issues(opened) 이벤트에서 실행된다. 담당자의 GitHub 아이디가
owner_accounts.csv에 없으면 지정하지 않고 끝낸다.
"""
import csv
import json
import os
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent


def read_map(name, key, value):
    with open(HERE / name, encoding="utf-8-sig", newline="") as f:
        return {r[key]: r[value] for r in csv.DictReader(f)}


def equipment_of(body):
    """문의 양식 본문의 '### 장비' 항목 값을 돌려준다."""
    m = re.search(r"^### 장비[ \t]*\n+(.+?)[ \t]*$", (body or "").replace("\r\n", "\n"), re.M)
    return m.group(1).strip() if m else None


def account_for(body, owners, accounts):
    return accounts.get(owners.get(equipment_of(body), ""))


def main():
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
        issue = json.load(f)["issue"]
    account = account_for(issue.get("body"), read_map("authors.csv", "장비", "담당자"),
                          read_map("owner_accounts.csv", "담당자", "GitHub"))
    if not account:
        print("담당자 계정을 찾지 못해 지정하지 않음")
        return
    url = f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/issues/{issue['number']}/assignees"
    req = urllib.request.Request(url, data=json.dumps({"assignees": [account]}).encode(), method="POST", headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        print("지정 완료", r.status)


if __name__ == "__main__":
    main()
