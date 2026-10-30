# Module 03 Lesson 04 — Evaluation research

Independent curriculum note for `rel-m03-l04`. It does not change course files. The lesson already has the right objects: a hidden grading service, four failures planted in earlier systems, a campaign that breaks a seasonal copy, a fluency judge, a pre-registered metric, and a workshop that must refuse a dot-vote. The implementation grades a paste of those objects. It does not yet grade measurement design.

## Recommendation

Keep this release as the place the course *executes* evaluation, after retrieval, the adapter, the calendar, and the approval rule exist. Move a one-page measurement contract earlier, into Module 1 Lesson 2, so every later build has a metric, a slice, a budget, and a disqualifier. Do not move the workshop, the campaign series, or the four log rows into week 1. Those rows are only meaningful once the student has built the systems that fail.

Inside this lesson, invert the foundation and the advanced path. Confidence intervals and the experiment record are the lesson. Uncommenting a GitHub job is plumbing.

Grade five instruments as a stack, not as rival religions:

| Instrument | Label | Role on this case |
| --- | --- | --- |
| Human gold held by the grader | Proven | Extraction fields, citation id plus span, journey state plus approval |
| Deterministic metrics on that gold | Proven | The score functions, once `extraction_f1` is renamed to field accuracy |
| Slice dashboard with Wilson intervals | Proven | A pool that clears 0.80 while one district, audience, or specialty fails |
| Calibrated checker | Emerging | Agreement against gold on rows where fluency and truth diverge. Reading the `pass` field is not this |
| Frozen, pre-registered experiment | Proven method, Experimental as a live test | `honest_pending` only, locked before the second count is shown. No patient randomization |

Delete the idea that an uncalibrated language-model judge plus a dot-vote workshop is an evaluation. Also delete the fix the current solution ships for that idea: `judge.mark` returns `bool(item.get("pass"))`. The calibration file in the student packet already contains `pass`. The required check `slice-judge` accepts an oracle.

The fixture printed in chapter 03 is the teaching object for power, and it should be treated as one. Arms `clause` and `short` each have `n` of 80. On `honest_pending` the rates are 48/80 and 40/80. A two-proportion z-test on those printed counts gives z about 1.27 and a two-sided normal p-value about 0.20. Wilson intervals with the lesson's own z of 1.96 overlap (about 0.49–0.70 and 0.39–0.61). The unit test still asserts that `clause` won. That assertion is the peek the notice forbids. This arithmetic is computed from the chapter, not taken from a paper.

## What to delete

- Calling the `pass` field a calibrated judge.
- Keyword `classify` on `unauthorized`, `friday`, `approval` plus `none`, and `not on file`, as the whole of error analysis.
- The name F1 for a field-match rate the words page already says is not the harmonic mean.
- An ungraded `experiment.md` beside a unit test that names the winner.
- A workshop grade that is the phrase `not the value model` plus four seat ids.
- A forecast grade that passes only an exact copy of realized February and March 2027 visits, described to the student as a forecast.
- The syllabus line that `chk-eval` is a draft, unless the prose rubric stays a draft on purpose. The Python checker is already strict about code and loose about sentences.

## What to keep

Hidden labels for the score slice. The two-line judge demo. The four names tied to earlier lessons (clause not on file, document not in force, Friday, booking with no approval). The campaign notice against a last-year copy. Empty-slice Wilson bounds of `(0, 1)`. One person holding lead, data, application, product, and architecture. The split that Lesson 5 does the second measurement. Triage staying out of scope. The dot-vote file as a temptation, with a real value model required in the notes.

## Index

| File | Contents |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What chapters, checks, and shells actually reward |
| [02-industry-research.md](02-industry-research.md) | Zheng, RAGAS, ARES, Inspect, agreement, Kohavi, failure taxonomies |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Five architectures, the pack, whether evaluation becomes the spine |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Self-paced tasks, rubrics, solution shape, prerequisites |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Tradeoffs, deletions, lessons to spawn, URLs |

Labels used throughout: **Proven** (a method with a stable definition and a way to grade it here), **Emerging** (sound, and still dependent on a judge, a panel, or a small human set), **Experimental** (a live or research procedure this course should simulate, not run on patients).
