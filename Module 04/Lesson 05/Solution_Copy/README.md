# Module 4, Lesson 5 — The proposal — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, staff sign-in, the bus, the handoff, late leave, the warehouse clock, the ranking, the gate record, the personal lab, the deployment architecture, the operations plan, the proposal, the readout, the retro, both interview notes, and the knowledge file. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Module 2, Lesson 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Module 2, Lesson 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Module 2, Lesson 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Module 2, Lesson 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Module 2, Lesson 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Module 3, Lesson 1 left one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. Module 3, Lesson 2 left a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed. Module 3, Lesson 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation. Module 3, Lesson 4 left a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stayed on the grading service. Module 3, Lesson 5 left one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief. Module 4, Lesson 1 left guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done. Module 4, Lesson 2 left a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done. Module 4, Lesson 3 left the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done. Module 4, Lesson 4 left two replicas, traffic on site-b after site-a dies, the breaker open on insure, and a rent-versus-buy draft that meets 8 February. A booking path that waits on insurance, or a purchase that cannot arrive before Ramadan, is not done. Today the contact center, the warehouse, and HR asked to be connected. You leave with staff sign-in and the bus still up after the drill, a handoff that has a summary, a late leave that cancels a session, a warehouse clock that is not the booking date, and a proposal that can be presented. A roadmap that starts with triage, or a handoff with no summary, is not done.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs requests, then sign-in, then bus, then handoff, then leave, then warehouse, then ranking, then proposal, staff sign-in holds, the bus keeps `session.cancelled`, a handoff has a summary, late leave cancels the session, the warehouse clock is the referred date, and the roadmap does not start with triage.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 06. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The connections](03-the-connections.md) | [signin.py](work/app/signin.py), [bus.py](work/app/bus.py), [handoff.py](work/app/handoff.py), [leave.py](work/app/leave.py), and [warehouse.py](work/app/warehouse.py) |
| 4 | [The proposal](04-the-proposal.md) | [rank.py](work/app/rank.py), [gates.py](work/app/gates.py), and [personal.py](work/app/personal.py) |
| 5 | [The pages](05-the-pages.md) | [architecture-deploy.md](work/architecture-deploy.md), [operations.md](work/operations.md), [proposal.md](work/rcp/proposal.md), [readout.md](work/readout.md), [retro.md](work/retro.md), and both notes files |
| 6 | [Knowledge](06-knowledge.md) | [knowledge.md](work/knowledge.md) |

[07 — Trainer session](07-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 06.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check integrate --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check ops --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check rcp --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
```

You should see five lines:

```text
chk-m04-l05-integrate passed.
chk-m04-l05-ops passed.
chk-m04-l05-rcp passed.
chk-readout passed.
chk-individual-m04-l05 passed.
```

There is no sixth passed line. If those lines are on the screen, the failure table from the lesson is not more work. Leave `problem_simulation/build` closed.
