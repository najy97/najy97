<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0%3A0f172a%2C50%3A1e3a8a%2C100%3A0891b2&height=200&section=header&text=Junyeong+Na&fontSize=60&fontColor=ffffff&fontAlignY=36&desc=AI+backend+engineer+%7C+LLM+agents+in+production&descAlignY=58&descSize=18&animation=fadeIn" alt="Junyeong Na, AI backend engineer" />

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=38BDF8&center=true&vCenter=true&width=640&lines=AI+backend+engineer+in+Seoul%3BLLM+agents+in+financial-services+production%3BOpen-source+contributor+to+agent+tooling%3BPython+%7C+FastAPI+%7C+AWS+%7C+MCP" alt="AI backend engineer in Seoul. LLM agents in financial-services production. Open-source contributor to agent tooling." /></a>

<a href="https://www.linkedin.com/in/junyeong-na-90355a211/"><img src="https://img.shields.io/badge/LinkedIn-Junyeong_Na-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>

KB증권 사내 AI 에이전트 서비스의 백엔드를 개발하고 있습니다. 코딩 에이전트 하네스 등 오픈소스 프로젝트에도 기여하고 있습니다.

</div>

## 👋 About

I build Python services that take LLM agents into production for financial-services teams, and I contribute to the runtime, session, and messaging layers of open-source coding-agent tools.

- **AI Engineer at 4season.ai**, building backend services for KB Securities' enterprise AI agent platform (on this client since Jul 2025): answer persistence, deterministic checks before scheduled agent results reach users, and asynchronous execution over SQS and Lambda.
- **Open-source contributor** to the Gajae Code agent ecosystem: <!-- oss:total:start -->49<!-- oss:total:end --> merged PRs across <!-- oss:repos:start -->3<!-- oss:repos:end --> repositories since Jul 2026.

```text
💼 Day job       AI Engineer at 4season.ai, KB Securities AI agent platform
🧩 Open source   Gajae Code runtime, gateway, and notification tooling
🛠️ Daily stack   Python, FastAPI, PostgreSQL, AWS Lambda and SQS
💬 Ask me about  Agent backends in regulated environments
```

## 🧩 Open source

<!-- oss:table:start -->
| Project | ★ | What it is | My contributions |
| --- | --: | --- | --- |
| **[Yeachan-Heo/gajae-code](https://github.com/Yeachan-Heo/gajae-code)** | 3.1k | Terminal AI coding-agent harness (TypeScript) | [33 merged PRs](https://github.com/Yeachan-Heo/gajae-code/pulls?q=is%3Apr%20is%3Amerged%20author%3Anajy97), [13 issues](https://github.com/Yeachan-Heo/gajae-code/issues?q=is%3Aissue%20author%3Anajy97) |
| **[Yeachan-Heo/gajae-way](https://github.com/Yeachan-Heo/gajae-way)** | 61 | Gateway for operator-owned agent sessions on Discord and Telegram | [11 merged PRs](https://github.com/Yeachan-Heo/gajae-way/pulls?q=is%3Apr%20is%3Amerged%20author%3Anajy97), [6 issues](https://github.com/Yeachan-Heo/gajae-way/issues?q=is%3Aissue%20author%3Anajy97) |
| **[Yeachan-Heo/clawhip](https://github.com/Yeachan-Heo/clawhip)** | 937 | Event-to-channel notification router (Rust) | [5 merged PRs](https://github.com/Yeachan-Heo/clawhip/pulls?q=is%3Apr%20is%3Amerged%20author%3Anajy97), [1 issue](https://github.com/Yeachan-Heo/clawhip/issues?q=is%3Aissue%20author%3Anajy97) |

<sub>Merged since 2026-07-01. Updated 2026-11-08 by GitHub Actions.</sub>
<!-- oss:table:end -->

### Selected contributions

- **Session and SDK lifecycle:** [a distinct event generation for every host start](https://github.com/Yeachan-Heo/gajae-code/pull/7227), [closing managed tmux owners on macOS and fencing relaunch races](https://github.com/Yeachan-Heo/gajae-code/pull/7399), [releasing proven pre-marker spawn mirrors](https://github.com/Yeachan-Heo/gajae-code/pull/7533), [preserving turn results and tail authority](https://github.com/Yeachan-Heo/gajae-code/pull/5104)
- **Safety boundaries:** refusing symlinked owner lifecycle paths ([#7433](https://github.com/Yeachan-Heo/gajae-code/pull/7433), [#7529](https://github.com/Yeachan-Heo/gajae-code/pull/7529)), [binding execution approval to transcript content, not inode](https://github.com/Yeachan-Heo/gajae-code/pull/6763), [one Anthropic credential per organization](https://github.com/Yeachan-Heo/gajae-code/pull/6686)
- **Messaging integrations:** [GitHub webhook signature verification](https://github.com/Yeachan-Heo/clawhip/pull/386), [a GitHub notifications source](https://github.com/Yeachan-Heo/clawhip/pull/392), [forwarding Telegram photos and files to the agent](https://github.com/Yeachan-Heo/gajae-way/pull/489), [Telegram media delivery](https://github.com/Yeachan-Heo/gajae-way/pull/639)
- **Agent behavior:** [porting pre-execution AST-condition matching](https://github.com/Yeachan-Heo/gajae-code/pull/6846), [Codex-compatible prompt suggestions](https://github.com/Yeachan-Heo/gajae-code/pull/7115), [premise and measurement checks in verification rules](https://github.com/Yeachan-Heo/gajae-code/pull/7457)

<!-- oss:details:start -->
<details>
<summary>All 49 merged PRs</summary>

**[Yeachan-Heo/gajae-code](https://github.com/Yeachan-Heo/gajae-code)** (33)

- [#7554](https://github.com/Yeachan-Heo/gajae-code/pull/7554) test(coding-agent): keep InteractiveMode.init() tests off the real star reminder (#7553)
- [#7533](https://github.com/Yeachan-Heo/gajae-code/pull/7533) feat(sdk): add gjc sdk broker attest-spawn-anchors to release proven pre-marker spawn mirrors
- [#7529](https://github.com/Yeachan-Heo/gajae-code/pull/7529) fix(gjc-session): refuse links in the shell and Python owner lifecycle writers
- [#7457](https://github.com/Yeachan-Heo/gajae-code/pull/7457) feat(prompts): premise, measurement, and hidden-reader checks in verification rules
- [#7445](https://github.com/Yeachan-Heo/gajae-code/pull/7445) feat(master): show the spawning master on peer rows (#7439)
- [#7441](https://github.com/Yeachan-Heo/gajae-code/pull/7441) fix(master): inject the peer snapshot once per session (#7438)
- [#7433](https://github.com/Yeachan-Heo/gajae-code/pull/7433) fix(gjc-runtime): refuse links in owner lifecycle writer paths
- [#7425](https://github.com/Yeachan-Heo/gajae-code/pull/7425) fix(coding-agent): run normally when a project .env names only the managed-owner child token
- [#7424](https://github.com/Yeachan-Heo/gajae-code/pull/7424) fix(coding-agent): refuse a linked lifecycle path before creating the owner root
- [#7399](https://github.com/Yeachan-Heo/gajae-code/pull/7399) fix(runtime): close managed tmux owners on macOS and fence relaunch races
- [#7397](https://github.com/Yeachan-Heo/gajae-code/pull/7397) fix(sdk): close spawned headless hosts through their endpoint and select headless on Windows
- [#7253](https://github.com/Yeachan-Heo/gajae-code/pull/7253) fix(sdk): stop orphaned spawn mirrors from fencing as legacy rows
- [#7227](https://github.com/Yeachan-Heo/gajae-code/pull/7227) fix(sdk): open a distinct event generation for every host start
- [#7226](https://github.com/Yeachan-Heo/gajae-code/pull/7226) fix(telegram): fence only the closed attachment after session_closed
- [#7203](https://github.com/Yeachan-Heo/gajae-code/pull/7203) fix(notifications): keep lean final answers across tool-loop follow-ups
- [#7139](https://github.com/Yeachan-Heo/gajae-code/pull/7139) fix(session): keep failed model changes out of the model MRU
- [#7145](https://github.com/Yeachan-Heo/gajae-code/pull/7145) fix(tmux): request UTF-8 client output so a localeless broker can parse tmux replies
- [#7115](https://github.com/Yeachan-Heo/gajae-code/pull/7115) feat(coding-agent): match Codex prompt-suggestion logic
- [#7109](https://github.com/Yeachan-Heo/gajae-code/pull/7109) refactor(cli): remove dead --smol/--slow role overrides and stale smol wording
- [#6881](https://github.com/Yeachan-Heo/gajae-code/pull/6881) fix(session): keep failed profile activation out of role materialization
- [#6854](https://github.com/Yeachan-Heo/gajae-code/pull/6854) chore(ttsr): correct matcher hook docs and name the test stub type
- [#6846](https://github.com/Yeachan-Heo/gajae-code/pull/6846) feat(ttsr): port oh-my-pi pre-execution astCondition matching
- [#6763](https://github.com/Yeachan-Heo/gajae-code/pull/6763) fix(workflow): bind execution approval to transcript content, not inode
- [#6704](https://github.com/Yeachan-Heo/gajae-code/pull/6704) fix(auth): attribute usage and resolve org selectors only on proof
- [#6686](https://github.com/Yeachan-Heo/gajae-code/pull/6686) fix(auth): keep one Anthropic credential per organization
- [#6379](https://github.com/Yeachan-Heo/gajae-code/pull/6379) fix(sdk): keep definite session CLI rejection codes (busy, unknown_operation, not_a_repository)
- [#6118](https://github.com/Yeachan-Heo/gajae-code/pull/6118) fix(session): defer receipt retirement a peer already claimed
- [#6066](https://github.com/Yeachan-Heo/gajae-code/pull/6066) fix(doctor): report a refused broker restart as a refusal, not an uncertain effect
- [#5104](https://github.com/Yeachan-Heo/gajae-code/pull/5104) fix(sdk): preserve turn result and tail authority
- [#2491](https://github.com/Yeachan-Heo/gajae-code/pull/2491) fix(coding-agent): scope phase-one memory jobs by cwd
- [#1436](https://github.com/Yeachan-Heo/gajae-code/pull/1436) fix(edit): preserve UTF-8 BOM in replace mode
- [#1435](https://github.com/Yeachan-Heo/gajae-code/pull/1435) fix(deep-interview): reject blank gate free text
- [#1346](https://github.com/Yeachan-Heo/gajae-code/pull/1346) Treat Deep Interview choice clarification as a non-answer

**[Yeachan-Heo/gajae-way](https://github.com/Yeachan-Heo/gajae-way)** (11)

- [#738](https://github.com/Yeachan-Heo/gajae-way/pull/738) feat(gateway): opt-in per-monitor session roll on observed context size
- [#739](https://github.com/Yeachan-Heo/gajae-way/pull/739) fix(gateway): a lane started from a monitor turn reports to the monitor's channel target
- [#733](https://github.com/Yeachan-Heo/gajae-way/pull/733) fix(gateway): an uncorrelated agent_end is not owned terminal evidence
- [#639](https://github.com/Yeachan-Heo/gajae-way/pull/639) feat(telegram): upload MEDIA: file deliveries with sendPhoto/sendDocument
- [#655](https://github.com/Yeachan-Heo/gajae-way/pull/655) fix(telegram): key inbound messages by chat-scoped Telegram ids so reactions resolve
- [#656](https://github.com/Yeachan-Heo/gajae-way/pull/656) fix(memory): bound memory git by a deadline and never wait on Bun reporting its exit
- [#612](https://github.com/Yeachan-Heo/gajae-way/pull/612) fix(gateway): re-prompt the persona after runs the runtime started on its own
- [#489](https://github.com/Yeachan-Heo/gajae-way/pull/489) feat(telegram): forward inbound photos and files so the persona can read them
- [#485](https://github.com/Yeachan-Heo/gajae-way/pull/485) fix(gateway): treat origins unbound by a broker cutover as history in ops.cycle
- [#356](https://github.com/Yeachan-Heo/gajae-way/pull/356) fix(gateway): keep the requester context when a turn is re-dispatched
- [#355](https://github.com/Yeachan-Heo/gajae-way/pull/355) fix(gateway): run memory git in the C locale

**[Yeachan-Heo/clawhip](https://github.com/Yeachan-Heo/clawhip)** (5)

- [#400](https://github.com/Yeachan-Heo/clawhip/pull/400) fix(github): deliver notification threads read before the next poll
- [#392](https://github.com/Yeachan-Heo/clawhip/pull/392) feat(github): add opt-in notifications source
- [#390](https://github.com/Yeachan-Heo/clawhip/pull/390) fix(github): resolve PR metadata for activity comments outside the PR window
- [#386](https://github.com/Yeachan-Heo/clawhip/pull/386) feat(webhook): verify GitHub signatures and route comment/review events
- [#382](https://github.com/Yeachan-Heo/clawhip/pull/382) feat(github): opt-in PR review and comment notifications

</details>
<!-- oss:details:end -->

## 🛠️ Tech stack

<div align="center">

**Backend**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />

**AI and agents**<br/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" /> <img src="https://img.shields.io/badge/vLLM-30A2FF?style=for-the-badge" alt="vLLM" /> <img src="https://img.shields.io/badge/MCP-111827?style=for-the-badge" alt="MCP" /> <img src="https://img.shields.io/badge/A2A-111827?style=for-the-badge" alt="A2A" /> <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge" alt="FAISS" />

**Cloud and observability**<br/>
<img src="https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white" alt="AWS Lambda" /> <img src="https://img.shields.io/badge/Amazon_SQS-FF4F8B?style=for-the-badge&logo=amazonsqs&logoColor=white" alt="Amazon SQS" /> <img src="https://img.shields.io/badge/AWS_Glue-8C4FFF?style=for-the-badge" alt="AWS Glue" /> <img src="https://img.shields.io/badge/OpenTelemetry-000000?style=for-the-badge&logo=opentelemetry&logoColor=white" alt="OpenTelemetry" />

**Open-source work**<br/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/Bun-000000?style=for-the-badge&logo=bun&logoColor=white" alt="Bun" /> <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />

</div>

## 🔬 Research (2022 to 2024)

- **[remotebiosensing/rppg](https://github.com/remotebiosensing/rppg)**: benchmark framework for fair evaluation of remote photoplethysmography. Preprocessing, signal processing, and model evaluation; 3rd contributor by commits. Co-author of [arXiv:2307.12644](https://arxiv.org/abs/2307.12644).
- M.S. in Electronics and Communications Engineering, Kwangwoon University (2024).

## 🐍 Contribution snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/najy97/najy97/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/najy97/najy97/output/github-contribution-grid-snake.svg" />
  <img width="100%" alt="GitHub contribution snake" src="https://raw.githubusercontent.com/najy97/najy97/output/github-contribution-grid-snake.svg" />
</picture>

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0%3A0891b2%2C50%3A1e3a8a%2C100%3A0f172a&height=110&section=footer" alt="" />
