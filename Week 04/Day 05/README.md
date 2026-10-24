# Week 4, Day 5

The contact center, the warehouse, and HR asked to be connected. The morning is a stand-up. The readout is followed by a short retrospective.

You leave with staff sign-in and the bus still up after the drill, a handoff that has a summary, a late leave that cancels a session, a warehouse clock that is not the booking date, and a proposal that can be presented. A roadmap that starts with triage, or a handoff with no summary, is not done.

## Roles

| Seat | Today |
|---|---|
| Lead | Presents |
| AI or data engineer | Brings measured results into the success metrics |
| Application engineer | Owns the handoff |
| Product manager | Owns the ranking and the roadmap |
| Architect | Owns both architecture documents |

## Order

1. [The requests](01-the-requests.md)
2. [The connections](02-the-connections.md)
3. [The proposal](03-the-proposal.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w4d5
```

That writes [data/rel-w4d5](../../data/rel-w4d5/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-requests.md](01-the-requests.md)
- [02-the-connections.md](02-the-connections.md)
- [03-the-proposal.md](03-the-proposal.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/signin.py](work/app/signin.py)
- [work/app/bus.py](work/app/bus.py)
- [work/app/handoff.py](work/app/handoff.py)
- [work/app/leave.py](work/app/leave.py)
- [work/app/warehouse.py](work/app/warehouse.py)
- [work/app/rank.py](work/app/rank.py)
- [work/app/gates.py](work/app/gates.py)
- [work/app/personal.py](work/app/personal.py)
- [work/tests/test_signin.py](work/tests/test_signin.py)
- [work/tests/test_bus.py](work/tests/test_bus.py)
- [work/tests/test_handoff.py](work/tests/test_handoff.py)
- [work/tests/test_leave.py](work/tests/test_leave.py)
- [work/tests/test_warehouse.py](work/tests/test_warehouse.py)
- [work/tests/test_rank.py](work/tests/test_rank.py)
- [work/tests/test_gates.py](work/tests/test_gates.py)
- [work/tests/test_personal.py](work/tests/test_personal.py)
- [work/sprint.md](work/sprint.md)
- [work/architecture-deploy.md](work/architecture-deploy.md)
- [work/operations.md](work/operations.md)
- [work/rcp/proposal.md](work/rcp/proposal.md)
- [work/readout.md](work/readout.md)
- [work/retro.md](work/retro.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/access-mgr.questions.txt](work/interviews/access-mgr.questions.txt)
- [work/interviews/access-mgr.notes.md](work/interviews/access-mgr.notes.md)
- [work/interviews/ea.questions.txt](work/interviews/ea.questions.txt)
- [work/interviews/ea.notes.md](work/interviews/ea.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/signin.py](app/signin.py)
- [app/bus.py](app/bus.py)
- [app/handoff.py](app/handoff.py)
- [app/leave.py](app/leave.py)
- [app/warehouse.py](app/warehouse.py)
- [app/rank.py](app/rank.py)
- [app/gates.py](app/gates.py)
- [app/personal.py](app/personal.py)
- [tests/test_signin.py](tests/test_signin.py)
- [tests/test_bus.py](tests/test_bus.py)
- [tests/test_handoff.py](tests/test_handoff.py)
- [tests/test_leave.py](tests/test_leave.py)
- [tests/test_warehouse.py](tests/test_warehouse.py)
- [tests/test_rank.py](tests/test_rank.py)
- [tests/test_gates.py](tests/test_gates.py)
- [tests/test_personal.py](tests/test_personal.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/architecture-deploy.md](templates/architecture-deploy.md)
- [templates/operations.md](templates/operations.md)
- [templates/proposal.md](templates/proposal.md)
- [templates/readout.md](templates/readout.md)
- [templates/retro.md](templates/retro.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w4d5/README.md](../../data/rel-w4d5/README.md).

- [data/rel-w4d5/connect/requests.json](../../data/rel-w4d5/connect/requests.json)
- [data/rel-w4d5/iam/staff.json](../../data/rel-w4d5/iam/staff.json)
- [data/rel-w4d5/bus/events.jsonl](../../data/rel-w4d5/bus/events.jsonl)
- [data/rel-w4d5/cc/handoff.jsonl](../../data/rel-w4d5/cc/handoff.jsonl)
- [data/rel-w4d5/hr/leave.jsonl](../../data/rel-w4d5/hr/leave.jsonl)
- [data/rel-w4d5/warehouse/feed.jsonl](../../data/rel-w4d5/warehouse/feed.jsonl)
- [data/rel-w4d5/value/model.json](../../data/rel-w4d5/value/model.json)
- [data/rel-w4d5/survey/readiness.json](../../data/rel-w4d5/survey/readiness.json)
- [data/rel-w4d5/raci/assistant.json](../../data/rel-w4d5/raci/assistant.json)
- [data/rel-w4d5/gates/stage-gate.md](../../data/rel-w4d5/gates/stage-gate.md)
- [data/rel-w4d5/personal/attack.json](../../data/rel-w4d5/personal/attack.json)
- [data/rel-w4d5/steering/steer-w4.md](../../data/rel-w4d5/steering/steer-w4.md)
