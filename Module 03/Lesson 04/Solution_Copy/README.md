# Module 3, Lesson 4 — Measure — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the score, the forecast, the failure names, the judge, the regression, the evaluation gate, the intervals, the experiment, the benchmark, the workshop notes, and the knowledge file. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Module 2, Lesson 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Module 2, Lesson 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Module 2, Lesson 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Module 2, Lesson 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Module 2, Lesson 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Module 3, Lesson 1 left one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. Module 3, Lesson 2 left a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed. Module 3, Lesson 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation. Today the hidden-test protocol is open. You leave with a draft benchmark that names the four planted failures with evidence, and with workshop notes. Labels stay on the grading service. A second measured run waits until Lesson 5.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs score, then failure, then workshop, and keeps the workshop on evidence, the benchmark names the four logs and the three metrics against their budgets, the workshop names the four seats and says the dot-vote is not the value model, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The harness](03-the-harness.md) | [score.py](work/app/score.py), [forecast.py](work/app/forecast.py), and [failures.py](work/app/failures.py) |
| 4 | [The gate](04-the-gate.md) | [judge.py](work/app/judge.py), [gate.py](work/app/gate.py), and [ci.yml](work/.github/workflows/ci.yml) |
| 5 | [The advanced path](05-the-advanced.md) | [intervals.py](work/app/intervals.py) and [experiment.py](work/app/experiment.py) |
| 6 | [The pages](06-the-pages.md) | [benchmark.md](work/benchmark.md), [workshop.md](work/workshop.md), and [experiment.md](work/experiment.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check eval --release rel-m03-l04 --work "../Module 03/Lesson 04/Solution_Copy/work" --profile practice
python -m alwaha.check judge --release rel-m03-l04 --work "../Module 03/Lesson 04/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-eval passed.
slice-judge passed.
```

If you see those two lines, the day is finished. Leave `problem_simulation/build` closed.
