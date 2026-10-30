# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The check also needs the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

Read the section What today is when you want the job for this release. The section above it says what you already finished. You do not paste a file on this page. There is no heading that starts with Replace.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 4, Lesson 4 — The drill. The file drop is `rel-m04-l04`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The proposal](<../../Lesson 05/Student_Copy/README.md>), file drop `rel-m04-l05`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 4, Lesson 3 left the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done.

## What this lesson is

Today the site drill is open. You leave with two replicas, traffic on site-b after site-a dies, the breaker open on insure, and a rent-versus-buy draft that meets 8 February. A booking path that waits on insurance, or a purchase that cannot arrive before Ramadan, is not done.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read today's drop. You run the demo. It prints two lines. The first is `site-a down`. The second is `site-b serving`. It does not print a budget, a hash, or a price. You interview the enterprise architect and finance. The notes for those interviews are pasted later.
2. You sequence the sprint: the drill, then the replicas, then the failover, then the breaker, then the patient view, then the trade-off.
3. You replace the replicas, the route, the failover, and the hashes, and you replace the work copies of their tests.
4. You replace the breaker, the degradation, the purchase choice, and the hospital split, and you replace the work copies of their tests. The suite imports all eight app files. You do not delete any of them.
5. You write the failover page and the architecture draft, you write both interview notes, and you answer two questions: what still works when the model is down, and why renting wins the deadline.

Chapters 00 through 04 are reading, the demo, and the two interviews. The first file you replace is in chapter 05. You do not run a check until chapter 09. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, one check runs. Its id is `chk-slo`. It loads `replicas.py`, `route.py`, `failover.py`, `hashes.py`, `breaker.py`, `degrade.py`, `procure.py`, and `hospitals.py` from `work/app`. It also reads `sprint.md`, `failover.md`, `architecture.md`, `knowledge.md`, `interviews/ea.notes.md`, and `interviews/finance.notes.md`. The suite imports all eight app modules. None of them is optional. The Lesson 3 load portion of this check stays on `rel-m04-l03`. This day does not run that portion.

A miss can say traffic stays on one replica, site-b is not serving after the drill, failover misses its time, an in-flight approval is dropped, the hash on site-b does not match the register, the booking path waits on insure, insurance is treated as a site, the patient reply fails closed when the model is down, the purchase route misses Ramadan, the hospital split uses one figure for every hospital, the failover note misses a required section, the architecture draft misses a required section, sprint.md does not open the drill first, the ea notes miss site-b, the finance notes miss the purchase lead time, knowledge.md does not say what still works when the model is down, knowledge.md does not say why renting wins the deadline, or the harness did not run. A route miss is the one line that site-b is not serving. A failover miss is that line, then the time, then the dropped approval. A failure does not print a hash, a second count, a SAR figure, a module count, or a date. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Open the drill first, then check the Ramadan date | [05](05-the-sprint.md) and [08](08-the-pages.md) |
| AI or data engineer | Confirm the hash on site-b matches the register | [06](06-the-sites.md) |
| Application engineer | Place both replicas, send traffic to site-b, and resume the approvals | [06](06-the-sites.md) |
| Product manager | Say what the patient still sees, and keep a booking off insure | [07](07-the-outage.md) and [08](08-the-pages.md) |
| Architect | Write the rent-versus-buy draft and the hospital split, and answer the two questions | [07](07-the-outage.md), [08](08-the-pages.md), and [09](09-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the check reads |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 04/Lesson 04/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m04-l04` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The check in `problem_simulation`. Chapter 01 turns it on. The folder it writes, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the sites, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 4, Lesson 3 left, and what you leave with today: two replicas, traffic on site-b after site-a dies, the breaker open on insure, and a rent-versus-buy draft that meets 8 February. A booking path that waits on insurance, or a purchase that cannot arrive before Ramadan, is not done.

Next: [01 — Setup](01-setup.md).
