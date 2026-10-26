# 00 — Background

Read this before chapter 01. It says what the four weeks are, what Week 1 Day 1 through Day 5, Week 2 Day 1 through Day 5, Week 3 Day 1 through Day 5, Week 4 Day 1, Week 4 Day 2, Week 4 Day 3, and Week 4 Day 4 already finished, and what today is inside that story.

This folder is the lesson. The check also needs the course folder, the one that contains `problem_simulation` and `Week 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

Read the section What today is when you want the job for this morning. The sections above it say what the earlier days already finished. You do not paste a file on this page. There is no heading that starts with Replace.

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

## What Week 3 Day 2 already finished

Week 3 Day 2 was the signed ruling. You left with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

## What Week 3 Day 3 already finished

Week 3 Day 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

## What Week 3 Day 4 already finished

Week 3 Day 4 left a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stayed on the grading service. The second measured run waited until Week 3 Day 5.

## What Week 3 Day 5 already finished

Week 3 Day 5 left one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

## What Week 4 Day 1 already finished

Week 4 Day 1 left guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done.

## What Week 4 Day 2 already finished

Week 4 Day 2 left a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done.

## What Week 4 Day 3 already finished

Week 4 Day 3 left the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done.

## What Week 4 Day 4 already finished

Week 4 Day 4 left two replicas, traffic on site-b after site-a dies, the breaker open on insure, and a rent-versus-buy draft that meets 8 February. A booking path that waits on insurance, or a purchase that cannot arrive before Ramadan, is not done.

## What today is

Today the contact center, the warehouse, and HR asked to be connected. You leave with staff sign-in and the bus still up after the drill, a handoff that has a summary, a late leave that cancels a session, a warehouse clock that is not the booking date, and a proposal that can be presented. A roadmap that starts with triage, or a handoff with no summary, is not done.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read today's drop. You run the demo. It prints one line. The line is `Which benefit is counted twice?` It does not say which two lines count the same calls. It does not print a lag, a survey count, or the attack text. You interview the access manager and the enterprise architect. The notes for those interviews are pasted later.
2. You sequence the sprint: the requests, then sign-in, then the bus, then the handoff, then leave, then the warehouse, then the ranking, then the proposal.
3. You replace sign-in, the bus, the handoff, leave, and the warehouse clock, and you replace the work copies of their tests.
4. You replace the ranking, the gate record, and the personal lab, and you replace the work copies of their tests. The suite imports all eight app files. You do not delete any of them.
5. You write the deployment architecture, the operations plan, the proposal, the readout, and the retro, you write both interview notes, and you answer two questions: which event a new consultant leave creates, and which problem is first and which dependency it has.

Chapters 00 through 04 are reading, the demo, and the two interviews. The first file you replace is in chapter 05. You do not run a check until chapter 09. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, five checks run. There is no sixth check. `chk-w4-integrate` loads `signin.py`, `bus.py`, `handoff.py`, `leave.py`, and `warehouse.py` from `work/app`. It also reads `sprint.md`, `interviews/access-mgr.notes.md`, and `interviews/ea.notes.md`. `chk-w4-ops` loads `gates.py` and reads `architecture-deploy.md` and `operations.md`. `chk-w4-rcp` loads `rank.py` and reads `rcp/proposal.md`. `chk-readout` reads `readout.md`, `retro.md`, and `knowledge.md`. `chk-individual-w4` loads `personal.py`. The suite imports all eight app modules. None of them is optional. The question files are not the graded notes.

A miss can say staff sign-in rejects a staff role, a service token is accepted as staff, the bus drops an event with an unknown field, the bus misses session.cancelled, the handoff has no summary, late leave leaves the session published, leave does not emit session.cancelled, the warehouse clock starts at booking, sprint.md does not open the requests first, the access-mgr notes miss the summary, or the ea notes miss late leave. A bus miss is those two bus lines. A late-leave miss is those two leave lines. Do not collapse either pair.

A miss can say the deployment architecture misses a required section, the operations plan misses an owner, the operations plan leaves the clinical safety cell empty, or the operations plan skips G4. The gates miss is the empty cell, then G4. An empty operations page is those two lines plus the missing owner. Do not collapse them.

A miss can say the roadmap starts with p-triage, the ranking follows the dot-vote, the proposal misses a dependency, success metrics were not measured, the adoption plan misses the phone-only channel, the proposal's client is not Al-Waha, the proposal treats the two savings as separate, the proposal contains a banned sentence, rcp/proposal.md is missing, or the harness did not run.

A miss can say the readout does not leave urgency with a clinician, the readout does not keep patient data off the external model, the readout does not name the first problem's dependency, the readout does not say the handoff needs a summary, the readout does not name session.cancelled, the readout does not answer the double-counted benefit, the readout does not name a phone-only channel, the ask log is missing, the readout does not cite a source, the readout contains a banned sentence, readout.md is missing, retro.md is missing, the retro note is missing a heading, knowledge.md does not say which event leave creates, or knowledge.md does not name a first problem and a dependency. An empty readout is that long list. Do not shorten it. `knowledge.md does not say which event leave creates` is the leave-event line. `leave does not emit session.cancelled` is the integrate line. Do not collapse them.

A miss can say the guardrail lets the attack book, the personal lab is missing, or the personal lab did not run. A failure does not print a lag, a survey count, a SAR figure, a hash, or the attack text. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Open the requests first, then present | [05](05-the-sprint.md) and [08](08-the-pages.md) |
| AI or data engineer | Bring a measured problem into the success metrics | [07](07-the-proposal.md) and [08](08-the-pages.md) |
| Application engineer | Keep staff sign-in, the bus, the handoff, late leave, and the warehouse clock | [06](06-the-connections.md) |
| Product manager | Write the ranking and a roadmap that does not start with triage | [07](07-the-proposal.md) and [08](08-the-pages.md) |
| Architect | Write both architecture documents and a proposal that can be presented | [08](08-the-pages.md) and [09](09-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 04/Day 05/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w4d5` | The name of today's file drop. It means week 4, day 5 |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the connections, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Week 4 Day 4 left, and what you leave with today: staff sign-in and the bus still up after the drill, a handoff that has a summary, a late leave that cancels a session, a warehouse clock that is not the booking date, and a proposal that can be presented. A roadmap that starts with triage, or a handoff with no summary, is not done.

Next: [01 — Setup](01-setup.md).
