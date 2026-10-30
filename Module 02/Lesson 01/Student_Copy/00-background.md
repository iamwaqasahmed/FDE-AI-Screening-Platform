# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 2, Lesson 1 — Sign in. The file drop is `rel-m02-l01`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Feeds](<../../Lesson 02/Student_Copy/README.md>), file drop `rel-m02-l02`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Lesson 5 was the steering readout. The Lesson 4 cases still passed. A timeout does not book. Two patients offered one slot produce one booking. You drew the architecture, wrote the design, answered the steering questions, and wrote a trace note for the emergency scenario.

## What this lesson is

Today is the first morning of Module 2. `his-wadi` publishes a new spec, and levels of assurance are published with it. You leave with a patient and a coordinator who can open the assistant, a session row in the application database, and a status question that still uses the Module 1 tool. Booking waits.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the FHIR notice and the new his-wadi spec. The pages are in this folder.
2. You sequence the sprint so the generated client comes before any booking.
3. You write the sign-in states and the token flow.
4. You generate the client, sign in the patient and the coordinator, and answer one status question with the Module 1 status tool.
5. You answer two questions: which assurance level may book, and where the session row lives.

At the end, two checks run. They load the shell in `work/app` and the three pages. A miss on the first check does not print the role list or the assurance level. A miss on the status read says the his-wadi read failed. It does not name a field or a count.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the sprint so the client comes before booking | [05](05-the-notice.md) |
| AI or data engineer | Keep the Module 1 status tool on the status question | [07](07-the-status.md) |
| Application engineer | Open the two pages and keep the session row | [07](07-the-status.md) |
| Product manager | Write the sign-in states | [06](06-the-sign-in.md) |
| Architect | Write the token flow | [06](06-the-sign-in.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 02/Lesson 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m02-l01` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the states, and the token flow, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
