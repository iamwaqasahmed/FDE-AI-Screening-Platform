# Week 2, Day 1 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the sign-in states, the token flow, the session row, and the status question. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Day 1 was the arrival. Day 2 was the leaders' numbers, the baselines, and the approach memo. Day 3 was `wf-intake`, from `referral.submitted` to a held approval. Day 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Today `his-wadi` published a new spec, and levels of assurance were published with it. A patient and a coordinator can open the assistant. The session row is in the application database. One status question still uses the Week 1 tool. Booking waits.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still generates the client before booking, the states still name the patient, the coordinator, and the first assurance level, the token flow still names the application database and keeps a service token off the patient, and the client is the one the generator writes.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 05. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is `Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [Sign-in](03-the-sign-in.md) | [states.md](work/states.md) and [token-flow.md](work/token-flow.md) |
| 4 | [The status](04-the-status.md) | [client.py](work/app/client.py) |
| 5 | [Knowledge](05-knowledge.md) | [knowledge.md](work/knowledge.md) |

[06 — Trainer session](06-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 05.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the two python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check auth --release rel-w2d1 --work "../Week 02/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check journey --release rel-w2d1 --work "../Week 02/Day 01/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-w2-auth passed.
chk-w2-journey passed.
```

Leave `problem_simulation/build` closed.
