# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The check also needs the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 2, Lesson 4 — Deploy. The file drop is `rel-m02-l04`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The Ain change](<../../Lesson 05/Student_Copy/README.md>), file drop `rel-m02-l05`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 2, Lesson 3 was the SMS receipt. The receipt follows the case clock. The access clauses and the usability scripts arrived. You left with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished. Booking from chat waited.

## What this lesson is

Today the deployment standard and the prod credentials arrive. You leave with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat still waits.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the deploy notice, the standard, the register, the credentials, and the two lines the deploy demo prints. The pages are in this folder.
2. You sequence the sprint so the deploy comes before the readout.
3. You replace the image admission, the probe, the router, the credentials, the manifest, and the work pipeline. The probe reports the registered hash. The image account is not root. Prod reads the prod credential.
4. You map the URL onto `zone-private`, write the operator steps, and fill the deployment note.
5. You answer two questions: which zone this URL is in, and what a rollback changes.

At the end, one check runs. It loads the app in `work/app` and reads the pages. A miss says the probe does not report the registered hash, the image runs as root, a national id is in the deploy log, prod uses the dev credential, the router leaves the private endpoint, or the deployment note is missing a required fact. It can also say the manifest is not in the team namespace, the health probe is missing, the pipeline is not in CI, the url is not in zone-private, the operator steps are missing, or the sprint does not book the readout after the deploy. It does not name a hash, a token, the quota, or a national id.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the deploy before the readout | [05](05-the-sprint.md) and [09](09-the-pages.md) |
| AI or data engineer | Make the probe report the registered hash | [07](07-the-probe.md) |
| Application engineer | Replace the image, the manifest, the router, the credentials, and the work pipeline | [06](06-the-image.md), [07](07-the-probe.md), and [08](08-the-endpoint.md) |
| Product manager | Write the operator steps | [09](09-the-pages.md) |
| Architect | Map the URL onto `zone-private` | [09](09-the-pages.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the check reads |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 02/Lesson 04/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m02-l04` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The check in `problem_simulation`. Chapter 01 turns it on. The folder it writes, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the probe, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
