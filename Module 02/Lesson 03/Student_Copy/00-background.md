# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 2, Lesson 3 — The receipt. The file drop is `rel-m02-l03`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Deploy](<../../Lesson 04/Student_Copy/README.md>), file drop `rel-m02-l04`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Module 2, Lesson 2 was the feeds. `eref` pushes `referral.submitted`. A cancelled clinic session arrives as `session.cancelled`. HL7 from two hospitals arrives through the integration engine. WhatsApp is open beside SMS. You left with intake from the `eref` webhook, `wf-session-cancelled` on the dev namespace, and a mart read labeled with the clock the team already distrusts. Booking from chat waited.

## What this lesson is

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
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 02/Lesson 03/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m02-l03` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the suite, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
