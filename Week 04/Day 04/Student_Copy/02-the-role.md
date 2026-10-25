# 02 — The role

[Chapter 00](00-background.md) said what the four weeks produce. This chapter is how you behave on the client's site today. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself. One person does all five parts. No team split.

You do not paste a file on this page. There is no heading that starts with Replace.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The sprint opens the drill first. A purchase that misses the Ramadan date is rejected |
| AI or data engineer | The hash on site-b matches the register. An unregistered hash stays off |
| Application engineer | Both replicas are placed. After site-a dies, new traffic is on site-b, and in-flight approvals resume |
| Product manager | Status still works during the outage. A booking does not wait on insure |
| Architect | Renting meets the deadline. Each hospital is billed its own share |

You do these in [chapter 05](05-the-sprint.md), [chapter 06](06-the-sites.md), [chapter 07](07-the-outage.md), and [chapter 08](08-the-pages.md), in that order. [Chapter 09](09-finish.md) files the two answers and runs the check.

The slo check reads [ea.notes.md](work/interviews/ea.notes.md) and [finance.notes.md](work/interviews/finance.notes.md). The question files are not the graded notes. [Chapter 03](03-the-drill.md) runs the interviews. [Chapter 08](08-the-pages.md) replaces the notes. You do not type into the question files.

## Where today sits

[Chapter 00](00-background.md) has the four-week table. New files arrive on a schedule. Today you work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Week 4 Day 3 left the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done. Today the site drill is open.

A watermarked file copied into `work/` fails the check. The message does not print the watermark. Do not copy a file that carries the mark into `work/`.

The packet copies of `replicas.py`, `route.py`, `failover.py`, `hashes.py`, `breaker.py`, `degrade.py`, `procure.py`, and `hospitals.py` stay the shells. You replace only the work copies. You do not delete any of them. The suite imports all eight. The slo check loads all eight. The packet tests stay the shell tests. You replace the work copies of the tests in the chapters that replace the matching app files. A second run of the prepare script puts the shell tests back. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite. The workflow is copied and not replaced.

This page is done when you can name the five parts and you have not copied a watermarked file into `work/`.

Next: [03 — The drill](03-the-drill.md).
