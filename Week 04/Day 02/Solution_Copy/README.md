# Week 4, Day 2 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the trace, the board, the meter, the hours cache, the three drifts, the override rate, the shadow hold, the timeline, the dashboard page, the runbook, both interview notes, and the knowledge file. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Day 1 was the arrival. Day 2 was the leaders' numbers, the baselines, and the approach memo. Day 3 was `wf-intake`, from `referral.submitted` to a held approval. Day 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Week 2 Day 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Week 2 Day 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Week 2 Day 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Week 2 Day 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Week 2 Day 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Week 3 Day 1 left one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. Week 3 Day 2 left a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed. Week 3 Day 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation. Week 3 Day 4 left a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stayed on the grading service. Week 3 Day 5 left one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief. Week 4 Day 1 left guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done. Today the replay is open. You leave with a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs replay, then dashboard, then timeline, then cache, then shadow, the board names latency, errors, and tool failures, the timeline matches the replay, the cache drops when the Ramadan circular changes, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 06. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The board](03-the-board.md) | [spans.py](work/app/spans.py), [dashboard.py](work/app/dashboard.py), and [meter.py](work/app/meter.py) |
| 4 | [The hours](04-the-hours.md) | [cache.py](work/app/cache.py), [drift.py](work/app/drift.py), [override.py](work/app/override.py), and [shadow.py](work/app/shadow.py) |
| 5 | [The pages](05-the-pages.md) | [timeline.md](work/timeline.md), [dashboard.md](work/dashboard.md), [runbook.md](work/runbook.md), and both notes files |
| 6 | [Knowledge](06-knowledge.md) | [knowledge.md](work/knowledge.md) |

[07 — Trainer session](07-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 06.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check incident --release rel-w4d2 --work "../Week 04/Day 02/Solution_Copy/work" --profile practice
python -m alwaha.check cache --release rel-w4d2 --work "../Week 04/Day 02/Solution_Copy/work" --profile practice
```

Each command prints its own line. You should see:

```text
chk-w4-incident passed.
slice-cache passed.
```

The cache check id is `slice-cache`. If those two lines are on the screen, the failure table from the morning is not more work. Leave `problem_simulation/build` closed.
