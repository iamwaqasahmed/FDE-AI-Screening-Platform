# The trace

The runner writes `trace.json`. Do not hand-edit it. The check runs the agent again.

Copy [templates/agent-note.md](templates/agent-note.md) to `Week 01/Day 04/work/agent-note.md`.

Under the tool list, name the tools the agent may call.

Under the privilege boundary, separate extract from book and message. Say when a second agent is worth its tokens: the extractor does not hold the book tool. Status stays one agent and one tool.

Under the refusal, write the sentence a patient sees when a coordinator says no, when a constraint fails, or when a stored preference cannot be reused.

The product manager owns that sentence. The architect owns the boundary. The lead runs the scenario whose message uses a phrase from the routing list, and checks that the trace does not book.
