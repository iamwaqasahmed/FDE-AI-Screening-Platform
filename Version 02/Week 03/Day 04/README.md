# Week 3, Day 4

The hidden-test protocol is open. The morning is a stand-up.

You leave with a draft benchmark that names the four planted failures with evidence, and with workshop notes from `ws-access`. Labels stay on the grading service. A second measured run waits until Day 5.

## Roles

| Seat | Today |
|---|---|
| Lead | Keeps the workshop on evidence |
| AI or data engineer | Computes the metrics |
| Application engineer | Turns one failure into a regression test |
| Product manager | Runs `ws-access` |
| Architect | Records which failure is a design bug |

## Order

1. [The protocol](01-the-protocol.md)
2. [The harness](02-the-harness.md)
3. [The failures](03-the-failures.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w3d4
```

That writes [data/rel-w3d4](../../data/rel-w3d4/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-protocol.md](01-the-protocol.md)
- [02-the-harness.md](02-the-harness.md)
- [03-the-failures.md](03-the-failures.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/score.py](work/app/score.py)
- [work/app/forecast.py](work/app/forecast.py)
- [work/app/failures.py](work/app/failures.py)
- [work/app/judge.py](work/app/judge.py)
- [work/app/intervals.py](work/app/intervals.py)
- [work/app/experiment.py](work/app/experiment.py)
- [work/app/gate.py](work/app/gate.py)
- [work/tests/test_score.py](work/tests/test_score.py)
- [work/tests/test_forecast.py](work/tests/test_forecast.py)
- [work/tests/test_failures.py](work/tests/test_failures.py)
- [work/tests/test_judge.py](work/tests/test_judge.py)
- [work/tests/test_intervals.py](work/tests/test_intervals.py)
- [work/tests/test_experiment.py](work/tests/test_experiment.py)
- [work/tests/test_gate.py](work/tests/test_gate.py)
- [work/sprint.md](work/sprint.md)
- [work/benchmark.md](work/benchmark.md)
- [work/workshop.md](work/workshop.md)
- [work/knowledge.md](work/knowledge.md)
- [work/experiment.md](work/experiment.md)
- [work/interviews/cdo.questions.txt](work/interviews/cdo.questions.txt)
- [work/interviews/cdo.notes.md](work/interviews/cdo.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/score.py](app/score.py)
- [app/forecast.py](app/forecast.py)
- [app/failures.py](app/failures.py)
- [app/judge.py](app/judge.py)
- [app/intervals.py](app/intervals.py)
- [app/experiment.py](app/experiment.py)
- [app/gate.py](app/gate.py)
- [tests/test_score.py](tests/test_score.py)
- [tests/test_forecast.py](tests/test_forecast.py)
- [tests/test_failures.py](tests/test_failures.py)
- [tests/test_judge.py](tests/test_judge.py)
- [tests/test_intervals.py](tests/test_intervals.py)
- [tests/test_experiment.py](tests/test_experiment.py)
- [tests/test_gate.py](tests/test_gate.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/benchmark.md](templates/benchmark.md)
- [templates/workshop.md](templates/workshop.md)
- [templates/knowledge.md](templates/knowledge.md)
- [templates/experiment.md](templates/experiment.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w3d4/README.md](../../data/rel-w3d4/README.md).

- [data/rel-w3d4/notices/hidden-test.md](../../data/rel-w3d4/notices/hidden-test.md)
- [data/rel-w3d4/notices/campaign.md](../../data/rel-w3d4/notices/campaign.md)
- [data/rel-w3d4/notices/ab-status.md](../../data/rel-w3d4/notices/ab-status.md)
- [data/rel-w3d4/budget/metrics.json](../../data/rel-w3d4/budget/metrics.json)
- [data/rel-w3d4/slices/score.jsonl](../../data/rel-w3d4/slices/score.jsonl)
- [data/rel-w3d4/slices/failures.jsonl](../../data/rel-w3d4/slices/failures.jsonl)
- [data/rel-w3d4/slices/calibration.jsonl](../../data/rel-w3d4/slices/calibration.jsonl)
- [data/rel-w3d4/demand/ophth.csv](../../data/rel-w3d4/demand/ophth.csv)
- [data/rel-w3d4/workshop/dot-vote.json](../../data/rel-w3d4/workshop/dot-vote.json)
- [data/rel-w3d4/workshop/seats.md](../../data/rel-w3d4/workshop/seats.md)
- [data/rel-w3d4/experiment/ab-status.json](../../data/rel-w3d4/experiment/ab-status.json)
