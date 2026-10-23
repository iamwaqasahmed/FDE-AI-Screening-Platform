# Week 1, Day 4

The intake workflow stops for a person. Today the medical director's rules, the scenario slice, and the tool catalog arrive.

You leave with `wf-self-service` running: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. You also leave a trace and a one-page agent note.

## Roles

| Seat | Today |
|---|---|
| Lead | Tries the emergency phrase |
| AI or data engineer | Owns the prompt and the schema |
| Application engineer | Owns the tools |
| Product manager | Writes what the patient sees on a refusal |
| Architect | Draws the privilege boundary |

## Order

1. [The rules](01-the-rules.md)
2. [The agent](02-the-agent.md)
3. [The trace](03-the-trace.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w1d4
```

That writes [data/rel-w1d4](../../data/rel-w1d4/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/agent-note.md). Leave the agent in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-rules.md](01-the-rules.md)
- [02-the-agent.md](02-the-agent.md)
- [03-the-trace.md](03-the-trace.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/agent/run.py](work/agent/run.py)
- [work/agent/model.py](work/agent/model.py)
- [work/agent/schema.py](work/agent/schema.py)
- [work/agent/memory.py](work/agent/memory.py)
- [work/agent/tools.py](work/agent/tools.py)
- [work/agent-note.md](work/agent-note.md)
- [work/knowledge.md](work/knowledge.md)
- [work/trace.json](work/trace.json)
- [work/interviews/med-dir.questions.txt](work/interviews/med-dir.questions.txt)
- [work/interviews/med-dir.notes.md](work/interviews/med-dir.notes.md)
- [work/interviews/coord-lead.questions.txt](work/interviews/coord-lead.questions.txt)
- [work/interviews/coord-lead.notes.md](work/interviews/coord-lead.notes.md)

Agent and the note:

- [agent/run.py](agent/run.py)
- [agent/model.py](agent/model.py)
- [agent/schema.py](agent/schema.py)
- [agent/memory.py](agent/memory.py)
- [agent/tools.py](agent/tools.py)
- [templates/agent-note.md](templates/agent-note.md)

## Files in the release

These appear after the build. Open them from [data/rel-w1d4/README.md](../../data/rel-w1d4/README.md).

- [data/rel-w1d4/policy/pol-approval.md](../../data/rel-w1d4/policy/pol-approval.md)
- [data/rel-w1d4/policy/pol-clinical-safety.md](../../data/rel-w1d4/policy/pol-clinical-safety.md)
- [data/rel-w1d4/tools/mcp-cluster.json](../../data/rel-w1d4/tools/mcp-cluster.json)
- [data/rel-w1d4/scenarios/ds-agent.jsonl](../../data/rel-w1d4/scenarios/ds-agent.jsonl)
- [data/rel-w1d4/scenarios/ds-sessions.jsonl](../../data/rel-w1d4/scenarios/ds-sessions.jsonl)
- [data/rel-w1d4/scenarios/ds-reason.jsonl](../../data/rel-w1d4/scenarios/ds-reason.jsonl)
- [data/rel-w1d4/scenarios/order.json](../../data/rel-w1d4/scenarios/order.json)

The build also copies the agent and the blank note into the pack. Use the copies under `work/` when you change a script. Read the scenarios where they already sit.
