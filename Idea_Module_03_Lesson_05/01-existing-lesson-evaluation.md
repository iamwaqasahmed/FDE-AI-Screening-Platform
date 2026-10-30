# Existing lesson evaluation — Module 03 Lesson 05

Release `rel-m03-l05`. Case date in the rehearsal notice: 2027-01-28. Student path: `Module 03/Lesson 05/Student_Copy`, chapters 00 through 10. Solution path mirrors that work with finished files. This evaluation reads those chapters, the slides, `course_design/module-03.md`, the curriculum map entry, the four checkers, and the gold builder. It does not treat the solution paste as evidence that a learner can write.

## What the lesson claims

The design note and the curriculum map agree on the purpose: one remeasured improvement, and `rcp/requirements.md` a later team could start from. Concepts named: iteration, non-goals, stage gates, scope that is not the sponsor sentence. Trap: requirements that copy the sponsor sentence, including triage. Checks: `chk-eval`, `chk-m03-l05-rcp`, `chk-readout`, `chk-individual-m03-l05`.

The syllabus line in `module-03.md` is wider than the lab: improve performance through iterative evaluation, testing, and optimization; run a client discovery workshop; decompose problems into requirements, scope, and priorities. The lab narrows that to one fix, one remeasure, one pasted spec, and a readout. The narrowing is the right instinct. The implementation then removes the decisions the narrowing was supposed to teach.

Roles in the design note: Product owns the spec, AI owns the remeasure, Arch maps requirements to systems, App names non-goals, Lead presents. The student background says one person holds all five parts. That self-paced rule is already correct. The chapters do not give that one person a workshop to run. They give them files to open and blocks to paste.

## What the learner actually does

Chapters 00 through 04 are reading and one demo. The demo, by the journey note, prints two lines and does not print a non-goal or a price. Chapter 03 sends the learner through the rehearsal notice, `steer-m03-l05`, the role cards, the stage-gate file, the price sheet, the annotation budget, the citation slice, the personal slice, and the backlog seed.

The CDO card is the sponsor sentence, in Layla Al-Harbi's voice: "The virtual front desk, including triage, goes live before Ramadan." A second line asks for one front door, live before Ramadan. Access wants shorter waits. The PHC lead wants fewer returned referrals. The DPO wants patient data and training data in the private cloud. Steering's five questions ask what the second run changed, what is in and out of the requirements, which gate and which risk tier, what the improvement costs, and what will not be copied from the sponsor sentence.

Chapter 05 sequences the sprint: fix, then second measurement, then spec. Chapter 06 replaces three modules:

- `repair` rewrites `doc_id` from `circ-ramadan-unauth` to `circ-ramadan` and copies every other field, including span.
- `remeasure` scores accuracy before that rewrite and after it. A hit is the same document id and the same span. The label stays the grader's label.
- `spend` multiplies a label count by a price and returns nothing when the product exceeds the budget. The price is the `sar` on `cost.label`, not the `price` key in `labels.json`.

Chapter 07 replaces `backlog.kept` so `p-triage` and `vendor-bot` drop and any other id is kept; `gates.gate_for` so only `req-cite` returns `G1` and every other id returns an empty string; and the workflow so `improvement-gate` is uncommented and runs `python -m unittest tests.test_remeasure`.

Chapter 08 replaces `personal.cite` and `personal.meets_budget`. A patient asking for a staff-audience document gets nothing. A kept citation carries audience, document id, and version. A value clears a floor when `value + 1e-9 >= floor`. The suite is eleven tests and does not read the pages.

Chapter 09 replaces five markdown files with blocks printed in the chapter. The requirements block is the brief the solution also holds: an objective about hours, scope `req-cite` plus `ext-large`, priorities that mention the dot-vote and then the sentence "That ranking is not the value model," non-goals naming `p-triage`, `vendor-bot`, and a clinician who owns urgency, systems mapping `req-cite` to `dms`, gates putting `req-cite` at G1, and evidence that names `dpo`, says the second run moved 1 citation, and lists four workshop seats. The chapter says to leave that count and not replace it with a number the learner computed.

Chapter 10 runs the four checks. Knowledge needs two answers: what the second run changed, and which requirement is out of scope and why.

## What the checks reward

`chk-eval` loads `repair`, `remeasure`, and `cost`. Repair fails if any gold row's document or span still disagrees with the label after the function runs. Remeasure fails if the after score does not rise, and fails again if before and after are not the gold metrics. Cost fails unless the return matches the sheet, including a sheet whose expected spend is nothing (`None`, not a clipped total). Notes fail unless sprint text contains "fix" before "second" before "spec"; the benchmark pairs `log-night`/`hallucination`, `log-circular`/`retrieval`, `log-friday`/`reasoning`, and `log-approval`/`workflow`, and also contains "second" and "retrieval"; the improvement page contains `cost.label`, `label`, and `retrieval`; knowledge has two answers with the retrieval/in-force fact and the out-of-scope/clinician fact; and the workflow's improvement job is not commented.

`chk-m03-l05-rcp` is the requirements rubric. Scope that contains "including triage" or "virtual front desk" is the sponsor miss. Scope that contains `p-triage` or `vendor-bot` without those phrases is the triage miss. Non-goals that lack `p-triage` are also the triage miss. Priorities that name a ranked id and do not contain "not the value model" are the dot-vote miss. Coverage is 80 percent of a mention list: both non-goal ids, the value-model phrase, the four seat ids, `dms` under Systems, `g1` and "risk" under Gates, "clinician" and "urgency" under Non-goals, `ext-large` anywhere, the measured moved-count under Evidence, and at least one seat under Evidence. The backlog function must drop gold non-goals and keep other stories. `gate_for` on the gold requirement id must return `G1`.

`chk-readout` wants the steering sections filled: remeasure (retrieval and second), spec (`p-triage` and a non-goal phrase), systems (`dms`), backlog (`p-triage`), cost (`cost.label` and label), plus a clinician on urgency, patient data off the external model, a citation of a release file, a non-empty Asks, and retro headings Keep, Drop, Open.

`chk-individual-m03-l05` loads `personal.py`. A citation the gold says to keep must return `doc_id`, `version`, and `audience`. A citation the gold says to withhold must return `None`. Each metric's `meets_budget` must match whether the value clears the floor. The gold keep flag is `audience != "staff"`. On the public personal rows both askers are `patient`, so the chapter's patient-and-staff test coincides with that flag. A later hidden row with a staff asker and a staff document would split the chapter's rule from the gold rule. The miss text would still say the citation serves a staff document to a patient.

The mention count is not a constant in the checker. `m03_l05.py` passes `moved(rows)` into the mention list. `moved` counts predictions whose document id differs from the label and ignores span. The public `before_public` list is four in-force rows and one unauthorized row, all with span `hours-c1`. On that fixture the count is 1, before-accuracy is 0.8, and after-accuracy is 1.0. The pasted "1" matches the fixture. It is not a measurement the learner made. A profile whose rows differed would reject a hardcoded 1, which is good checker design wasted by a chapter that forbids recomputation.

## Thesis test

**One measured fix is the right size for a lesson.** Proven, inside this course. The repair touches one mechanism: an unauthorized circular cited as if it were in force. Hallucination (`log-night`), Friday reasoning (`log-friday`), and booking without approval (`log-approval`) stay open. The improvement page says GPU hours are not the cost of this fix. G1 on the citation requirement does not close G2. That residual is the best teaching move in the week. A learner who leaves with "we moved retrieval and we did not move the other three" has a true sentence about this system.

**One measured fix is the wrong size for teaching improvement.** The syllabus word is iterative. The lab is one substitution, explained before it is pasted, scored on a slice of five rows whose labels the learner is not shown. There is no second hypothesis, no alternative repair (filter at retrieval time, refuse, ask the DPO, drop the answer), no pre-registered decision about what rise would count as success, and no written reason to stop. Breck, Cai, Nielsen, Salib, and Sculley, in the ML Test Score paper, treat production readiness as 28 tests across data, model, infrastructure, and monitoring, scored by the minimum of the four section scores, because a single strong area does not make the system ready. This lesson's "improvement gate" is one unittest job. On that rubric it is, at most, a documented manual check of one behavior. It is not an improvement practice.

The cost function is the piece that does teach a stop. Returning `None` above the budget is a constraint, not a success metric. The pages never have to show the product or the budget figure. `chk-eval` accepts `cost.label` as a string. A learner can price nothing in public and still pass.

**Requirements that restate the sponsor are the failure mode, and this lesson grades a parody of that failure.** Proven as a risk. The checker really does reject the CDO's two phrases in Scope, and it really does reject triage left in scope. Emerging as a skill: the learner never writes a sentence that could commit that error. The antidote is in the same chapter as the task. Paraphrase is ungraded. "One front door for every hospital, live before Ramadan" is the CDO's second line. It contains neither banned phrase nor a ranked id. Placed under Scope, it can pass the sponsor probe. Placed under Objectives, the probe does not look there at all. The probe reads Scope for those strings and reads Non-goals for the id `p-triage`. A brief can praise the virtual front desk in Objectives, omit the id from Scope, name `p-triage` once under Non-goals, and satisfy the trap logic.

The dot-vote probe is a phrase probe. Priorities may name `p-triage` if they also contain "not the value model." The chapter puts that sentence in the paste. Lesson 4's design note says the dot-vote is not the value model because the team computed value ranges. This lesson does not ask the learner to use those ranges. The sentence replaces the model.

**A later team could not start from the finished brief.** The file has the headings the template asked for. It does not have what a stranger needs:

| Stranger's question | What the pasted brief supplies |
| --- | --- |
| What outcome moves, in a unit, by when? | "A patient can ask for hours and receive a citation they are allowed to see." No rate, no population, no date. |
| What is the test? | No test id. The second-run fact is a count of document swaps, not the accuracy the remeasure function returns. |
| What must not be built, as a verifiable system behavior? | "A clinician owns urgency" sits under Non-goals. That is a declaration. It does not say which action is refused, or which test shows the refusal. |
| What is assumed? | Nothing. The in-force id, the audience words, the open DPIA, and the label budget are all assumed in code and absent as assumptions. |
| What are latency, cost, and safety budgets? | `ext-large` is named. No latency number. No sar figure. The personal floors (0.8, with values 0.9 and 0.5) never enter the spec. |
| Which stakeholder conflict was decided, and by whom? | Seats are listed. The CDO's demand and the DPO's constraint are not placed in conflict. The solution's interview notes exist and the checks do not read them. The morning did not ask for an interview. |

29148's clause 5.2.3, read from the 2018 text, says initial stakeholder concerns do not serve as stakeholder requirements, because they often lack definition, analysis, consistency, and feasibility. The role cards are concerns. The pasted sections are those concerns sorted into headings. Clause 5.2.5 requires each requirement to be necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, and conforming. The scope line binds two concerns (cite the in-force document, and keep patient data off `ext-large`) in one paragraph. That fails singular. "Allowed to see" fails verifiable until audience, version, and asker are conditions. "Owns" fails the keyword rule the same standard gives: facts and declarations use "will"; mandatory provisions use "shall"; preferences use "should."

## What is already strong

These pieces should survive a redesign. They are Proven inside this course's fiction and aligned with the sources in `02`.

**Residual risk is named.** Three failures stay open, with log ids and mechanism names. That is more honest than a lesson that celebrates a single accuracy number. The benchmark's last line — the other three stay open — is the improvement lesson hiding inside a paste.

**Exclusions are first-class.** `p-triage` and `vendor-bot` are ids in `seed.json`, dropped by `kept`, and required under Non-goals. The stories are "Set clinical urgency" and "Replace the contact center with the vendor bot." Those are solution statements. Refusing them is the right product decision. Burying the clinician rule in the same section is the mistake, not the existence of the section.

**The budget can veto the fix.** `spend` returns `None` when `count * price > budget_sar`. Gold treats that as "the labeling does not fit, rather than a clipped total." That is a non-functional constraint with a real comparison. The pages throw it away by forbidding the learner to type an amount.

**The gate does not pretend the DPIA is done.** `stage-gate.md` lists G0 intake, G1 risk tier, G2 DPIA, G3 pilot approval, G4 go-live, G5 post-launch review, and states that G1 is the risk tier. The shell sends every requirement to G4. The replacement puts only `req-cite` on G1. Leaving G2 open matches Module 4 Lesson 1, which fills the DPIA. The defect is the empty string for every other requirement id. Residency (`ext-large`) has no gate. The clinician rule has no gate. An empty return cannot be traced.

**Labels stay off the learner's disk.** The public slice has predictions and no label field. That continues Lesson 4's hidden-test protocol. A redesign that asks the learner to "look at the labels and fix the misses" would break that protocol. The second measurement can stay blind.

**One person, five parts.** The background already refuses a team handoff. The redesign should keep that and give the one person the four seat jobs as documents they must reconcile, not as roles waiting for classmates.

## Structural problems that are not the trap

**The workshop is a reading list.** `ws-access` is the name on the role-card file. Hidden answers "stay in the interview." The solution's `cdo.notes.md` and `dpo.notes.md` are trainer notes the morning did not ask for and the checks do not read. Slides say the instructor plays `dpo` and `cdo` in disagreement for three minutes. A self-paced run has no instructor in the room. The conflict the trap depends on is optional theater.

**The personal lab is a second copy of Lesson 3.** Lesson 3's trap is citing `circ-ramadan-unauth` or serving a staff leaflet to a patient. Lesson 5's personal chapter repeats the audience rule with the words `staff` and `patient` and warns the learner not to rewrite them as `public` or `restricted`. The metric half is new and unused: two floors, one miss, no path into `requirements.md`. The individual check is real work. It is the wrong week if this week is the brief.

**Iteration is a word in the sprint file.** The checker looks for the substrings fix, second, and spec in that order. "The spec comes before we fix the second problem" can still match, depending on position. More importantly, the order is given in chapter 05 and pasted. Sequencing is the decision. The lesson announces it.

**Traceability is a mention list.** Eighty percent of tokens is not a trace. A requirement id does not point at a test. `req-cite` points at `dms` and at `G1`. It does not point at `test_repair`, `test_remeasure`, or the personal citation rows. FAA report TC-16-39, quoting ARP4754A section 5.3.1.1, says requirements defined to prevent failure conditions or to provide safety-related functions should be uniquely identified and traceable through the levels of development. The course's safety-relevant lines (no staff document to a patient, no clinical urgency from the assistant, no patient data on `ext-large`) are not uniquely identified. `req-cite` is the only id, and it bundles a citation behavior with a residency constraint.

**The improvement page cannot carry a number.** Chapter 09 says not to type an amount from `prices.csv`. The checker does not want the amount. The advanced layer in `module-03.md` is "the improvement's cost in labels or GPU hours." The foundation page names the price-sheet key and forbids the quantity. Steering question 4 asks what the improvement costs, in labels or GPU hours. The readout answers with the key name.

## Deletions, stated as curriculum actions

Delete the finished-page paste as the assessment. Keep the template headings only if each heading has a job a checker can distinguish from keyword presence. Delete the sentence that tells the learner the moved count is already 1. Delete phrase-grading of "not the value model" once a value comparison is the task. Delete `personal.py` from this lesson's critical path; if the floors stay, they move into the budget section of the spec and an existing Lesson 3 test covers audience. Delete the claim that an uncommented unittest job is an improvement gate. Delete dependence on a live facilitator for the CDO/DPO conflict.

Do not delete the four log ids, the non-goal ids, the open DPIA, the label-budget veto, the blind slice, or the rule that a sponsor sentence is not a brief. Those are the lesson's actual content. The paste is the delivery vehicle, and the vehicle is what fails the thesis.

## Fit against the rest of the program

Lesson 4 drafts the benchmark and runs the workshop notes. This lesson is supposed to be the second measured run and the rehearsal brief. Module 4 Lesson 1 opens the attack window and fills the DPIA, and it assumes G1 was named and G2 was not closed. Module 4 Lesson 5's proposal depends on "the requirements from Module 3, Lesson 5." A split that still emits `rcp/requirements.md` before `rel-m04-l01` preserves that dependency. A split that moves the brief after the DPIA would make Module 4 Lesson 1 specify a system the brief has not bounded.

The curriculum map's "new terms" for this lesson are the rehearsal brief and G1 as the risk tier. Both are introduced as labels for files the learner already has. Neither term is practiced as a decision. That is the evaluation in one line: the week names the right objects and then pastes them.
