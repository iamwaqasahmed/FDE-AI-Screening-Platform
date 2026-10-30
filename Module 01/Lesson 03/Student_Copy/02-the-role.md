# 02 — The role

[Chapter 00](00-background.md) said which release this is. This chapter is how you behave on the client's site for this release. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The due dates in the scenario log, checked against the SLA policy and the calendar |
| AI or data engineer | Specialty and facility read from the letter into fixed ids |
| Application engineer | `wf-intake` running from `referral.submitted` to a held approval |
| Product manager | The acceptance line: the workflow stops for a coordinator and does not book |
| Architect | The event contract kept as the shape of every event |

[Chapter 05](05-the-stream.md) is the reading. [Chapter 06](06-the-worker.md) is the worker and the log. [Chapter 07](07-the-note.md) is the intake note. You do every part.

## What the workflow may do

The workflow may extract, retrieve the criteria that is in force, flag a duplicate, suggest a clinic, and stop when a coordinator holds the approval.

The workflow does not accept the referral. It does not return the referral. It does not book a slot. A sentence in a letter must not give a slot away.

## Where today sits

[Chapter 00](00-background.md) names this release. New files arrive on a schedule. You work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Coding assistants are allowed on the scripts. [Chapter 06](06-the-worker.md) says what may enter a prompt. [events/intake.jsonl](packet/release/events/intake.jsonl) stays out. One letter in that file carries a watermark. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit.

Next: [03 — The client](03-the-client.md).
