# 00 — Background

Read this before chapter 01. It says what the four weeks are, what Day 1, Day 2, Day 3, Day 4, Day 5, Week 2 Day 1, Week 2 Day 2, Week 2 Day 3, Week 2 Day 4, Week 2 Day 5, and Week 3 Day 1 already finished, and what today is inside that story.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Week 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For these four weeks the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The four weeks, in order:

| Week | You leave with |
| --- | --- |
| 1 | A small working proof of the assistant, a picture of the design, and a note that says why |
| 2 | The assistant signed in to the cluster and deployed on the cluster's private cloud |
| 3 | Models fitted to the cluster, answers drawn from the cluster's documents, and an evaluation |
| 4 | Security, monitoring, a design that can take a surge, and a plan for running it |

Each morning the cluster hands you only that day's files. A choice that is reasonable today can be incomplete by Thursday, because a later morning brings a file you do not have yet. Today you stay inside this folder.

## What Day 1 already finished

Day 1 was the arrival. You filed an access request. You kept a tiny pipeline green, and you left the sample letter and the watermark out of it. You interviewed two people. You sketched the three zones from the kickoff. You still had no measurements. A leader's sentence from that morning is still a claim until a file or a baseline supports it.

## What Day 2 already finished

Day 2 was the leaders' numbers. You read nine problems and the pages of figures. You ran four baselines. You wrote an approach memo and a draft brief. A figure on those pages stayed a claim until a baseline printed it, or until you could point at the number in a file. One of those problems was the wait-time clock. The date column on that extract is the column Week 2 Day 2 named again.

## What Day 3 already finished

Day 3 was the intake workflow. The event stream, the SLA policy, and the business calendar arrived. `wf-intake` runs from `referral.submitted` to a held approval. That workflow does not accept, return, or book. It stops for a coordinator.

## What Day 4 already finished

Day 4 was the medical director's rules. The approval policy, the routing list, the tool catalog, and the scenario slice arrived. You ran `wf-self-service`. A patient can ask for status and book a slot. A return cannot leave without a coordinator. You kept the trace and wrote a one-page agent note.

## What Day 5 already finished

Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. You drew the architecture, wrote the design, answered the steering questions, and wrote a trace note for the emergency scenario.

## What Week 2 Day 1 already finished

Week 2 Day 1 was sign-in. `his-wadi` published a new spec, and levels of assurance were published with it. A patient and a coordinator can open the assistant. The session row is in the application database. One status question still uses the Week 1 tool. Booking waited.

## What Week 2 Day 2 already finished

Week 2 Day 2 was the feeds. `eref` pushes `referral.submitted`. A cancelled clinic session arrives as `session.cancelled`. HL7 from two hospitals arrives through the integration engine. WhatsApp is open beside SMS. You left with intake from the `eref` webhook, `wf-session-cancelled` on the dev namespace, and a mart read labeled with the clock the team already distrusts. Booking from chat waited.

## What Week 2 Day 3 already finished

Week 2 Day 3 was the SMS receipt. The receipt follows the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat waited.

## What Week 2 Day 4 already finished

Week 2 Day 4 was the deployment. The deployment standard and the prod credentials arrived. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited.

## What Week 2 Day 5 already finished

Week 2 Day 5 was the change to include Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file.

## What Week 3 Day 1 already finished

Week 3 Day 1 was the approved data request. You left with one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. A mother and a newborn stayed two people. Phone photos were photos. The sample did not copy a real letter.

## What today is

Today the ruling is signed. You leave with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the ruling, the model register, the quota, the price cap, and the slices. You run the demo. It prints one line. You do not type that line's hidden mark. The line does not print the mark.
2. You sequence the sprint: the baseline, then the adapter, then the register, then the memo. The cloud fine-tune is closed.
3. You replace the prompt, the letter relabel, and the message intent. The prompt stays weak, and it is not served.
4. You replace the adapter, the router, and the cost. You also replace the rank fit, the domain filter, and the preference edit. The two checks do not require those last three. You still replace them. You do not delete them.
5. You revise the approach memo, you record residency, and you answer two questions: which problem stays on retrieval, and which hash is legal to serve.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, two checks run. They load the app in `work/app` and the model check reads the pages. A model miss can say the prompt baseline is still the served model, extraction F1 is outside the budget, intent F1 is outside the budget, the cost is over the price cap, the call sends phi to ext-large, the hash is not on reg-models, the gpu count is over the quota, the latency is over the budget, the adapter did not run, hours questions are not left on retrieval, dna is not a tabular model, family does not fit, the measured value does not match the adapter, the residency note lets a phi field leave, approach.md is missing, sprint.md does not sequence the adapter, knowledge.md needs two answers, knowledge.md does not say which problem stays on retrieval, or knowledge.md does not say which hash is legal to serve. A LoRA miss can say the prompt baseline clears the slice, ext-large at the price cap does not clear the slice, or the adapter did not run. A check does not print a hash, a GPU count, a price, an F1, or a gold label. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the baseline, then the adapter, then the register, then the memo, and close the cloud fine-tune | [05](05-the-sprint.md) |
| AI or data engineer | Serve the registered adapter, and fit the rank, the domain lines, and the preference edit | [07](07-the-adapter.md) and [08](08-the-advanced.md) |
| Application engineer | Keep the prompt weak and local, relabel the letters, classify the messages, refuse a bad call, and price the local tokens | [06](06-the-baseline.md) and [07](07-the-adapter.md) |
| Product manager | Revise the approach memo and keep the Week 1 families | [09](09-the-pages.md) |
| Architect | Record residency for the phi fields, and answer which hash is legal to serve | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 03/Day 02/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w3d2` | The name of today's file drop. It means week 3, day 2 |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the adapter, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Week 3 Day 1 left, and what you leave with today: a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

Next: [01 — Setup](01-setup.md).
