# Module 2, Lesson 2 — Feeds — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the webhook intake, the cancellation worker, the patient-visible states, the zone crossing, the SMS line, and the mart clock. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Module 2, Lesson 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Today `eref` pushes `referral.submitted`. A cancelled clinic session arrives as `session.cancelled`. You leave with intake from that webhook, `wf-session-cancelled` on the dev namespace, and a mart read labeled with the clock the desk already distrusts. Booking from chat still waits.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still subscribes before the mart, the four patient lines are filled, the engine is in `zone-hospital` and the worker is in `zone-private`, the SMS names a booking and carries no national id, the mart note names the date column and leaves the wait figure out, and the three worker files do what chapters 03 and 05 describe.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 06. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The worker](03-the-worker.md) | [intake.py](work/app/intake.py) and [cancel.py](work/app/cancel.py) |
| 4 | [The pages](04-the-pages.md) | [states.md](work/states.md), [zones.md](work/zones.md), and [sms.md](work/sms.md) |
| 5 | [The mart](05-the-mart.md) | [mart.py](work/app/mart.py) and [mart.md](work/mart.md) |
| 6 | [Knowledge](06-knowledge.md) | [knowledge.md](work/knowledge.md) |

[07 — Trainer session](07-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 06.

## See the check pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. Then run:

```text
cd problem_simulation
python -m alwaha.check journey --release rel-m02-l02 --work "../Module 02/Lesson 02/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-journey passed.
```

Leave `problem_simulation/build` closed.
