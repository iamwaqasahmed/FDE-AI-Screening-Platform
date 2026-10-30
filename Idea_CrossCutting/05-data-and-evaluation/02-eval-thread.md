# The evaluation thread

Evaluation should be a longitudinal thread: every lesson appends a metric the reader can recompute. The two late lessons should stay, with a narrower job. They are the wrong place to introduce measurement.

## What the course already measures, and when the reader is told

The harness is already longitudinal. Module 1 scores approach family, person split, intake scenarios, tool traces, `timeout`, and `race-slot`. Module 2 scores the journey, seeded faults, and the deployment. Module 3 Lesson 1 scores cluster precision and recall, agreement with `ann-v2`, the fidelity card, train-on-synthetic test-on-real, and canaries. Lesson 2 scores extraction and intent F1 inside a cost and latency budget. Lesson 3 scores citation id, version, status, audience, and span. Lesson 4 is where the syllabus asks for a draft benchmark, the four planted names, an uncalibrated judge, and a pre-registered experiment. Lesson 5 remeasures one fix. Module 4 adds hidden attacks, disparity, SLOs, and the handoff.

A self-paced reader can pass the early checks as chores. Nothing in the morning chapter calls those checks a scorecard, so Lesson 4 arrives as a new subject. The four names then float free of the lessons that planted them. The one remeasured fix has no frozen baseline from the week the fault was introduced, so a gain on the draft benchmark can be a change in the test, the judge, or the campaign mix.

## One criterion, many slices

Kohavi, Tang, and Xu define an overall evaluation criterion as a quantitative measure of the experiment's objective: measurable during the experiment, and believed to drive the longer-term goal. They want one criterion, possibly a weighted combination, because a single number forces the tradeoff once. A pile of new headline metrics does not.

For this assistant the criterion is operational. Use the share of access requests that reach the correct terminal state inside the SLA: booked, queued for Ain's nightly file, held for a coordinator, or handed to the contact center with a summary. Emergency wording always redirects. Clinical urgency is not the criterion and is not a score the assistant optimizes.

Guardrails sit beside that number and can veto a launch: unauthorized or superseded citations, PHI in logs, a mother merged with a newborn, cluster precision below the published floor, disparity by district and insurance class, cost per conversation, and latency under the shared GPU quota. Module 4's CPU-only dashboard is the picture of a metric that cannot see the incident. The longitudinal thread should make that failure familiar before the incident week.

Each lesson adds a slice row, not a new overall criterion. A slice has a unit (person, referral, clause, conversation), a gold source, a budget, the failure type it can see, and the failure type it cannot see. `chk-eval` already requires the report to name a planted example of each type. The scorecard is how the reader knows which earlier check planted it.

Suggested rows, using checks the course already has:

| When | Slice row | Type it can see | Type it cannot see |
| --- | --- | --- | --- |
| Module 1, approach | Gap between row-split and person-split scores | Workflow, once identity is wrong | Whether the cited clause is in force |
| Module 1, intake and agent | SLA calendar, idempotency, `timeout`, `race-slot`, emergency redirect | Workflow | Hallucination in a fluent status sentence |
| Module 2, feeds | Mart wait versus the booking system, at the mart's as-of | Reasoning on a stale count | Channel template legality |
| Module 3, Lesson 1 | Cluster precision and recall; `ann-v2` agreement; fidelity card; canary absence; synthetic-to-real gap | Workflow from a bad person id; label drift | Retrieval |
| Module 3, Lesson 2 | Intent and extraction F1, SAR, latency, against the prompt baseline | A share of reasoning and workflow | Hours answers, which stayed on retrieval |
| Module 3, Lesson 3 | Exact citation: id, version, status, audience, span, language | Retrieval | A fluent sentence that cites the right span and adds a claim |
| Module 3, Lessons 4–5 | The four names with evidence; judge agreement on the calibration set; one remeasure; the other three do not regress | The residual the slices missed | A live show-rate under the campaign |
| Module 4 | Hidden attacks, deletion across stores, disparity, SLO, cache drop on `document.changed`, handoff summary | Workflow and retrieval after release | Anything the team retuned the judge to ignore |

## Why reference-free RAG scores are the wrong headline

Es, James, Espinosa-Anke, and Schockaert (RAGAS) define faithfulness as the share of claims in the answer that an LLM says are supported by the retrieved context. The current docs use the same ratio. Context precision without a reference asks an LLM whether each chunk is relevant to the generated response. The paper itself reports that context relevance was the hardest of their three dimensions, and that ChatGPT often failed to pick the crucial sentences, especially in longer contexts.

Roychowdhury and colleagues, in a telecom QA study, found faithfulness broadly concordant with experts and still sensitive to how statements are split, context relevance dependent on context length and hard to interpret, and answer relevance tied to cosine similarity in a way that is a poor absolute score. They also note that RAGAS does not show how the number was derived.

Those metrics answer a different question from `chk-m03-l03-rag`. A sentence can be faithful to `circ-ramadan-unauth`, or to a superseded hours circular, or to the English staff leaflet. Context precision without a reference rewards chunks that match the answer the model just wrote, including a wrong answer. The course already has gold: document id, version, status, audience, and span, plus unanswerable and conflicting pairs in `ds-retrieve`. That exact check is the retrieval metric. Use a claim-level faithfulness score only on the residual, and only after the citation check has passed, so "supported by the retrieved text" is not mistaken for "supported by the in-force clause."

## The judge is a calibrated instrument, or it is not a gate

Zheng and colleagues show that a strong LLM judge can agree with humans at roughly the same rate humans agree with each other: on MT-Bench, GPT-4 versus humans reached about 85% agreement on non-tie votes, against about 81% among humans. They also show the failure modes that make an uncalibrated judge a trap. On similar answers, GPT-4's position-swap consistency was 65%. A repetitive-list verbosity attack fooled GPT-4 on 8.7% of a 23-item set and fooled Claude-v1 and GPT-3.5 on 91.3%. GPT-4's win rate for itself sat about 10 points above the human win rate; the paper does not treat that gap as proof of self-enhancement. Agreement was higher when the two models were far apart, which is the opposite of the pairs a team argues about. On math, a reference-free judge often repeated the candidate's mistake; a reference-guided prompt cut that failure sharply.

Liu and colleagues separate that kind of agreement from calibration. An off-the-shelf judge given only a score range is weakly aligned; AutoCalibrate drafts, filters, and revises scoring criteria against a human label set and raises correlation with experts. The course already has the right object: `slice-judge` fails an uncalibrated model judge and passes a judge checked on the calibration set, and `eval/judge_calibration.jsonl` is the facilitator set, with a student subset on `rel-m03-l04`.

Teach the check in this order. Score the calibration set before the judge is allowed to gate anything. Swap answer order when the judge compares two replies. Prefer the registered local model as judge when the candidate text came from that same model, and publish the disagreement with a second judge. Where a clause id or a workflow state exists, the gold wins and the judge does not vote. Use the judge for the residual rubric (caregiver comprehension, tone, whether a refusal names the constraint). Report agreement on the calibration set beside the benchmark. A higher benchmark score from a judge that was not rechecked is not the Lesson 5 improvement.

## Offline harness, then one pre-registered online comparison

This program cannot randomize clinical care, and a self-paced lab has no live patients. The offline harness is the real evaluation: planted failures, held-out people, point-in-time gold, and budgets in tokens, seconds, and SAR. Kohavi's criterion still applies inside that harness. The overall number has to be computable on each release and tied to access outcomes, not to a proxy the team can inflate.

Gruson and colleagues, comparing playlist rankers, state the limit of that harness. Offline scores from ordinary logs are biased by the interface and by the policy that chose what users saw. Online tests answer the causal question and cost more, in time and in user harm. A carefully debiased offline estimate can rank candidates for the online test; it does not replace it. The course's campaign forecast is the same warning: yesterday's status traffic is the wrong mix for a campaign week, and the Lesson 4 trap is a forecast that ignores the campaign.

So the longitudinal thread is offline slices. The capstone adds exactly one online-shaped experiment, the pre-registered `ab-status` comparison, on a non-clinical status reply. The randomization unit is the person, held constant for the experiment. The criterion is the access outcome above, with the guardrails as vetoes. Shadow traffic must not change the patient reply. Show-rate, reminder response, and handoff completeness are the quantities the offline suite does not identify. They wait for a real pilot under the stage gate. They are not estimated by an LLM judge.

## What the two late lessons keep

Lesson 4 is the naming lesson and the honesty lesson. The reader points at one planted example of each failure type, shows which slice row caught it, and shows one that the slice row missed. They run the judge on the calibration set and record that an uncalibrated judge is not a result. They pre-register `ab-status`, including the campaign in the forecast, before looking at a second run.

Lesson 5 changes one thing and remeasures. The chosen failure moves. The other three types, the cost cap, and the latency budget do not get worse. The requirements file states the overall criterion, the guardrails, and the non-goals, including triage. A requirement that copies the sponsor sentence fails the check the course already has.

That is the argument. Every lesson adds a slice row so a self-paced reader can see what broke. Two late lessons remain so the reader cannot launder a new judge, a new test mix, or a new overall number into a claimed improvement.
