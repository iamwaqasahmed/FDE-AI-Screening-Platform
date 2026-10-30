# 16 — Architecture decisions

Each decision is the one this folder implements. The rejected line is the strongest alternative that was actually considered.

## ADR-1 — One engagement, three parties

**Decision.** Al-Waha, the National Desk, and a Coverage Partner. The student inherits `assistant-0.9`.

**Why.** The cohort needs a clinical decision they must not automate, and a channel and a payer so that a single database is not the whole problem.

**Rejected.** A procurement agency or a permit office as the spine. Their interesting bytes are also restricted. The cloud boundary does not get cleaner. A second industry is a later course.

## ADR-2 — Three logs, no shared clock

**Decision.** `log_hospital`, `log_channel`, and `log_payer`. No cross-log key. No total order. A KPI that drops its authority fails.

**Why.** One log makes the warehouse a defect of a single clock. The hard case is a correct aggregate of the wrong authority.

**Rejected.** One event log with a `clock_kind` column. That still offers a global sequence.

## ADR-3 — Nine investigations

**Decision.** INV-01 through INV-09, cumulative checks, distinctions off the blocking path.

**Why.** A long list of locks will not be finished by a mixed solo learner, and many locks were the same insight sliced into answer keys. Nine is inside the range a pacing review judged finishable, and each one has a holdout.

**Rejected.** Twenty short lessons that name the repair in the chapter. A catalog of roughly thirty sequential locks. A rule that the chapter may never name a mechanism.

## ADR-4 — Prediction, then the name on another object

**Decision.** Prediction file required and unscored. Chapter names the mechanism on a different object. Graded row unnamed. Binding is field paths and role tags.

**Why.** Silence stalls a solo learner. Naming the graded row makes the check a copy task.

**Rejected.** Printed solution chapters. Symptom-only chapters with no later name.

## ADR-5 — No model in the grader, no model in the account

**Decision.** Fixtures and deterministic compares. The template fails if it contains a model resource. Public text is an object. Restricted bytes stay on the laptop.

**Why.** As of 30 October 2026 the Regions guide had no Saudi geography. Gulf model endpoints are not in-Kingdom execution. A live grader moves when weights move.

**Rejected.** Bedrock as the production model. A geographic profile described as “stays in the region.”

## ADR-6 — Capability in the tool, key on the operation

**Decision.** The coordinator mints a capability. `book` checks it. The business idempotency key is stored with the operation. Step Functions and SQS do not replace either.

**Why.** Schema validity, prompt text, a callback token, and a FIFO queue each look like the guarantee and are not.

**Rejected.** Prompt instructions as the control. Exactly-once as a queue feature.

## ADR-7 — Filter before score, page on the served document

**Decision.** Audience and status apply before rank. Citations carry a content hash. The SLI that pages is the served document id. Prompt bodies are not stored.

**Why.** Rank-then-filter leaks. Host metrics stay green when the hours change. The useful log line is often the personal data.

**Rejected.** Rank-then-filter. A vector database as the lesson. CPU and p95 as the only page. Deleting a database row and calling the person gone while the citation index still serves them. A prompt-filter product as the security boundary. A model-tool protocol as a substitute for the capability check.

## ADR-8 — Local policy check, optional apply

**Decision.** `cdk synth` or the equivalent, plus a policy pack, is the cloud check. A live apply is a distinction with a budget alarm first and a destroy after.

**Why.** An account is not required to learn the boundary. An account without an alarm is how a lab becomes a bill.

**Rejected.** A local cloud emulator that needs a vendor token, as the thing every student must run.

## ADR-9 — A stop ends the feature it names

**Decision.** Refusing `dec-clinical` ends that feature. Later investigations are the access workflow.

**Why.** A stop that continues into the same build is a planted sentence.

**Rejected.** Ending the entire course at the refusal. The student would never practice the repairs.

## ADR-10 — Fictional law, real map

**Decision.** Case rules are analogues. One orientation page points at official documents and does not merge their vocabularies. Student text that claims compliance fails review.

**Why.** The illustrative restricted tier is enough to justify the byte rule. Teaching the exercise as the statute is not.

**Rejected.** A law module. A certification exercise.
