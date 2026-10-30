# Module 2, Lesson 5 — The Ain change — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the booking, the nightly file, the notice, the contract, the zone rows, the operator steps, the deployment note, the readout, and the retro. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Module 2, Lesson 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Module 2, Lesson 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Module 2, Lesson 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Module 2, Lesson 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Today steering asks to include Ain. You leave with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stays queued for the nightly file.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs smoke, then change, then readout, then retro, Ain stays queued, a missed night keeps yesterday, a failed notice stays queued, the contract accepts `queued` and rejects `booked`, the zone table has both rows, the deployment note sequences `cr-ain` after the smoke test, the readout answers the seven headings, the retro has Keep, Drop, and Open, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The booking](03-the-booking.md) | [queue.py](work/app/queue.py), [file_ain.py](work/app/file_ain.py), and [notify.py](work/app/notify.py) |
| 4 | [The contract](04-the-contract.md) | [contract.py](work/app/contract.py) and [test_contract.py](work/tests/test_contract.py) |
| 5 | [The pages](05-the-pages.md) | [zones.md](work/zones.md), [operators.md](work/operators.md), and [deployment.md](work/deployment.md) |
| 6 | [The readout](06-the-readout.md) | [readout.md](work/readout.md) and [retro.md](work/retro.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check deploy --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check journey --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-deploy passed.
chk-journey passed.
chk-readout passed.
chk-individual-m02 passed.
```

Leave `problem_simulation/build` closed.
