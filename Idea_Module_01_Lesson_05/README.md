# Idea — Module 01 Lesson 05 — Score, design, readout

Research only. This folder does not change `Module 01/Lesson 05`, the checks, or the packs. Lesson id: `rel-m01-l05`.

## Verdict

Make this lesson the **agent-evaluation spine**. Keep statistical evaluation in Module 3. The spine is a small contract later lessons extend: an outcome scorer, a trajectory scorer, a written failure budget, and one decision record whose consequences name what the proof does not yet show.

The steering readout **can be graded without a facilitator in the room**. Grade the memo. The interview command already plays `cdo`. Oral delivery is a different skill and stays off the pass line.

What stands today is a deterministic policy grader plus five pasted pages. `chk-agent` and `chk-trajectory` are real scorers. `architecture.md`, `design.md`, `readout.md`, `trace-note.md`, and the sentences in `knowledge.md` are not yet an architecture decision or an evaluation the learner can defend.

## How to read this folder

| File | Question it answers |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What the lesson, the solution, the slides, and the tests actually grade |
| [02-industry-research.md](02-industry-research.md) | Trajectory versus outcome, Inspect, vendor harnesses, ADRs, C4, arc42, slot races, executive evidence, artifact rubrics. Each practice is Proven, Emerging, or Experimental |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Four alternatives. The recommended spine. How the mock should show a hold and a conflict. What later modules append |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Exercises, the self-paced rubric, and the order of instruction |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Tradeoffs, deletions, the recommendation, and the sources |

## Recommendation in one pass

1. Keep the re-run of the agent. A timeout that books still fails. A second `slots.book` on one slot still fails. Emergency still redirects. Triage stays unbuilt. G2 stays open.
2. Name those checks as fitness functions and put the allowance in a failure-budget table the learner writes from the trace.
3. Split outcome from trajectory. Exact tool order stays only where the policy requires it (write after approval, redirect before any book, no book after timeout).
4. Replace the pasted design with one Nygard decision record plus a considered-options list. The rejected option is `p-triage`. The consequences include the sequential mock and the missing hold expiry.
5. Replace the pasted flowchart with one C4 container diagram and one dynamic view whose human step is the coordinator’s authority over `slots.book`.
6. Grade `readout.md` as a one-page decision memo: decision, evidence, residual, ask. Require G2, not any gate from G1 through G5. A scripted challenge question is answered in writing.
7. Leave Module 3 Lesson 4 as the home of slices, calibration, and the judge. Leave Module 4 Lesson 1 as the home of the DPIA. This lesson names G2 as open and lists the evidence still missing.
8. Treat Braintrust, LangSmith, and Phoenix as optional viewers. The scorers stay in the course checker.

## What this research will not do

It will not invent a clinic SLO, a pass rate the proof must hit, or a vendor the learner must adopt. Numbers that appear in the research files are quotations from the cited source, marked as that source’s result, and are not targets for Al-Waha.
