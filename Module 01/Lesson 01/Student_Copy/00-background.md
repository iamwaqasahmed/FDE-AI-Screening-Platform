# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The interview and the checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You will hear that wish in this lesson. You do not treat the wish as the plan. You learn what is actually true, then you build.

The four modules, in order:

| Module | You leave with |
| --- | --- |
| 1 | An approach, an intake path, an agent, and a readout |
| 2 | Sign-in, feeds, tests, a private-cloud URL, and the Ain change |
| 3 | Honest labels, a registered adapter, citations, a measurement, and requirements |
| 4 | Guardrails, an incident you can reconstruct, a surge plan, a site drill, and a proposal |

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](00-background.md) and on the [course guide](../../../learning/README.md). This folder is Module 1, Lesson 1 — Arrival. The file drop is `rel-m01-l01`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The approach](<../../Lesson 02/Student_Copy/README.md>), file drop `rel-m01-l02`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What this lesson is

This lesson is the arrival. You are not building the assistant. You are one person, and you do all five parts of the job yourself.

You do four things, in this order:

1. You learn who asked, what they asked, and which approval gate you are standing in.
2. You file an access request for the files and the dev credential this day needs. The cluster does not give you its full history today.
3. You keep a tiny pipeline green. It only answers "I am up." Its real job is to reject a secret or a patient letter if one is copied into your work. Coding assistants are allowed. Patient data and secrets are not.
4. You interview two of the cluster's people. They answer the question you ask. They do not volunteer the constraint that would change the design.

At the end, two checks look at your pipeline and your two interviews. A short `knowledge.md` file holds your own answers. The trainer reads that file. The checks do not.

That is the end of this release, not the end of the lesson. The next lesson is the approach. The leaders' numbers arrive there. You run four baselines and write an approach memo. Every problem gets a family. `p-triage` stays blocked. You are still not building the assistant. At the end of that second release, two checks look at the memo and the brief.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write every piece into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | File the access request | [06](06-the-access-request.md) |
| AI or data engineer | Decide what may enter a coding-assistant prompt | [07](07-the-pipeline.md) |
| Application engineer | Own the pipeline and keep the scan green | [07](07-the-pipeline.md) |
| Product manager | Choose the two people and write the questions | [08](08-the-interviews.md) |
| Architect | Sketch the three zones from the kickoff only | [05](05-the-kickoff.md), [09](09-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 01/Lesson 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m01-l01` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, such as referral, triage, and specialty, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
