# Week 2, Day 3 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the calendar, the reply, the receipt, the usability table, the definition of done, the zone rows, and the fixture note. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Day 1 was the arrival. Day 2 was the leaders' numbers, the baselines, and the approach memo. Day 3 was `wf-intake`, from `referral.submitted` to a held approval. Day 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Week 2 Day 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Week 2 Day 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Today the SMS receipt follows the case clock. The access clauses and the usability scripts arrive. You leave with a suite that goes red when `receipt-late` is on, and with `status-short` and `caregiver` finished. Booking from chat still waits.

This folder is one way to finish that day. The example sentences can differ in wording when the suite still comes before usability sign-off, the calendar uses the cluster week, the reply is judged by `intent` and the journey by `booked`, the receipt follows the case clock and stays pending while the switch is on, the two foundation scripts are finished with the four clause ids, the definition of done names the switch, the two zone rows are present, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is `Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The calendar](03-the-calendar.md) | [calendar_count.py](work/app/calendar_count.py) and [test_calendar.py](work/tests/test_calendar.py) |
| 4 | [The reply](04-the-reply.md) | [schema.py](work/app/schema.py), [test_schema.py](work/tests/test_schema.py), and [test_journey.py](work/tests/test_journey.py) |
| 5 | [The receipt](05-the-receipt.md) | [receipt.py](work/app/receipt.py) and [test_receipt.py](work/tests/test_receipt.py) |
| 6 | [The pages](06-the-pages.md) | [usability.md](work/usability.md), [dod.md](work/dod.md), [crossings.md](work/crossings.md), and [fixtures.md](work/fixtures.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. Then run:

```text
cd problem_simulation
python -m alwaha.check tests --release rel-w2d3 --work "../Week 02/Day 03/Solution_Copy/work" --profile practice
python -m alwaha.check ux --release rel-w2d3 --work "../Week 02/Day 03/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-w2-tests passed.
chk-w2-ux passed.
```

Leave `problem_simulation/build` closed.
