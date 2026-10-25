# 00 — Background

Read this before chapter 01. It says what the four weeks are, what Day 1, Day 2, Day 3, Day 4, Day 5, Week 2 Day 1, and Week 2 Day 2 already finished, and what today is inside that story.

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

## What today is

Today the SMS receipt follows the case clock. The access clauses and the usability scripts arrive. You leave with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat still waits.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the timing notice, the clock file, and the two lines the receipt demo prints. The pages are in this folder.
2. You sequence the sprint so the suite comes before usability sign-off.
3. You replace the calendar, the reply, the receipt, and the four tests. The suite goes red when the switch is on.
4. You finish `status-short` and `caregiver`, name the switch on the definition of done, and write the two zone rows and the fixture note.
5. You answer two questions: why a fixed sleep is a bad receipt test, and what makes a journey test an AI test.

At the end, two checks run. The first loads the app in `work/app`. A miss says the calendar does not match, the receipt test sleeps, the suite accepted the receipt fault, the reply schema is missing, or the journey followed the sentence. It does not name an interval, a delay, or a due date. The second reads the pages. A miss says a usability script is unfinished, an accessibility clause is missing, the fault is not in the definition of done, or a zone-crossing case is missing. It does not name the script, the clause, or the case.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the suite before sign-off, and name the switch | [05](05-the-sprint.md) and [09](09-the-pages.md) |
| AI or data engineer | Write the fixture note | [09](09-the-pages.md) |
| Application engineer | Replace the calendar, the reply, and the receipt | [06](06-the-calendar.md), [07](07-the-reply.md), and [08](08-the-receipt.md) |
| Product manager | Finish `status-short` and `caregiver` | [09](09-the-pages.md) |
| Architect | Write the two zone rows | [09](09-the-pages.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 02/Day 03/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w2d3` | The name of today's file drop. It means week 2, day 3 |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the suite, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
