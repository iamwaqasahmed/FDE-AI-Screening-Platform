# Week 3, Day 2 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the prompt baseline, the letter relabel, the message intent, the adapter, the router, the cost, the rank fit, the domain filter, the preference edit, the approach memo, and the residency note. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Day 1 was the arrival. Day 2 was the leaders' numbers, the baselines, and the approach memo. Day 3 was `wf-intake`, from `referral.submitted` to a held approval. Day 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Week 2 Day 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Week 2 Day 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Week 2 Day 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Week 2 Day 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Week 2 Day 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Week 3 Day 1 left one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. Today the ruling is signed. You leave with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs baseline, then adapter, then register, then memo, and says the cloud fine-tune is closed, the prompt stays weak and is not served, the adapter is the approved `lora-local` row, hours stay on retrieval, the four phi fields stay in `zone-private`, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is `Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The baseline](03-the-baseline.md) | [prompt.py](work/app/prompt.py), [extract.py](work/app/extract.py), and [intent.py](work/app/intent.py) |
| 4 | [The adapter](04-the-adapter.md) | [adapter.py](work/app/adapter.py), [route.py](work/app/route.py), and [cost.py](work/app/cost.py) |
| 5 | [The advanced path](05-the-advanced.md) | [qlora.py](work/app/qlora.py), [domain.py](work/app/domain.py), and [prefs.py](work/app/prefs.py) |
| 6 | [The pages](06-the-pages.md) | [approach.md](work/approach.md) and [residency.md](work/residency.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check model --release rel-w3d2 --work "../Week 03/Day 02/Solution_Copy/work" --profile practice
python -m alwaha.check lora --release rel-w3d2 --work "../Week 03/Day 02/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-w3-model passed.
slice-lora passed.
```

Leave `problem_simulation/build` closed.
