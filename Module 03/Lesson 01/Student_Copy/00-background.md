# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 3, Lesson 1 — Honest data. The file drop is `rel-m03-l01`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The adapter](<../../Lesson 02/Student_Copy/README.md>), file drop `rel-m03-l02`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 2, Lesson 5 was the change to include Ain. You left with a smoke-tested URL, `deployment.md` sequencing `cr-ain`, the readout, and the retro notes. A booking at Ain stayed queued for the nightly file.

## What this lesson is

Today the data request is approved. You leave with one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card.

Module 1 left `p-waitlist` open. The diagram called that open item a split identity: duplicate rows, and one person stored as two. Module 2, Lesson 1 used the word identity for the sign-in note. That note is not today's job. Today's identity check is the waitlist person.

The full history has both shapes. An Iqama row whose `replaces` field names a visitor number is one person stored as two rows. A mother and a newborn can share a national id and stay two people. Twins can share a phone. An MRN can be reused. Linking every shared national id, phone, or MRN would merge those people. The cluster job links only the rows that are the same person.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the data request, the guideline, the clinic catalog, and the history. You run the demo. It prints four lines. You do not type the first three.
2. You sequence the sprint: the cluster job, then the relabel, then the sample, then the scan. Adjudication is on that list.
3. You replace the date conversion, the clinic code, and the cluster job.
4. You replace the relabel, the synthetic sample, and the scan. You also replace the invite-time features and the label budget. The three checks do not require those last two. Replace them after the finish checks are green. Do not delete them.
5. You define one patient, you write the class table, and you answer two questions: why a row count is not a patient count, and what a fidelity card compares.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, three checks run. They load the app in `work/app` and read the pages. An identity miss can say a mother and a newborn were merged, twins were merged, a reused MRN was linked, a Hijri month boundary is off by a day, the stale clinic code was kept, a row count was used as a patient count, the clusters do not match, the date conversion did not run, the clinic code did not run, the cluster job did not run, `patients.md` does not define one patient, or `sprint.md` does not sequence the cluster job. A labels miss can say a phone photo is still a scan, a sub-specialty is still blank, the sample still follows ann-v1, or the relabel did not run. A synthetic miss can say the synthetic sample misses the fidelity card, the synthetic sample contains a watermark, the synthetic sample contains a national id, the synthetic sample did not run, the scan did not run, the classification note is missing, `knowledge.md` needs two answers, `knowledge.md` does not say why a row is not a patient, or `knowledge.md` does not say what a fidelity card compares. A check does not name a national id, a converted date, or a rate. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the cluster job, then the relabel, then the sample, then the scan, and book adjudication | [05](05-the-sprint.md) |
| AI or data engineer | Relabel under ann-v2, and build the synthetic sample | [07](07-the-sample.md). [08](08-the-advanced.md) is after the finish checks are green |
| Application engineer | Replace the dates, the clinic codes, and the cluster job | [06](06-the-clusters.md) |
| Product manager | Define one patient | [09](09-the-pages.md) |
| Architect | Class national id, date of birth, name, and phone before any export | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 03/Lesson 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m03-l01` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the cluster job, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 2, Lesson 5 left, and what you leave with today: one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card.

Next: [01 — Setup](01-setup.md).
