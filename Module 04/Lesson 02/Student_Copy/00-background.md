# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

Read the section What today is when you want the job for this release. The section above it says what you already finished. You do not paste a file on this page. There is no heading that starts with Replace.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 4, Lesson 2 — The incident. The file drop is `rel-m04-l02`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The surge](<../../Lesson 03/Student_Copy/README.md>), file drop `rel-m04-l03`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 4, Lesson 1 left guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done.

## What this lesson is

Today the replay is open. You leave with a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read today's drop. You run the demo. It prints three lines: a tool, a hash, and a token count. It does not print the error detail. You interview the CISO and the patient representative. The notes for those interviews are pasted later.
2. You sequence the sprint: the replay, then the dashboard, then the timeline, then the cache, then shadow.
3. You replace the trace, the board, and the meter, and you replace the work copies of their tests.
4. You replace the hours cache, the drift names, the override rate, and the shadow hold, and you replace the work copies of their tests. The suite imports all seven app files. You do not delete any of them.
5. You write the timeline, the dashboard page, the runbook, and both interview notes, and you answer two questions: the three drifts, and which event drops the cache.

Chapters 00 through 04 are reading, the demo, and the two interviews. The first file you replace is in chapter 05. You do not run a check until chapter 09. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, two checks run. The incident check loads `spans.py`, `dashboard.py`, `meter.py`, `drift.py`, `override.py`, and `shadow.py` from `work/app`. It also reads `sprint.md`, `dashboard.md`, `timeline.md`, `runbook.md`, `knowledge.md`, `interviews/ciso.notes.md`, and `interviews/patient-rep.notes.md`. The cache check loads `cache.py`. Its id is `slice-cache`. The suite imports all seven app modules. None of them is optional. A spans, dashboard, meter, drift, override, shadow, sprint, dashboard-page, timeline, runbook, knowledge, CISO-note, or patient-rep-note miss fails only the incident check. A cache miss fails only the cache check.

An incident miss can say the trace is missing a tool, a hash, or a token count, the dashboard only has CPU, the alert is outside the SLO, cost is missing a hospital, a drift is unnamed, the override rate is missing, shadow traffic changes the patient reply, a hash is promoted with no comparison, the timeline does not match the replay, the runbook misses a required field, sprint.md does not open the replay first, the ciso notes miss the replay or the dashboard, the patient-rep notes miss the old hours, knowledge.md does not name the three drifts, knowledge.md does not say which event drops the cache, knowledge.md needs two answers, or the harness did not run. A cache miss can say old clinic hours are still served, or the harness did not run. A failure does not print a timestamp, a hash, a rate, a cost, the error detail, or the old-hours sentence. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Open the replay first, then own the timeline | [05](05-the-sprint.md) and [08](08-the-pages.md) |
| AI or data engineer | Keep the tool, the hash, and the token count, then name the three drifts | [06](06-the-board.md) and [07](07-the-hours.md) |
| Application engineer | Board latency, errors, and tool failures, sum every hospital, and drop the cached hours when the circular changes | [06](06-the-board.md) and [07](07-the-hours.md) |
| Product manager | Compute the override rate as the stamped share | [07](07-the-hours.md) |
| Architect | Hold shadow traffic until a comparison, write the runbook, and answer the two questions | [07](07-the-hours.md), [08](08-the-pages.md), and [09](09-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 04/Lesson 02/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m04-l02` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the board, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 4, Lesson 1 left, and what you leave with today: a board for latency, errors, and tool failures, a timeline that matches the replay, and cached clinic hours that drop when the Ramadan circular changes. A board that only has CPU, or a cache that still serves the old hours, is not done.

Next: [01 — Setup](01-setup.md).
