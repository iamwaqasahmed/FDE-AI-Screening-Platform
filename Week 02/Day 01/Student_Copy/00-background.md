# 00 — Background

Read this before chapter 01. It says what the four weeks are, what Day 1, Day 2, Day 3, Day 4, and Day 5 already finished, and what today is inside that story.

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

Day 2 was the leaders' numbers. You read nine problems and the pages of figures. You ran four baselines. You wrote an approach memo and a draft brief. A figure on those pages stayed a claim until a baseline printed it, or until you could point at the number in a file.

## What Day 3 already finished

Day 3 was the intake workflow. The event stream, the SLA policy, and the business calendar arrived. `wf-intake` runs from `referral.submitted` to a held approval. That workflow does not accept, return, or book. It stops for a coordinator.

## What Day 4 already finished

Day 4 was the medical director's rules. The approval policy, the routing list, the tool catalog, and the scenario slice arrived. You ran `wf-self-service`. A patient can ask for status and book a slot. A return cannot leave without a coordinator. You kept the trace and wrote a one-page agent note.

## What Day 5 already finished

Day 5 was the steering readout. The Day 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. You drew the architecture, wrote the design, answered the steering questions, and wrote a trace note for the emergency scenario.

## What today is

Today is the first morning of Week 2. `his-wadi` publishes a new spec, and levels of assurance are published with it. You leave with a patient and a coordinator who can open the assistant, a session row in the application database, and a status question that still uses the Week 1 tool. Booking waits.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the FHIR notice and the new his-wadi spec. The pages are in this folder.
2. You sequence the sprint so the generated client comes before any booking.
3. You write the sign-in states and the token flow.
4. You generate the client, sign in the patient and the coordinator, and answer one status question with the Week 1 status tool.
5. You answer two questions: which assurance level may book, and where the session row lives.

At the end, two checks run. They load the shell in `work/app` and the three pages. A miss on the first check does not print the role list or the assurance level. A miss on the status read says the his-wadi read failed. It does not name a field or a count.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the sprint so the client comes before booking | [05](05-the-notice.md) |
| AI or data engineer | Keep the Week 1 status tool on the status question | [07](07-the-status.md) |
| Application engineer | Open the two pages and keep the session row | [07](07-the-status.md) |
| Product manager | Write the sign-in states | [06](06-the-sign-in.md) |
| Architect | Write the token flow | [06](06-the-sign-in.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 02/Day 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w2d1` | The name of today's file drop. It means week 2, day 1 |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the states, and the token flow, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
