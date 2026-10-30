# Idea pack — Module 01 Lesson 02 — Which approach, if any

This folder is an independent curriculum-research memo for `rel-m01-l02`. It does not replace the student copy, the solution copy, the slides, or the checker. No file under `Module 01`, `course_design`, `instructional`, or `problem_simulation` was edited to produce it. A later editor who adopts a recommendation must change those trees on purpose. Nothing here is a student handout. Participants should not read it before the finish chapter.

Case date inside the lesson remains 11 January 2027. The research date for vendor pages and papers is 30 October 2026. Where a vendor page can move, the citation says so. Where a number was not re-measured from a primary PDF, the citation says that too.

## Thesis

A multiple-choice approach memo is too static for the decision this lesson claims to teach. The syllabus line is to compare prompting, retrieval, fine-tuning, agents, and traditional machine learning, and to select an architecture. The graded artifact is a nine-row table whose families, measurements, citations, claim rows, sizes, and even a full ranking are printed in student chapter 07 before the learner types anything. Chapter 04 already prints the practice DNA result `person 0.0000` and explains why `p16` through `p23` disagree with the one-feature rule. A learner can pass `chk-approach` and `chk-brief` by transcription.

That was a defensible classroom shortcut when the menu felt stable: rules, a classical model, retrieval, an agent, or nothing. It is a weak shortcut after 2025–2026. Reasoning models make a single tool-using call look like a universal architecture. Small on-prem models make fine-tuning look cheap and private. Vendor optimization docs now tell new users that hosted fine-tuning is winding down and that a frontier prompt is the start. Classical forecasting evidence still says a seasonal baseline, ETS-class models, or gradient boosting on a later window, not a language model that ingests the monthly counts. Clinical urgency remains a blocked decision under the cluster rule and under device-regulation analogues. Slot holding remains a transaction in a scheduling system of record. The lesson should force a costed, measured selection, including problems where any model is the wrong tool.

The nine problem ids stay. The family floor stays, because Lesson 3 intake, Lesson 4 tools, and the Module 3 adapter already depend on it. What should change is the work that earns the floor: a baseline the heavier method must beat, a split that matches the unit of decision, a price from `prices.csv`, a system of record, a forbidden action, and a written reason a 2026 default (reasoning model, small fine-tune, or agent) loses.

## Status labels used in this pack

| Label | Meaning in these pages |
| --- | --- |
| Proven | A textbook method, a regulator's published criterion, a replicated empirical result, or a behavior already fixed in this course's gold and checks. Safe to teach as the default. |
| Emerging | A real shift in tools or practice with a narrow, evidenced use. Teach as a conditional option that must beat the proven default on this client's data. |
| Experimental | A preprint, a vendor claim, a method that failed the ablations we could verify, or a transfer from another industry. Teach as a hypothesis the memo must reject or park, not as a technique to deploy. |

Uncertainty is marked in the sentence that carries it. This pack does not invent benchmark scores. Clinic demand figures from DeLurgio and colleagues (2009) and the M5 retail competition are not Al-Waha results. The practice-file scores (`row 0.7692`, `person 0.0000`, `keyword 0.3125`, `filled 5`, `seasonal 2.1667`, `mean 12.0324`) are the course's own printout, from the solution copy, not external science.

## What was read

In the repo: `instructional/curriculum-understanding-map.md` (Lesson 2); `course_design/module-01.md` and `course_design/slides/module-01-lesson-02.md`; every student-copy markdown in `Module 01/Lesson 02/Student_Copy`; the solution README and chapters 01 and 03 through 06; `packet/templates/approach.md` and `brief.md`; the four baseline scripts; `prices.csv`; the opportunity register and the five extracts; `problem_simulation/design/02-real-problems.md`; family gold in `alwaha/samples/gold.py`; `tests/test_m01_l02_checks.py`; the module 1 trace. The letter sample was not copied into this folder.

Outside the repo, pages were fetched or searched on 30 October 2026. The load-bearing ones are listed in `05-tradeoffs-recommendations-sources.md`. Five that most change the lesson are repeated in the executive close of that file.

## How to read the pack

| File | Job |
| --- | --- |
| `01-existing-lesson-evaluation.md` | What the current release teaches, what the checks actually enforce, where chapter 07 collapses the lab into a key, which traps are real, which are softer than the facilitator map. |
| `02-industry-research.md` | Decision frameworks, person-level leakage, clinic-demand forecasting, DNA prediction and its ethical limit, triage as a safety boundary, build versus buy for patient access. |
| `03-redesign-architecture-and-simulation.md` | Four architectures compared. A simulation that keeps `rel-m01-l02` and adds the measurements the memo now needs. Failure cases. A redesigned row for each problem id. |
| `04-exercises-assessment-instruction.md` | Prerequisites, a self-paced path that does not print the nine answers, exercises, and a rubric the checker can enforce without echoing the hidden family. |
| `05-tradeoffs-recommendations-sources.md` | What to delete, what to keep, what not to promote into a new calendar day, tradeoffs, and the source list. |

Read 01 before 03. Read 02 before treating any redesign number as external fact. The course's fictional SAR figures are teaching weights. `harm.week_waiting` is explicitly a teaching harm weight in `02-real-problems.md`, not a clinical utility.

## The decision the current memo flattens

Gold in `gold.py` already encodes the safety floor. Required and forbidden families:

| Id | Required | Forbidden model families | 2026 pressure that chapter 07 does not make the learner meet |
| --- | --- | --- | --- |
| `p-bounce` | `extract` and `retrieve` | none | A small on-prem fine-tune looks like the whole answer. The return still needs the clause that is in force. Labels cost `cost.label`. The adapter belongs in Module 3. |
| `p-waitlist` | `no-model` | none | Probabilistic matching is easy to sell. The harm is a bad merge (twins, mother and newborn). The money figure parked on this row is the director's return cost, not a waitlist measurement. |
| `p-dna` | `classical-ml` | none | A reasoning model "reading the row," a row split, or `appointment_status_final`. The honest action is a reminder or a human callback, not silent overbooking of `d-rim`. |
| `p-status` | `agent` | none | A long prompt that states status without a tool. Also the opposite error: an autonomous agent that books. Status is one read-only tool call. |
| `p-slots` | `no-model` | every model family | A reasoning model that "judges" whether to hold a slot. The session book already serializes that write. |
| `p-clock` | `no-model` | every model family | Any model of the median. The defect is `booking_date`. |
| `p-info` | `retrieve` | none | Fine-tuning the circular into weights, or a long-context model that still cites a draft. |
| `p-forecast` | `forecast` | none | An LLM forecaster that never beats `seasonal` on a later window. |
| `p-triage` | `blocked` | every other allowed family | Ranking the 3,000,000 SAR claim first, or calling urgency a fine-tune because a vendor table lists medical diagnosis as a training example. |

`chk-approach` already rejects a model word on `p-clock`, `p-slots`, and `p-triage`, and it does not print the family that would have fitted. That part is worth keeping. The chapter that precedes the check prints the fitting rows anyway. The trap "ranking `p-triage` first" is softer than the facilitator map: any order of the nine ids passes, and triage may lead if the same line says a clinician assigns urgency. A sponsor-friendly ranking can still put the blocked use case in slot 1.

## What this pack refuses to do

It does not publish a DNA overbooking procedure, a feature recipe aimed at a district, or an urgency-grading prompt. Those are the harms the lesson exists to refuse. It does not tell a learner to paste PHI, the letter file, or a watermark into a coding assistant. It does not treat Epic, Oracle Health, or Mawid as the fictional cluster's installed system. Al-Waha has its own named systems (wait-time mart, session book, referral record, clinic documents). The commercial and national systems are what a forward deployed engineer must ask about before building a second scheduler.

It does not add a twenty-first release. The understanding map already pairs `rel-m01-l01` and `rel-m01-l02` inside one classroom day. A longer lab has to replace the transcription, not sit on top of it. Fine-tuning a local model stays in the later adapter lesson. This lesson records the trigger and the cost, and stops.

## Deletions, in one place

The full argument is in file 05. The deletions a later editor would make, if they adopt this pack:

1. The pasted approach rows, claim rows, size rows, and ranking key in student chapter 07.
2. The practice-file spoilers that `person` prints `0.0000` and that `p16`–`p23` all miss, in chapters 04 and 06.
3. The grading rule that any permutation of the nine ids passes.
4. The exception that `p-triage` may be rank 1 when the urgency sentence shares the line.
5. The optional status of cost, as the only economics in the graded memo. The 84-word letter count can remain a warm-up. It cannot be the business case.
6. The use of `510000` as the size of `p-waitlist`. That figure is the director's returned-referral claim. The waitlist has no baseline yet.

Keep the four scripts, the person-versus-row comparison, the unread column `appointment_status_final`, the watermark rule, the family vocabulary, the blocked row, and checkers that name the miss without naming the hidden family.

## Editor's next step

Treat this pack as a design review. If a change is accepted, the student chapters, the solution chapters, `gold.py` only where a forbidden set should grow, and `test_m01_l02_checks.py` move together. Widening the prose while leaving chapter 07 as an answer key will not change what learners do. Tightening the checker while leaving the answer key in the chapter will only change the transcription target.
