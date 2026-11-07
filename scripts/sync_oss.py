#!/usr/bin/env python3
"""Regenerate the Open Source section of README.md from the GitHub API.

Counts merged pull requests and opened issues by USER in repositories owned
by someone else, starting at SINCE. Replaces the text between the
`<!-- oss:* -->` markers and leaves the rest of README.md untouched.
Exits non-zero without writing when the API answer is incomplete.
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER = "najy97"
SINCE = "2026-07-01"
README = Path(__file__).resolve().parent.parent / "README.md"

# Repository descriptions written for this profile. Repositories missing here
# fall back to their GitHub description.
DESCRIPTIONS = {
    "Yeachan-Heo/gajae-code": "Terminal AI coding-agent harness (TypeScript)",
    "Yeachan-Heo/gajae-way": "Gateway for operator-owned agent sessions on Discord and Telegram",
    "Yeachan-Heo/clawhip": "Event-to-channel notification router (Rust)",
}

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def search(query):
    items, page = [], 1
    while True:
        params = urllib.parse.urlencode({"q": query, "per_page": 100, "page": page})
        data = get(f"{API}/search/issues?{params}")
        if data.get("incomplete_results"):
            sys.exit(f"incomplete search results for: {query}")
        items.extend(data["items"])
        if len(items) >= data["total_count"] or not data["items"]:
            return items
        page += 1


def repo_name(item):
    return item["repository_url"].removeprefix(f"{API}/repos/")


def stars(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def replace(text, name, body, inline=False):
    pattern = re.compile(rf"(<!-- oss:{name}:start -->)(.*?)(<!-- oss:{name}:end -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker oss:{name} not found in README.md")
    sep = "" if inline else "\n"
    return pattern.sub(lambda m: f"{m.group(1)}{sep}{body}{sep}{m.group(3)}", text)


def main():
    merged = search(f"author:{USER} is:pr is:merged -user:{USER} merged:>={SINCE}")
    issues = search(f"author:{USER} is:issue -user:{USER} created:>={SINCE}")
    if not merged:
        sys.exit("no merged pull requests returned; refusing to overwrite README.md")

    prs = defaultdict(list)
    for item in merged:
        prs[repo_name(item)].append(item)
    issue_count = defaultdict(int)
    for item in issues:
        issue_count[repo_name(item)] += 1

    repos = sorted(prs, key=lambda r: (-len(prs[r]), r))
    info = {r: get(f"{API}/repos/{r}") for r in repos}

    q_pr = "pulls?q=" + urllib.parse.quote(f"is:pr is:merged author:{USER}")
    q_issue = "issues?q=" + urllib.parse.quote(f"is:issue author:{USER}")
    rows = [
        "| Project | ★ | What it is | My contributions |",
        "| --- | --: | --- | --- |",
    ]
    for r in repos:
        url = f"https://github.com/{r}"
        desc = DESCRIPTIONS.get(r) or (info[r].get("description") or "").replace("|", "\\|")
        cells = [f"[{plural(len(prs[r]), 'merged PR')}]({url}/{q_pr})"]
        if issue_count[r]:
            cells.append(f"[{plural(issue_count[r], 'issue')}]({url}/{q_issue})")
        rows.append(
            f"| **[{r}]({url})** | {stars(info[r]['stargazers_count'])} | {desc} | {', '.join(cells)} |"
        )

    lines = []
    for r in repos:
        lines.append(f"\n**[{r}](https://github.com/{r})** ({len(prs[r])})\n")
        for item in sorted(prs[r], key=lambda i: i["closed_at"], reverse=True):
            title = item["title"].replace("|", "\\|")
            lines.append(f"- [#{item['number']}]({item['html_url']}) {title}")

    today = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")
    table = "\n".join(rows) + f"\n\n<sub>Merged since {SINCE}. Updated {today} by GitHub Actions.</sub>"
    details = (
        f"<details>\n<summary>All {len(merged)} merged PRs</summary>\n"
        + "\n".join(lines)
        + "\n\n</details>"
    )

    text = README.read_text()
    text = replace(text, "total", str(len(merged)), inline=True)
    text = replace(text, "repos", str(len(repos)), inline=True)
    text = replace(text, "table", table)
    text = replace(text, "details", details)
    README.write_text(text)
    print(f"{len(merged)} merged PRs, {len(issues)} issues, {len(repos)} repositories")


if __name__ == "__main__":
    main()
