# 00 — Background

Read this before chapter 01. It says what the four weeks are, what Day 1, Day 2, Day 3, Day 4, Day 5, Week 2 Day 1, Week 2 Day 2, Week 2 Day 3, and Week 2 Day 4 already finished, and what today is inside that story.

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

## What today is

Today steering asks to include Ain. You leave with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stays queued for the nightly file.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the change request, the steering questions, and the six lines the demo prints. You read the nightly file and the missed-night file. The clinic codes stay in those files.
2. You sequence the sprint: smoke, then the change, then the readout, then the retro.
3. You replace the booking, the file, the notice, and the contract. The smoke files stay as they were copied.
4. You map the URL onto `zone-private` and the file path onto `zone-hospital`. You fill the deployment note, including Ain and the change. You write what patients will see, the readout, and the retro.
5. You answer two questions: why Ain cannot confirm a slot today, and what Stage 2 adds to monitoring.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, four checks run. They load the app in `work/app` and read the pages. A miss says the probe does not report the registered hash, the image runs as root, a national id is in the deploy log, prod uses the dev credential, the router leaves the private endpoint, or the deployment note is missing a required fact. It can also say the deployment note promises a live slot, the url is not in zone-private, the file path is not in zone-hospital, the operator steps are missing, or the sprint does not sequence the change before the readout. A journey miss says a live slot was promised, a missed night cleared the slots, the nightly file did not replace yesterday, or a failed notice confirmed a slot. A readout miss says the readout does not answer the smoke test, does not sequence the change, or does not name the file path. An individual miss says the contract test accepted the live-slot fault, or the contract test rejected the queued booking. A check does not name a hash, a token, the quota, a national id, or a clinic code.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence smoke, then the change, then the readout, then the retro | [05](05-the-sprint.md) and [08](08-the-pages.md) |
| AI or data engineer | State `local-small`, the quota, and what Stage 2 adds | [09](09-the-readout.md) and [10](10-finish.md) |
| Application engineer | Keep the smoke files, and replace the booking, the file, the notice, and the contract | [06](06-the-booking.md) and [07](07-the-contract.md) |
| Product manager | Say a patient at Ain sees a queued booking | [09](09-the-readout.md) |
| Architect | Name the nightly file in `zone-hospital` | [06](06-the-booking.md) and [08](08-the-pages.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 02/Day 05/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w2d5` | The name of today's file drop. It means week 2, day 5 |
| `rel-w2d4` | Yesterday's file drop. The checks still read it for the smoke test |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the booking, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
