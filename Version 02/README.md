# Version 02: advanced track

For engineers who already put services in production: ML specialists, data scientists, data and software engineers, architects, technical product managers, and consultants, working in mixed teams of five or six.

The client is the same as in [Version 01](<../Version 01/README.md>): Hartland Regional Health Authority and its diabetic eye screening programme. Here the world is much deeper. The Chief Digital Officer wants an AI triage pilot live. Your team has six weeks to find which problems are real, size them, build what is justified, and hand over something the authority can run and govern.

Everyone and everything in it is fictional. Nothing here is a real patient's record or a protocol for care.

## What is here

| Folder | Who it is for | Start with |
|---|---|---|
| [data](data/README.md) | Participants. Everything the authority hands you: 19 system exports, 1,927 documents, stakeholder personas, user research, economics, and the weekly drops. | [data/README.md](data/README.md) |
| [Week 01 — Problem discovery](<Week 01 - Problem Discovery/README.md>) | Participants. Interviews, profiling, the timeline, the sizing, and the first brief. | [Week 01](<Week 01 - Problem Discovery/README.md>) |
| [Week 02 — Enterprise data](<Week 02 - Enterprise Data/README.md>) | Participants. Identity, the care-path record, contracts, and the schema-change drop. | [Week 02](<Week 02 - Enterprise Data/README.md>) |
| [Week 03 — Retrieval and ML evidence](<Week 03 - Retrieval and ML Evidence/README.md>) | Participants. The corpus index, the vendor evidence, and the data-protection restriction. | [Week 03](<Week 03 - Retrieval and ML Evidence/README.md>) |
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
| 4 | The agent and the integration | A letter bureau incident |
| 5 | Evaluation, cost, and the executive story | A scope change and a press query |
| 6 | Architecture, governance, and handoff | A decision on clinical safety ownership |

The full design, including the hidden world model and the gold for each outcome, is in [problem_simulation/PLAN.md](problem_simulation/PLAN.md). Participants should not read it during the engagement.

## Getting started

The data files are not in git; only `data/README.md` is. Generate them once after cloning (about six minutes, about 380 MB):

```text
cd problem_simulation
pip install -r requirements.txt
python -m simulation --no-repeat
```

The same seed always produces the same data.

Participants: read [data/README.md](data/README.md), then open `data/handover/interfaces/` and `data/engagement/personas/`.

Facilitators, from `problem_simulation/`:

```text
pip install -r requirements.txt
python -m simulation                      # rebuild data/ from its seed (about six minutes)
python -m serve --system all --port 8800  # mock APIs over data/
python -m simulation.audit                # check the hardness rule
```
