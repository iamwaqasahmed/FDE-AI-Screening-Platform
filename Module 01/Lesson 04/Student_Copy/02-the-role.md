# 02 — The role

[Chapter 00](00-background.md) said which release this is. This chapter is how you behave on the client's site for this release. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The emergency phrase tried, and a trace that does not book that visit |
| AI or data engineer | A schema the reply fits, and a prompt that follows the approval rules |
| Application engineer | `wf-self-service` running on the tool catalog |
| Product manager | The sentence a patient sees when the visit does not proceed |
| Architect | The privilege boundary: the extractor does not hold book or message |

[Chapter 05](05-the-rules.md) is the reading. [Chapter 06](06-the-agent.md) is the agent and the trace. [Chapter 07](07-the-note.md) is the agent note. You do every part.

## What the agent may do

The agent may report status from the status tool, offer a slot, and book after the patient confirms and a coordinator decides. After that booking it sends an SMS.

The agent does not send a return before a coordinator decides. It does not book from a sentence in a letter. It does not book when a routing phrase matches. It does not reuse a stored preference unless consent allows it.

## Where today sits

[Chapter 00](00-background.md) names this release. New files arrive on a schedule. You work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Coding assistants are allowed on the scripts. [Chapter 06](06-the-agent.md) says what may enter a prompt. The scenario files stay out. One letter in [ds-agent.jsonl](packet/release/scenarios/ds-agent.jsonl) carries a watermark. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit.

Next: [03 — The client](03-the-client.md).
