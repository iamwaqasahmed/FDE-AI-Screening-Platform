# Redesign — architecture, simulation, and the requirements artifact

This file specifies a self-paced replacement for `rel-m03-l05`. It assumes `01` and `02`. It does not edit the course. The stranger in the thesis is a second person, or the same learner on a later day, who receives only the public pack plus `rcp/requirements.md` and has to implement the in-scope change and the tests without the chapter paste.

## Split the lesson

**Recommendation: yes, split into two lessons. Do not split into three.**

| | Lesson 5a — One measured change | Lesson 5b — The brief |
| --- | --- | --- |
| Release | Keep `rel-m03-l05` for the code and the second run, or mint `rel-m03-l05a` if packs must not share a checker | `rel-m03-l05b`, still before `rel-m04-l01` |
| Job | Move one named failure. Price it. Stop if the budget refuses it. Leave the other mechanisms open. | Write the requirements a later team starts from. Refuse the sponsor sentence by analysis, not by paste. |
| Code the learner replaces | `repair.py`, `remeasure.py`, `cost.py` | None, or a thin `trace.py` that reads requirement ids and points at test names. No new model. |
| Pages | `hypothesis.md`, `benchmark.md` second run, `improvement.md` with the stop rule | `rcp/requirements.md`, `assumptions.md`, `readout.md`, `retro.md` |
| Checks | `chk-eval` rewritten to grade the hypothesis and the stop, not a pasted count | `chk-m03-l05-rcp` rewritten to grade structure, trace, and paraphrase resistance |
| What it is not | A production-readiness program | A full 29148 specification or a USDS sprint |

Why two is enough: Module 4 Lesson 1 needs the risk tier named and the DPIA still open. Module 4 Lesson 5 needs `rcp/requirements.md`. Both products exist by the end of 5b, before guardrails. A third lesson called "continuous improvement" would steal the incident, cache, and surge work from Module 4 and would still be one more scripted loop. The thesis is that one fix cannot teach improvement as a practice. 5a teaches the shape of a loop (hypothesis, change, measure, residual, stop) with a single change. That is the honest size. Naming the un-run iterations is part of the lesson, not a prompt to run them.

Why not keep one lesson: chapters 06 through 09 already overflow a paste day. Adding an assumption log and a trace matrix on top of six pasted modules and five pasted pages makes the failure mode worse. The fallback, if the calendar cannot grow, is in `05`: delete the personal lab and the finished paste, and keep a single harder lesson. That fallback is worse than the split and better than the status quo.

**Label: Experimental** until one self-paced pilot finishes both lessons without a facilitator. The split itself is a curriculum hypothesis, not a standard.

## Simulation the learner walks alone

The packet already has the conflicting seats. The redesign makes the conflict the work, because the slides' three-minute role-play does not exist in a self-paced run.

Inputs, all public, none of them new patient rows:

- Role cards, unchanged. The CDO concern stays visible so the learner can refuse it.
- Lesson 4's value note, cited, not recomputed from scratch. If that note is not in this pack, copy the already-released value ranges forward. Do not invent new ones.
- `stage-gate.md`, unchanged.
- `slices/before.jsonl`, unchanged: predictions, no labels.
- `prices.csv` and `labels.json`, unchanged.
- `personal.jsonl` floors, moved into the spec's budget table. The cite-or-refuse behavior stays a Lesson 3 regression, named by test id.
- `seed.json`, rewritten as proposed solutions, not as requirements. Titles stay solution-shaped so the learner has something to reject.
- A new one-page `conflicts.md` that states three disagreements in the seats' own words and gives no resolution: CDO wants triage live before Ramadan; DPO wants patient data off the external model and has not closed G2; access and PHC want wait and return outcomes that the citation slice does not measure. This file is an elicitation aid. It is not the answer key. **Label: Emerging.**

The learner writes, in one sitting, four seat jobs as jobs rather than solutions ("when I am the access manager, the job is to cut no-show cost"; "when I am the CDO, the demand on the table is a front door including triage"). Then they mark which demands are concerns, which are outcomes, and which are solutions. Torres's tree is the picture. USDS's rule is the test of the first paragraph: if a solution noun appears in the problem statement, the paragraph is not done. Nouns that fail that test in this case include triage, virtual front desk, vendor bot, chatbot, and go-live.

One person holds every seat. The readout's Asks section is where the learner records the decision they are not allowed to pretend was unanimous. Example of a legal ask, still inside the fiction: which document versions the pilot may cite while G2 is open. The DPO seat owns that ask. The learner does not interview a classmate.

## Three artifacts, compared

A fourth shape, a safety-case diagram, is named and rejected as the week's primary artifact.

### Artifact A — Outcome-traced requirement slice

**Label: Proven** method, **Experimental** as this lesson's graded file.

The file `rcp/requirements.md` holds a small set of shall-statements with the 29148 attributes the checker can see without a requirements database:

- Unique id, never reused (`REQ-CITE-1`, `REQ-AUD-1`, `REQ-RES-1`, `REQ-URG-1`, `REQ-COST-1`).
- Parent outcome id (`OUT-HOURS` or `OUT-WAIT`). A requirement with no parent fails.
- Statement using shall, one predicate.
- Conditions (asker, audience, version rule, slice).
- Verification method and test id.
- Gate id, and whether the gate is open or closed.
- Priority only among requirements that are in the set.

Beside it, `assumptions.md` has one row per assumption: statement, owner seat, status (`untested`, `tested-pass`, `tested-fail`, `deferred`), and the evidence or the deferral point. 29148 says assumptions are documented and validated. NASA says they are confirmed before baseline. Status is how a lesson grades that without a multi-month baseline.

The exclusion register is a section that is not a requirement section. Each row is a concern id, the seat that raised it, the reason it is not in the set, and the consequence if someone adds it later. `p-triage` and `vendor-bot` live here. They do not use shall.

Trace table, the piece a stranger implements from:

| Outcome | Requirement | Test the stranger writes or points at | Gate |
| --- | --- | --- | --- |
| A patient asking for hours gets a citation they may see | `REQ-CITE-1` | `tests.test_repair`, `tests.test_remeasure` on the public slice | G1, not closed by this file |
| The same answer respects audience | `REQ-AUD-1` | Lesson 3 audience test id, named, not reimplemented | G1 |
| Patient content does not go to the external model | `REQ-RES-1` | Existing residency check from Lesson 2, named | G1 |
| Clinical urgency is recorded by a clinician | `REQ-URG-1` | A negative path written as a positive assertion: no urgency field is set by the assistant in the fixture | G1, and G2 still open for the DPIA |
| The repair is claimed only inside the label budget | `REQ-COST-1` | `tests.test_cost` including the over-budget `None` | G1 |

A stranger's job is to implement those test names against the public fixture and to refuse any story in the exclusion register. They do not need the chapter's prose. They need the ids, the conditions, and the expected comparison.

What this artifact does poorly: it can become a template exercise, every shall-statement equally lifeless. The problem statement and the tree are what keep the CDO sentence from being translated into shall-statements by reflex ("the system shall provide a virtual front desk"). The checker rejects a shall-statement whose parent is a solution id.

### Artifact B — Opportunity solution tree as the primary deliverable

**Label: Proven** as a discovery picture (Torres, page opened in `02`). **Label: Emerging** as a substitute for `rcp/requirements.md`.

One page, four bands. Outcome is a measure from the value model, not "better experience." Opportunities are sentences in the user's job, grounded in the role cards' problem lines (no-shows, returned referrals, an answer the asker may see). Solutions include the citation rewrite, triage, and the vendor bot, each hanging off an opportunity or marked unconnected. The experiment band has one row: the unauthorized-id rewrite, the slice, the before and after the learner computed, and the assumption it tested. Unconnected solutions are the non-goals.

A stranger cannot implement from a tree. There is no shall, no test id, no budget unit, no gate. Module 4's proposal author would re-interpret the picture and the sponsor sentence would return. Torres is explicit that the tree guides discovery when an outcome exists. She is not offering it as a verification baseline.

Use the tree as a required page inside artifact A, two bands above the shall-statements. Do not grade the tree as the contract.

### Artifact C — Acceptance-tested stories plus an exclusion register

**Label: Proven** in agile teams. 29148 note 2 allows stories without the word shall. **Label: Experimental** as the only artifact in this case, because the current `seed.json` shows the failure: the stories are already the sponsor's solutions.

Each in-scope story would carry given/when/then pointed at the public slice. The exclusion register would carry `p-triage` and `vendor-bot`. This is the smallest step from the current backlog chapter, which is why it is tempting and why it is the wrong primary artifact. Given/when/then written by a learner who has just read the CDO card will test "triage goes live before Ramadan" and the checker will need the same banned phrases it has now. Stories do not force an outcome, an assumption, or a budget. Data 4-style prohibitions become another story someone can delete.

Stories are allowed as the verification attribute of artifact A (the "then" clause is the test). They are not the requirements set.

### Rejected fourth — safety-case graphic as the week's spec

Claim, argument, evidence diagrams are how some safety cases are reviewed. **Label: Experimental**, and a poor fit. The learner has not had the DPIA lesson yet. A graphic with no shall-statements fails the stranger test the same way the tree does. Module 4 Lesson 1 can point back at `REQ-URG-1` and `REQ-RES-1` when the DPIA is filled. That is traceability enough.

### Choice

Adopt A, with B's top two bands as the first pages and C's then-clause as the verification attribute. Call the bundle the rehearsal brief. Keep the file name `rcp/requirements.md` so Module 4's dependency does not break. Put the assumption log in the same file or in `assumptions.md` if the checker wants a separate path. One file is easier for a stranger. Two files are easier to grade. Prefer two files and a trace table that both must agree.

## The measured change, redesigned without pretending it is a program of improvement

5a keeps the code's size. It changes the decision around the code.

The learner reads the four log ids and writes a hypothesis before pasting repair: which mechanism this change can move, which it cannot, and what comparison will count as moved. The public slice supports only the retrieval mechanism. A hypothesis that claims the Friday offer will move is wrong, and the chapter should say why in the solution, not before the attempt. **Label: Experimental** as a graded prediction. Keep the stakes low: the check looks for the log id they chose and whether the after score moved that id's mechanism, not for a numeric forecast they cannot know without labels.

Repair stays a special case, in the sense of the Palantir careers page that was opened: one unauthorized document id, other fields copied, so a wrong span is not silently "fixed." The requirement in 5b must not name `circ-ramadan-unauth`. Naming the fixture id in the spec freezes a design 29148 calls inappropriate. The spec says: when the cited document is not the version in force for that asker and audience, the reply cites the in-force version or cites nothing. The fixture id lives in the test, which is allowed to be specific.

Remeasure stays blind. The learner reports before and after by running their function on the rows the test builds, in the suite, and copies those two numbers into `improvement.md`. The chapter does not pre-print them. The checker already knows the gold metrics. Today the chapter also prints the evidence count. That print goes away.

Cost stays a veto. `improvement.md` includes the product and the budget, read from the sheet, and the sentence that a product over the budget is not a shipped improvement. GPU hours are out of this change's cost and are an assumption deferred to Module 4, not a boast.

The benchmark keeps the four failures. The second-run paragraph may claim only the mechanism the hypothesis named. Claiming all four moved is a fail even if the words "second" and "retrieval" are present.

This is one iteration in the measurement sense. The retro's Open section lists the experiments not run: a retrieval-filter instead of an id rewrite, a refusal instead of a replacement citation, a label spend on the hallucination slice. The learner does not build them. Writing them is how the lesson teaches that improvement is a loop without faking a second loop. **Label: Emerging.**

## Datasets and synthetic data

Do not add patient rows, notes, or a new generator of clinical text. The honesty rule of Lesson 1 still applies. The public citation slice and the personal rows are enough.

Use, unchanged:

- Five public predictions, four already in force, one unauthorized, shared span. Document the fixture's structure in the instructor key. Do not document the after-accuracy in the student chapter.
- Two personal citations (patient/patient kept, patient/staff withheld) and two metric rows (0.9 against 0.8, 0.5 against 0.8). These floors become `REQ` budget rows. They are not a new model benchmark. The paper's 36-team scores are not a comparison point.
- Three stories in the seed, two excluded.

Add only text fixtures:

- `conflicts.md`, the unresolved seat disagreements.
- A trace template with empty test-id cells.
- An assumption template with the statuses above.

Synthetic dialogue for a fake workshop transcript is **Experimental** and unnecessary. The role cards are already the elicitation. A generated transcript would let the learner quote a puppet instead of deciding.

Labels stay on the grading service. The stranger implements against public fields and against tests whose expected documents are in the test file the course already ships. If the redesign wants the stranger to write a new test, the expected in-force id can sit in the test fixture the pack already reveals through the repair chapter's constants. Prefer pointing at existing tests to asking for a new oracle.

## Production scenarios the spec has to survive

These are the edge cases a keyword brief ignores. Each one is a row the assumption log or the requirement conditions must cover. None of them requires a new service.

**Right document, wrong span.** Accuracy needs both. `moved()` counts documents only. A spec that says "the second run moved 1 citation" is ambiguous about which function moved. The trace's verification line names the comparison: document and span, on the held-out pairs the grader holds.

**In-flight version.** Lesson 3 keeps the criteria version a referral started on. A requirement that says "always cite the latest in-force document" uses a totality word 29148 warns against and contradicts the in-flight rule. Condition: hours questions use the current in-force hours circular; referrals already in flight keep the criteria version they started with. Two requirements, or one requirement with two conditions. Not one adverb.

**Audience vocabulary drift.** Lesson 5's personal slice says `staff` and `patient`. Lesson 3 says `public` and `restricted`. A stranger who implements `REQ-AUD-1` against the wrong pair will pass one lesson and fail the other. The requirement names the vocabulary of the slice it tests and points at the Lesson 3 ids as a second test, rather than redefining audience.

**Paraphrased sponsor.** "One front door before Ramadan" contains no banned token. Artifact A's checker fails a problem statement or a shall-statement that promises a channel, a go-live date, or clinical urgency as an assistant output, using a small lexicon plus a structural rule: a date-before-Ramadan claim with no measured baseline is an unbound constraint and is rejected as infeasible. The lexicon is in the instructor key. The student chapter shows two paraphrases that fail and does not show the gold brief.

**Dot-vote.** The tree marks triage as a solution with no opportunity that the value model ranks first. The priorities attribute ranks only in-set requirements. The phrase "not the value model" is not evidence. Evidence is a pointer to the Lesson 4 value note and a sentence that names which outcome won the tradeoff (citation integrity versus a wait-time outcome the slice cannot move). If the value note cannot support a numeric tradeoff, the assumption is `untested` and the priority is marked provisional. That is an acceptable 5b outcome. Pretending the tradeoff was computed is not.

**Budget overrun.** If `count * price` exceeds `budget_sar`, 5a does not claim an improvement. 5b's `REQ-COST-1` says the change is not accepted. The readout tells steering the fix was refused by the budget. The current gold can represent that case. The current pages cannot.

**Open G2.** G1 on the citation requirements does not assert that personal-data assessment is done. `REQ-RES-1` and `REQ-URG-1` carry the attribute `gate_status: open` for G2. Module 4 Lesson 1 closes that attribute. A stranger who treats G1 as permission to ship to patients has misread the gate column.

**Campaign and no-shows.** Lesson 4's campaign can change volume. A citation repair does not change no-show cost. The outcome band may mention waits only as a parent the citation work does not claim to move. Writing `OUT-WAIT` as the parent of `REQ-CITE-1` is a trace error. The access manager's job stays on the tree as an opportunity with no solution in this release.

**Deletion.** Data 5 in the ML Test Score paper says a deletion has to reach training data and learned models. This spec defers that to Module 4 with an assumption row, owner DPO, status deferred, review point `rel-m04-l01`. A stranger does not build deletion here.

**Latency.** No number is invented. Assumption: chat latency under load is owned by the surge lesson; this brief sets no latency shall-statement. NASA's checklist is why the deferral is written. An empty performance section would be an incomplete set. A deferred row is a complete statement of what this set does not yet bind.

## Architectures for the brief, in the software sense

The assistant architecture does not change in 5b. No new index, model, or tool. The "architecture" is the information architecture of the spec:

1. Problem statement and tree (discovery).
2. Requirement objects with ids (contract).
3. Assumption log (what would make the contract false).
4. Trace to tests and gates (what a stranger builds and what a reviewer can audit).

That is four small texts, not four systems. The code path that stays is the citation repair on the public slice, the cost veto, and the existing audience regression. Stage gates remain the course's G0–G5 fiction. They are not ISO 15288 stages. The spec uses them as attributes because the rest of the course does, and it does not pretend a G1 stamp is a design review.

## What the stranger receives

A zip of the public pack, `rcp/requirements.md`, `assumptions.md`, and the test files with the repair assertions. They do not receive chapter 09. They can make the suite pass and they can say which stories they will not build. If they cannot, the brief failed, not the stranger. That is the acceptance test of the redesign, run by an author before the chapters ship. **Label: Experimental** as a release gate for the curriculum itself. It is the right gate.
