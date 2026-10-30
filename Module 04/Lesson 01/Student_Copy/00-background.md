# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 4, Lesson 1 — Guardrails. The file drop is `rel-m04-l01`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [The incident](<../../Lesson 02/Student_Copy/README.md>), file drop `rel-m04-l02`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Module 3, Lesson 5 left one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

## What this lesson is

Today the attack window is open. You leave with guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read today's drop. You run the demo. It prints two lines. It does not print ignore. You interview the CISO. The notes for that interview are pasted later.
2. You sequence the sprint: the notice, then the guardrail, then access, then the DPIA, then the request.
3. You replace the guard, the output, the supply check, the log redaction, and the session limit, and you replace the work copies of their tests.
4. You replace access and deletion, and their tests. Then you replace the disparity and the stamp rate, and that test. The suite imports all eight app files. You do not delete any of them.
5. You write the guardrail page, the DPIA, the two requests, the breach note, and the CISO notes, and you answer two questions: when the 72-hour clock starts, and what excessive agency is in `wf-intake`.

Chapters 00 through 04 are reading, the demo, and the CISO interview. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, four checks run. The redteam check loads `guard.py`, `output.py`, `supply.py`, `redact.py`, and `limit.py` from `work/app`. It also reads the families in `guardrails.json`. The privacy check loads `erase.py`. It reads `sprint.md`, `dpia.md`, `requests.md`, `breach.md`, `knowledge.md`, and `interviews/ciso.notes.md`. The access check loads `access.py`. It reads the checklist in `guardrails.json`. The fair check loads `fair.py`. The suite imports all eight app modules. None of them is optional. A guard, output, supply, redact, limit, or guardrail-family miss fails only the redteam check. A sprint, DPIA, request, breach, knowledge, CISO-note, or erase miss fails only the privacy check. An access-module miss, or a checklist miss in `guardrails.json`, fails only the access check. A `fair.py` miss fails only the fair check.

A redteam miss can say a letter still books a slot, the hidden prompt is returned, a booking runs with no approval, model html is still rendered, an unregistered hash still loads, a tool description still runs, a poisoned label is still accepted, an unauthorized circular is still cited, a superseded circular is still cited, a canary or a national id is still in the log, a session exceeds the token cap, a hold does not expire, the guardrail config misses a family, a direct injection still runs a tool, a clean label is dropped, an in-force document is replaced, or the harness did not run. A privacy miss can say the DPIA misses a required field, the breach clock does not start at the notice, the patient reply is missing, the deletion request leaves a store, sprint.md does not open the notice first, knowledge.md needs two answers, knowledge.md does not say when the clock starts, knowledge.md does not say what excessive agency is, the ciso notes miss the log or the checklist, the access export is incomplete, deletion leaves the vector index, deletion leaves memory, a permitted log still returns the person, or the harness did not run. An access miss can say a stale staff grant is still open, an expired delegate can still book, break-glass has no audit row, the go-live checklist is incomplete, an open staff grant was closed, or the harness did not run. A fair miss can say the disparity table hides a district or an insurance class, the rubber-stamp rate is missing, the disparity is outside the published bound, or the harness did not run. A failure does not print a hash, a canary, a national id, the case timestamp, a change id, a rate, or the bound. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Open the notice first, then the breach timeline | [05](05-the-sprint.md) and [09](09-the-pages.md) |
| AI or data engineer | Load a hash only when it is on the register, then file the disparity and the stamp rate | [06](06-the-guard.md) and [08](08-the-fair.md) |
| Application engineer | Turn on guardrails, and delete the person from the row, memory, the index, and the logs | [06](06-the-guard.md) and [07](07-the-request.md) |
| Product manager | Write the reply: the records are removed, and no slot was booked from the letter | [09](09-the-pages.md) |
| Architect | Complete the DPIA, and answer when the clock starts and what excessive agency is | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 04/Lesson 01/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m04-l01` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the guard, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 3, Lesson 5 left, and what you leave with today: guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct ignore phrase, or a deletion that clears the row and leaves the index, is not done.

Next: [01 — Setup](01-setup.md).
