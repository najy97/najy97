#!/usr/bin/env python3
"""Regenerate the Open Source section of README.md from the GitHub API.

Counts merged pull requests and opened issues by USER in repositories owned
by someone else, starting at SINCE. Replaces the text between the
`<!-- oss:* -->` markers and leaves the rest of README.md untouched.
Exits non-zero without writing when the API answer is incomplete.
"""

import html
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
    "Yeachan-Heo/gajae-code": "Terminal AI coding-agent harness",
    "Yeachan-Heo/gajae-way": "Gateway for operator-owned agent sessions on Discord and Telegram",
    "Yeachan-Heo/clawhip": "Event-to-channel notification router",
}

# Language badge colour and simple-icons logo.
LANGUAGES = {
    "TypeScript": ("3178c6", "typescript"),
    "JavaScript": ("f7df1e", "javascript"),
    "Python": ("3776ab", "python"),
    "Rust": ("b7410e", "rust"),
    "Go": ("00add8", "go"),
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


def badge(label, message, color, logo=None, style="flat-square"):
    def part(s):
        return urllib.parse.quote(str(s).replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")
    path = f"{part(label)}-{part(message)}-{color}" if label else f"{part(message)}-{color}"
    src = f"https://img.shields.io/badge/{path}?style={style}"
    if logo:
        src += f"&logo={logo}&logoColor=white"
    alt = html.escape(f"{label} {message}".strip())
    return f'<img src="{src}" alt="{alt}" />'


def link(href, inner):
    return f'<a href="{href}">{inner}</a>'


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
    rows = []
    for r in repos:
        url = f"https://github.com/{r}"
        owner = r.split("/")[0]
        desc = html.escape(DESCRIPTIONS.get(r) or info[r].get("description") or "")
        lang = info[r].get("language")
        color, logo = LANGUAGES.get(lang, ("6e7681", None))
        lang_cell = badge("", lang, color, logo) if lang else ""
        contrib = [link(f"{url}/{q_pr}", badge("merged PRs", len(prs[r]), "8957e5", "github"))]
        if issue_count[r]:
            contrib.append(link(f"{url}/{q_issue}", badge("issues", issue_count[r], "1f6feb", "github")))
        rows.append(
            "<tr>\n"
            f'<td><img src="https://github.com/{owner}.png?size=48" width="24" height="24" alt="" /> '
            f'<a href="{url}"><b>{html.escape(r)}</b></a><br /><sub>{desc}</sub></td>\n'
            f'<td align="center">{link(f"{url}/stargazers", badge("★", stars(info[r]["stargazers_count"]), "e3b341"))}</td>\n'
            f'<td align="center">{lang_cell}</td>\n'
            f'<td>{"<br />".join(contrib)}</td>\n'
            "</tr>"
        )
    total_issues = sum(issue_count.values())
    summary = " ".join([
        badge("merged PRs", len(merged), "8957e5", "github", style="for-the-badge"),
        badge("repositories", len(repos), "0891b2", "github", style="for-the-badge"),
        badge("issues opened", total_issues, "1f6feb", "github", style="for-the-badge"),
    ])
    header = (
        '<thead><tr><th align="left">Project</th><th>Stars</th>'
        '<th>Language</th><th align="left">My contributions</th></tr></thead>'
    )

    lines = []
    for r in repos:
        lines.append(f"\n**[{r}](https://github.com/{r})** ({len(prs[r])})\n")
        for item in sorted(prs[r], key=lambda i: i["closed_at"], reverse=True):
            title = item["title"].replace("|", "\\|")
            lines.append(f"- [#{item['number']}]({item['html_url']}) {title}")

    today = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")
    table = (
        f'<div align="center">\n\n{summary}\n\n</div>\n\n'
        f"<table>\n{header}\n<tbody>\n" + "\n".join(rows) + "\n</tbody>\n</table>\n\n"
        f"<sub>Merged since {SINCE}. Updated {today} by GitHub Actions.</sub>"
    )
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
