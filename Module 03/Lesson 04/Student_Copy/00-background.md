# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 3, Lesson 4 — Measure. The file drop is `rel-m03-l04`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [One fix](<../../Lesson 05/Student_Copy/README.md>), file drop `rel-m03-l05`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Module 3, Lesson 3 left an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

## What this lesson is

Today the hidden-test protocol is open. You leave with a draft benchmark that names the four planted failures with evidence, and with workshop notes. Labels stay on the grading service. A second measured run waits until Lesson 5.

Module 1's forecast family compared a seasonal line with a mean. That seasonal line copies last year. Today's campaign says ophthalmology demand after the announcement is not last year's month. Module 1's calendar does not count Friday as a working day. A Friday offer is a reasoning gap, not a missing document. Module 1's booking waits for an approval. A booked slot with no approval is a workflow miss. Yesterday's citation rule is the retrieval failure: the document is not in force for the asker. A clause that is not on file is a hallucination. The four names are those four misses.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the protocol, the campaign notice, the budgets, the development slice, the failure log, the calibration subset, and the workshop files. You run the demo. It prints two lines. The lines do not print the calibration item, the span, or the doc id.
2. You sequence the sprint: the score, then the failures, then the workshop. The workshop stays on evidence.
3. You replace the score, the forecast, and the failure names. Then you replace the judge, the regression, and the evaluation gate.
4. You replace the intervals and the experiment report. The two checks do not require those two files. Replace them after the finish checks are green. Do not delete them. `slice-judge` does not read them. You do not delete `gate.py`. The suite imports it.
5. You write the benchmark, the workshop notes, and the experiment page, and you answer two questions: what a retrieval failure is, and why a judge is calibrated.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, two checks run. The eval check loads `failures.py`, `forecast.py`, and `score.py` from `work/app`. It also reads `sprint.md`, `benchmark.md`, `workshop.md`, `knowledge.md`, and the work copy of `.github/workflows/ci.yml`. The judge check loads `judge.py`. It does not read the four pages or the workflow. A page miss, and a commented gate, fail only the eval check.

An eval miss can say the extraction score misses the held-out slice, the citation score misses the held-out slice, the journey score misses the held-out slice, the forecast ignores the campaign, the forecast scores the fit window, the forecast misses the later window, a planted failure is misnamed, the report misses a planted failure, the report misses a metric against its budget, sprint.md does not sequence the evaluation, sprint.md does not keep the workshop on evidence, the workshop notes miss a seat, the workshop notes treat the dot-vote as the value model, the workshop notes put triage in scope, knowledge.md needs two answers, knowledge.md does not say what a retrieval failure is, knowledge.md does not say why a judge is calibrated, the evaluation gate is still commented, or the harness did not run. A judge miss can say the judge is not checked on the calibration set, or the judge did not run. A failure does not print a log id, a visit count, an F1, or the calibration item. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the score, then the failures, then the workshop, and keep the workshop on evidence | [05](05-the-sprint.md) |
| AI or data engineer | Score extraction, citation, and journey, forecast the later window, and name the failures, then the intervals and the experiment | [06](06-the-harness.md). [08](08-the-advanced.md) is after the finish checks are green |
| Application engineer | Mark with the calibration label, reject a fluent wrong citation, and uncomment the evaluation gate | [07](07-the-gate.md) |
| Product manager | Write the workshop notes from the seats and the dot-vote. Do not copy a seat's wish that triage goes live | [09](09-the-pages.md) |
| Architect | Record which failure is a design bug, and answer what a retrieval failure is and why a judge is calibrated | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 03/Lesson 04/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m03-l04` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the harness, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 3, Lesson 3 left, and what you leave with today: a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stay on the grading service. A second measured run waits until Lesson 5.

Next: [01 — Setup](01-setup.md).
