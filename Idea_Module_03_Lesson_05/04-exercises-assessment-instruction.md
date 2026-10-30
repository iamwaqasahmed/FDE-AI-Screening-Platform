# Exercises, assessment, and self-paced instruction

The learner is one person. They hold the CDO, DPO, access, PHC, and engineer seats by writing them, not by waiting for a group. There is no facilitator performing the three-minute disagreement. There is no cohort workshop. Prerequisites are the earlier lessons this course already requires. Time is unscheduled; each exercise ends when its check passes or when the learner's page records a budget refusal.

## Prerequisites

From Module 1: `p-triage` is blocked; a sponsor sentence is not a plan; G2 can be open while other work proceeds; claim, request, and fact are different. From Module 2: patient data stays off `ext-large`; the model register exists. From Module 3 Lessons 1–4: labels are not the learner's to invent; retrieval cites an in-force document the asker may see; in-flight referrals keep their criteria version; the benchmark draft names four failure types; a dot-vote is not the value model; an uncalibrated judge is not a measurement. The learner does not need 29148, ARP4754A, or the ML Test Score paper. The chapters teach the slices of those sources that the exercises use, in the course's own words, with the external names in a margin note. **Label: Proven** as sequencing. Adding a standards-reading homework before the lab is **Experimental** and should stay optional.

## Lesson 5a exercises

**E1. Hypothesis, before any paste.** The learner fills `hypothesis.md`: the log id they will try to move; the mechanism name; two log ids they will not move and why those mechanisms differ; the comparison (document and span, before and after); the cost key they will use; the rule if spend returns nothing. The chapter does not contain the finished paragraph. A sidebar defines mechanism names they already met in Lesson 4.

Check: the chosen id is `log-circular`; the other three ids appear as residuals; the comparison names both document and span; `cost.label` appears with the veto sentence. This replaces the substring sprint check. **Label: Experimental.**

**E2. Repair and remeasure.** Same functions as now. The learner may still be shown a worked pattern of copying a dict and replacing one field, because syntax is not the lesson. They are not shown the two ids side by side in the paste. The unauthorized id and the in-force id are constants they find in the public slice and in the release note that already distinguishes the unauthorized circular. If that note does not name both ids, the test file's fixture does, and the chapter points at the test rather than inlining the function.

Check: unchanged behavioral checks on repair and remeasure. Add a fail if `improvement.md` states a before or after that disagrees with the function's return on the gold rows. The learner runs the suite and copies the numbers. The chapter does not print them. **Label: Proven** behavior, **Emerging** assessment.

**E3. Cost veto.** The learner calls `spend` with the sheet's price and the budget file's ceiling and writes the result. Over budget, the improvement page's claim line says the change is not shipped. The benchmark's second-run sentence is omitted in that branch. Steering would rather hear a refusal than a fake gain.

Check: the number matches gold, including `None`. The page's claim is consistent with that result. **Label: Proven** for the function. **Emerging** for grading consistency between the function and the page. Today's check grades them separately, so a page can claim a gain the budget refused.

**E4. Residual list.** Three failures stay open, each with mechanism and the reason this change cannot move it (different defect: clause not on file, Friday calendar, missing approval). Retro Open names one experiment not run.

Check: the four pairs remain. A sentence that says the second run moved hallucination, reasoning, or workflow fails, even if retrieval is also present. **Label: Emerging.** This is the deletion of "second" plus "retrieval" as a sufficient bigram.

5a does not ask for `rcp/requirements.md`. The readout at the end of 5a is five lines: what moved, what did not, what it cost, what was refused, what assumption the slice tested. That page is the input to 5b, not the client spec.

## Lesson 5b exercises

**E5. Problem statement.** Half a page. People (patient asking for hours; clerk; DPO). Job (get an answer they may see; keep patient data in the private cloud). Consequence of doing nothing (the unauthorized circular remains citable). No solution noun from the banned-and-paraphrase list. The CDO card is attached so the learner has to decide not to copy it.

Check: solution lexicon absent from this section; a person and a job present; the unauthorized-citation harm present in the learner's words, graded by a small set of content facts (unauthorized or not-in-force, and a patient or asker), not by a pasted sentence. **Label: Experimental.**

**E6. Tree, one page.** Outcome, at least two opportunities drawn from different seats, at least three solutions of which two are marked unconnected, one experiment row pointing at 5a's result. Triage hangs off no opportunity, or off an opportunity the learner explicitly says the value note does not support.

Check: `p-triage` and `vendor-bot` appear only in the unconnected or exclusion band; `req-cite` or its successor id appears under an opportunity; the experiment row cites the 5a before/after. Missing picture-perfect graphic design is not a fail. A table with four headings is enough. **Label: Emerging.**

**E7. Shall-statements.** Five requirements, ids stable, one shall each, conditions, verification test id, gate. The clinician rule is a positive shall. Residency is its own id, not a clause glued to citation. The cost veto is its own id. Audience names the vocabulary of the test it points at.

Check replaces the 80 percent mention score. Structural fails, each reported once, without printing the learner's missing token back at them if the current checkers' silence rule stays:

- A shall-statement with two predicates.
- A requirement whose parent outcome is `OUT-WAIT` or whose text promises wait time, no-shows, or returned referrals.
- A requirement that names the fixture document ids (those belong in tests).
- Safety-relevant ids (`REQ-AUD-1`, `REQ-RES-1`, `REQ-URG-1`) missing a test id.
- `p-triage` or `vendor-bot` inside a shall-statement.
- Scope or problem statement containing the sponsor sentence or a paraphrase the lexicon lists (front door, before Ramadan, virtual front desk, including triage).
- Gate G4 or "go-live" on any of these ids.
- G2 marked closed.

The old facts that are still right — DPO as the seat for the residency ruling, `dms` as the system for the citation requirement, G1 as the risk tier — become attributes, not free-text souvenirs. **Label: Experimental** for the new checker. **Proven** for the underlying rules.

**E8. Assumption log.** At least four rows. Required rows the gold expects to exist, not the prose:

| Id | What must be true | Acceptable status |
| --- | --- | --- |
| `ASM-SPAN` | A hit is document and span, not document alone | tested-pass, evidence is the 5a comparison |
| `ASM-BUDGET` | Label spend fits the annotation budget | tested-pass or tested-fail, consistent with E3 |
| `ASM-LAT` | Latency under campaign load | deferred, owner named, review at the surge lesson |
| `ASM-DEL` | Deletion reaches indexes and models | deferred, owner DPO, review at Module 4 Lesson 1 |
| `ASM-VALUE` | Citation work outranks triage on the value model | untested if the learner cannot point at Lesson 4's ranges; tested-pass only with a pointer |

An assumption marked tested-pass with no evidence pointer fails. **Label: Emerging.** This is the 29148 assumption attribute, shrunk to a table.

**E9. Trace and stranger check.** The learner fills the trace table in `03`. Then they write a paragraph titled "What you can build from this file alone" that names the tests and the exclusions and does not name a chapter. An author, not the learner, later runs the real stranger test on a draft of the gold brief before chapters ship. The learner's own paragraph is necessary and not sufficient.

Check: every in-set requirement id appears in the trace; every trace test id exists in the course or is marked "new" with a one-line oracle; every exclusion id is absent from the trace's requirement column. **Label: Experimental.**

**E10. Readout to steering.** Same five questions as `steer-m03-l05`, answered from 5a and 5b rather than from a paste. Question 5 ("what will you not copy") is answered with the exclusion register's reason, not with the slogan that copying is bad. Retro Keep / Drop / Open stays. Drop is the practice of pasting the sponsor's solution into Scope. Open is the three failures and the deferred assumptions.

Check: each steering question has a pointer to a requirement id or an assumption id. A readout that restates the CDO card fails the lexicon. **Label: Emerging.**

The personal lab is not an exercise in 5b. Audience is `REQ-AUD-1`'s test pointer. Floors are a budget attribute on the citation quality requirement, using the 0.8 already in the public personal file, with the 0.5 row as the example that fails the floor. The learner does not re-paste `personal.py`.

## How a solution looks

The solution copy is a reference brief, not a chapter the student can paste during the attempt. It is released when 5b's finish chapter says the checks passed, same rule as today.

The reference problem statement talks about a patient asking for hours and receiving a document that is in force for them, and about the harm of the unauthorized circular. It does not say front door, Ramadan, or triage.

The reference tree's outcome is citation integrity on hours questions, parented to the patient's job, not to the CDO's channel. Opportunities include "the answer cites a document I am allowed to see" and "no-shows are expensive," and only the first has a solution in this release. Triage and the vendor bot are unconnected. The experiment row shows the before/after the gold remeasure returns on the public fixture (0.8 then 1.0 on the five-row slice, one document moved) and states that this does not move the other three logs.

The reference shall-statements follow E7. The reference assumptions follow E8, with `ASM-VALUE` set to whatever Lesson 4's published ranges actually support. If those ranges do not rank citation above triage in a way an author can point at, the reference marks `ASM-VALUE` untested rather than inventing a ranking. That choice should be made by reading Lesson 4's value note when the chapters are written. This research does not invent the ranking.

The reference trace matches E9. The reference readout answers the five steering questions with ids. Interview notes for CDO and DPO, which the current solution carries and the checker ignores, become unnecessary. The conflict is in `conflicts.md` and the decision is in the exclusion register. If authors want color, they can keep unscored notes. They must not hide a required fact only in those notes. Today's solution already records that the checks do not read them. The redesign keeps that honesty and stops using the notes as if they were the workshop.

## Assessment principles

Grade artifacts the learner composed. Do not grade a block that appears in the chapter above the exercise.

Prefer structural fails to phrase fails. Keep a small lexicon for the sponsor paraphrase, because structure alone will not catch "one front door." Publish the idea of the lexicon ("channel, date, and triage claims") in the words chapter. Do not publish every banned string if the course's current practice is to avoid handing the answer to the checker. The current checker already uses exact strings. Moving to a lexicon is not a secrecy improvement. It is a coverage improvement. **Label: Emerging.**

Do not print prices, document ids, or gate ids in failure messages if that silence rule is still wanted. The redesign can say "the cost claim disagrees with the budget" without printing the sar figure. It can say "a safety requirement has no test" without printing the id the author forgot, or it can print the id. Printing the requirement id helps a self-paced learner. Printing the gold document id does not. Split that rule. Today's silence is one message for both.

Keep the watermark and canary behavior. A copied gold file still fails closed.

The improvement-gate workflow job changes meaning. In 5a it runs `tests.test_remeasure` and `tests.test_cost`. It is named `regression`, not `improvement-gate`. The stage gate lives in the spec's attribute column. A YAML comment is a weak model of G1. **Label: Proven** that regression tests should run. **Experimental** to delete the theatrical job name. Deletion is recommended.

`chk-individual-m03-l05` moves out. If program structure demands an individual check on every lesson, point it at E5 and E8 written alone, without a partner. Do not keep a second audience function as the individual evidence.

Coverage at 80 percent goes away. A missing safety requirement is not offset by mentioning four seat names. Seat names move to the tree and are necessary there, not a substitute for `REQ-URG-1`.

## Self-paced instructional design

Chapters stay short and single-purpose. The current chapters spend most of their lines on paste mechanics. Those lines exist because the course has been hurt by styled pastes. If 5b is mostly tables the learner fills, the paste-mechanics boilerplate shrinks. Provide empty templates in the packet, the way the current requirements template provides headings, and stop providing filled bodies in the student chapter.

Suggested 5a chapter order: background; the four failures and the one this change can affect; hypothesis; repair and remeasure; cost veto; residual page; finish. Suggested 5b order: the sponsor card and why a concern is not a requirement; problem statement; tree; shall-statements and the shall/will/should note; assumption log; trace; readout; finish. Words pages define shall, will, should, non-goal, safety requirement, assumption status, and trace. They define them before the exercise, with examples that are not the gold ids.

One person, five jobs, sequenced so they cannot be skipped:

1. Engineer: 5a measurement.
2. Access and PHC: opportunities written from those cards, including the ones this release will not serve.
3. CDO: the concern copied into a "heard" column and kept out of the shall-statements.
4. DPO: residency, audience, open G2, deferred deletion.
5. Lead: readout that shows the disagreement and the decision.

A learner who writes only as the CDO fails E5 and E7. A learner who writes only as the engineer fails the tree's second opportunity. That is the workshop, done on paper.

## What not to assess

Do not grade graphic quality of the tree, tone, or whether the learner "sounded like" a consultant. Do not grade a recitation of 29148's nine characteristics. Do not grade an ML Test Score out of 5. Do not grade a latency number the packet does not contain. Do not grade a second code change. Do not grade interview role-play. Do not grade the personal module twice.

## Pilot

Before chapters replace the current lesson, one author who did not write the gold brief implements from the reference `rcp/requirements.md` and the public pack only. They either pass the existing repair, remeasure, cost, and audience tests or they mark the brief's line that blocked them. A second author paraphrases the CDO card into the problem statement in three ways and confirms the checker fails each. A third pass is the budget-over-ceiling profile, if the gold builder can already emit `spend is None`, and confirms 5a does not claim a gain. Those three dry runs are the release gate for the redesign. **Label: Experimental.** They are also the only assessment of the curriculum that matches the thesis: a stranger could start.
