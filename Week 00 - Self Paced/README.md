# Week 00 — Self Paced

You are in the four-day track. The program map is [README.md](../README.md). The six-week track on the same client is [Week 01 — Week 06](<../Week 01 - Week 06/README.md>).

Discover the problem in a messy drop, then follow a small system through to a handoff that keeps the pilot stopped.

Who it is for, and what you leave able to do, is [target_audience.md](../target_audience.md). The practice this case trains is [FDE.md](../FDE.md). The words for the case are in [Health language](../health_language.md).

## Path

| | Read | You leave with |
|---|---|---|
| 1 | [Who this course is for](../target_audience.md) | The participants, the work, and the limit of this case |
| 2 | [FDE.md](../FDE.md) | The practice these modules train |
| 3 | [Module 01 — Problem Discovery](<Module 01 - Problem Discovery/README.md>) | An ask log and a problem brief |
| 4 | [Module 02 — Tools the agent can trust](<Module 02 - Tools the agent can trust/README.md>) | Functions that match the discovery counts |
| 5 | [Module 03 — Retrieval](<Module 03 - Retrieval/README.md>) | A cited passage, with in-force and draft kept apart |
| 6 | [Module 04 — The agent](<Module 04 - The agent/README.md>) | A reply that names the tool, the document, and the result |
| 7 | [Module 05 — Evaluation](<Module 05 - Evaluation/README.md>) | A scored set, with failures named |
| 8 | [Module 06 — Run it in their environment](<Module 06 - Run it in their environment/README.md>) | A start, an access log, and a result file |
| 9 | [Module 07 — The handoff](<Module 07 - The handoff/README.md>) | Two pages, a runbook, and a pilot that stays stopped |
| 10 | [Module 08 — Capstone](<Module 08 - Capstone/README.md>) | A refusal or a later slice for a new ask |

About four days. Each module is about half a day. From Module 02 on, the code in the module folder is the reference. You read it, run the checker, and explain the result.

## Before the checks

From the repository root:

```text
cd "Week 00 - Self Paced"
pip install pandas openpyxl
```

Every checker on this page runs in that folder, `Week 00 - Self Paced`. Module 01 can be done with a spreadsheet. The later checkers need those two packages. No API key. Docker is optional.

## 1. Module 01 — Problem discovery

[Module 01](<Module 01 - Problem Discovery/README.md>) teaches the words the case uses, then walks the engagement one note at a time. A health background is not required.

You are embedded at a simulated authority. The only request in front of you is an AI Screening Platform. Find the problem underneath that sentence before you design a system.

**Write two artifacts.** An ask log, then a problem brief. Open the debrief only after the brief exists. This module has no checker.

### The simulated engagement

There is no real client and no real patient data. We simulated the engagement and generated the files.

The client is Hartland Regional Health Authority, a fictional regional service that reports to a Ministry of Health. The generated world is a diabetic eye screening service:

- a registry of people with diabetes
- retinal photos recorded as rows
- a grader workbook
- letters and referrals
- a vendor score file
- the written rules for that service

| | |
|---|---|
| How the world was built | [problem_simulation/README.md](problem_simulation/README.md) |
| What each file means | [data/README.md](data/README.md) |
| The drop you use | [data/handover](data/handover) and [data/corpus](data/corpus) |
| Leave closed | `data/truth` and `data/eval`, when present. They are the hidden copy and the answer key |

The module tells you when to open the extract. Leave the grading files and the generator closed until it says otherwise.

## 2. Module 02 — Tools the agent can trust

Then open [Module 02](<Module 02 - Tools the agent can trust/README.md>).

The screening tools are the only part of the system allowed to count. The agent in Module 04 chooses a tool and repeats what it returns. It does not invent coverage, a queue, or a letter field in prose. The handover disagrees with itself: the cover note, the dictionary, and the issued procedure do not define eligibility the same way, and urgent cases are written as free text. A model that answers those questions from memory will sound sure and be wrong.

The reference functions live in [screening_tools](<Module 02 - Tools the agent can trust/screening_tools>). No language model. A checker accepts the run only when those functions match the Module 01 debrief, and when a reading that trusts the cover note fails.

## 3. Module 03 — Retrieval

Then open [Module 03](<Module 03 - Retrieval/README.md>).

Retrieval cites the written rule. It does not count. The issued procedure and the 14-day draft can both look similar. The retriever returns a passage with its document id and its status, and it does not relabel a draft as in force. `screening_retrieval` is the reference. No model and no network.

## 4. Module 04 — The agent

Then open [Module 04](<Module 04 - The agent/README.md>).

The agent calls the Module 02 tools and the Module 03 retriever. The reply names the tool, the document, and the result. It refuses to grade a retina, to refer without a grader, and to treat the 14-day draft as current policy. The checker uses a scripted model. A live OpenAI-compatible model is optional.

## 5. Module 05 — Evaluation

Then open [Module 05](<Module 05 - Evaluation/README.md>).

A demo is not a measurement. The practice set in that folder is scored for tool, document, result, and refusal, plus latency and how many times the model was called. `data/eval` stays the instructor set. The practice check is enough to finish the module.

## 6. Module 06 — Run it in their environment

Then open [Module 06](<Module 06 - Run it in their environment/README.md>).

The service starts the agent, writes who asked to an access log, and appends the reply to a result file. It does not copy patient images or the API key. The checker does not need Docker.

## 7. Module 07 — The handoff

Then open [Module 07](<Module 07 - The handoff/README.md>).

One scope for the Chief Digital Officer and the ophthalmology lead, plus a runbook. The clinical safety owner is unassigned, so the pilot does not start. The pack in [handoff](handoff) is the reference. The checker reads it and does not call a model.

## 8. Module 08 — Capstone

Then open [Module 08](<Module 08 - Capstone/README.md>).

Three new asks use the same data. You write four lines on each ask, then compare them with the reference note. Each reference answer refuses the ask or leaves it for a later slice, and cites a file already in the program. The platform is not rebuilt. The pilot does not start.

## Done

You are finished when both of these are true.

The two Module 01 pages exist, and you have marked them against the debrief.

From `Week 00 - Self Paced`, each of these prints a pass:

```text
python -m course screening_tools.check
python -m course screening_retrieval.check
python -m course screening_agent.check
python -m course screening_eval.check
python -m course screening_service.check
python -m course screening_handoff.check
python -m course screening_capstone.check
```

You can also say, without the notes open, which tool a count came from, which document a rule came from, and why the pilot has not started.
