# 05 — Tradeoffs, recommendations, and sources

## Tradeoffs

Human gold only is the most honest gate and the least scalable. This course does not need scale. The pack is frozen, the cohort is one person, and the keys are small: three extraction fields, a document id, a span, a state, a bit. Paying for that gold once, in the item bank, is cheaper than teaching every student to trust a judge. The loss is coverage of open answers. The case already excludes those answers by blocking triage. Reopening them so the judge has something to do would be the wrong trade.

Deterministic metrics will call a fluent, fully supported, unauthorized circular a success if the only metric is faithfulness to retrieved text. RAGAS is explicit that faithfulness uses the retrieved context. Keeping RAGAS as a reading and out of the gate is the trade. Students who arrive believing "RAG evaluation means RAGAS" need the `log-circular` counterexample more than they need a library install.

A calibrated judge catches fluent wrong citations that lack a simple key, and it creates a second model to evaluate. Zheng and colleagues show position bias, verbosity bias, and a failure to grade reasoning even when the judge can solve the item alone. Their headline agreement, over 80% with humans and 85% versus humans on non-tie MT-bench votes, is preference agreement on general chat, higher when the quality gap is large. It is the wrong comfort for a citation. Inspect's answer is operational: exact scorers for targets, model graders with temperature, seed, unscored parse failures, and a later check against oracle labels. The self-paced trade is a local checker banned from the label column, plus a hidden file. That teaches calibration as measurement. It does not teach prompt design for GPT-4. Prompt design for a hosted judge belongs in a course that is allowed to send data to that host. This one is not, after Lesson 2's residency ruling.

An online experiment is the right instrument for the status wording and the wrong instrument for the campaign. The campaign is an announced shock. Randomizing it is not on offer. Copying last year through it is the forecast failure. Those are different mistakes, and the current release glues them together by calling the 2027 readout a forecast. Splitting them costs a chapter and saves the word. The peeking trade is sharper. Refusing to crown `clause` on n of 80 will frustrate students who can subtract 48 and 40. The frustration is the objective. Always-valid p-values (Johari, Koomen, Pekelis, and Walsh) are a platform feature, not a lesson. The lesson ends at "do not look at the second metric, and do not call a winner inside overlapping intervals."

A slice dashboard prevents a pool of 0.81 from hiding a failing audience. It also multiplies intervals until every cell says `no_evidence`. Cap the contract at the slices Lesson 3 and the campaign already made meaningful: audience, document status, district, task. Leave insurance-class fairness to Module 4, where the check already exists, and point to it so this lesson does not pretend to finish fairness.

Moving the whole lab earlier would detach the failures from the systems. Moving nothing earlier leaves Module 1 choosing families with no metric. The thin contract is the compromise, and it is **Proven** as a writing task.

Making intervals and the experiment record required will lengthen the release. The paste of `ci.yml` can move to advanced to pay for that time. A green pipeline that does not run the evaluation is a worse omission than a commented workflow job, and the workflow is also the easier paste.

Grading prose for meaning, not substrings, raises authoring cost. The current checker is stable and gameable. A hybrid keeps the banned phrase `triage is in scope` and the required ids, and adds a check that the failing slice name appears and that `clears its budget` is absent for any metric under the floor. Full natural-language grading is **Experimental** here and unnecessary.

## Recommendations

1. Keep `rel-m03-l04` after retrieval and the adapter. Spawn the measurement contract in Module 1 Lesson 2. Reuse it in Lesson 2's floor and in Lesson 5's remeasure.
2. Treat human gold plus deterministic metrics as the gate for keyed tasks. Rename `extraction_f1` to field accuracy. Say in the words page that harmonic-mean F1 is a different function, the one Inspect's token scorer implements.
3. Require the slice dashboard and the Wilson empty-slice rule inside `chk-eval`. A pool that clears 0.80 with a failing required slice fails.
4. Replace `mark` returning `pass`. Hide labels from the function. Grade disagreement on a hidden set. Set the agreement budget in the pack. Do not copy a figure from Zheng.
5. On the public `ab-status` counts, the decision is no call. Retire the assertion that `clause` won. Lock the OEC before the JSON is shown. Keep `contained` as the tempting peek.
6. Grade failure names on paraphrases and on a codebook aligned with Barnett's missing-content case and with this course's extra case, the wrong authority. Split the bundled Friday row before Lesson 5, or require the student to say which fault they would fix.
7. Keep the workshop, and require an OEC. The dot-vote remains a trap. It is not the value model, and that sentence alone is not the note.
8. Leave hosted LLM judges, ARES fine-tunes, live randomization, and clinician panels as reading. Label them **Emerging** or **Experimental** in the student page so a pass is not heard as production validation. Barnett's line, that RAG validation happens in operation, belongs in the finish chapter.
9. Stop calling `chk-eval` a draft once the report is checked against the grader's rates. Until then the draft label is accurate for the prose and misleading for the code.

## Deletions

- The solution identity of calibration and `item["pass"]`.
- Keyword classification as a sufficient reference solution, once paraphrases exist.
- The name F1 for the field-match rate.
- `experiment.md` ungraded, beside a unit test that names a winner.
- The trainer sentence that the experiment report names no winner, unless the code is changed to match it.
- A forecast pass condition that is exact equality with realized post-campaign visits, unless the page calls that a readout of the series.
- Constant-1.0 as the only broken score. Add the true pool that hides a slice.
- Any student-facing sentence that a language-model judge agrees with people "about 80% of the time" without Zheng's setup (MT-bench or Arena, non-tie or not, preference rather than clinical truth).
- Landis-and-Koch style kappa bands as a pass-fail rule. Artstein and Poesio are the teaching source: the coefficient has no universal cutoff.

## Additions that are not new lessons

A public disagreement matrix. A hidden paraphrase log. A hidden judge file. A slice gold file. An experiment hash step. A knowledge answer that mentions gold the judge does not read. A finish line that states offline pass is not a campaign-month guarantee.

## Lessons to spawn

**Measurement contract** inside Module 1 Lesson 2, not a new day. One table. Families without a metric are unfinished. Label **Proven**. This is the spine.

**This release, rebuilt** as the execution day. Not a new lesson id. The advanced chapter swaps with the foundation as file 04 describes.

**Do not spawn a live experimentation course** inside the health cluster. A frozen-log exercise covers peeking, OEC, overlap, and sample ratio. A patient A/B of access wording can be a Module 4 reading next to the SLO lesson, with Kohavi's "analyze at the end" and an explicit refusal to randomize triage or the campaign. Label the reading **Proven** and the live test **Experimental**.

**Do not spawn a labeling-vendor lesson.** Lesson 1's `ann-v2` agreement is the human-label home. This lesson adds the judge as another coder on a synthetic matrix. A third lesson on annotation operations would need raters the self-paced format does not have.

**Optional seminar page, not a release:** ARES and prediction-powered inference, for students who will later own an eval harness. No code, no GPU, no claim about the 59.3 and 14.4 point deltas beyond "the authors report these on their benchmarks, and they still use a human set."

## Labels in one list

| Idea | Label |
| --- | --- |
| Hidden human gold for keyed fields | Proven |
| Field accuracy, exact citation, journey conjunction | Proven |
| Slice dashboard with Wilson intervals, empty slice = (0, 1) | Proven |
| Pre-registered OEC, no peek, no call on overlap | Proven |
| Chance-corrected agreement on a provided matrix | Proven |
| Measurement contract in Module 1 Lesson 2 | Proven |
| RAGAS faithfulness as the gate | Emerging, and a bad fit for wrong-authority citations |
| Local judge calibrated on hidden gold | Emerging |
| ARES with a human validation set and PPI | Emerging |
| Inspect as a harness shape | Proven |
| Inspect model grading against a hosted API in this course | Experimental |
| Live patient experiment | Experimental, and out of scope |
| Uncalibrated LLM judge plus a dot-vote | Delete |
| Oracle `pass` field as the calibrated judge | Delete |

## Sources

Opened for this note. Figures in file 02 are quoted from these pages and scoped there.

Zheng et al. MT-bench and Chatbot Arena. https://arxiv.org/abs/2306.05685 and the HTML https://arxiv.org/html/2306.05685

RAGAS faithfulness. https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/  
Context precision and the list of metrics. https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/

Saad-Falcon et al. ARES. https://arxiv.org/abs/2311.09476 and https://aclanthology.org/2024.naacl-long.20/

UK AI Security Institute, Inspect. https://inspect.aisi.org.uk/  
Model grading. https://inspect.aisi.org.uk/model-graded.html  
Standard scorers, including token F1 as the harmonic mean. https://inspect.aisi.org.uk/standard-scorers.html  
Scoring overview. https://inspect.aisi.org.uk/scoring.html  
Log files, including the CJE calibration pointer. https://inspect.aisi.org.uk/eval-logs.html  
Software citation they publish: AI Security Institute, UK. Inspect AI: Framework for Large Language Model Evaluations. 2024. https://github.com/UKGovernmentBEIS/inspect_ai

Artstein and Poesio, Inter-Coder Agreement for Computational Linguistics. https://doi.org/10.1162/coli.07-034-r2

Hayes and Krippendorff, Answering the Call for a Standard Reliability Measure for Coding Data. https://www.asc.upenn.edu/sites/default/files/2021-03/Answering%20the%20Call%20for%20a%20Standard%20Reliability%20Measure%20for%20Coding%20Data.pdf

Kohavi, Tang, and Xu, Trustworthy Online Controlled Experiments. Cambridge University Press, 2020. https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59  
Chapter 1 excerpt (OEC, analyze at the end). https://experimentguide.com/wp-content/uploads/TrustworthyOnlineControlledExperiments_PracticalGuideToABTesting_Chapter1.pdf

Johari, Koomen, Pekelis, and Walsh, Peeking at A/B Tests. KDD 2017. https://dl.acm.org/doi/10.1145/3097983.3097992

Wilson score interval, including the 1927 attribution. https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval

Barnett et al. Seven failure points in RAG systems. https://arxiv.org/abs/2401.05856

Platform-orchestrated agent failures. https://arxiv.org/html/2509.23735v1

FMTAX, failure modes of LLM-agent services (kappa 0.70 is their coder-versus-anchor figure). https://lexuanbach.github.io/publication/ICSOC2026e.pdf

Hugging Face evaluation guidebook, model-as-a-judge tips, including the medical-domain caveat. https://github.com/huggingface/evaluation-guidebook/blob/main/contents/model-as-a-judge/tips-and-tricks.md

Course files this note is about, not external evidence: `course_design/module-03.md` Lesson 4, `course_design/slides/module-03-lesson-04.md`, `instructional/curriculum-understanding-map.md` Lesson 4, `Module 03/Lesson 04/Student_Copy` chapters 00–10, `Solution_Copy` work modules and pages, `problem_simulation/alwaha/check/eval_m03_l04.py`, `judge_m03_l04.py`, `notes_m03_l04.py`, and `problem_simulation/tests/test_m03_l04_checks.py`.

The z-test, Wilson bounds, and sample-size arithmetic on `honest_pending` are computed from the counts in the student chapter's picture of `ab-status.json` (48 and 40 over n of 80, and the contained counts 30 and 55). They are not in the papers above.
