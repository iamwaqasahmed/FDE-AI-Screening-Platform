# Module 1, Lesson 4 — The agent — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the emergency phrase, the prompt and the schema, the tool calls, the refusal sentence, and the privilege boundary. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Today the medical director's rules, the scenario slice, and the tool catalog arrived. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator.

This folder is one way to finish that day. The example sentences can differ in wording when the tool trace, the approval, the redirect, and the refusal still match.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 05. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The rules](02-the-rules.md) | The policies and the catalog in `sources/` |
| 3 | [The agent](03-the-agent.md) | [model.py](work/agent/model.py), [schema.py](work/agent/schema.py), and [memory.py](work/agent/memory.py) |
| 4 | [The note](04-the-note.md) | [agent-note.md](work/agent-note.md) and [trace.json](work/trace.json) |
| 5 | [Knowledge](05-knowledge.md) | [knowledge.md](work/knowledge.md) |

[06 — Trainer session](06-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 05.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. Then run:

```text
cd problem_simulation
python -m alwaha.check agent --work "../Module 01/Lesson 04/Solution_Copy/work" --profile practice
python -m alwaha.check trajectory --work "../Module 01/Lesson 04/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-agent passed.
chk-trajectory passed.
```

Leave `problem_simulation/build` closed.
