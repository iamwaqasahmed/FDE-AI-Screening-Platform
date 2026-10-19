# Week 01 — Week 06

You are in the six-week track. The program map is [README.md](../README.md). The four-day introduction to the same client is [Week 00 — Self Paced](<../Week 00 - Self Paced/README.md>). You can start here without finishing it.

Read the shared notes before the weeks: [who it is for](../target_audience.md), [the practice](../FDE.md), and [health language](../health_language.md). Hartland's counts are in [the data guide](data/README.md), not in the health-language note.

For engineers who already put services in production: ML specialists, data scientists, data and software engineers, architects, technical product managers, and consultants, working in mixed teams of five or six.

The client is Hartland Regional Health Authority and its diabetic eye screening programme. The world here is deep: nineteen systems, a large corpus, and a new drop each week. The Chief Digital Officer wants an AI triage pilot live. Your team has six weeks to find which problems are real, size them, build what is justified, and hand over something the authority can run and govern.

Everyone and everything in it is fictional. Nothing here is a real patient's record or a protocol for care.

## What is here

| Folder | Who it is for | Start with |
|---|---|---|
| [data](data/README.md) | Participants. Everything the authority hands you: 19 system exports, 1,927 documents, stakeholder personas, user research, economics, and the weekly drops. | [data/README.md](data/README.md) |
| [Week 01 — Problem discovery](<Week 01 - Problem Discovery/README.md>) | Participants. Interviews, profiling, the timeline, the sizing, and the first brief. | [Week 01](<Week 01 - Problem Discovery/README.md>) |
| [Week 02 — Enterprise data](<Week 02 - Enterprise Data/README.md>) | Participants. Identity, the care-path record, contracts, and the schema-change drop. | [Week 02](<Week 02 - Enterprise Data/README.md>) |
| [Week 03 — Retrieval and ML evidence](<Week 03 - Retrieval and ML Evidence/README.md>) | Participants. The corpus index, the vendor evidence, and the data-protection restriction. | [Week 03](<Week 03 - Retrieval and ML Evidence/README.md>) |
| [Week 04 — Graph retrieval and integration](<Week 04 - Graph Retrieval and Integration/README.md>) | Participants. The bureau incident, who was not reached, and a graph that cites its path. | [Week 04](<Week 04 - Graph Retrieval and Integration/README.md>) |
| [Week 05 — The agent and the re-plan](<Week 05 - The Agent and the Re-plan/README.md>) | Participants. The scope change, the public line, and an agent that stops when a rule forbids the action. | [Week 05](<Week 05 - The Agent and the Re-plan/README.md>) |
| [Week 06 — Architecture, governance, and handoff](<Week 06 - Architecture, Governance, and Handoff/README.md>) | Participants. The clinical safety owner, the production path, and a handoff that keeps the pilot stopped. | [Week 06](<Week 06 - Architecture, Governance, and Handoff/README.md>) |
| [problem_simulation](problem_simulation/README.md) | Facilitators and maintainers. The generator that builds `data/` from a seed, the checks, the eval set and scorer, the baselines, and the mock APIs. | [problem_simulation/README.md](problem_simulation/README.md) |

## What you will practise

| Outcome | Where the evidence is |
|---|---|
| Business and AI opportunity discovery | Interviews, user research, workshop votes, economics, and the operational data behind them |
| Enterprise AI and data | Nineteen systems with no shared key, schema changes, late and duplicate feeds, a data catalogue and lineage |
| AI solution development | A corpus in real formats with status and dates, PII, prompt injection, an ML evidence set, budgets per question |
| AI architecture and governance | Trust zones, an EA current state, a model register, AI governance policy, data sharing agreements, security standards |
| Product and project delivery | A backlog, roadmap, freezes, funding gates, procurement routes, a benefits register, a RACI |
| Consulting and stakeholder management | Twelve stakeholders with conflicting positions, an interview simulator, a press query |
| Forward deployed engineering practice | Weekly drops that change the ground under you, and workstream contracts that make the team integrate |

## The six weeks

| Week | Focus | Drop |
|---|---|---|
| 1 | Discovery: interviews, profiling, the timeline, sizing problems. [Week 01](<Week 01 - Problem Discovery/README.md>) | The base handover |
| 2 | Enterprise data: identity, the care-path record, data quality. [Week 02](<Week 02 - Enterprise Data/README.md>) | Registry schema v3 |
| 3 | Retrieval and ML evidence. [Week 03](<Week 03 - Retrieval and ML Evidence/README.md>) | A data protection restriction |
| 4 | Graph retrieval and integration. [Week 04](<Week 04 - Graph Retrieval and Integration/README.md>) | A letter bureau incident |
| 5 | The agent and the re-plan. [Week 05](<Week 05 - The Agent and the Re-plan/README.md>) | A scope change and a press query |
| 6 | Architecture, governance, and handoff. [Week 06](<Week 06 - Architecture, Governance, and Handoff/README.md>) | A decision on clinical safety ownership |

The full design, including the hidden world model and the gold for each outcome, is in [problem_simulation/PLAN.md](problem_simulation/PLAN.md). Participants should not read it during the engagement.

## Getting started

Read this page, then [data/README.md](data/README.md), then [Week 01](<Week 01 - Problem Discovery/README.md>).

The data files are not in git. Only `data/README.md` is. From the repository root, generate them once (about six minutes, about 380 MB):

```text
cd "Week 01 - Week 06/problem_simulation"
pip install -r requirements.txt
python -m simulation --no-repeat
```

The same seed always produces the same data. After it finishes, come back to this folder.

Participants then open `data/handover/interfaces/` and `data/engagement/personas/`.

Week checks, such as `python -m course discovery_check`, run from `Week 01 - Week 06`. They do not run from the repository root, and they do not run from `problem_simulation`.

Facilitators, from `Week 01 - Week 06/problem_simulation`:

```text
pip install -r requirements.txt
python -m simulation                      # rebuild data/ from its seed (about six minutes)
python -m serve --system all --port 8800  # mock APIs over data/
python -m simulation.audit                # check the hardness rule
```
