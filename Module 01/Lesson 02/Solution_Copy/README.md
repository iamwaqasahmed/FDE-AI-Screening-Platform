# Module 1, Lesson 2 — The approach — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the baselines, the choice of what is a tool, the ranking, the challenge to the sponsor sentence, and the system of record on each row. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Today the leaders' numbers arrived. The assistant itself comes later.

This folder is one way to finish that day. Another ranking order can also pass. The example reasons can differ in wording when the family, the measurement, and the citation still match.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 05. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The extracts](02-the-extracts.md) | The figures you copied, and the claims in [brief.md](work/brief.md) |
| 3 | [The baselines](03-the-baselines.md) | [baseline-output.md](work/baseline-output.md) |
| 4 | [The memo](04-the-memo.md) | [approach.md](work/approach.md) and [brief.md](work/brief.md) |
| 5 | [Knowledge](05-knowledge.md) | [knowledge.md](work/knowledge.md) |

[06 — Trainer session](06-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 05.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. Then run:

```text
cd problem_simulation
python -m alwaha.check approach --work "../Module 01/Lesson 02/Solution_Copy/work" --profile practice
python -m alwaha.check brief --work "../Module 01/Lesson 02/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-approach passed.
chk-brief passed.
```

Leave `problem_simulation/build` closed.
