# 04 — Exercises, assessment, and instruction

## Prerequisites

The student needs the prior systems, not a statistics course. From Module 1: Friday is not a working day, a booking waits for approval, a seasonal forecast copies last year, triage is blocked. From Module 3 Lesson 1: a label can be adjudicated, and agreement with that adjudication is a check. From Lesson 2: a floor and a price cap are budgets, and external models are closed for PHI. From Lesson 3: a citation is an in-force document the asker may see, drafts are not citations, and an unauthorized circular is not a source.

Arithmetic introduced on this release, at teaching depth: a rate and its Wilson interval with z = 1.96, including the empty-slice convention already in the solution; the difference between raw agreement and a chance-corrected coefficient, computed on a given table; a two-proportion comparison read as "intervals overlap, so no call," not as a derivation of the z-test. Students who want the z formula can have it in the advanced notes. The graded skill is the decision rule.

One person holds every role. The workshop is a file. There is no labeling vendor and no cohort required for agreement. Double annotation is a matrix in the pack.

## Exercises

Each exercise says what the student produces, what is hidden, and which architecture from file 03 it trains. Paste chapters remain for the workflow file only. The metric, the judge, the codebook, and the experiment decision are written, not pasted.

### E1. Measurement contract, used here and born in Module 1

**Proven.** A half page, one row per live problem (`p-status`, `p-info`, and the forecast). Columns: metric, denominator, slice, budget, disqualifier. `p-triage` appears as a row whose metric is "no metric, blocked." The dot-vote ranking is printed beside the table and is not copied into the weights.

This is the early-spine artifact. On this release the student fills it for real. On a future Module 1 Lesson 2 they fill a stub with the same columns and empty numbers. Assessment there is "the column exists and triage is blocked." Assessment here is "the numbers match the pack."

### E2. Scores against hidden gold

**Proven.** Implement field accuracy, citation exact match, and journey pass. The development file has no labels. The grader joins labels. Budgets stay 0.80 unless the item writer changes them. The report must quote the grader's returned rates. It must not invent them. If the course continues to hide the numeric score in the failure message, the pass line should still echo the three rates once, so the page and the code cannot diverge. Secrecy of log ids and visit counts can remain.

Rename the function. Teaching the harmonic mean under the name F1 and implementing a match rate under the same name is how a later module's Inspect-style token F1 will be "already done" and wrong.

Add one failing test the student can see: an empty citation slice is 0, a row that matches the document and misses the span is a miss, a journey that matches state and misses approval is a miss. The hidden set adds the slice split from E5.

### E3. Codebook on a paraphrase log

**Proven.** Public log stays, with types still absent, as now. The student writes `classify` against the codebook in file 03. The grader includes paraphrases without the four substrings. Returning `pass` for an unrecognized row stays correct. Guessing a type for a vague row is a miss. A row that bundles Friday and a gender-preference miss, as `log-friday` does today, should be split in the new pack so Lesson 5 can fix one thing. If the pack is not split, the benchmark must name both faults and say which one the student would fix first, with a reason that is not a vote.

Evidence means a quoted span from the log plus the codebook clause, not the type word alone.

### E4. Fluency is not a judge

**Emerging** instrument, **Proven** exercise. Public calibration rows stay visible. `mark` may read the answer, the fluent flag, and any citation fields, and must not read `pass`. A unit test deletes `pass` and still expects the fluent-wrong item to be rejected for a reason the student computes (empty doc id, or a doc id on a banned list provided in the pack). `slice-judge` runs a hidden file. The grade is agreement with hidden labels, reported as a count of disagreements by cell: fluent/wrong, fluent/right, terse/wrong, terse/right. A threshold is set by the item writer on that hidden file and printed as a budget, the same way 0.80 is printed. Do not borrow 80% or 85% from Zheng. Those are preference-agreement figures under the setups in file 02.

The knowledge question becomes: why can a fluent citation be wrong, and what did you compare the judge to? The second sentence must name the hidden set or the gold, not the word "fluent" alone. Keyword `fluent` plus `correct` is too weak a rubric once the chapter has used those words in the question.

A short reading item, not a build: Zheng's position swap and the reference-guided math probe; RAGAS faithfulness as a check against retrieved context, which would miss `log-circular`; Inspect's choice of exact match when a target exists. One paragraph in the student's own words, checked for the claims "preference agreement is not citation correctness" and "a judge that sees the gold label is not calibrated." No API call.

### E5. Slice dashboard

**Proven.** Return bounds per required slice and a pass bit per slice. Required cases: a pool at or above 0.80 with one audience below the budget; an empty district with bounds `(0, 1)` and a status of `no_evidence`; two districts that do not share a point estimate. The page names the failing slice and says the pool is the wrong summary. `chk-eval` reads this module. It is not optional.

The shell to beat is a dashboard of ones, which already exists, and a new shell that reports only the pool.

### E6. Experiment record

**Proven** design, frozen data. Sequence:

1. Submit `experiment.md` with the metric name `honest_pending`, the direction, the slice (all status replies in the log, not a district subset chosen later), and the decision rule "overlap means no call." The check stores a hash.
2. Open the counts.
3. Fill rates and Wilson intervals with the course function. Decision on the printed 80-versus-80 log is `no_call`.
4. A second hidden protocol with non-overlapping intervals must produce `call` and the arm name, so the rule is real.

Using `contained` as the metric fails. Declaring `clause` on the public log fails. The current unit test is retired. The trainer line "the report does not name which arm won" becomes true of the code as well as the page, for this protocol.

The power worksheet is three numbers the student computes or the notebook computes and the student interprets: z, whether the intervals overlap, and a statement that a 10-point gap at these rates needs a few hundred per arm under the approximation in file 02. Grading checks the decision and the presence of the n the student used. It does not require a hand-derived sample-size formula if the worksheet shows the result and the inputs. Inventing a p-value without the counts fails.

### E7. Agreement on a toy matrix

**Proven.** A CSV of two synthetic raters, about forty rows, mostly "pass," with a handful of disagreements on hallucination versus retrieval. The student reports percent agreement and Cohen's kappa, and one sentence: raw agreement is high because the class is common. Optional second file with a missing rater on some rows, and a prompt to say why alpha is the coefficient that fits. Do not grade a numeric alpha unless the solution ships the same library call the student uses. A hand formula for alpha on missing data is a poor use of the sitting. The conceptual sentence is the point.

No claim is made about how often human clinicians agree. The matrix is fiction, marked as fiction.

### E8. Value note

**Proven** as writing, if the rubric stops being a phrase. Required content, in the student's sentences: the four seat ids and a constraint from each; the sentence that the dot-vote ranks triage first; an OEC for the status wording (`honest_pending`) and why `contained` would pick the other arm; triage out of scope; the workflow failure named as a design bug. The exact tokens `not the value model` can remain as a required phrase so the old trap still fires, and they are no longer sufficient.

### E9. Advanced, after the checks

Keep a second layer, and change what is in it. Foundation is E2 through E6. Advanced is: continuity-corrected Wilson or a note that the lesson uses the uncorrected form (Wikipedia's binomial-interval page distinguishes them); a sample-ratio check on a log where n is 80 and 50; a paragraph on ARES-style correction that stops at "a judge needs a human set and an interval," with no fine-tune; Inspect's unscored grade when the panel splits. None of these need a model endpoint.

## Assessment

`chk-eval` should stop being marked draft once the prose rubric checks claims rather than tokens. Proposed checks, still two commands so the finish page stays simple:

`chk-eval` loads score, forecast or the new interval forecast, failures, slices, and the experiment decision. It reads the contract, the benchmark, the value note, and the knowledge answers. It fails if any required slice misses the budget, if the seasonal copy is the forecast, if a planted or paraphrased row is misnamed, if the experiment file's hash is missing or the decision peeks, if triage is placed in scope, or if the benchmark says a metric cleared when the grader's rate is under the floor.

`slice-judge` loads `mark` and the hidden calibration file with `pass` removed from the object the function receives. It fails on disagreement above the printed budget, or if the function's source text contains `item.get("pass")` or `["pass"]`. A source scan is a blunt instrument and will false-positive on a comment. Prefer deleting the key before the call, and a hidden set that a fluency rule fails. A source scan can be a secondary guard.

Messages stay free of log ids, spans, visit counts, and gold labels, as they are now. They should name the slice when a slice fails ("the patient-audience citation score misses its budget") because the lesson's point is the slice. They should not print the rate if secrecy is still required. Naming the slice does not reveal the rate.

Written rubric, four dimensions already used elsewhere in the course, applied to this release:

- Evidence: each failure name is tied to a quoted log span and a codebook line.
- Decision: the experiment decision matches the interval rule, and the value note names an OEC.
- Scope: triage and any banned clinical claim are absent.
- Honesty: under-budget slices and `no_evidence` slices are written as such. A pool average alone fails this dimension.

Lesson 5's remeasure is in scope only as a pointer: the student names which single failure the next release will fix, and which metric and slice will be recomputed. They do not recompute it here. That preserves the current split.

## Solution approach

The reference solution is short modules, same layout as today.

`score.py` returns field accuracy and the two exact rates. Docstrings use those names.

`slices.py` calls the score functions per group and `bounds` from `intervals.py`. Empty groups return `(0.0, 1.0)` and `no_evidence`.

`failures.py` matches codebook patterns that include paraphrases the author generated, not a single substring. The public examples still pass. A catch-all `pass` remains.

`judge.py` rejects a citation whose document id is missing or is on the banned-id list in the pack, and rejects fluency as a sufficient condition. It does not read `pass`.

`experiment.py` returns metric, rates, intervals, and `no_call` or `call`. The public protocol is `no_call`.

`forecast.py`, if the series is split, returns an interval per district-month from the pre-period plus a campaign flag, and the grader checks coverage of held months and rejects a zero-width interval equal to last year. If the series is not split, the interim solution keeps the later-window readout and the page must say "this is the realized series, not a forecast made on 27 January." Honesty about the task is better than the word predict on a filter.

Pages are prose a person can read. The trainer chapter shows the interval overlap on the public counts so a facilitator can defend `no_call` when a student points at 48 versus 40.

Tests the student can see cover empty slices, fluent-wrong without a `pass` field, overlap, and an empty district. Tests the student cannot see cover paraphrases, the hidden judge file, the failing audience, and the non-overlapping experiment fixture. That is the same hidden-gold pattern the score path already uses. Extend it. Do not invent a second philosophy.

## Instructional design

Self-paced, no timetable, one person. The current chapter order is right: read the protocol, run the two-line demo, then build. Change the middle. Chapters 06 and 07 should show the shell, state the invariant, and give a stub with `raise NotImplementedError`, not the finished function in a fence. The journey log's "pastes: 13" is the smell. A student who can paste cannot yet measure, and the finish check cannot tell.

Time. E1 through E8 is a full release. If a cohort is short, cut E7 and the advanced layer, and do not cut E5 or E6. The current course cuts the opposite pair.

Reading load. One page of Zheng's limitations, the RAGAS faithfulness definition, the Inspect sentence that exact match is for targets and model grading is for open text, and the Kohavi definition of an OEC. The rest of file 02 is for the author, not the student. The student words page should gain: OEC, peek, overlap, no call, chance-corrected agreement, and slice. It should lose the implication that calibration means "return the pass field."

Facilitation. The demo stays. After it, ask what feature the judge used. The answer is fluency. Then ask what feature the filled judge in today's solution uses. The honest answer is the label. That conversation is the redesign in one minute. The trainer chapter should stop saying the experiment report names no winner while `test_experiment.py` asserts `clause`.

Assessment of the assessors. Item writers are the labeling vendor. Their gold needs a second reviewer inside the team that maintains the course, scored with the same kappa exercise, on the paraphrase log. A single author who plants `unauthorized` and then grades the substring `unauthorized` will recreate this lesson. The codebook is reviewed before the substrings are chosen.

What "done" looks like on the screen: `chk-eval passed.` and `slice-judge passed.`, plus a benchmark that names one failing slice, four failures with quoted evidence, and an experiment decision of no call. The workshop page states an OEC. The knowledge page says a retrieval failure is a citation that is not in force for the asker, and a judge is calibrated by agreement with gold it does not get to read. Lesson 5 is still the second measurement.
