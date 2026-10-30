# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 1, Lesson 4 — The agent. The file drop is `rel-m01-l04`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Score the proof](<../../Lesson 05/Student_Copy/README.md>), file drop `rel-m01-l05`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Lesson 3 was the intake workflow. The event stream, the SLA policy, and the business calendar arrived. `wf-intake` runs from `referral.submitted` to a held approval. That workflow does not accept, return, or book. It stops for a coordinator.

Today the assistant can book, and only inside the medical director's rules.

## What this lesson is

Today the medical director's rules, the scenario slice, and the tool catalog arrive. You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do four things, in this order:

1. You read the approval rules, the routing list, the tool catalog, and the scenario slice. The pages are in this folder.
2. You run `wf-self-service`. A patient can ask for status and book a slot. A return cannot leave without a coordinator.
3. You keep the trace the runner writes, and you write a one-page agent note.
4. You answer two questions: when a second agent is worth its tokens, and what must be true before a slot is booked.

At the end, two checks run the agent again and read the agent note and the knowledge file. The trainer reads the sentences in `knowledge.md`. On that file the checks only require two numbered lines with a word after the number. They do not grade those sentences. They do grade the trace and the note.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Try the emergency phrase and check that the trace does not book | [06](06-the-agent.md) |
| AI or data engineer | Own the prompt and the schema | [06](06-the-agent.md) |
| Application engineer | Replace the model, the schema, and the memory | [06](06-the-agent.md) |
| Product manager | Write what the patient sees on a refusal | [07](07-the-note.md) |
| Architect | Draw the privilege boundary on the agent note | [07](07-the-note.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 01/Lesson 04/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m01-l04` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the agent words you will use in the trace, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
