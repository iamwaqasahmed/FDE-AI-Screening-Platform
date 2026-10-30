# 03 — Redesign, architectures, and simulation

## Where the lesson should sit

Evaluation should become the spine of the course in the thin sense: every build carries a measurement contract, and this release is where the contract is executed against hidden gold. It should not become the spine by moving `rel-m03-l04` to Module 1.

The four planted rows are callbacks. Hallucination needs the citation rule from Lesson 3. Retrieval-as-wrong-authority needs audience and in-force status from the same lesson. Friday needs the working-day calendar from Module 1. The approval miss needs the hold from the agent lesson. A week-1 student who names those rows is reciting a glossary. The campaign series is meaningful only after Module 1 has taught a seasonal copy as a serious baseline. The dot-vote is meaningful only after triage has been blocked for three modules.

What is missing early is the contract, not the lab. Module 1 Lesson 2 assigns each problem id to a family (baseline, classification, retrieval, agent, forecast, no-model, blocked) and does not require a metric, a slice, a budget, or a sentence of the form "we would abandon this family if …". Module 3 Lesson 2 then scores an adapter against a floor the student did not pre-register. Module 1 Lesson 5 grades scenarios as pass or fail on a script. Those are the moments to hang a contract on. This lesson remains the first time the contract meets a hidden slice, a known shock, and a second metric that disagrees.

**Proven** to move earlier, as a one-page template with no new code: problem id, decision the metric is for, numerator and denominator, slice that must not be averaged away, budget, and the observation that would kill the approach. **Experimental** and rejected: teaching Wilson intervals, judge panels, and `ab-status` before the student has a system to measure.

Lesson 5 stays the single remeasure. This release should end with a locked baseline and a named failure to fix, not with a second score. That split is already right.

## Five architectures

They compose. Picking one is how a team fools itself. The comparison is which instrument is allowed to decide which question on this case.

### 1. Human gold only

**Proven.** The grading service holds labels. The development file shows predictions. The student writes a scorer. The grader joins labels and scores. No model is asked whether the answer was good.

Use it for every field that has a key: `source_type`, `specialty`, `sub_specialty`, document id, span, journey state, `approved`. The current `score.py` path is this architecture, and it is the part of the lesson that should survive a redesign. Cost: someone must label, which in this course is the item writer, once, when the pack is built. That is the labeling vendor. The student never is. A self-paced cohort of one can be graded forever on a frozen key. The key cannot cover open advice ("what should I do about this symptom"), and the course already blocks triage, so the uncovered region is out of scope on purpose.

Failure mode: a gold set that matches the demo distribution and misses the slice that matters. Three lines in `score.jsonl` are not a gold set. The held-out slice is. The student never sees its size. The report should still be required to name the slice definition (specialty, audience, district, document status) even when the rows are hidden. Otherwise "clears its budget" is a slogan.

### 2. Automated metrics

**Proven** when they are deterministic functions of gold and prediction. Field accuracy (rename it), exact citation, journey conjunction, id-based context precision as RAGAS documents it for id systems. **Emerging** when the metric is itself a model: RAGAS faithfulness, answer relevancy, an LLM extraction of claims. Those are useful as monitored diagnostics and unsafe as the gate.

On the planted rows, deterministic metrics and RAGAS answer different questions. Faithfulness can be high for the unauthorized circular and low for the night-hours clause, as file 02 spells out. A Friday slot can be a perfect citation and a failed journey. The gate should fail the journey. An automated generation score should not be allowed to wash the journey out.

Failure mode already in the shell: a constant 1.0. A second failure mode to add: a micro-average that clears 0.80 because a large district is fine and a small district is not. The shell returns a point. The new shell should return a true pooled score that hides a slice. The pass condition is the slice table, not the pool.

### 3. Calibrated judge

**Emerging.** A judge is any function from answer to label that is not the gold column. Calibration is a measured agreement with gold on a set the function does not read, plus a statement of where it fails. Zheng's reference-guided result (their math probe, 70% failure down to 15% when a reference is shown) is the reason to prefer a checker that sees the in-force span over a checker that sees fluency. ARES is the reason to put an interval on the judge's error using a human set, and also the reason not to assign ARES as the lab: it wants on the order of a hundred or a few hundred human labels and a fine-tune.

Self-paced form that is still a judge. The student writes `mark(item)` allowed to read `answer`, `fluent`, `doc_id`, and `span`, and not allowed to read `pass`. The grader compares `mark` to a hidden label. The revealed calibration set is the teaching set: the student computes agreement, and a disagreement matrix, between a fluency rule and gold, including the fluent-wrong and terse-right rows. The graded set is a larger hidden file where fluency and truth diverge in both directions. An oracle that indexes `pass` fails because the attribute is absent. A fluency function fails the hidden set. A function that checks "span non-empty and doc id on the in-force list" can pass the citation rows and must still fail closed on journey rows it is not given.

Inspect's model grader is the hosted version of the same idea: temperature and seed recorded, unparsable grades unscored, panel majority, and a later calibration against oracle labels (their CJE pointer). Do not require a hosted model. Residency from Lesson 2 already forbids sending PHI to `ext-large`. The calibration subset is clinical-shaped text. A local deterministic judge is the assessable instrument. A panel of API models is **Experimental** here and should stay a reading.

Failure mode of the current solution: error rate is zero because the judge is the label. Failure mode of an uncalibrated LLM: the demo line, "marked the citation correct."

### 4. Online experiment

**Proven** as a design discipline. **Experimental** as a procedure on patients, and out of bounds for this case. Triage is blocked. An eye-screening campaign is a real-world shock, not an arm the student may randomize. `ab-status` is a wording test on status replies. Even that, if it were live, would need an OEC, a power statement, a randomization unit, and a stop rule. The course can grade the design on a frozen log.

Kohavi, Tang, and Xu: pick an OEC that is measurable now and tied to the harm you care about; do not analyze by watching every metric until one flatters you. Johari, Koomen, Pekelis, and Walsh: peeking breaks ordinary intervals. The fixture is already the simulation. `honest_pending` is the OEC. `contained` is the peek. The written rule is "no call when the intervals overlap." The code rule today is "argmax the rate," and the test requires `clause`. Replace the assertion. The report should return the metric, both rates, both intervals, and `decision: no_call` on this file. A second fixture with a large gap and non-overlapping intervals should return a winner, so the student cannot hard-code `no_call`.

Power is part of the design, not a footnote. The worksheet uses the printed n of 80 and the printed counts, shows a z near 1.3 and overlapping Wilson intervals, and computes the per-arm n at which a 10-point gap would be detectable. About 380 per arm under the normal approximation in file 02. The student is not asked to invent a clinically meaningful effect. The notice already refused to state one. The honest decision is that this log cannot crown an arm.

Failure modes to simulate in the frozen log, all gradable without traffic: a sample-ratio check (the two arms' n values differ from the planned split by enough to refuse the analysis); a peek field that reverses the winner; a metric move that is large on a vanity count and flat on the OEC (Twyman's law as Kohavi's book flags it). Do not simulate harm to a patient. The status wording is the outer limit of what this case should randomize, and only on paper.

### 5. Slice dashboard

**Proven**, and currently the optional file. `by_district` exists and is not wired to citation or journey, and `chk-eval` does not read it. Module 4's fairness check arrives later, by district and insurance class. The harm of waiting is that Lesson 5's "one fix" can optimize the pool.

The dashboard for this release is small enough to grade:

| Slice | Why it can diverge from the pool |
| --- | --- |
| District | Campaign lift and clinic volume differ. An empty district is `(0, 1)`, not a perfect rate |
| Audience | Patient versus staff. The staff leaflet cited to a patient is a retrieval failure the pool of staff questions will not show |
| Document status | In force, draft, unauthorized, superseded. Lesson 3's trap |
| Specialty | v4 covers three specialties. A pool dominated by those three hides the rest |
| Task | Extraction, citation, journey. A single "quality" number is the average the budgets were written to prevent |

A row passes the dashboard when every required slice meets its budget or is reported as `no_evidence` with the full interval. A pool above 0.80 with one failing slice fails the check. Intervals are foundation. The GitHub job can stay, and it should run this table.

Failure mode: too many slices on too little data, every interval from 0 to 1, nothing decidable. The contract names three slices, not a cross of everything. Power and slices are the same topic. A slice smaller than the worksheet's detectable n is reported, not celebrated.

## Recommended stack for the case

Human gold for keyed fields. Deterministic metrics on that gold. A slice dashboard with Wilson intervals as the thing `benchmark.md` must contain. A calibrated checker only for the fluent-citation task, banned from reading `pass`, scored on a hidden split. A frozen experiment record whose only legal decision on the current counts is no call. The workshop writes the OEC and the non-goals. It does not vote.

**Delete** as an architecture: "ask a strong model, hold a workshop, ship what the room liked." Zheng's own breakdown says the judge is weakest when the two answers are close, which is when a workshop is most confident. The seats file is a workshop of that kind. Layla's Ramadan date, Noura's no-show story, Hassan's arbitrary returns, and Sara's data-protection caution do not combine by dots. They combine by constraints: triage stays blocked, patient data stays in the residency ruling, demand after the announcement is not last year's month, and a booking without approval is a design bug.

## Simulation and datasets

The pack should keep secrets where it already does, and stop revealing the ones the skill requires.

Keep hidden, as now: held-out extraction, citation, and journey labels; the canary; visit counts out of the failure message. The student may read `ophth.csv` because the notice says to. The graded forecast should change, though. Split the series. Give months through January 2027 in the student file. Hold February and March on the grader. The student's function returns a prediction from the pre-campaign history plus the announcement flag. The grader scores a proper scoring rule or an interval that covers the held months, and fails a point prediction equal to last year's months. An exact copy of the held months is then impossible, which removes today's pass condition of reading the answer. If that is too large a jump for one release, an intermediate grade is acceptable: the function must refuse a seasonal copy and must attach an interval whose width is greater than zero. Exact equality to realized visits would no longer pass.

Reveal, as now, a small calibration file where fluency and truth disagree. Add a hidden calibration file the function cannot see. Three public rows teach the pattern. They do not measure a judge.

Add a paraphrase log of the four failures, held out, with the same types and none of the substrings `unauthorized`, `friday`, `not on file`, or `approval: none`. Grade `classify` on the union of the public log and the paraphrase log. Keyword order bugs (unauthorized before friday) become visible if one paraphrase contains two clues. Publish the codebook: hallucination means the claim is not in any citable document; retrieval means a document was used and it is not in force for this asker; reasoning means a calendar or preference rule was broken; workflow means a required human step did not happen. Ask the student to mark which Barnett point a retrieval row is, when the trace includes rank and context. If the trace is only the final sentence, the codebook should say "insufficient" rather than force a guess. That option is **Proven** and stops the keyword game.

Add a double-annotation matrix, synthetic and labeled as synthetic. Two raters, a few dozen rows, one skewed class so raw agreement and kappa separate. The student computes both and writes one sentence on why they differ. No vendor. The matrix is the dataset. A third rater with missing rows is the alpha exercise, optional and still arithmetic.

Add a slice score file the grader holds: same metrics, broken by district and audience, with one empty district and one audience under the budget while the pool is over it. The student function returns a dict of slices. The page must name the failing slice. "Clears its budget" without a slice name fails.

Keep `ab-status.json` counts public only after `experiment.md` is hashed or submitted. Practical self-paced mechanism: chapter 3 shows the notice and not the JSON; a check records the OEC file; a later chapter opens the counts; the analysis check loads both and fails if the OEC file's hash was missing, or if the decision uses `contained`, or if a winner is declared while intervals overlap. The unit test that asserts `winner == clause` is removed.

Campaign simulation stays tabular. Do not add a stochastic demand model unless the forecast task changes as above. A one-parameter lift ("visits increase by a factor the student must set") is **Experimental** and will be gamed. An interval that must cover a held outcome is harder to game and still small.

Edge cases the pack should contain at least once:

- Empty district, interval `(0, 1)`, and a report that treats it as a failure of evidence rather than a rate of zero or one.
- Fluent and wrong; terse and right; fluent and right. The third exists in the public file and must not be the only pattern.
- A citation of an in-force document with the wrong span. Retrieval versus hallucination has to be distinguishable. Today's keywords never collide.
- A Friday offer that respects gender preference, and a weekday offer that ignores it. `log-friday` currently bundles both faults. A single label hides which fix Lesson 5 should ship.
- A booking with approval and a wrong slot. Workflow can pass while the journey fails.
- An in-flight referral still on criteria v3, which Lesson 3 said is correct. Labeled as a retrieval failure, it teaches the wrong lesson.
- Arms of unequal n, so a rate comparison that ignores n fails.
- A metric that improves while the OEC worsens, which the current contained-versus-honest_pending pair already is.

Production scenario the readout must be allowed to say: offline gold on a frozen pack is not evidence the assistant will survive the campaign month. Barnett's paper says RAG validation happens in operation. The course's honest version is a monitoring list for Lesson 5 and Module 4: citation failures by audience, journey failures by approval state, demand versus the session plan, and the OEC on status wording if that test is ever run. No new model.

## What one person can hold

The five roles stay. They become checks on artifacts, which they already are, with harder artifacts.

Lead locks the OEC and the slice list before the counts, and sequences score, then failure names, then the value note. Data computes the metrics, the intervals, and the agreement on the public matrix. Application writes the checker that cannot see `pass`, and the regression that rejects a fluent wrong citation by its span, not by its label column. Product writes the value note from the four seats: the OEC, the blocked triage line, and the reason a dot-vote is not a weight. Architect marks which failure is a design bug (the missing approval) and which would be a model bug (the clause not on file), and refuses a diagram of an LLM judge as the quality system.

Nobody interviews a live colleague. The seats file is the room. That is the right self-paced constraint and should stay.
