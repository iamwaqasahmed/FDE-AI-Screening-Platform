# 00 — Background

Read this before chapter 01. It says where this lesson sits in the four modules, and what this lesson is.

This folder is the lesson. The checks also need the course folder, the one that contains `problem_simulation` and `Module 01`. [Chapter 01](01-setup.md) installs Python if it is missing, finds that course folder or downloads it, and checks that you are in the right place before any other command.

## What this whole thing is

You are in a training program for forward deployed engineers. A forward deployed engineer sits with a client, works on the client's problem, and leaves something the client can run.

For this course the client is invented. The client is the Al-Waha Health Cluster, a made-up health system in Saudi Arabia. The hospitals, the staff, and the documents are not real. No page here is a real patient's record.

The job is one assistant for patient access. Patient access means referrals, appointments, reminders, and the phone line. A referral is a request from a local clinic for a hospital appointment. The cluster's digital leader wants an AI front desk that books, reschedules, answers questions, and chases referrals, live before Ramadan. You heard that wish on the first morning. You do not treat the wish as the plan. You learn what is actually true, then you build.

The course is four modules. You work through them in order, at your own pace. There is no timetable. The picture of all four modules is in [Lesson 1](<../../../Module 01/Lesson 01/Student_Copy/00-background.md>) and on the [course guide](../../../learning/README.md). This folder is Module 3, Lesson 3 — Cite. The file drop is `rel-m03-l03`. That id is the pack name the checks use. It is not a schedule. When this lesson's checks have passed, open [Measure](<../../Lesson 04/Student_Copy/README.md>), file drop `rel-m03-l04`. A later lesson can make a choice from an earlier lesson incomplete. You stay inside this folder until its finish chapter names the next one. This module's page is [the module](../../README.md).

## What the previous lesson already finished

That work was the previous lesson.

Module 3, Lesson 2 was the signed ruling. You left with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

## What this lesson is

Today criteria v4 is in force for three specialties. You leave with an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

Module 1, Lesson 3 used the criteria document that was in force when the referral started. For endocrinology that document was v3. v4 was still a draft, so the intake workflow did not use it. Today's feed is what moves v4 to in force, and only for endo, ophth, and card. A referral that started before that window still cites v3, even after the feed marks v3 superseded. Neuro is not on the notice, so neuro stays on v3. Yesterday's `local-embed` row is the name of today's token vector. It is still not a training loop. Hours questions stayed on retrieval. This index is that retrieval.

You are one person, and you do all five parts of the job yourself. No part is handed to someone else.

You do five things, in this order:

1. You read the criteria notice, the snapshot, the change feed, and the dev slice. You run the demo. It prints two titles, then one line. You do not type the titles. The line does not print the watermark. It does not print the clause that tells the two leaflets apart.
2. You sequence the sprint: the index, then the filter, then the cite, then the sync. v4 is endo, ophth, and card, not all specialties.
3. You replace the chunk split, the local embed, the index, and the search.
4. You replace the audience filter, the criteria bind, the citation, and the sync. You also replace the photo read, the booking conflict, and the catalog lookup. The three checks do not require those last three. Replace them after the finish checks are green. Do not delete them. `slice-hybrid` and `slice-acl` do not read them.
5. You write the refusal, you set who may see a staff document, and you answer two questions: what makes a document in force, and who may see a staff document.

Chapters 00 through 04 are reading and one demo. The first file you replace is in chapter 05. You do not run a check until chapter 10. The rest of this page names what a miss can say. You do not need those sentences until a check prints `failed`.

At the end, three checks run. They load `bind.py`, `cite.py`, `embed.py`, `filter.py`, `index.py`, `search.py`, and `sync.py` from `work/app`. The rag check also reads the four pages. A rag miss can say the citation is not the in-force span, a draft is cited, the unauthorized circular is cited, an in-flight referral is restarted on v4, v4 is applied outside its specialties, the answer does not refuse, a staff document is shown to a patient, the index ignores the change feed, the index did not run, sprint.md does not sequence the index, sprint.md does not limit v4 to three specialties, the refusal copy is missing, the audience note lets a patient see a staff document, knowledge.md needs two answers, knowledge.md does not say what makes a document in force, or knowledge.md does not say who may see a staff document. A hybrid miss can say vector search alone clears the slice, the unauthorized circular is cited, the citation is not the in-force span, or the index did not run. An ACL miss can say a staff document is shown to a patient, the citation is not the in-force span, or the index did not run. A failure does not print a doc id, a span, or a clause. A watermark message does not print the watermark.

## The five parts, all yours

You hold every part. Later chapters tell you how. You write the graded pieces into the same `work/` folder.

| Part | You do this | Chapter |
| --- | --- | --- |
| Lead | Sequence the index, then the filter, then the cite, then the sync, and limit v4 to endo, ophth, and card, not all | [05](05-the-sprint.md) |
| AI or data engineer | Chunk, embed, index, and search, then the photo read, the booking conflict, and the catalog lookup | [06](06-the-index.md). [08](08-the-advanced.md) is after the finish checks are green |
| Application engineer | Filter by audience, bind the criteria, cite or refuse, and apply the change feed | [07](07-the-citation.md) |
| Product manager | Write the refusal: no document binds, or the asker cannot see it | [09](09-the-pages.md) |
| Architect | Set the audience table, and answer what makes a document in force and who may see a staff document | [09](09-the-pages.md) and [10](10-finish.md) |

## Words this folder uses

| Word | Meaning |
| --- | --- |
| This student copy | The pages you are reading, plus the file drawer in `packet/` |
| `packet/` | The files the chapters tell you to open. Not a second lesson |
| `work/` | The folder you fill in. This is the folder the checks read |
| Course folder | The folder on your computer that contains `problem_simulation` and `Module 01`. This student copy sits inside it, at `Module 03/Lesson 03/Student_Copy`. Chapter 01 checks that you can see it |
| `practice` | The shared classroom world. Everyone in the room uses it today |
| `rel-m03-l03` | The pack name for this lesson. The checks use it. It is not a schedule |
| The grader | The checks in `problem_simulation`. Chapter 01 turns them on. The folder they write, `problem_simulation/build`, stays closed |

The cluster's care words, and the words you will use in the sprint, the index, and the pages, are in [chapter 04](04-words.md). Read that chapter when you reach it.

This page is done when you can say what Module 3, Lesson 2 left, and what you leave with today: an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

Next: [01 — Setup](01-setup.md).
