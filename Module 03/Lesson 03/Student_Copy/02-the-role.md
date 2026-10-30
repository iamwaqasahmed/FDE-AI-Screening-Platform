# 02 — The role

[Chapter 00](00-background.md) said which release this is. This chapter is how you behave on the client's site for this release. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The sprint: index, then filter, then cite, then sync, with v4 limited to three specialties, not all |
| AI or data engineer | The index, and the photo read, the booking conflict, and the catalog lookup |
| Application engineer | An audience filter, a criteria bind that keeps an in-flight referral on its start version, a citation or a refusal, and a sync that applies the change feed |
| Product manager | The refusal: no document binds, or the asker cannot see it |
| Architect | The audience table: a patient sees public only, staff see public and staff, and records see restricted |

You do these in [chapter 05](05-the-sprint.md), [chapter 06](06-the-index.md), [chapter 07](07-the-citation.md), [chapter 08](08-the-advanced.md), and [chapter 09](09-the-pages.md), in that order. [Chapter 10](10-finish.md) files the two answers and runs the three checks.

There is no interview today. The checks do not read an interview note. You do not run an interview command, and you do not write interview notes.

## Where today sits

[Chapter 00](00-background.md) names this release. New files arrive on a schedule. You work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Criteria v4 is in force for endo, ophth, and card. It is not in force for every specialty. A referral that already started keeps the criteria version it started with. An unauthorized circular is not a citation. A draft can be searched. A draft is not citable.

A watermarked file copied into `work/` fails the check. The message does not print the watermark. Do not copy a file that carries the mark into `work/`.

The packet copies of `chunk.py`, `embed.py`, `index.py`, `search.py`, `filter.py`, `bind.py`, `cite.py`, `sync.py`, `vision.py`, `conflict.py`, and `catalog.py` stay the shells. You replace only the work copies. You do not delete `vision.py`, `conflict.py`, or `catalog.py`. The three checks do not require them. The suite does. `slice-hybrid` and `slice-acl` do not read them. Replace them after the finish checks are green. The tests are copied and not replaced.

This page is done when you can name the five parts and you have not copied a watermarked file into `work/`.

Next: [03 — The criteria](03-the-criteria.md).
