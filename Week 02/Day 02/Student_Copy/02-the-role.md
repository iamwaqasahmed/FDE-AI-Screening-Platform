# 02 — The role

[Chapter 00](00-background.md) said what the four weeks produce. This chapter is how you behave on the client's site today. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The sprint, with the subscriptions before any use of the mart, and the mart clock |
| AI or data engineer | The patient SMS, using a booking reference |
| Application engineer | Intake from the `eref` webhook, and `wf-session-cancelled` for a cancelled clinic session |
| Product manager | The four lines the patient can see |
| Architect | The zone of the integration engine and the zone of the worker |

[Chapter 05](05-the-sprint.md) is the sprint. [Chapter 06](06-the-worker.md) is the two subscriptions. [Chapter 07](07-the-pages.md) is the states, the zones, and the SMS. [Chapter 08](08-the-mart.md) is the mart clock. You do every part.

There is no interview today. The check does not read an interview note. It does not read a note about the engine sample, and it does not read a note about WhatsApp.

## What the assistant may do

The assistant may take `referral.submitted` from the webhook. It may take `session.cancelled`, text the patient about the booking, and release a hold when that text fails.

The assistant does not book from chat today. Booking from chat waits. A field the registry does not list is ignored. The webhook file stays out of `work/`.

## Where today sits

[Chapter 00](00-background.md) has the four-week table. New files arrive on a schedule. Today you work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Coding assistants are allowed on the scripts. [Chapter 06](06-the-worker.md) says what may enter a prompt. The webhook file stays out. [referral.submitted.json](packet/release/webhooks/referral.submitted.json) carries a watermark. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit. Do not copy that webhook file into `work/`.

Next: [03 — The feeds](03-the-feeds.md).
