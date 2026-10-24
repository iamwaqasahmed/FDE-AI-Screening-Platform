# Week 3, Day 5

Steering asks for the rehearsal brief. The morning is a stand-up. The readout is followed by a short retrospective.

You leave with one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

## Roles

| Seat | Today |
|---|---|
| Lead | Presents |
| AI or data engineer | Owns the remeasure |
| Application engineer | Names the non-goals in the backlog |
| Product manager | Owns the spec |
| Architect | Maps requirements to systems |

## Order

1. [The brief](01-the-brief.md)
2. [The fix](02-the-fix.md)
3. [The spec](03-the-spec.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w3d5
```

That writes [data/rel-w3d5](../../data/rel-w3d5/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-brief.md](01-the-brief.md)
- [02-the-fix.md](02-the-fix.md)
- [03-the-spec.md](03-the-spec.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/repair.py](work/app/repair.py)
- [work/app/remeasure.py](work/app/remeasure.py)
- [work/app/cost.py](work/app/cost.py)
- [work/app/backlog.py](work/app/backlog.py)
- [work/app/gates.py](work/app/gates.py)
- [work/app/personal.py](work/app/personal.py)
- [work/tests/test_repair.py](work/tests/test_repair.py)
- [work/tests/test_remeasure.py](work/tests/test_remeasure.py)
- [work/tests/test_cost.py](work/tests/test_cost.py)
- [work/tests/test_backlog.py](work/tests/test_backlog.py)
- [work/tests/test_gates.py](work/tests/test_gates.py)
- [work/tests/test_personal.py](work/tests/test_personal.py)
- [work/sprint.md](work/sprint.md)
- [work/benchmark.md](work/benchmark.md)
- [work/improvement.md](work/improvement.md)
- [work/rcp/requirements.md](work/rcp/requirements.md)
- [work/readout.md](work/readout.md)
- [work/retro.md](work/retro.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/cdo.questions.txt](work/interviews/cdo.questions.txt)
- [work/interviews/cdo.notes.md](work/interviews/cdo.notes.md)
- [work/interviews/dpo.questions.txt](work/interviews/dpo.questions.txt)
- [work/interviews/dpo.notes.md](work/interviews/dpo.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/repair.py](app/repair.py)
- [app/remeasure.py](app/remeasure.py)
- [app/cost.py](app/cost.py)
- [app/backlog.py](app/backlog.py)
- [app/gates.py](app/gates.py)
- [app/personal.py](app/personal.py)
- [tests/test_repair.py](tests/test_repair.py)
- [tests/test_remeasure.py](tests/test_remeasure.py)
- [tests/test_cost.py](tests/test_cost.py)
- [tests/test_backlog.py](tests/test_backlog.py)
- [tests/test_gates.py](tests/test_gates.py)
- [tests/test_personal.py](tests/test_personal.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/benchmark.md](templates/benchmark.md)
- [templates/improvement.md](templates/improvement.md)
- [templates/requirements.md](templates/requirements.md)
- [templates/readout.md](templates/readout.md)
- [templates/retro.md](templates/retro.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w3d5/README.md](../../data/rel-w3d5/README.md).

- [data/rel-w3d5/notices/rehearsal.md](../../data/rel-w3d5/notices/rehearsal.md)
- [data/rel-w3d5/steering/steer-w3.md](../../data/rel-w3d5/steering/steer-w3.md)
- [data/rel-w3d5/workshop/role-cards.md](../../data/rel-w3d5/workshop/role-cards.md)
- [data/rel-w3d5/gates/stage-gate.md](../../data/rel-w3d5/gates/stage-gate.md)
- [data/rel-w3d5/finance/prices.csv](../../data/rel-w3d5/finance/prices.csv)
- [data/rel-w3d5/budget/labels.json](../../data/rel-w3d5/budget/labels.json)
- [data/rel-w3d5/slices/before.jsonl](../../data/rel-w3d5/slices/before.jsonl)
- [data/rel-w3d5/slices/personal.jsonl](../../data/rel-w3d5/slices/personal.jsonl)
- [data/rel-w3d5/backlog/seed.json](../../data/rel-w3d5/backlog/seed.json)
