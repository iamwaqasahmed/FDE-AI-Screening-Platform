# 02 — The role

[Chapter 00](00-background.md) said which release this is. This chapter is how you behave on the client's site for this release. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The sprint: cluster, then relabel, then sample, then scan, with adjudication on the list |
| AI or data engineer | Labels under ann-v2, and a synthetic sample inside the fidelity card |
| Application engineer | The date conversion, the clinic code, and the cluster job |
| Product manager | One patient: not one row, not one MRN, and not one national id |
| Architect | A class table, and a scan before the synthetic file is shared |

You do these in [chapter 05](05-the-sprint.md), [chapter 06](06-the-clusters.md), [chapter 07](07-the-sample.md), [chapter 08](08-the-advanced.md), and [chapter 09](09-the-pages.md), in that order. [Chapter 10](10-finish.md) files the two answers and runs the three checks.

There is no interview today. The checks do not read an interview note. [Sara Al-Mutairi](packet/kickoff/personas/dpo.md) is the Data Protection Officer. Her id is `dpo`. You can read her page. You do not run an interview command, and you do not write interview notes. [Maha Al-Shammari](packet/kickoff/personas/coord-lead.md) is the referral coordinator lead. Her id is `coord-lead`. You can read her page. You do not interview her on this page.

## Where today sits

[Chapter 00](00-background.md) names this release. New files arrive on a schedule. You work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

The data request is approved. The history is the full history. Patient data still stays off `ext-large`.

Coding assistants are allowed on the scripts. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says a watermark stays out of prompts, tickets, and the work you submit. The clerk file in the built pack carries a watermark. Do not copy `letters/clerk.jsonl` into `work/`. The scan reads it from the built pack.

The packet copies of `dates.py`, `codes.py`, `cluster.py`, `labels.py`, `synthetic.py`, `scan.py`, `pit.py`, and `budget.py` stay the shells. You replace only the work copies. You do not delete `pit.py` or `budget.py`. The three checks do not require them. The suite does. Replace them after the finish checks are green.

This page is done when you can name the five parts and you have not copied `letters/clerk.jsonl` into `work/`.

Next: [03 — The request](03-the-request.md).
