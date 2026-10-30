# Module 1, Lesson 5 — Score the proof — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the failures, the trace, the diagram, the readout, and the ask log. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Today the steering questions arrived. The Lesson 4 cases still pass. A timeout does not book. Two patients offered one slot produce one booking.

This folder is one way to finish that day. The example sentences can differ in wording when the trace, the diagram, the design, the readout, and the trace note still match.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 06. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The score](02-the-score.md) | [trace.json](work/trace.json) |
| 3 | [The agent](03-the-agent.md) | [model.py](work/agent/model.py), [schema.py](work/agent/schema.py), and [memory.py](work/agent/memory.py) |
| 4 | [The diagram](04-the-diagram.md) | [architecture.md](work/architecture.md) and [design.md](work/design.md) |
| 5 | [The readout](05-the-readout.md) | [readout.md](work/readout.md) and [trace-note.md](work/trace-note.md) |
| 6 | [Knowledge](06-knowledge.md) | [knowledge.md](work/knowledge.md) |

[07 — Trainer session](07-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 06.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the five python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check agent --release rel-m01-l05 --work "../Module 01/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check trajectory --release rel-m01-l05 --work "../Module 01/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check design --work "../Module 01/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --work "../Module 01/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --work "../Module 01/Lesson 05/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-agent passed.
chk-trajectory passed.
chk-design passed.
chk-readout passed.
chk-individual-m01 passed.
```

Leave `problem_simulation/build` closed.
