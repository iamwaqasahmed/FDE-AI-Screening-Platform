# 00 — Background

Read this before chapter 01. It says what the four weeks are, and what today is inside them.

This folder is the lesson. The interview and the checks also need the course folder, the one that contains `problem_simulation` and `Week 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For these four weeks the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You will hear that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The four weeks, in order:

| Week | You leave with |
| --- | --- |
| 1 | A small working proof of the assistant, a picture of the design, and a note that says why |
| 2 | The assistant signed in to the cluster and deployed on the cluster's private cloud |
| 3 | Models fitted to the cluster, answers drawn from the cluster's documents, and an evaluation |
| 4 | Security, monitoring, a design that can take a surge, and a plan for running it |

Each morning the cluster hands you only that day's files. A choice that is reasonable today can be incomplete by Thursday, because a later morning brings a file you do not have yet. Today you stay inside this folder.

## What today is

Today is the arrival. You are not building the assistant. You are one person, and you do all five parts of the job yourself.

You do four things, in this order:

1. You learn who asked, what they asked, and which approval gate you are standing in.
2. You file an access request for the files and the dev credential this day needs. The cluster does not give you its full history today.
3. You keep a tiny pipeline green. It only answers "I am up." Its real job is to reject a secret or a patient letter if one is copied into your work. Coding assistants are allowed. Patient data and secrets are not.
4. You interview two of the cluster's people. They answer the question you ask. They do not volunteer the constraint that would change the design.

At the end, two checks look at your pipeline and your two interviews. A short `knowledge.md` file holds your own answers. The trainer reads that file. The checks do not.

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
| Course folder | The folder on your computer that contains `problem_simulation` and `Week 01`. This student copy sits inside it, at `Week 01/Day 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-w1d1` | The name of today's file drop. It means week 1, day 1 |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, such as referral, triage, and specialty, are in [chapter 04](04-words.md). Read that chapter when you reach it.

Next: [01 — Setup](01-setup.md).
