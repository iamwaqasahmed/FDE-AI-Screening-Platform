# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 1, Lesson 3 — Intake. The file drop is `rel-m01-l03`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The agent](<../../Lesson 04/Student_Copy/README.md>), file drop `rel-m01-l04`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Lesson 2 was the leaders' numbers. You read nine problems and the pages of figures. You ran four baselines. You wrote an approach memo and a draft brief. A figure on those pages stayed a claim until a baseline printed it, or until you could point at the number in a file.

You are still not building the assistant that books on its own. Today you build the intake workflow that stops for a person.

## What this lesson is

Today the event stream, the SLA policy, and the business calendar arrive. You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do four things, in this order:

1. You read the stream, the policy, the calendar, and the event contract. The pages are in this folder.
2. You run `wf-intake` from `referral.submitted` to a held approval. The workflow does not accept, return, or book.
3. You keep the scenario log the worker writes, and you write a one-page intake note.
4. You answer two questions: which clock starts an SLA, and what a second delivery of the same event should do.

At the end, one check runs the worker again and reads the intake note and the knowledge file. The trainer reads the sentences in `knowledge.md`. On that file the check only requires two numbered lines with a word after the number. It does not grade those sentences. It does grade the worker and the note.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Check the SLA examples against the due dates in the log | [06](06-the-worker.md) |
| AI or data engineer | Read the specialty and the facility from the letter | [06](06-the-worker.md) |
| Application engineer | Replace the worker and the calendar count | [06](06-the-worker.md) |
| Product manager | Write the acceptance line on the intake note | [07](07-the-note.md) |
| Architect | Read the event contract and keep the workflow inside it | [05](05-the-stream.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the check reads |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 01/Lesson 03/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m01-l03` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The check in `problem_simulation`. Chapter 01 turns it on. The folder it writes, `problem_simulation/build`, stays closed |

The cluster's care words, and the workflow words you will use in the log, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
