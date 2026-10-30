# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 3, Lesson 5 — One fix. The file drop is `rel-m03-l05`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Guardrails](<../../../Module 04/Lesson 01/Student_Copy/README.md>), file drop `rel-m04-l01`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 3, Lesson 4 left a draft benchmark that names the four planted failures with evidence, and workshop notes. Labels stayed on the grading service. The second measured run waited until today.

## What this lesson is

Today is the second measured run and the rehearsal brief. You leave with one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

The failure you move is yesterday's retrieval failure, `log-circular`. The hallucination, the Friday offer, and the booking with no approval stay open. Module 1 left `p-triage` blocked and left G2, the DPIA, open. Today's spec does not close G2 and does not build triage. The citation requirement sits on G1, the risk tier. Module 1's sponsor sentence is still not the plan.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the rehearsal notice, the steering questions, the role cards, the stage gate, the price sheet, the annotation budget, the citation slice, the personal slice, and the backlog seed. You run the demo. It prints two lines. The lines do not print a non-goal or a price.
2. You sequence the sprint: the fix, then the second measurement, then the spec. The lead presents.
3. You replace the repair, the second run, and the label cost. Then you replace the backlog, the stage gate, and the improvement gate.
4. You replace the personal citation lab. The suite imports it. You do not delete it. You do not delete `repair.py`, `remeasure.py`, `cost.py`, `backlog.py`, or `gates.py`. The suite imports all six.
5. You write the benchmark, the improvement plan, the rehearsal brief, the readout, and the retro, and you answer two questions: what the second run changed, and which requirement is out of scope and why.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, four checks run. The eval check loads `repair.py`, `remeasure.py`, and `cost.py` from `work/app`. It also reads `sprint.md`, `benchmark.md`, `improvement.md`, `knowledge.md`, and the work copy of `.github/workflows/ci.yml`. The rcp check loads `backlog.py` and `gates.py`. It reads `rcp/requirements.md`. The readout check reads `readout.md` and `retro.md`. The individual check loads `personal.py`. A sprint, benchmark, improvement, knowledge, or commented-gate miss fails only the eval check. A requirements, backlog, or stage-gate miss fails only the rcp check. A readout or retro miss fails only the readout check. A `personal.py` miss fails only the individual check.

An eval miss can say the repair leaves the unauthorized citation, the second run does not move the retrieval failure, the second run misses the held-out slice, the improvement cost misses the price sheet, the report misses a planted failure, the report misses the second run, the improvement plan misses the label cost, sprint.md does not sequence the fix before the spec, knowledge.md needs two answers, knowledge.md does not say what the second run changed, knowledge.md does not say which requirement is out of scope, the improvement gate is still commented, or the harness did not run. An rcp miss can say the requirements restate the sponsor sentence, the requirements leave triage in scope, the requirements follow the dot-vote, the requirements miss the rehearsal brief, the requirements contain a banned sentence, the backlog keeps a non-goal, the backlog drops an in-scope story, the backlog did not run, the stage gate skips the risk tier, the stage gate did not run, rcp/requirements.md is missing, or the harness did not run. A readout miss can say the readout does not answer the second run, the readout does not name the non-goal, the readout does not leave urgency with a clinician, the readout does not keep patient data off the external model, the readout does not name the backlog, the readout does not price the fix, the readout does not name a system, the readout does not cite a source, the ask log is missing, the readout contains a banned sentence, readout.md is missing, retro.md is missing, or the retro note is missing a heading. An individual miss can say the citation drops the version or the audience, the citation serves a staff document to a patient, the metric read ignores its budget, the personal lab is missing, or the personal lab did not run. A failure does not print a price, a count, a doc id, or a gate id. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the fix, then the second measurement, then the spec, and present | [05](05-the-sprint.md) |
| AI or data engineer | Repair the citation, score the second run, price the labels, then keep version and audience on a personal citation | [06](06-the-fix.md) and [08](08-the-personal.md) |
| Application engineer | Drop the non-goals in the backlog, put the citation requirement on the risk tier, and uncomment the improvement gate | [07](07-the-spec.md) |
| Product manager | Write the rehearsal brief. Triage stays a non-goal. A clinician owns urgency | [09](09-the-pages.md) |
| Architect | Record the four failures, the label cost, the readout, and the retro, and answer what the second run changed and which requirement is out of scope | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 03/Lesson 05/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m03-l05` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the fix, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 3, Lesson 4 left, and what you leave with today: one moved retrieval failure, the benchmark, the improvement plan, `rcp/requirements.md`, and the readout. A requirements list that copies the sponsor sentence, including triage, is not a brief.

Next: [01 — Setup](01-setup.md).
