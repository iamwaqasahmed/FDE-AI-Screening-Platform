# 02 — Industry research

Sources below were opened. Figures are the authors' or the pages' figures, scoped to the experiment they describe. None of them is a license to skip a gold set on Al-Waha citations. The agreement arithmetic on `ab-status` at the end of the Kohavi section is computed from counts printed in the student chapter. It is not a statistic from these papers.

## Zheng et al., MT-bench and Chatbot Arena

Lianmin Zheng and colleagues, "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," arXiv:2306.05685. The HTML of the paper was opened. They introduce MT-bench, 80 multi-turn questions, ten in each of eight categories (writing, roleplay, extraction, reasoning, math, coding, STEM knowledge, humanities and social science), and Chatbot Arena, a crowdsourced blind vote. The abstract says strong judges such as GPT-4 can match controlled and crowdsourced human preferences well, "achieving over 80% agreement, the same level of agreement between humans."

The body is more specific, and the setup changes the number. They define agreement as the probability that randomly selected judges of two types agree on a randomly selected question. On MT-bench, setup S2 keeps non-tie votes only. In that setup they report GPT-4 versus human agreement of 85%, and human-versus-human agreement of 81%. Setup S1 also counts ties and treats position-inconsistent votes as ties. A breakdown on non-tied votes shows GPT-4–human agreement rising with the performance gap between the two models, from 70% to nearly 100%. Close calls, which are the decisions a product team argues about, sit at the weak end of that range. When a human disagreed with GPT-4, the authors showed the model judgment back and report that humans called it reasonable in 75% of those cases and were willing to change their own choice in 34%. That second number is not agreement. It is persuasiveness.

Limitations they measure, which this lesson's fluent-wrong demo already points at:

Position bias. On pairs of similar answers, swapping order, the default prompt gave GPT-4 consistent decisions in 65.0% of cases, biased toward the first position in 30.0%, toward the second in 5.0%, format errors 0. Their same table shows Claude-v1 consistent in 23.8% and biased toward the first position in 75.0%. Few-shot examples raised GPT-4 consistency from 65.0% to 77.5%. The authors write that high consistency may not imply high accuracy, and that the examples may add new biases. Their mitigation for grading is to judge both orders and declare a win only if the same side wins both, otherwise a tie.

Verbosity bias. They build a repetitive-list attack: a numbered answer is lengthened by a rephrased copy of the same items and no new information. A judge fails if it prefers the longer copy. They say every model they tried can be moved this way, and that GPT-4 resists better. Identical answers were correctly tied. The attack is the lab analogue of `cal-fluent-wrong`: a settled tone is not a correct citation.

Self-enhancement. They report a 10% higher win rate for GPT-4 grading itself and 25% for Claude-v1 grading itself, relative to humans, and then say the study cannot determine whether self-enhancement bias exists, because they cannot restyle an answer into another model's voice without changing quality. Teach the attempt. Do not teach "judges prefer themselves by 10%" as a settled constant.

Math and reasoning. A judge can mark a wrong solution correct even when, asked separately, the same model can solve the item. The authors say the judge is misled by the answer in context. Chain-of-thought still copies the candidate's mistake. A reference-guided prompt, which shows an independently produced reference, cut the failure rate on their 10-question math probe from 70% to 15%. That pair of percentages is their probe, not a general property of judges. It is the result that matters for this course: the clinic has a reference (the in-force document and the span). A fluency grade ignores it. A reference-guided grade uses it. Reading the `pass` column uses the grade itself and teaches neither.

What not to carry into Al-Waha. MT-bench measures preference on open chat, with graduate-student raters, on English general-purpose questions. It does not measure whether a citation is the in-force circular a patient is allowed to see. Agreement is higher when one answer is obviously better. Hallucinated clinic hours in a fluent sentence are the opposite case: the prose is the attack. The Hugging Face evaluation guidebook, opened at the model-as-a-judge tips page, states the domain caveat in one line: for medical, legal, or mathematical tasks, non-expert human raters can be as weak a baseline as an uncalibrated model. The course's data-protection and clinical seats exist because of that fact. A self-paced lab still should not pretend a language-model preference score is a clinical gold set.

## RAGAS

Official metric pages were opened. Faithfulness, on the RAGAS docs, is the share of claims in the response that can be inferred from the retrieved context. The docs' example splits "Einstein was born in Germany on 20th March 1879" into two claims against a context that says 14 March 1879 and scores 1/2. The metric is a claim check against whatever was retrieved. It does not know audience, version, or "in force."

If `log-circular` retrieved the unauthorized Ramadan circular and quoted it accurately, faithfulness to that context is high. The course's retrieval failure is exactly that case: the text is supported by a document the asker may not use. Context precision, as documented, scores whether relevant chunks are ranked above irrelevant ones, either against a reference answer or, in the no-reference variant, against the generated response. Judging chunks by the response circularly rewards a retrieval that matches a bad answer. Answer relevancy embeds the user question and questions reverse-engineered from the answer. The docs say it does not evaluate factual accuracy. A fluent wrong citation of night hours can be relevant to "when is the eye clinic open."

So a RAGAS dashboard can go green on the four planted rows for different reasons: the night-hours clause is unfaithful only if it is absent from the context; the unauthorized circular can be faithful; the Friday offer is not a retrieval claim; the missing approval is not a generation claim. RAGAS is **Emerging** as a slice of generation quality and a poor primary metric for this case. The deterministic checks the lesson already has (doc id, span, state, approval) are the ones that match the keys.

The docs also note a non-LLM context precision that uses string similarity, and an id-based precision when both sides have document ids. Id-based precision is the **Proven** cousin of `citation_accuracy`, and it is what Lesson 3's citation log can support without a judge.

## ARES

Jon Saad-Falcon, Omar Khattab, Christopher Potts, and Matei Zaharia, "ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems," arXiv:2311.09476, also NAACL 2024. The HTML was opened. ARES scores context relevance, answer faithfulness, and answer relevance. It generates synthetic questions from the corpus, fine-tunes lightweight judges, and then uses prediction-powered inference (Angelopoulos et al., 2023, as cited by ARES) on a human validation set. The paper says this set is about 150 annotated points or more, and the abstract says the method uses only a few hundred human annotations across the evaluation. The authors report beating RAGAS by 59.3 percentage points on context relevance and 14.4 on answer relevance, averaged on their KILT and SuperGLUE setups. Those deltas are their comparison, on their tasks. They are not a number to quote as "RAGAS is 59 points worse" in a clinic.

The part to teach is the shape. A judge is a model with an error rate. A small human set estimates that error and corrects the score on a larger unlabeled set, and the result is an interval. ARES without the human set is another uncalibrated judge. The course already has the seed of this design: labels on the grading service, a calibration subset in the pack. The subset has three rows and includes the label. Three rows cannot estimate a judge's error. Using the label as the judge's output sets the error to zero by construction.

ARES is **Emerging**. It is the wrong required build for a self-paced student with no GPU quota left from Lesson 2 and no labeling vendor. It is the right picture of why `slice-judge` should compare a checker to hidden labels and report disagreement, rather than return the label.

## UK AISI Inspect

Inspect is the UK AI Security Institute's open-source evaluation framework. The docs at https://inspect.aisi.org.uk/ were opened, including scoring, standard scorers, and model grading. A task is a dataset of labeled samples, a solver, and a scorer. Standard scorers include exact match, pattern, includes, a token-overlap `f1` defined as the harmonic mean of precision and recall, and `model_graded_qa` / `model_graded_fact` for open answers. The built-in `f1` is the quantity this lesson's words page correctly says `extraction_f1` is not. Rename the course function. Leave harmonic-mean F1 for a later extractive-QA slice if one is ever added.

Model grading is documented as a separate instrument. The default grader may run at the provider's default temperature, which the page says is often non-zero, so borderline grades move between epochs. The documented controls are temperature 0, a seed where the provider allows it, and multiple epochs to see residual variance. Temperature 0 does not remove disagreement. A panel of graders uses a majority reducer; a grade that more than half the panel does not share leaves the sample unscored rather than picking a side by list order. Grade extraction uses the last `GRADE:` line so a submission cannot inject an earlier grade. Dataset text is fenced so the model under test cannot close the data block and write its own instructions. The scoring-policy page says an unparsable verdict is `Score.unscored(reason="grader_failed")` with no automatic retry. The log-files page points at CJE, a tool to calibrate model-graded scores against oracle labels.

That is the teaching contrast with `judge.py`. Inspect treats the grader as a measurement instrument with a failure mode, a variance, and a path back to oracle labels. The course treats the oracle label as the instrument. For rows with a key (doc id, span, approved), Inspect's own guidance is to use exact or pattern scorers. Model grading is for open answers and for facts buried in a narrative. `log-night` is the second kind. `log-approval` is a state key and should never go to a judge.

Inspect is **Proven** as a harness shape (dataset, solver, scorer, log). Requiring students to run Inspect against a hosted model is **Experimental** in this course: it needs an API key, and the residency ruling in Lesson 2 closed external models for PHI. The lab can copy the shape in local Python without the dependency.

## Agreement: Cohen and Krippendorff

Two opened teaching sources, not a new labeling study.

Artstein and Poesio, "Inter-Coder Agreement for Computational Linguistics," Computational Linguistics 34(4), 2008, DOI 10.1162/coli.07-034-r2. Chance-corrected agreement has the form (observed agreement minus expected agreement) divided by (1 minus expected agreement). Cohen's kappa (Cohen 1960, as they cite) is the two-rater case. Expected agreement uses each rater's own marginals, so two raters who both mark almost everything "pass" can agree often and still show a low kappa, because chance already predicted the agreement. The zero point is chance, not "no overlap." Values can be negative when agreement is worse than chance. The survey argues that weighted, alpha-like coefficients fit many annotation tasks better than unweighted kappa, and that the number is harder to interpret once disagreements have degrees. Do not teach a cutoff band (the familiar 0.6 or 0.8 rules of thumb) as a pass mark. The paper's point is that the coefficient does not carry a universal interpretation.

Andrew F. Hayes and Klaus Krippendorff, "Answering the Call for a Standard Reliability Measure for Coding Data" (the University of Pennsylvania PDF of that paper was opened). They argue for Krippendorff's alpha because it allows any number of observers, missing ratings, and different levels of measurement. Alpha is 1 minus observed disagreement over expected disagreement. Perfect agreement is 1. Chance is 0. Raters must code independently, on units drawn as a sample of the universe whose reliability is at issue, under shared instructions.

Teaching depth that fits one sitting, **Proven** as arithmetic on a provided matrix:

- Percent agreement hides a skewed label. If both raters say "pass" on 95 of 100 rows, raw agreement looks excellent and kappa does not.
- Cohen's kappa needs exactly two raters and a complete table. Use it for "fluent heuristic versus gold" on the calibration slice, which is two coders.
- Krippendorff's alpha is the one to name when a third rater is missing some rows, or when hallucination versus retrieval is an ordinal severity rather than a flat nominal set. The formula does not need to be derived. The empty-cell rule does: missingness is allowed, and inventing a label for a blank is a different analysis.
- The coefficient is undefined or unstable on a tiny table. Three calibration rows cannot support either statistic. Say so, then give a matrix large enough to compute.

Module 3 Lesson 1 already has an agreement check against `ann-v2`. This lesson should reuse that idea for judges. A language-model judge is another coder. Its agreement with gold is the calibration. The gold is not the judge's source code.

No judge-agreement rate is stated here beyond the Zheng figures above, which are preference agreement on MT-bench and Arena under the setups named. Do not import them as the expected kappa for a citation judge.

## Pre-registration, peeking, and the fixture

Ron Kohavi, Diane Tang, and Ya Xu, *Trustworthy Online Controlled Experiments*, Cambridge University Press, 2020. The Cambridge catalog page and the publisher's chapter 1 excerpt on experimentguide.com were opened. The overall evaluation criterion (OEC) is a quantitative measure of the experiment's objective. It has to be measurable during the experiment and believed to drive the longer-term goal. The excerpt says revenue alone is a bad OEC because it can be raised by plastering a site with ads. Bing's example weighs revenue against usage. The chapter's figure caption says to analyze at the end of the experiment. The catalog page lists Twyman's law and carryover among the pitfalls: a result that looks surprisingly large is often a bug in the measurement.

Ramesh Johari, Pete Koomen, Leonid Pekelis, and David Walsh, "Peeking at A/B Tests," KDD 2017, DOI 10.1145/3097983.3097992. The abstract was opened. Optional stopping, watching a p-value until it crosses a line, makes ordinary p-values and confidence intervals unreliable. Their contribution is always-valid inference so that continuous monitoring has a defined error rate. The course does not need always-valid p-values. It needs the disease: a second metric, read after the first disappoints, is a peek.

Map that onto `ab-status` without adding a patient experiment. The notice names `honest_pending` before the counts. The shell then optimizes `contained`, which moves the other way and by a larger gap (30/80 versus 55/80). That gap is the Twyman-shaped warning: the easy metric jumped, the pre-registered metric did not agree, and a workshop will want to ship `short` because the dashboard looks decisive. `honest_pending` is the closer OEC if the harm is a status line that implies the referral is finished. `contained` is a vanity metric. The dot-vote is not an OEC at all. Kohavi's tenet is that the organization is bad at judging the value of ideas. The seats file is that tenet in costume.

Worked numbers from the printed fixture only. `clause` 48/80 = 0.60, `short` 40/80 = 0.50, pooled proportion 0.55, standard error sqrt(0.55 × 0.45 × (1/80 + 1/80)) ≈ 0.0787, z ≈ 1.27, two-sided normal p-value ≈ 0.20. Wilson intervals with z = 1.96, the same center-and-margin form as `intervals.py`, are about 0.49 to 0.70 for `clause` and about 0.39 to 0.61 for `short`. They overlap. A rough equal-n sample-size formula, n = (1.96 + 0.84)² × (0.60×0.40 + 0.50×0.50) / (0.10)², is about 380 per arm to detect a 10-point gap near these rates at 80% power and a two-sided 5% level. The fixture has 80. Shipping a winner is **Experimental** in the bad sense. Teaching that the study is too small is **Proven** and fully assessable on a calculator.

The Wilson score interval itself is E. B. Wilson, 1927, as summarized on the binomial-proportion page of Wikipedia (opened). It stays inside 0 and 1 and does not collapse to a point at 0 or 1 the way a naive normal interval does. The course formula matches that interval. The empty-total rule `(0, 1)` is a local convention meaning "no evidence," and it is the right one to keep. A point mass at 1, which is the shell, is a claim of certainty.

Pre-registration in a self-paced lab is a file written before the count file is readable: metric name, slice, direction of improvement, and the rule for overlap ("no winner"). The current pack shows the notice and the JSON in the same chapter, and the unit test states the winner. The procedure is announced. The peek is still available.

## Error taxonomies that were opened

Scott Barnett, Stefanus Kurniawan, Srikanth Thudumu, Zach Brannelly, and Mohamed Abdelrazek, "Seven Failure Points When Engineering a Retrieval Augmented Generation System," arXiv:2401.05856, an experience report from research, education, and biomedical case studies. The HTML was opened. Their two takeaways: validation of a RAG system is only feasible in operation, and robustness evolves rather than being designed in at the start. The seven points:

1. Missing content. The question cannot be answered from the documents. The honest behavior is to say so. Related questions get a fluent invention. That is `log-night`.
2. Missed the top-ranked documents. The answer is in the corpus and outside the top k.
3. Not in context. Retrieved, then dropped by the consolidation step before generation.
4. Not extracted. Present in the context, lost in noise or contradiction.
5. Wrong format.
6. Incorrect specificity.
7. Incomplete. Not false, and still missing a part that was in the context.

The course's single word "retrieval" covers Barnett's points 2 and 3 and also a failure Barnett's list does not have: the document was retrieved, extracted, and cited, and it is the wrong authority (unauthorized circular, staff leaflet to a patient, superseded criteria). Lesson 3 already separated audience, version, and in-force status. Collapsing those into one keyword throws away the diagnosis Lesson 5 would need. Point 1 is the hallucination row. Points 4 through 7 are not in the four-name syllabus. A Friday booking and a missing approval are outside this paper because they are not retrieval failures.

Agent writeups that were opened, all preprints or a proceedings PDF, and all more specific than a four-word list:

"Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems," arXiv:2509.23735. The authors annotate 307 failure logs into agent-level, workflow-level, and platform-level causes. They report that automatic root-cause identification, even with the taxonomy in the prompt, reaches at most 33.6% accuracy on their benchmark. Use that as their ceiling, not as a universal agent-debug rate. It supports a modest claim: naming a failure from a trace is hard enough that a keyword list will look better than it is. `log-approval` is their workflow class (a missing check). `log-friday` is closer to an agent knowledge failure (the calendar rule). `log-circular` is a policy filter on a tool result, which their platform-versus-agent split only partly captures.

"A Failure-Mode Taxonomy for LLM-Agent Services" (FMTAX), the ICSOC PDF that was opened. The authors code GitHub issues from LangChain, LlamaIndex, MCP, and CrewAI. They report kappa of 0.70 between rule coders and a human-coded anchor. That kappa is inter-coder agreement on issue labels, not an LLM-as-judge preference rate. They report that 66–82% of the agent-specific failures they marked sit at service boundaries: tool arguments, provider errors, tool servers. The course's agent already has a tool boundary and an approval hold. A workflow failure that is only the sentence "Approval: none" does not teach a boundary. A trajectory check that the booking tool was called without the approval tool does.

A third preprint, "Compound AI System Reliability," arXiv:2610.02503, was opened. It groups incidents into retrieval, generation, tool, orchestration, and integration. The effectiveness percentages in that preprint are the authors' fault-injection claims. They are not used here as curriculum facts. The category list is enough to show that "hallucination, retrieval, reasoning, workflow" is a syllabus compression, not a production codebook.

Barnett's operational takeaway cuts against a purely offline lab. The course can still assess the offline half: given a frozen log, name the point in the pipeline. It cannot assess production drift. Say that in the lesson so a green `chk-eval` is not heard as "the assistant is ready for Ramadan."

## What a self-paced student can be graded on

No labeling vendor, no clinician panel, no live traffic.

Assessable now, because the grader holds keys or the student can compute from printed inputs: field accuracy, citation exact match, journey state, a paraphrase set of the four failures, Wilson bounds including the empty slice, a power worksheet on the printed `n`, a kappa on a matrix the pack provides, a pre-registration file scored before counts are revealed, a slice table that fails if any required slice misses its budget, a value note that refuses triage and states an OEC.

Not assessable as a solo performance: recruiting annotators, a real Cohen study among humans, an ARES fine-tune, a patient A/B, a claim that a hosted judge "matches humans at 80%." The 80% sentence belongs to Zheng's preference study under the setups above.

Simulable: two scripted raters with a disagreement file; a frozen `ab-status` log; the campaign series already in `ophth.csv`; a judge trace that is fluent and wrong, scored against a hidden `pass` the function cannot see.
