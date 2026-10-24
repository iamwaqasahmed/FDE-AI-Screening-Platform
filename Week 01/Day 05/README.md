# Week 1, Day 5

The proof of concept runs. Today the steering questions arrive.

You leave with a score for the scenario set, including a timeout and a slot race, plus `architecture.md`, `design.md`, and the readout. The morning is a stand-up. The readout is followed by a short retrospective.

## Roles

| Seat | Today |
|---|---|
| Lead | Owns the ask log |
| AI or data engineer | Presents the failures |
| Application engineer | Presents the trace |
| Product manager | Leads the readout |
| Architect | Presents the diagram |

## Order

1. [The questions](01-the-questions.md)
2. [The score](02-the-score.md)
3. [The note](03-the-note.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w1d5
```

That writes [data/rel-w1d5](../../data/rel-w1d5/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/architecture.md). Leave the agent in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-questions.md](01-the-questions.md)
- [02-the-score.md](02-the-score.md)
- [03-the-note.md](03-the-note.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/agent/run.py](work/agent/run.py)
- [work/agent/model.py](work/agent/model.py)
- [work/agent/schema.py](work/agent/schema.py)
- [work/agent/memory.py](work/agent/memory.py)
- [work/agent/tools.py](work/agent/tools.py)
- [work/architecture.md](work/architecture.md)
- [work/design.md](work/design.md)
- [work/readout.md](work/readout.md)
- [work/trace-note.md](work/trace-note.md)
- [work/knowledge.md](work/knowledge.md)
- [work/trace.json](work/trace.json)
- [work/interviews/cdo.questions.txt](work/interviews/cdo.questions.txt)
- [work/interviews/cdo.notes.md](work/interviews/cdo.notes.md)
- [work/interviews/dpo.questions.txt](work/interviews/dpo.questions.txt)
- [work/interviews/dpo.notes.md](work/interviews/dpo.notes.md)

Agent and the templates:

- [agent/run.py](agent/run.py)
- [agent/model.py](agent/model.py)
- [agent/schema.py](agent/schema.py)
- [agent/memory.py](agent/memory.py)
- [agent/tools.py](agent/tools.py)
- [templates/architecture.md](templates/architecture.md)
- [templates/design.md](templates/design.md)
- [templates/readout.md](templates/readout.md)
- [templates/trace-note.md](templates/trace-note.md)

## Files in the release

These appear after the build. Open them from [data/rel-w1d5/README.md](../../data/rel-w1d5/README.md).

- [data/rel-w1d5/steering/steer-w1.md](../../data/rel-w1d5/steering/steer-w1.md)
- [data/rel-w1d5/scenarios/ds-failures.jsonl](../../data/rel-w1d5/scenarios/ds-failures.jsonl)
- [data/rel-w1d5/scenarios/order.json](../../data/rel-w1d5/scenarios/order.json)

The build also copies the blank templates into the pack. Use the copies under `work/` when you change a file. Read the scenarios where they already sit. The Day 4 pack stays where it is.
