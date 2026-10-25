# 02 — The role

[Chapter 00](00-background.md) said what the four weeks produce. This chapter is how you behave on the client's site today. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The ask log at the bottom of the readout |
| AI or data engineer | The failures named on the trace: a timeout, and one booking when two patients are offered one slot |
| Application engineer | `wf-self-service` still running, with those two failures on the rows |
| Product manager | The readout that answers the steering questions |
| Architect | The diagram, with a human step, and the design |

[Chapter 05](05-the-reading.md) is the reading. [Chapter 06](06-the-agent.md) is the agent and the trace. [Chapter 07](07-the-diagram.md) is the diagram and the design. [Chapter 08](08-the-readout.md) is the readout and the trace note. You do every part.

## What the agent may do

The agent may report status from the status tool, offer a slot, and book after the patient confirms and a coordinator decides. After that booking it sends an SMS.

The agent does not send a return before a coordinator decides. It does not book from a sentence in a letter. It does not book when a routing phrase matches. It does not reuse a stored preference unless consent allows it. It does not book when the offer times out. It does not book the same slot twice.

## Where today sits

[Chapter 00](00-background.md) has the four-week table. New files arrive on a schedule. Today you work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Coding assistants are allowed on the scripts. [Chapter 06](06-the-agent.md) says what may enter a prompt. The scenario files stay out. One letter in [ds-agent.jsonl](packet/day4/scenarios/ds-agent.jsonl) carries a watermark. One letter in [ds-failures.jsonl](packet/release/scenarios/ds-failures.jsonl) carries a watermark. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit.

Next: [03 — The client](03-the-client.md).
