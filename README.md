# Forward deployed engineering

This repository is a guided case. The client is Hartland Regional Health Authority, a fictional regional health service that reports to a Ministry of Health. The service in the files is diabetic eye screening. Nothing here is a real patient's record, and nothing here is a protocol for care.

A forward deployed engineer sits with that customer, turns a vague request into a small system the customer can run, and stops when the person who must sign has not signed.

| Shared note | What it gives you |
|---|---|
| [Who it is for](target_audience.md) | Which track to take, and what you leave able to do |
| [FDE.md](FDE.md) | The practice both tracks train |
| [Health language](health_language.md) | The words, before you open a data file |

## Read in this order

| | Read | You then know |
|---|---|---|
| 1 | This page | The two tracks, the folders, and what stays closed |
| 2 | [Who it is for](target_audience.md) | Which track is yours |
| 3 | [FDE.md](FDE.md) | The practice |
| 4 | [Health language](health_language.md) | The vocabulary |
| 5 | Your track guide, linked below | The modules or weeks, and the commands |

## Two tracks, one client

Both tracks are for one person. You do every note, from the first ask to the handoff. A job title in a note is a hat you put on for that note. You are the software engineer, the data scientist, the architect, the product manager, and the consultant, one after another.

Week 00 is a four-day introduction. The world is small. You read the reference, run a checker, and explain the result.

Weeks 1 to 6 are for someone who already puts services in production. You work through a deeper copy of the same screening service. A new drop arrives each week and changes something you have already used.

You can start at Week 1 without finishing Week 00. Week 00 is the shorter way to learn the client and the practice.

| | Week 00 — Self Paced | Week 01 — Week 06 |
|---|---|---|
| Time | About four days. Each module is about half a day. | Six weeks |
| Who | One person, end to end | One person, end to end, wearing a different hat on each note |
| The request | An AI Screening Platform | An AI triage pilot, wanted live |
| The world | One extract, one corpus, one vendor score file | Nineteen systems, 1,927 documents, and a drop each week |
| Your job | Find the problem, follow a small agent to a handoff, and keep the pilot stopped | Find which problems are real, build what is justified, and hand over a system the authority can govern |
| Guide | [Week 00 — Self Paced](<Week 00 - Self Paced/README.md>) | [Week 01 — Week 06](<Week 01 - Week 06/README.md>) |

## Week 00, module by module

The working guide, including how to run the checkers, is [Week 00 — Self Paced](<Week 00 - Self Paced/README.md>). Run those commands from the `Week 00 - Self Paced` folder.

| Module | You leave with |
|---|---|
| [01 — Problem discovery](<Week 00 - Self Paced/Module 01 - Problem Discovery/README.md>) | An ask log and a problem brief |
| [02 — Tools the agent can trust](<Week 00 - Self Paced/Module 02 - Tools the agent can trust/README.md>) | Functions that match the discovery counts |
| [03 — Retrieval](<Week 00 - Self Paced/Module 03 - Retrieval/README.md>) | A cited passage, with the rule in force kept apart from a draft |
| [04 — The agent](<Week 00 - Self Paced/Module 04 - The agent/README.md>) | A reply that names the tool, the document, and the result |
| [05 — Evaluation](<Week 00 - Self Paced/Module 05 - Evaluation/README.md>) | A scored set, with each failure named |
| [06 — Run it in their environment](<Week 00 - Self Paced/Module 06 - Run it in their environment/README.md>) | A start command, an access log, and a result file |
| [07 — The handoff](<Week 00 - Self Paced/Module 07 - The handoff/README.md>) | Two pages, a runbook, and a pilot that stays stopped |
| [08 — Capstone](<Week 00 - Self Paced/Module 08 - Capstone/README.md>) | A refusal, or a later slice, for a new ask |

## Weeks 1 to 6

The working guide is [Week 01 — Week 06](<Week 01 - Week 06/README.md>). Generate the data once before Week 1. The commands are in that guide. Participants then work from [the data guide](<Week 01 - Week 06/data/README.md>).

Facilitators and maintainers use [problem_simulation](<Week 01 - Week 06/problem_simulation/README.md>). [PLAN.md](<Week 01 - Week 06/problem_simulation/PLAN.md>) is the design, including the hidden model and the answer key. Leave it closed during the engagement.

| Week | What arrives | You leave with |
|---|---|---|
| [01 — Problem discovery](<Week 01 - Week 06/Week 01 - Problem Discovery/README.md>) | The base handover | A brief that says which problems are real, and how big they are |
| [02 — Enterprise data](<Week 01 - Week 06/Week 02 - Enterprise Data/README.md>) | A new registry schema | One record per person, and contracts that fail when the feed changes |
| [03 — Retrieval and ML evidence](<Week 01 - Week 06/Week 03 - Retrieval and ML Evidence/README.md>) | A data-protection restriction | A cited rule, and a vendor number the memo still allows |
| [04 — Graph retrieval and integration](<Week 01 - Week 06/Week 04 - Graph Retrieval and Integration/README.md>) | A letter-bureau incident | Who was not reached, and an answer that needed more than one record |
| [05 — The agent and the re-plan](<Week 01 - Week 06/Week 05 - The Agent and the Re-plan/README.md>) | A new scope, and a press query | A refusal with a plan, and an agent that stops when a rule forbids the action |
| [06 — Architecture, governance, and handoff](<Week 01 - Week 06/Week 06 - Architecture, Governance, and Handoff/README.md>) | A named safety owner, with conditions | A pack the authority can govern, and a pilot that stays stopped |

## Where the files are

| Path | What it is |
|---|---|
| `README.md`, `FDE.md`, `target_audience.md`, `health_language.md` | Shared. Both tracks use them. |
| `Week 00 - Self Paced/` | The eight modules, their reference code, the small extract in `data/`, and that world's generator in `problem_simulation/` |
| `Week 01 - Week 06/` | The six week folders, the deep extract in `data/`, and the generator, checks, and mock APIs in `problem_simulation/` |

The two `data/` folders are different worlds. A count, a date, or a site from one does not belong in the other.

| Extract | Guide | How it gets here |
|---|---|---|
| Week 00 | [data/README.md](<Week 00 - Self Paced/data/README.md>) | Already in the repository |
| Weeks 1 to 6 | [data/README.md](<Week 01 - Week 06/data/README.md>) | Generated once after cloning. Only the guide is in git. |

## What stays closed

`data/truth` and `data/eval`, in either track, are the hidden copy and the answer key. The client did not hand them to you.

In Weeks 1 to 6, also leave each week's `reference_*` folder closed, and leave a later week's drop closed until that week starts.

## Commands

Run a track's commands from that track's folder.

Week 00 checkers run from `Week 00 - Self Paced`. The list is at the end of [that guide](<Week 00 - Self Paced/README.md>).

Weeks 1 to 6 generate their data from `Week 01 - Week 06/problem_simulation`, then run each week's checker from `Week 01 - Week 06`. The commands are in [that guide](<Week 01 - Week 06/README.md>).
