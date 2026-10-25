# Week 3, Day 3 — Solution copy

Open this after the attempt.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the chunk split, the local embed, the index, the search, the audience filter, the criteria bind, the citation, the sync, the photo read, the booking conflict, the catalog lookup, the refusal, and the audience table. The four-week job is an assistant for referrals, appointments, reminders, and the phone line. Day 1 was the arrival. Day 2 was the leaders' numbers, the baselines, and the approach memo. Day 3 was `wf-intake`, from `referral.submitted` to a held approval. Day 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Week 2 Day 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Week 2 Day 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Week 2 Day 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Week 2 Day 4 deployed the assistant. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited. Week 2 Day 5 included Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file. Week 3 Day 1 left one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. Week 3 Day 2 left a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed. Today criteria v4 is in force for three specialties. You leave with an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

This folder is one way to finish that day. The example sentences can differ in wording when the sprint still runs index, then filter, then cite, then sync, and limits v4 to endo, ophth, and card, not all specialties, the citation is an in-force span the asker may see, an in-flight referral keeps its start version, the unauthorized circular is not cited, a patient does not see a staff document, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the morning is `Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The index](03-the-index.md) | [chunk.py](work/app/chunk.py), [embed.py](work/app/embed.py), [index.py](work/app/index.py), and [search.py](work/app/search.py) |
| 4 | [The citation](04-the-citation.md) | [filter.py](work/app/filter.py), [bind.py](work/app/bind.py), [cite.py](work/app/cite.py), and [sync.py](work/app/sync.py) |
| 5 | [The advanced path](05-the-advanced.md) | [vision.py](work/app/vision.py), [conflict.py](work/app/conflict.py), and [catalog.py](work/app/catalog.py) |
| 6 | [The pages](06-the-pages.md) | [refusal.md](work/refusal.md) and [audience.md](work/audience.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the checks pass

The course folder is the one that contains `problem_simulation` and `Week 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check rag --release rel-w3d3 --work "../Week 03/Day 03/Solution_Copy/work" --profile practice
python -m alwaha.check hybrid --release rel-w3d3 --work "../Week 03/Day 03/Solution_Copy/work" --profile practice
python -m alwaha.check acl --release rel-w3d3 --work "../Week 03/Day 03/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-w3-rag passed.
slice-hybrid passed.
slice-acl passed.
```

If you see those three lines, the day is finished. Leave `problem_simulation/build` closed.
