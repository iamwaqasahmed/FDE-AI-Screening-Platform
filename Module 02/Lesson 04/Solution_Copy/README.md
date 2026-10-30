# Module 2, Lesson 4 — Deploy — Solution copy

Open this after this release's checks have passed.

There is no timetable. Work through the lessons in order.

You spent the day as one forward deployed engineer at the Al-Waha Health Cluster, a made-up health system. You held all five parts yourself: the sprint, the image, the probe, the router, the credentials, the manifest, the work pipeline, the zone row, the operator steps, and the deployment note. The two-module job is an assistant for referrals, appointments, reminders, and the phone line. Lesson 1 was the arrival. Lesson 2 was the leaders' numbers, the baselines, and the approach memo. Lesson 3 was `wf-intake`, from `referral.submitted` to a held approval. Lesson 4 was the medical director's rules. `wf-self-service` runs: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. Module 2, Lesson 1 signed a patient and a coordinator in, wrote the session row, and answered one status question. Booking from chat waited. Module 2, Lesson 2 took the `eref` webhook, subscribed to `session.cancelled`, and labeled the mart clock. Booking from chat still waited. Module 2, Lesson 3 made the SMS receipt follow the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waited. Today the deployment standard and the prod credentials arrive. You leave with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat still waits.

This folder is one way to finish that day. The example sentences can differ in wording when the deploy still comes before the readout, the probe reports the approved `local-small` row, the image account is not root, the national id leaves the emitted log, prod reads the prod credential, the router stays on `ep-local-small` in `zone-private`, the manifest is in `ns-team` with a health probe, the work pipeline runs the suite, the zone row is present, the operator steps name the health probe and prod, the deployment note carries the required facts, and both knowledge answers are present.

## Start here

Open [01 — What done is](01-what-done-is.md). Follow the chapters in number order, from 01 through 07. Finish a chapter before you open the next one.

`work/` in this folder is the finished example. Do not start there. Your own work from the lesson is `../Student_Copy/work`, the folder you filled in beside this one.

## Order

| Order | Chapter | Compare it with |
| --- | --- | --- |
| 1 | [What done is](01-what-done-is.md) | The files linked in that chapter |
| 2 | [The sprint](02-the-sprint.md) | [sprint.md](work/sprint.md) |
| 3 | [The image](03-the-image.md) | [admit.py](work/app/admit.py), [test_admit.py](work/tests/test_admit.py), and [Dockerfile](work/deploy/Dockerfile) |
| 4 | [The probe](04-the-probe.md) | [health.py](work/app/health.py), [test_health.py](work/tests/test_health.py), and [deployment.yaml](work/deploy/deployment.yaml) |
| 5 | [The endpoint](05-the-endpoint.md) | [router.py](work/app/router.py), [secrets.py](work/app/secrets.py), and [ci.yml](work/.github/workflows/ci.yml) |
| 6 | [The pages](06-the-pages.md) | [zones.md](work/zones.md), [operators.md](work/operators.md), and [deployment.md](work/deployment.md) |
| 7 | [Knowledge](07-knowledge.md) | [knowledge.md](work/knowledge.md) |

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it. The answers are in chapters 01 through 07.

## See the check pass

The course folder is the one that contains `problem_simulation` and `Module 01`. On Windows, open it in File Explorer, click the address bar, type `cmd`, and press Enter. On macOS, open Terminal, type `cd ` with a space, drag that folder onto the window, and press Enter. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. Then run:

```text
cd problem_simulation
python -m alwaha.check deploy --release rel-m02-l04 --work "../Module 02/Lesson 04/Solution_Copy/work" --profile practice
```

You should see:

```text
chk-deploy passed.
```

Leave `problem_simulation/build` closed.
