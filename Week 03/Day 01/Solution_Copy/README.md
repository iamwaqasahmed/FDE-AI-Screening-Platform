# Week 3, Day 1 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the date conversion, the clinic code, the cluster job, the relabel, the synthetic sample, the scan, the invite-time features, the label budget, the patient page, and the class table. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Day 1 was the arrival. Day 2 was the leaders' numbers, the baselines, and the approach memo. Day 3 was `wf-intake`, from `referral.submitted` to a held approval. Day 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Week 2 Day 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Week 2 Day 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Week 2 Day 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Week 2 Day 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Week 2 Day 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Today the data request is approved. You leave with one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs cluster, then relabel, then sample, then scan, and mentions adjudication, one patient is not one row or one MRN or one national id, the class table marks national id, date of birth, name, and phone as phi, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is `Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The clusters](03-the-clusters.md) | [dates.py](work/app/dates.py), [codes.py](work/app/codes.py), and [cluster.py](work/app/cluster.py) |
| 4 | [The sample](04-the-sample.md) | [labels.py](work/app/labels.py), [synthetic.py](work/app/synthetic.py), and [scan.py](work/app/scan.py) |
| 5 | [The advanced path](05-the-advanced.md) | [pit.py](work/app/pit.py) and [budget.py](work/app/budget.py) |
| 6 | [The pages](06-the-pages.md) | [patients.md](work/patients.md) and [classes.md](work/classes.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check identity --release rel-w3d1 --work "../Week 03/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check labels --release rel-w3d1 --work "../Week 03/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check synthetic --release rel-w3d1 --work "../Week 03/Day 01/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-w3-identity passed.
chk-w3-labels passed.
chk-w3-synthetic passed.
```

Leave `problem_simulation/build` closed.
