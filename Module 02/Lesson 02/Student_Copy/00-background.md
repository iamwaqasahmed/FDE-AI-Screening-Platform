# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 2, Lesson 2 — Feeds. The file drop is `rel-m02-l02`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The receipt](<../../Lesson 03/Student_Copy/README.md>), file drop `rel-m02-l03`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 2, Lesson 1 was sign-in. `his-wadi` published a new spec, and levels of assurance were published with it. A patient and a coordinator can open the assistant. The session row is in the application database. One status question still uses the Module 1 tool. Booking waited.

## What this lesson is

Today `eref` pushes `referral.submitted`. A cancelled clinic session arrives as `session.cancelled`. HL7 from two hospitals arrives through the integration engine. WhatsApp is open beside SMS. You leave with intake from the `eref` webhook, `wf-session-cancelled` on the dev namespace, and a mart read labeled with the clock the team already distrusts. Booking from chat still waits.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the feeds notice, the schema registry, and the two lines the HL7 demo prints. The pages are in this folder.
2. You sequence the sprint so the subscriptions come before any use of the mart.
3. You subscribe to the webhook and to `session.cancelled`. A repeated event books once. A failed text releases the hold. A cancellation with no slot does not book.
4. You write what the patient sees, where two pieces sit, the SMS line, and the mart clock.
5. You answer two questions: who owns `referral.submitted`, and what a replay of `session.cancelled` does.

At the end, one check runs. It loads the worker in `work/app` and the pages from the sprint, the states, the zones, the SMS, and the mart. It also reads the two answers in `knowledge.md`. A miss says the intake still polls, the replay booked again, the wait number was used as truth, or the knowledge file does not name the owner. It does not print the extra field, the wait figure, or the owner id.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the subscription before the mart, and name the clock | [05](05-the-sprint.md) and [08](08-the-mart.md) |
| AI or data engineer | Write the patient SMS | [07](07-the-pages.md) |
| Application engineer | Subscribe to the webhook and to `session.cancelled` | [06](06-the-worker.md) |
| Product manager | Write what the patient sees | [07](07-the-pages.md) |
| Architect | Place the integration engine and the worker | [07](07-the-pages.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the check reads |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 02/Lesson 02/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m02-l02` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The check in `problem_simulation`. Chapter 01 turns it on. The folder it writes, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the states, the zones, the SMS, and the mart, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
