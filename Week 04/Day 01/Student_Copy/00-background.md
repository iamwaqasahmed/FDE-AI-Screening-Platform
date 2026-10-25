# 00 — Background

Read this before chapter 01. It says what the four weeks are, what Week 1 Day 1 through Day 5, Week 2 Day 1 through Day 5, Week 3 Day 1 through Day 5 already finished, and what today is inside that story.

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

## What Week 3 Day 2 already finished

Week 3 Day 2 was the signed ruling. You left with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

## What Week 3 Day 3 already finished

Week 3 Day 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

## What Week 3 Day 4 already finished

Week 3 Day 4 left a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stayed on the grading service. The second measured run waited until Week 3 Day 5.

## What Week 3 Day 5 already finished

Week 3 Day 5 left one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

## What today is

Today the attack window is open. You leave with guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read today's drop. You run the demo. It prints two lines. It does not print ignore. You interview the CISO. The notes for that interview are pasted later.
2. You sequence the sprint: the notice, then the guardrail, then access, then the DPIA, then the request.
3. You replace the guard, the output, the supply check, the log redaction, and the session limit, and you replace the work copies of their tests.
4. You replace access and deletion, and their tests. Then you replace the disparity and the stamp rate, and that test. The suite imports all eight app files. You do not delete any of them.
5. You write the guardrail page, the DPIA, the two requests, the breach note, and the CISO notes, and you answer two questions: when the 72-hour clock starts, and what excessive agency is in `wf-intake`.

Chapters 00 through 04 are reading, the demo, and the CISO interview. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, four checks run. The redteam check loads `guard.py`, `output.py`, `supply.py`, `redact.py`, and `limit.py` from `work/app`. It also reads the families in `guardrails.json`. The privacy check loads `erase.py`. It reads `sprint.md`, `dpia.md`, `requests.md`, `breach.md`, `knowledge.md`, and `interviews/ciso.notes.md`. The access check loads `access.py`. It reads the checklist in `guardrails.json`. The fair check loads `fair.py`. The suite imports all eight app modules. None of them is optional. A guard, output, supply, redact, limit, or guardrail-family miss fails only the redteam check. A sprint, DPIA, request, breach, knowledge, CISO-note, or erase miss fails only the privacy check. An access-module miss, or a checklist miss in `guardrails.json`, fails only the access check. A `fair.py` miss fails only the fair check.

A redteam miss can say a letter still books a slot, the hidden prompt is returned, a booking runs with no approval, model html is still rendered, an unregistered hash still loads, a tool description still runs, a poisoned label is still accepted, an unauthorized circular is still cited, a superseded circular is still cited, a canary or a national id is still in the log, a session exceeds the token cap, a hold does not expire, the guardrail config misses a family, a direct injection still runs a tool, a clean label is dropped, an in-force document is replaced, or the harness did not run. A privacy miss can say the DPIA misses a required field, the breach clock does not start at the notice, the patient reply is missing, the deletion request leaves a store, sprint.md does not open the notice first, knowledge.md needs two answers, knowledge.md does not say when the clock starts, knowledge.md does not say what excessive agency is, the ciso notes miss the log or the checklist, the access export is incomplete, deletion leaves the vector index, deletion leaves memory, a permitted log still returns the person, or the harness did not run. An access miss can say a stale staff grant is still open, an expired delegate can still book, break-glass has no audit row, the go-live checklist is incomplete, an open staff grant was closed, or the harness did not run. A fair miss can say the disparity table hides a district or an insurance class, the rubber-stamp rate is missing, the disparity is outside the published bound, or the harness did not run. A failure does not print a hash, a canary, a national id, the case timestamp, a change id, a rate, or the bound. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Open the notice first, then the breach timeline | [05](05-the-sprint.md) and [09](09-the-pages.md) |
| AI or data engineer | Load a hash only when it is on the register, then file the disparity and the stamp rate | [06](06-the-guard.md) and [08](08-the-fair.md) |
| Application engineer | Turn on guardrails, and delete the person from the row, memory, the index, and the logs | [06](06-the-guard.md) and [07](07-the-request.md) |
| Product manager | Write the reply: the records are removed, and no slot was booked from the letter | [09](09-the-pages.md) |
| Architect | Complete the DPIA, and answer when the clock starts and what excessive agency is | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 04/Day 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w4d1` | The name of today's file drop. It means week 4, day 1 |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the guard, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Week 3 Day 5 left, and what you leave with today: guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done.

Next: [01 — Setup](01-setup.md).
