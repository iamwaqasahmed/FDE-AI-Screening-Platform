# Week 4, Day 2

The replay is already on disk. The morning is a stand-up.

You leave with a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done.

## Roles

| Seat | Today |
|---|---|
| Lead | Owns the timeline |
| AI or data engineer | Reads the model traces |
| Application engineer | Owns the dashboard |
| Product manager | Computes the override rate |
| Architect | Writes the runbook |

## Order

1. [The replay](01-the-replay.md)
2. [The board](02-the-board.md)
3. [The hours](03-the-hours.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w4d2
```

That writes [data/rel-w4d2](../../data/rel-w4d2/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-replay.md](01-the-replay.md)
- [02-the-board.md](02-the-board.md)
- [03-the-hours.md](03-the-hours.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/spans.py](work/app/spans.py)
- [work/app/dashboard.py](work/app/dashboard.py)
- [work/app/meter.py](work/app/meter.py)
- [work/app/cache.py](work/app/cache.py)
- [work/app/drift.py](work/app/drift.py)
- [work/app/override.py](work/app/override.py)
- [work/app/shadow.py](work/app/shadow.py)
- [work/tests/test_spans.py](work/tests/test_spans.py)
- [work/tests/test_dashboard.py](work/tests/test_dashboard.py)
- [work/tests/test_meter.py](work/tests/test_meter.py)
- [work/tests/test_cache.py](work/tests/test_cache.py)
- [work/tests/test_drift.py](work/tests/test_drift.py)
- [work/tests/test_override.py](work/tests/test_override.py)
- [work/tests/test_shadow.py](work/tests/test_shadow.py)
- [work/sprint.md](work/sprint.md)
- [work/timeline.md](work/timeline.md)
- [work/dashboard.md](work/dashboard.md)
- [work/runbook.md](work/runbook.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/ciso.questions.txt](work/interviews/ciso.questions.txt)
- [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md)
- [work/interviews/patient-rep.questions.txt](work/interviews/patient-rep.questions.txt)
- [work/interviews/patient-rep.notes.md](work/interviews/patient-rep.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/spans.py](app/spans.py)
- [app/dashboard.py](app/dashboard.py)
- [app/meter.py](app/meter.py)
- [app/cache.py](app/cache.py)
- [app/drift.py](app/drift.py)
- [app/override.py](app/override.py)
- [app/shadow.py](app/shadow.py)
- [tests/test_spans.py](tests/test_spans.py)
- [tests/test_dashboard.py](tests/test_dashboard.py)
- [tests/test_meter.py](tests/test_meter.py)
- [tests/test_cache.py](tests/test_cache.py)
- [tests/test_drift.py](tests/test_drift.py)
- [tests/test_override.py](tests/test_override.py)
- [tests/test_shadow.py](tests/test_shadow.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/timeline.md](templates/timeline.md)
- [templates/dashboard.md](templates/dashboard.md)
- [templates/runbook.md](templates/runbook.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w4d2/README.md](../../data/rel-w4d2/README.md).

- [data/rel-w4d2/replay/note.md](../../data/rel-w4d2/replay/note.md)
- [data/rel-w4d2/replay/spans.jsonl](../../data/rel-w4d2/replay/spans.jsonl)
- [data/rel-w4d2/dms/circ-ramadan-hours.md](../../data/rel-w4d2/dms/circ-ramadan-hours.md)
- [data/rel-w4d2/events/document-changed.json](../../data/rel-w4d2/events/document-changed.json)
- [data/rel-w4d2/meter/gateway.jsonl](../../data/rel-w4d2/meter/gateway.jsonl)
- [data/rel-w4d2/actions/overrides.jsonl](../../data/rel-w4d2/actions/overrides.jsonl)
- [data/rel-w4d2/drifts/signals.jsonl](../../data/rel-w4d2/drifts/signals.jsonl)
- [data/rel-w4d2/experiment/shadow-extract.json](../../data/rel-w4d2/experiment/shadow-extract.json)
- [data/rel-w4d2/templates/runbook.md](../../data/rel-w4d2/templates/runbook.md)
