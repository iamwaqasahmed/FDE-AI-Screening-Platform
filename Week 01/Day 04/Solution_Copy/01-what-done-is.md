# 01 — What done is

This page is the map. The day is finished by the agent, the trace, the agent note, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [agent/model.py](work/agent/model.py) | `wf-self-service`. Turns drive the tools. Explained in [chapter 03](03-the-agent.md) |
| [agent/schema.py](work/agent/schema.py) | The reply and the trace row. A count is the tool result, or empty. Explained in chapter 03 |
| [agent/memory.py](work/agent/memory.py) | Session facts, and a preference only when consent allows it. Explained in chapter 03 |
| [agent/tools.py](work/agent/tools.py) | The mock client. It was not changed |
| [agent/run.py](work/agent/run.py) | The runner. It was not changed |
| [trace.json](work/trace.json) | The trace the runner writes. Explained in [chapter 04](04-the-note.md) |
| [agent-note.md](work/agent-note.md) | The one-page note. Explained in chapter 04 |
| [med-dir.notes.md](work/interviews/med-dir.notes.md) | What the medical director says about urgency, the routing list, and a return. You were not asked to write this note. The checks do not read it |
| [coord-lead.notes.md](work/interviews/coord-lead.notes.md) | What the coordinator lead says about the queue and Thursday afternoon. You were not asked to write this note. The checks do not read it |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 05](05-knowledge.md) |

The checks print `passed` when they can run the agent, the trace matches the approval rules, and the note has the tool list, the privilege boundary, and the refusal sentence. They do not grade the sentences in `knowledge.md`. The trainer reads those.

The checks run `run.py` again. A trace you typed by hand is not what they grade. This copy of the trace is here so you can read the rows beside chapter 04.

The scenario files are not in this folder. A copy of one here would fail the checks.

Next: [02 — The rules](02-the-rules.md).
