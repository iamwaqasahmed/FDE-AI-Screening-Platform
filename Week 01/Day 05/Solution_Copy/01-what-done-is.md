# 01 — What done is

This page is the map. The day is finished by the agent, the trace, the diagram, the design, the readout, the trace note, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [agent/model.py](work/agent/model.py) | `wf-self-service`, including a timeout and one booking for two patients on one slot. Explained in [chapter 03](03-the-agent.md) |
| [agent/schema.py](work/agent/schema.py) | The reply and the trace row. A count is the tool result, or empty. `failure` names `timeout` or `race-slot`. Explained in chapter 03 |
| [agent/memory.py](work/agent/memory.py) | Session facts, and a preference only when consent allows it. Explained in chapter 03 |
| [agent/tools.py](work/agent/tools.py) | The mock client. It was not changed |
| [agent/run.py](work/agent/run.py) | The runner. It was not changed |
| [trace.json](work/trace.json) | The trace the runner writes. Explained in [chapter 02](02-the-score.md) |
| [architecture.md](work/architecture.md) | The diagram, the zones, and the tools. Explained in [chapter 04](04-the-diagram.md) |
| [design.md](work/design.md) | The approach, what this proof will not build, and stage 2. Explained in chapter 04 |
| [readout.md](work/readout.md) | The answers to the steering questions. Explained in [chapter 05](05-the-readout.md) |
| [trace-note.md](work/trace-note.md) | The emergency row: the tool, the document, and the refusal. Explained in chapter 05 |
| [cdo.notes.md](work/interviews/cdo.notes.md) | What the chief digital officer says about the board date. You were not asked to write this note. The checks do not read it |
| [dpo.notes.md](work/interviews/dpo.notes.md) | What the data protection officer says about where patient data sits. You were not asked to write this note. The checks do not read it |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 06](06-knowledge.md) |

The checks print `passed` when they can run the agent, the trace matches the approval rules and the two new failures, the diagram has a human step, the design leaves urgency with a clinician, the readout answers the five questions, and the trace note names the emergency tool, the document, and the refusal. They do not grade the sentences in `knowledge.md`. The trainer reads those. The design check only checks that both answers are there.

The checks run `run.py` again. A trace you typed by hand is not what they grade. This copy of the trace is here so you can read the rows beside chapter 02.

The scenario files are not in this folder. A copy of one here would fail the checks.

Next: [02 — The score](02-the-score.md).
