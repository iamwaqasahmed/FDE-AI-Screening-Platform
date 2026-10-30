# Module 3, Lesson 5 — One fix — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the repair, the second run, the label cost, the backlog, the stage gate, the improvement gate, the personal citation lab, the benchmark, the improvement plan, the rehearsal brief, the readout, the retro, and the knowledge file. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Module 2, Lesson 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Module 2, Lesson 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Module 2, Lesson 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Module 2, Lesson 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Module 2, Lesson 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Module 3, Lesson 1 left one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. Module 3, Lesson 2 left a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed. Module 3, Lesson 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation. Module 3, Lesson 4 left a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stayed on the grading service. The second measured run waited until today. Today you leave with one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs fix, then second, then spec, the benchmark names the four logs and the second run, the improvement page names `cost.label`, the requirements page keeps `p-triage` as a non-goal and says the ranking is not the value model, the readout cites a release file, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The fix](03-the-fix.md) | [repair.py](work/app/repair.py), [remeasure.py](work/app/remeasure.py), and [cost.py](work/app/cost.py) |
| 4 | [The spec](04-the-spec.md) | [backlog.py](work/app/backlog.py), [gates.py](work/app/gates.py), and [ci.yml](work/.github/workflows/ci.yml) |
| 5 | [The personal lab](05-the-personal.md) | [personal.py](work/app/personal.py) |
| 6 | [The pages](06-the-pages.md) | [benchmark.md](work/benchmark.md), [improvement.md](work/improvement.md), [requirements.md](work/rcp/requirements.md), [readout.md](work/readout.md), and [retro.md](work/retro.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check eval --release rel-m03-l05 --work "../Module 03/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check rcp --release rel-m03-l05 --work "../Module 03/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --release rel-m03-l05 --work "../Module 03/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --release rel-m03-l05 --work "../Module 03/Lesson 05/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-eval passed.
chk-m03-l05-rcp passed.
chk-readout passed.
chk-individual-m03-l05 passed.
```

If you see those four lines, the day is finished. Leave `problem_simulation/build` closed.
