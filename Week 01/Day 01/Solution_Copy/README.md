# Week 1, Day 1 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the access request, the rule for the coding assistant, the pipeline, the two interviews, and the zone sketch. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Today was only the arrival. The assistant itself comes later.

This folder is one way to finish that arrival. Your own name on the access request can differ. Another pair of interviews can also pass, when those two conversations reach what those people will say.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 05. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is `Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The reading and the request](02-the-reading-and-the-request.md) | Your morning worksheet and the [finished request](work/access-request.md) |
| 3 | [The pipeline](03-the-pipeline.md) | [app.py](work/app.py) and [scan.py](work/scan.py) |
| 4 | [The interviews](04-the-interviews.md) | [med-dir questions](work/interviews/med-dir.questions.txt) and [dpo questions](work/interviews/dpo.questions.txt) |
| 5 | [Knowledge](05-knowledge.md) | [knowledge.md](work/knowledge.md) |

[06 — Trainer session](06-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 05.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. Then run:

```text
cd problem_simulation
python -m alwaha.check repo --work "../Week 01/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check interview --work "../Week 01/Day 01/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-w1-repo passed.
chk-w1-interview passed.
```

Leave `problem_simulation/build` closed.
