# Module 1, Lesson 3 — Intake — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the SLA examples against the log, the specialty and the facility from the letter, the worker, the acceptance line, and the event contract. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Today the event stream, the SLA policy, and the business calendar arrived. `wf-intake` runs from `referral.submitted` to a held approval. The workflow does not accept, return, or book.

This folder is one way to finish that day. The example sentences can differ in wording when the clock, the one approval, the calendar, and the held stop still match.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 05. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The stream](02-the-stream.md) | The policy, the calendar, and the contract in `sources/` |
| 3 | [The worker](03-the-worker.md) | [worker.py](work/workflow/worker.py) and [calendar_count.py](work/workflow/calendar_count.py) |
| 4 | [The note](04-the-note.md) | [intake.md](work/intake.md) and [scenario-log.json](work/scenario-log.json) |
| 5 | [Knowledge](05-knowledge.md) | [knowledge.md](work/knowledge.md) |

[06 — Trainer session](06-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 05.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. Then run:

```text
cd problem_simulation
python -m alwaha.check events --work "../Module 01/Lesson 03/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-events passed.
```

Leave `problem_simulation/build` closed.
