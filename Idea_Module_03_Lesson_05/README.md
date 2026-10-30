# Module 03 Lesson 05 — research index

Independent curriculum research for **One fix and the requirements** (`rel-m03-l05`). This folder does not change course files. It evaluates the lesson that exists, compares it with requirements and production-ML practice, and proposes a self-paced redesign a later author could implement.

Labels used in every file:

| Label | Meaning here |
| --- | --- |
| Proven | A published standard, a government method, or a behavior this course already grades |
| Emerging | A reputable practice that fits this case and is not yet the lesson's artifact |
| Experimental | A course design that should be piloted on one self-paced run before it replaces chapters |

The case is fiction (Al-Waha, the stage-gate ids, the sponsor sentence). Citations below are about methods. They are not claims that the case's law is real.

## Recommendation

Split this lesson into two. Keep one remeasured retrieval change as the first lesson. Move authorship of `rcp/requirements.md` into the second. One measured fix is the right size for a lab and the wrong size for teaching improvement. A requirements page that a student pastes from chapter 09 is the wrong size for teaching a brief a stranger could build from.

**Lesson 5a — One measured change.** The student still replaces repair, remeasure, and cost. They pre-register which failure they will move (`log-circular`), score the public slice before and after, price the move in `cost.label`, and stop if the product exceeds the annotation budget. The other three planted failures stay open on purpose. The written product is a decision record: hypothesis, result, residual failures, stop rule. It is not a client specification.

**Lesson 5b — A brief a stranger can start from.** The student writes `rcp/requirements.md` without a finished paste. The artifact is an outcome-traced slice of a stakeholder specification: a problem statement that refuses the sponsor sentence, a small set of verifiable requirements, an assumption log, non-functional budgets, an exclusion register, and a trace from business outcome to test id and stage gate. Module 4 Lesson 5 already depends on this file. Lesson 5b stays before `rel-m04-l01`.

If the program cannot add a lesson, do not keep both jobs in the current paste day. Delete the personal-lab chapter and the finished-page paste, and spend the recovered time on 5b's writing task inside the same release. That fallback still fails to teach an improvement loop. The preferred design is the split.

The requirements artifact to adopt is a hybrid, not a new brand name:

1. A USDS-style problem statement on the first page (people, job, consequence, no solution).
2. A one-page opportunity solution tree that shows why triage is an executive solution and not the outcome.
3. A short ISO/IEC/IEEE 29148-shaped requirement set for the one in-scope outcome, with assumption attributes, budgets, and a trace matrix.

Three alternatives are compared in `03-redesign-architecture-and-simulation.md`. The hybrid is the one a stranger can implement. The tree alone is a discovery picture. Stories alone copy the sponsor.

## What to delete

- The chapter 09 paste of a finished `rcp/requirements.md`, `benchmark.md`, `improvement.md`, `readout.md`, and `retro.md` as the student's writing.
- The instruction that the evidence line already says the second run moved 1 citation and that the student must leave that count.
- Grading the phrase `not the value model` as the proof that priorities are independent of the dot-vote.
- The personal citation lab as a second audience exercise inside the requirements week. Audience and version already belong to Lesson 3. The floors in `personal.jsonl` belong in the spec's budget table, not in a sixth pasted module.
- The workflow job that only reruns `tests.test_remeasure` and is presented as an improvement gate. A unit rerun is a regression check. It is not a stage gate and it is not an ML production score.
- The facilitator-only three-minute disagreement between `dpo` and `cdo` as the only place the conflict is real. A self-paced learner has no facilitator. The conflict has to be in the packet.

## What to keep

- One retrieval failure moved, three named and left open.
- `p-triage` and `vendor-bot` as exclusions. A clinician holds urgency.
- Patient data stays off `ext-large`.
- Label spend that is refused when it exceeds the annotation budget, rather than a clipped total.
- `req-cite` mapped to `dms`, sitting on G1, while G2 (the DPIA) stays open.
- Sprint order: change, then second measurement, then specification.
- Labels staying on the grading service. The public slice has no label field.

## How the six files divide the work

| File | Question it answers |
| --- | --- |
| `01-existing-lesson-evaluation.md` | What `rel-m03-l05` actually teaches, what the four checks reward, and where the paste defeats the trap |
| `02-industry-research.md` | What 29148, NASA, FAA/ARP4754A, Torres, the ML Test Score, USDS, and Palantir's opened careers page say that this lesson needs |
| `03-redesign-architecture-and-simulation.md` | The two-lesson split, three requirements artifacts, the simulation, datasets, and failure cases |
| `04-exercises-assessment-instruction.md` | Self-paced exercises, checks, solution shape, and prerequisites |
| `05-tradeoffs-recommendations-sources.md` | Tradeoffs, deletions, lessons to spawn or refuse, and the source list |

## One-page recommendation for an author who will not read further

The current morning is honest about scope and dishonest about authorship. A learner can finish every check without deciding anything the chapter has not already decided. Chapter 06 explains the repair, then the student pastes it. Chapter 09 contains the brief that `chk-m03-l05-rcp` accepts, then the student pastes it. The trap — requirements that copy "The virtual front desk, including triage, goes live before Ramadan" — is implemented as a banned-phrase scan of the Scope section. A learner who pastes the chapter cannot fail that trap, and a learner who paraphrases the CDO card ("one front door, live before Ramadan") can pass it.

The public fixture makes the pasted number true: five citation predictions, four already on `circ-ramadan` with span `hours-c1`, one on `circ-ramadan-unauth` with the same span. `moved()` counts document mismatches, so the evidence count is 1. Accuracy before is 4/5 and after is 5/5, because a hit in `remeasure` requires document and span. On this fixture those two facts move together. The chapter tells the student not to compute the count. That is the opposite of a second measurement.

A stranger given the finished `rcp/requirements.md` still cannot build the system. The objective is a sentence about hours. Scope names `req-cite` and `ext-large` in one paragraph. Gates say G1 is the risk tier and do not say what evidence closes G1 or why G2 stays open. There is no acceptance test, no latency budget, no cost figure, no assumption that could be wrong, and no link from "a patient can ask for hours" to `tests.test_remeasure` or to the personal floors (0.8). ISO/IEC/IEEE 29148:2018 says a requirement is verifiable when it is measurable, and that initial stakeholder concerns are not yet requirements. The CDO card is a stakeholder concern. The pasted brief is a concern with headings.

Improvement, as this course's syllabus names it, is iterative evaluation. The lesson ships one string substitution and stops. That stop is a good engineering decision if it is argued: the other failures are different mechanisms, the label budget is the constraint, and a second change would be a different experiment. The lesson does not ask for that argument. It asks for `cost.label` to appear beside the word retrieval.

Teach the stop in 5a. Teach the contract in 5b. Grade 5b by whether another person could write the test from the requirement id, the condition, and the verification method, without opening the chapter paste.

## Decision rules for the review

Adopt the split if both of these stay true: Module 4 Lesson 1 still receives a named G1 and an open G2, and Module 4 Lesson 5 still receives `rcp/requirements.md` produced in 5b. Reject any redesign that pastes the gold brief into the student chapter, that grades the sentence "not the value model" as a substitute for the value note, or that treats one unittest rerun as iterative optimization. The three artifact options are a traced shall-set, a Torres tree, and acceptance-tested stories. Only the shall-set, with the tree in front and tests as attributes, is the contract a stranger can build. The pilot in `04` — one author implements from the reference brief alone, one author fails three sponsor paraphrases, one author hits the budget veto — is the release gate for replacing chapters.

## Reading order for a curriculum editor

1. This page.
2. `01` if the question is "is the current lesson already doing this?"
3. `02` if the question is "which external practice, exactly?"
4. `03` if the question is "what do we build instead?"
5. `04` if the question is "what does the learner do on Monday, alone?"
6. `05` if the question is "what do we cut, and what must not become a third lesson?"
