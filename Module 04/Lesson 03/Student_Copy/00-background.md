# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

Read the section What today is when you want the job for this release. The section above it says what you already finished. You do not paste a file on this page. There is no heading that starts with Replace.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 4, Lesson 3 — The surge. The file drop is `rel-m04-l03`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The drill](<../../Lesson 04/Student_Copy/README.md>), file drop `rel-m04-l04`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Module 4, Lesson 2 left a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done.

## What this lesson is

Today the surge is on the forecast. You leave with the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read today's drop. You run the demo. It prints two lines. The first is `missed`. The second is the cold start. It does not print a price or the backlog count. You interview finance and the BI lead. The notes for those interviews are pasted later.
2. You sequence the sprint: the forecast, then the server, then the batch, then the quota, then the scale, then the capacity table.
3. You replace the adapters, the batch, the route, and the public cache, and you replace the work copies of their tests.
4. You replace the quota, the scale, the price, and the capacity table, and you replace the work copies of their tests. The suite imports all eight app files. You do not delete any of them.
5. You write the capacity page and both interview notes, and you answer two questions: why reactive scaling misses the first minutes, and what the price change punished.

Chapters 00 through 04 are reading, the demo, and the two interviews. The first file you replace is in chapter 05. You do not run a check until chapter 09. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, two checks run. The slo check loads `adapters.py`, `batch.py`, `quota.py`, `scale.py`, `price.py`, and `capacity.py` from `work/app`. It also reads `sprint.md`, `capacity.md`, `knowledge.md`, `interviews/finance.notes.md`, and `interviews/bi-lead.notes.md`. The surge check loads `batch.py`, `route.py`, and `public.py`. Its id is `slice-surge`. The suite imports all eight app modules. None of them is optional. An adapters miss fails only the slo check. A batch miss fails both checks. A route or public miss fails only the surge check. A quota, scale, price, capacity-module, sprint, capacity-page, knowledge, finance-note, or bi-lead-note miss fails only the slo check.

A slo miss can say a registered adapter is missing, an unregistered hash is loaded, the backlog misses 48 hours, chat misses its latency while the batch runs, reactive scaling misses the first window, the plan still uses yesterday's price, the capacity table misses the backlog or the price, the capacity note misses a required section, sprint.md does not open the forecast first, the finance notes miss the price change, the bi-lead notes miss the campaign backlog, knowledge.md does not say why reactive scaling misses the first minutes, knowledge.md does not say what the price change punished, knowledge.md needs two answers, or the harness did not run. A surge miss can say the batch is unbatched, the batch is on ext-large, public answers still hit the GPU, or the harness did not run. A failure does not print a price, a hash, a tokens-per-second figure, the backlog count, or the peak time. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Open the forecast first, then reject a stale price | [05](05-the-sprint.md) and [08](08-the-pages.md) |
| AI or data engineer | Serve the registered adapters on one process, batch the load, keep a phi row local, and return a cached public answer | [06](06-the-server.md) |
| Application engineer | Start one cold start before the peak | [07](07-the-surge.md) |
| Product manager | Check the forecast against the eye-screening campaign | [03](03-the-forecast.md) and [08](08-the-pages.md) |
| Architect | Keep a chat reserve, record today's price on the capacity table, and answer the two questions | [07](07-the-surge.md), [08](08-the-pages.md), and [09](09-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 04/Lesson 03/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m04-l03` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the server, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 4, Lesson 2 left, and what you leave with today: the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done.

Next: [01 — Setup](01-setup.md).
