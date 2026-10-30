# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 2, Lesson 5 — The Ain change. The file drop is `rel-m02-l05`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Honest data](<../../../Module 03/Lesson 01/Student_Copy/README.md>), file drop `rel-m03-l01`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Module 2, Lesson 4 was the deployment. The deployment standard and the prod credentials arrived. You left with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat waited.

## What this lesson is

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
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 02/Lesson 05/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m02-l05` | The pack name for this lesson. The checks use it. It is not a schedule |
| `rel-m02-l04` | Yesterday's file drop. The checks still read it for the smoke test |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the booking, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
