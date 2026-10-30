# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 3, Lesson 2 — The adapter. The file drop is `rel-m03-l02`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Cite](<../../Lesson 03/Student_Copy/README.md>), file drop `rel-m03-l03`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the earlier release today already finished

That work was earlier today. Its checks should already say passed.

Module 3, Lesson 1 was the approved data request. You left with one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. A mother and a newborn stayed two people. Phone photos were photos. The sample did not copy a real letter.

## What this lesson is

Today the ruling is signed. You leave with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the ruling, the model register, the quota, the price cap, and the slices. You run the demo. It prints one line. You do not type that line's hidden mark. The line does not print the mark.
2. You sequence the sprint: the baseline, then the adapter, then the register, then the memo. The cloud fine-tune is closed.
3. You replace the prompt, the letter relabel, and the message intent. The prompt stays weak, and it is not served.
4. You replace the adapter, the router, and the cost. You also replace the rank fit, the domain filter, and the preference edit. The two checks do not require those last three. Replace them after the finish checks are green. Do not delete them. `slice-lora` does not read them.
5. You revise the approach memo, you record residency, and you answer two questions: which problem stays on retrieval, and which hash is legal to serve.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, two checks run. They load the app in `work/app` and the model check reads the pages. A model miss can say the prompt baseline is still the served model, extraction F1 is outside the budget, intent F1 is outside the budget, the cost is over the price cap, the call sends phi to ext-large, the hash is not on reg-models, the gpu count is over the quota, the latency is over the budget, the adapter did not run, hours questions are not left on retrieval, dna is not a tabular model, family does not fit, the measured value does not match the adapter, the residency note lets a phi field leave, approach.md is missing, sprint.md does not sequence the adapter, knowledge.md needs two answers, knowledge.md does not say which problem stays on retrieval, or knowledge.md does not say which hash is legal to serve. A LoRA miss can say the prompt baseline clears the slice, ext-large at the price cap does not clear the slice, or the adapter did not run. A check does not print a hash, a GPU count, a price, an F1, or a gold label. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the baseline, then the adapter, then the register, then the memo, and close the cloud fine-tune | [05](05-the-sprint.md) |
| AI or data engineer | Serve the registered adapter, and fit the rank, the domain lines, and the preference edit | [07](07-the-adapter.md). [08](08-the-advanced.md) is after the finish checks are green |
| Application engineer | Keep the prompt weak and local, relabel the letters, classify the messages, refuse a bad call, and price the local tokens | [06](06-the-baseline.md) and [07](07-the-adapter.md) |
| Product manager | Revise the approach memo and keep the Module 1 families | [09](09-the-pages.md) |
| Architect | Record residency for the phi fields, and answer which hash is legal to serve | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 03/Lesson 02/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m03-l02` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the adapter, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 3, Lesson 1 left, and what you leave with today: a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

Next: [01 — Setup](01-setup.md).
