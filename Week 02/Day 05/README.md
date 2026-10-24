# Week 2, Day 5

Steering asks to include Ain. The morning is a stand-up. The readout is followed by a short retrospective.

You leave with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stays queued for the nightly file.

## Roles

| Seat | Today |
|---|---|
| Lead | Presents the change decision |
| AI or data engineer | States the model limits |
| Application engineer | Presents the smoke test |
| Product manager | States what patients at Ain will see |
| Architect | Presents the file path |

## Order

1. [The change](01-the-change.md)
2. [The file](02-the-file.md)
3. [The readout](03-the-readout.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w2d5
```

That writes [data/rel-w2d5](../../data/rel-w2d5/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-change.md](01-the-change.md)
- [02-the-file.md](02-the-file.md)
- [03-the-readout.md](03-the-readout.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/admit.py](work/app/admit.py)
- [work/app/health.py](work/app/health.py)
- [work/app/router.py](work/app/router.py)
- [work/app/secrets.py](work/app/secrets.py)
- [work/app/queue.py](work/app/queue.py)
- [work/app/file_ain.py](work/app/file_ain.py)
- [work/app/notify.py](work/app/notify.py)
- [work/app/contract.py](work/app/contract.py)
- [work/deploy/Dockerfile](work/deploy/Dockerfile)
- [work/deploy/deployment.yaml](work/deploy/deployment.yaml)
- [work/tests/test_admit.py](work/tests/test_admit.py)
- [work/tests/test_health.py](work/tests/test_health.py)
- [work/tests/test_router.py](work/tests/test_router.py)
- [work/tests/test_secrets.py](work/tests/test_secrets.py)
- [work/tests/test_queue.py](work/tests/test_queue.py)
- [work/tests/test_file.py](work/tests/test_file.py)
- [work/tests/test_notify.py](work/tests/test_notify.py)
- [work/tests/test_contract.py](work/tests/test_contract.py)
- [work/sprint.md](work/sprint.md)
- [work/deployment.md](work/deployment.md)
- [work/zones.md](work/zones.md)
- [work/operators.md](work/operators.md)
- [work/readout.md](work/readout.md)
- [work/retro.md](work/retro.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/ea.questions.txt](work/interviews/ea.questions.txt)
- [work/interviews/ea.notes.md](work/interviews/ea.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/admit.py](app/admit.py)
- [app/health.py](app/health.py)
- [app/router.py](app/router.py)
- [app/secrets.py](app/secrets.py)
- [app/queue.py](app/queue.py)
- [app/file_ain.py](app/file_ain.py)
- [app/notify.py](app/notify.py)
- [app/contract.py](app/contract.py)
- [deploy/Dockerfile](deploy/Dockerfile)
- [deploy/deployment.yaml](deploy/deployment.yaml)
- [tests/test_admit.py](tests/test_admit.py)
- [tests/test_health.py](tests/test_health.py)
- [tests/test_router.py](tests/test_router.py)
- [tests/test_secrets.py](tests/test_secrets.py)
- [tests/test_queue.py](tests/test_queue.py)
- [tests/test_file.py](tests/test_file.py)
- [tests/test_notify.py](tests/test_notify.py)
- [tests/test_contract.py](tests/test_contract.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/deployment.md](templates/deployment.md)
- [templates/zones.md](templates/zones.md)
- [templates/operators.md](templates/operators.md)
- [templates/readout.md](templates/readout.md)
- [templates/retro.md](templates/retro.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w2d5/README.md](../../data/rel-w2d5/README.md).

- [data/rel-w2d5/notices/cr-ain.md](../../data/rel-w2d5/notices/cr-ain.md)
- [data/rel-w2d5/systems/sched-ain.md](../../data/rel-w2d5/systems/sched-ain.md)
- [data/rel-w2d5/steering/steer-w2.md](../../data/rel-w2d5/steering/steer-w2.md)
- [data/rel-w2d5/openapi/sched-ain.yaml](../../data/rel-w2d5/openapi/sched-ain.yaml)
- [data/rel-w2d5/fixtures/queued.json](../../data/rel-w2d5/fixtures/queued.json)
- [data/rel-w2d5/fixtures/live-slot.json](../../data/rel-w2d5/fixtures/live-slot.json)
- [data/rel-w2d5/fixtures/nightly.json](../../data/rel-w2d5/fixtures/nightly.json)
- [data/rel-w2d5/fixtures/missed.json](../../data/rel-w2d5/fixtures/missed.json)
