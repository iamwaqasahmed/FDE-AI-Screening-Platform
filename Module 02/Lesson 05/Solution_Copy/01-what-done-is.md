# 01 — What done is

This page is the map. The day is finished by the sprint, the booking, the nightly file, the notice, the contract, the smoke files carried from Lesson 4, the deployment note, the zone rows, the operator steps, the readout, the retro, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Smoke, then the change, then the readout, then the retro. Explained in [chapter 02](02-the-sprint.md) |
| [app/queue.py](work/app/queue.py) | Ain stays queued. A live-slot fault is booked. Explained in [chapter 03](03-the-booking.md) |
| [app/file_ain.py](work/app/file_ain.py) | A missed night keeps yesterday. A new file replaces it. Explained in chapter 03 |
| [app/notify.py](work/app/notify.py) | A queued booking stays queued when the notice fails. Explained in chapter 03 |
| [app/contract.py](work/app/contract.py) | `holds` is true only for `queued`. Explained in [chapter 04](04-the-contract.md) |
| [tests/test_queue.py](work/tests/test_queue.py) | Ain stays queued. The live-slot line still expects `booked` |
| [tests/test_file.py](work/tests/test_file.py) | A missing night keeps yesterday |
| [tests/test_notify.py](work/tests/test_notify.py) | A failed notice stays queued |
| [tests/test_contract.py](work/tests/test_contract.py) | A queued booking stays green. The live-slot fault goes red |
| [app/admit.py](work/app/admit.py) | The Lesson 4 smoke file. It rejects root and drops a national id. It was not rewritten today |
| [app/health.py](work/app/health.py) | The Lesson 4 probe. It reports the approved `local-small` hash |
| [app/router.py](work/app/router.py) | The Lesson 4 router. It stays on `ep-local-small` in `zone-private` |
| [app/secrets.py](work/app/secrets.py) | The Lesson 4 credentials. Prod reads `prod.json` |
| [tests/test_admit.py](work/tests/test_admit.py) | The Lesson 4 admission tests. Same bytes as the packet |
| [tests/test_health.py](work/tests/test_health.py) | The Lesson 4 probe test |
| [tests/test_router.py](work/tests/test_router.py) | The Lesson 4 router test |
| [tests/test_secrets.py](work/tests/test_secrets.py) | The Lesson 4 credential test |
| [deploy/Dockerfile](work/deploy/Dockerfile) | The last account line is `USER 1000`. Same bytes as the packet |
| [deploy/deployment.yaml](work/deploy/deployment.yaml) | Namespace `ns-team`, a non-root account flag, and readiness on `/v1/health`. Same bytes as the packet |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | Runs the suite. Same bytes as the packet |
| [deployment.md](work/deployment.md) | The Lesson 4 headings, plus Ain and Change. Explained in [chapter 05](05-the-pages.md) |
| [zones.md](work/zones.md) | `url` in `zone-private`, and `sched-ain` in `zone-hospital` |
| [operators.md](work/operators.md) | Read the health probe with the prod credential |
| [readout.md](work/readout.md) | The seven headings. Explained in [chapter 06](06-the-readout.md) |
| [retro.md](work/retro.md) | Keep, Drop, and Open |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [ea.notes.md](work/interviews/ea.notes.md) | What the enterprise architect says. The checks do not read it |
| [ea.questions.txt](work/interviews/ea.questions.txt) | The questions that produced those notes. The checks do not read them |

The checks print `passed` when the smoke test still holds, the deployment note carries the Lesson 4 facts plus Ain and Change, the zone table has both rows, the operator steps name health and prod, the sprint sequences smoke before the change before the readout before the retro, Ain stays queued, a missed night keeps yesterday, a failed notice stays queued, the readout answers its headings and cites a source, the retro has three headings, the contract accepts `queued` and rejects `booked`, and both knowledge answers are present.

The live-slot fixture is not in this folder. A copy of it here would fail the check. The message does not print the watermark. The contract test reads that fixture from the built pack.

Next: [02 — The sprint](02-the-sprint.md).
