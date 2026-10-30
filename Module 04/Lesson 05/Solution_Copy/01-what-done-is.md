# 01 — What done is

This page is the map. The day is finished by the sprint, staff sign-in, the bus, the handoff, late leave, the warehouse clock, the ranking, the gate record, the personal lab, the deployment architecture, the operations plan, the proposal, the readout, the retro, the access-manager notes, the enterprise-architect notes, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Requests, then sign-in, then bus, then handoff, then leave, then warehouse, then ranking, then proposal. Explained in [chapter 02](02-the-sprint.md) |
| [app/signin.py](work/app/signin.py) | Accept a staff role. Refuse a service token. Explained in [chapter 03](03-the-connections.md) |
| [app/bus.py](work/app/bus.py) | Keep the event, including a field this consumer does not know. Explained in chapter 03 |
| [app/handoff.py](work/app/handoff.py) | A handoff with no summary is refused. Explained in chapter 03 |
| [app/leave.py](work/app/leave.py) | Late leave cancels the published session. Explained in chapter 03 |
| [app/warehouse.py](work/app/warehouse.py) | The referral clock is the referred date. Explained in chapter 03 |
| [tests/test_signin.py](work/tests/test_signin.py) | Staff is accepted and the service token is refused. The shell test treats the service token as staff. The two files are not the same |
| [tests/test_bus.py](work/tests/test_bus.py) | An unknown field still keeps the cancellation. The shell test drops both |
| [tests/test_handoff.py](work/tests/test_handoff.py) | A summary is kept and an empty one is refused. The shell test returns an empty summary |
| [tests/test_leave.py](work/tests/test_leave.py) | Late leave cancels the session. The shell test leaves it published |
| [tests/test_warehouse.py](work/tests/test_warehouse.py) | The clock is the referred date. The shell test reads the booking date |
| [app/rank.py](work/app/rank.py) | Return the first problem that has no blocker. Explained in [chapter 04](04-the-proposal.md) |
| [app/gates.py](work/app/gates.py) | Name the clinical safety owner at go-live. Explained in chapter 04 |
| [app/personal.py](work/app/personal.py) | Stop a direct attack. Do not book. Explained in chapter 04 |
| [tests/test_rank.py](work/tests/test_rank.py) | A blocked problem is not first. The shell test starts with triage |
| [tests/test_gates.py](work/tests/test_gates.py) | Go-live names the clinical safety owner. The shell test skips go-live |
| [tests/test_personal.py](work/tests/test_personal.py) | The direct family is blocked. The shell test lets the attack book |
| [architecture-deploy.md](work/architecture-deploy.md) | Zones, Flows, and Boundary. Explained in [chapter 05](05-the-pages.md) |
| [operations.md](work/operations.md) | Owners, RACI, Gate, and Incident. Explained in chapter 05 |
| [proposal.md](work/rcp/proposal.md) | Client, Ranking, Roadmap, Plan, Metrics, and Adoption. Explained in chapter 05 |
| [readout.md](work/readout.md) | Ranking, Handoff, Leave, Benefit, Channel, and Asks. Explained in chapter 05 |
| [retro.md](work/retro.md) | Keep, Drop, and Open. Explained in chapter 05 |
| [access-mgr.notes.md](work/interviews/access-mgr.notes.md) | The summary. The integrate check reads this file |
| [ea.notes.md](work/interviews/ea.notes.md) | Leave, `session.cancelled`, and bi. The integrate check reads this file |
| [access-mgr.questions.txt](work/interviews/access-mgr.questions.txt) | The questions the interview command reads. The check does not read this file |
| [ea.questions.txt](work/interviews/ea.questions.txt) | The questions the interview command reads. The check does not read this file |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 06](06-knowledge.md) |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The test job. This day does not replace it. The packet copy is the same file |

The checks print `passed` when staff sign-in holds, the bus keeps an unknown field and `session.cancelled`, a handoff has a summary, late leave cancels the session and emits `session.cancelled`, the warehouse clock is the referred date, the sprint opens the requests first, both notes are present, the deployment architecture has its sections, the operations plan names an owner, `med-dir`, and G4, the ranking does not follow the dot-vote, the roadmap does not start with `p-triage`, the proposal can be presented, the readout answers `steer-m04-l05`, the retro has its headings, both knowledge answers are present, and the direct family is blocked.

A bus miss is two lines on `chk-m04-l05-integrate`. A late-leave miss is two lines on that same check. A gates miss is two lines on `chk-m04-l05-ops`. An empty operations page is three lines. An empty readout is the long list on `chk-readout`. `knowledge.md does not say which event leave creates` is not the integrate line.

The suite imports all eight app modules. None of them is optional.

Next: [02 — The sprint](02-the-sprint.md).
