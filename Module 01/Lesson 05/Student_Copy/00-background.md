# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 1, Lesson 5 — Score the proof. The file drop is `rel-m01-l05`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Sign in](<../../../Module 02/Lesson 01/Student_Copy/README.md>), file drop `rel-m02-l01`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Lesson 4 was the medical director's rules. The approval policy, the routing list, the tool catalog, and the scenario slice arrived. You ran `wf-self-service`. A patient can ask for status and book a slot. A return cannot leave without a coordinator. You kept the trace and wrote a one-page agent note.

Today the steering questions arrive, and the proof has to survive two more cases.

## What this lesson is

Today you are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the steering questions, yesterday's rules, and the two new cases. The pages are in this folder.
2. You score the scenario set. The Lesson 4 cases still have to pass. A timeout does not book. Two patients offered one slot produce one booking.
3. You draw the architecture and write the design, including what this proof will not build.
4. You answer the steering questions in a readout, and you write a trace note for the emergency scenario.
5. You answer two questions: one failure the scenario set exposed, and which stage gate is still open.

At the end, five checks run. Two of them run the agent again. The trainer reads the sentences in `knowledge.md`. The design check grades the diagram, the urgency section, and the Stage 2 table. On `knowledge.md` it only requires two numbered lines with a word after the number. It does not grade those sentences.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Write the ask log at the bottom of the readout | [08](08-the-readout.md) |
| AI or data engineer | Name the failures the scenario set exposed | [06](06-the-agent.md) |
| Application engineer | Replace the model, the schema, and the memory, and keep the trace | [06](06-the-agent.md) |
| Product manager | Answer the steering questions in the readout | [08](08-the-readout.md) |
| Architect | Draw the diagram and write the design | [07](07-the-diagram.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 01/Lesson 05/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m01-l04` | Yesterday's file drop. The score still runs those scenarios. It means module 1, lesson 4 |
| `rel-m01-l05` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the diagram and the readout, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
