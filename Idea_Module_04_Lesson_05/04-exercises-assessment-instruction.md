# 04 — Exercises, assessment, and self-paced instruction

One person holds every hat. There is no cohort to rotate, no facilitator in the room, and no labeling vendor. The assessment map's steering sheet is a file. The checks stay deterministic. They grade artifacts and field equality against a planted gold file. They do not grade style, and they do not call a model to judge a model.

## Prerequisites

Before 5A the learner has already: passed the Lesson 4 drill (two sites, insurance breaker, rent-versus-buy); written requirements that refuse the sponsor sentence (Module 3 Lesson 5); kept identity in front of the waitlist; left clinical urgency with a clinician; kept patient data off `ext-large`. The value model, the readiness survey, and the stage-gate note are in the pack. The learner does not need a new authentication course. Sign-in here is the staff-versus-service confirmation after that drill.

Before 5B the learner can read a JSON call row and has seen, in Module 1, that emergency wording routes to a human and a return cannot leave without a coordinator. Those rules bound containment. 5B does not reopen the agent design.

Before 5C the learner has the evidence files from 5A and 5B on disk. A memo that cites a measure those files do not contain fails traceability. If structure B is used, the same rule applies across studios inside one folder.

Reading load for the learner, not the reviser: the Service Manual baseline page, the FHIR cancelled-status comment, and a one-page briefing schema in the chapter. The AWS narrative post is optional facilitator reading. Vendor handoff essays stay out of the student packet. The chapter states the pattern in course language and cites the defect in the pack.

## Hat map for a single learner

The person changes hat by changing the file they are allowed to edit in that studio. The chapter says which hat is speaking. The checker does not care about the hat. It cares about the file.

| Studio | Hat in the foreground | File |
| --- | --- | --- |
| 5A connect | Application engineer, then architect | `leave.py`, `bus.py`, `signin.py`, `warehouse.py`, `architecture-deploy.md` |
| 5B handoff | Application engineer, then product | `handoff.py`, `briefings.json`, `containment.csv`, `adoption-staff.md` |
| 5C decision | Product and AI together, then lead | `register.csv`, `rank.py`, `rcp/proposal.md`, `readout.md`, `operations.md` |

The lead's readout is written last, after the memo, with the memo closed, so the five steer answers are recall plus the pack, not a second paste of the memo. The architect's operations file is the place client owners are named. The AI hat's only job in 5C is to attach measure definitions to metrics. That replaces "bring a measured problem" as a slogan.

## Studio 5A — connect

**Exercise A1. Staff after the drill.** Given `iam/staff.json`, implement `accept` so a staff actor is staff and a service actor is not, even when the service actor's role string is `admin`. Add one test the shell does not have: a missing `kind` is not staff. **Proven.** Solution shape: compare `kind` to `staff`, ignore `role`. The current reference already does this. The new test is the point.

**Exercise A2. Tolerant cancel.** Given the bus file, keep unknown fields and keep `session.cancelled`. Then add a producer change: a new optional field on the cancel event. The old reader must still mark the event kept and must still expose the topic. **Proven** against Fowler's tolerant reader. Solution shape: copy through id, topic, and a kept flag; do not bind a generated class that lists the fields.

**Exercise A3. Late leave, and the rows that must not cancel.** Apply the visible leave row so a published session becomes cancelled and emits `session.cancelled`. Hidden rows: early leave, other consultant, duplicate id, already arrived, unknown session. Duplicate id emits the event once. Arrived stays arrived and emits nothing. **Proven** pattern from the FHIR cancel comment plus ordinary idempotency. Solution shape: the reference predicate (same consultant and entered after published) plus a status guard and a set of leave ids already applied. The chapter describes the predicate in words. It does not paste the function. The worked solution lives in `Solution_Copy`, opened after the check, as today.

**Exercise A4. Clock.** `clock` returns `referred_at`. A one-row metric file defines wait from that clock to a named end. A submission that stores `booking_date` fails the metric file and the function. **Proven** measurement definition. This is where "success metrics were measured" starts, one definition early.

**Exercise A5. Boundary sketch.** Fill Zones, Flows, and Boundary without a paste block. The checker still requires the three zone tokens, `cc`, `bi`, `hr`, `bus`, clinician, and urgency. Add one sentence that names the scheduling service as the only writer of the cancel. **Proven** tokens, **Emerging** extra sentence. A banned sentence still fails.

Chapter text shows the shell, the defect, and the test names. It does not show the filled module. That is the deletion that makes A1–A4 practice.

## Studio 5B — the twenty-second handoff

**Exercise B1. Schema.** The learner completes a table: for each briefing field, who needs it in the first twenty seconds, and what goes wrong if it is wrong. Fields: caller intent, actions already taken, unresolved question, referral or patient identifier, channel, and a next step the human may override. Urgency is not a field the assistant fills. **Proven** as a design exercise. The checker looks for the field names and for the sentence that urgency stays with a clinician.

**Exercise B2. Write six briefings.** Visible corpus only. For each call, write the fields or a refusal code (`empty`, `too_long`, `urgency_invented`, `id_mismatch`). **Emerging** product work, graded as field match against author gold, not as prose quality. Solution approach: fill from the call's structured fields; do not paraphrase the whole transcript into `unresolved`; refuse when the gold refusal applies. A briefing that copies the caller's clinical self-assessment into an urgency field fails even if every other field matches.

**Exercise B3. Repeat-explanation probe.** A scripted human turn says "which referral?" The learner marks whether the briefing already contained the identifier. The score is the count of probes that were necessary, stored as a result id. The chapter does not print the count. **Emerging** metric. It replaces containment as the handoff's success measure. Containment is exercise B4, a separate table.

**Exercise B4. Finish or hand off.** For each intent, `finish` or `handoff`. Status questions may finish only if the status tool's answer is on the row and no emergency flag is set. Anything with emergency wording or a coordinator-required return is `handoff`. **Proven** relative to earlier course rules. A row that finishes an emergency fails the boundary dimension.

**Exercise B5. Staff adoption, half a page.** Name the behavior that should change in the first week (open the briefing before speaking), the person who shows a colleague (a client contact-center lead, not the learner), and the signal that it failed (repeat-explanation probe still firing). **Emerging**, drawn from the shape of the McKinsey insurance case without its numbers. The checker looks for a client role name, a behavior, and a signal id from B3. It does not look for a percentage.

The individual lab, if it lives here: one hidden call, one briefing, one refusal. Done alone. It replaces `personal.py` as the graded individual. The attack smoke can still run in the unit suite.

## Studio 5C — the evidence pack

**Exercise C1. Register.** Rows for the benefits the learner is willing to defend. Each row has an id, a segment, a baseline citation (a pack file id), a target described as a direction if the pack has no numeric target, a class (cashable, non-cashable, user-time), a client owner, and a dependency. **Proven** against the Service Manual and Teal Book chapter 19. At least one row uses the referral clock. At least one row is the phone-only segment. The forward-deployed engineer is not the owner.

**Exercise C2. Reconciliation.** Two ledger lines, one reason table. Output one retained id and one dropped id, with the shared reason code. **Proven** double-count rule from the Digital and Data Benefits framework (one case, no double claim). The Plan section of the memo points at this file. The words "same" and "call" are not sufficient and are not required.

**Exercise C3. Ranking sheet.** Fill value, feasibility, effort, and impact only where a citation exists. Set `open` false when a blocker is present. `first` returns the first open id in the learner's defended order, and the prose roadmap's earliest problem id matches it. Dot-vote is a column that is not read by `first`. **Emerging** instrument, **Proven** outcome on this pack if the gold decision remains `p-clock` with the identity dependency stated. A roadmap whose first id is `p-triage` or `vendor-bot` fails, as today.

**Exercise C4. The memo.** Purpose, the decision, the initiative, the risks, the owners. Section budget small enough to read in one sitting. Appendices are the register, the reconciliation, the briefing schema, and the leave negatives. Client is Al-Waha. **Proven** reading order from the AWS narrative description, shortened. The chapter shows a blank section list. The solution copy shows one finished memo after the checks pass, labeled as one acceptable path when the citations hold.

**Exercise C5. Hostile reader.** With the memo window closed, answer the five steer questions in `readout.md`, each with a citation id. Then open a finance objection card that quotes the two ledger lines and asks which one was dropped. The learner revises the Plan section if the objection finds a second claim. **Proven** as a self-paced substitute for the fifteen-minute silent read plus the room's comments. `knowledge.md` keeps two numbered lines: the cancel event, and the first problem with its dependency. Those lines are recall, and they stay separate from the integrate miss messages, as the current lesson insists.

**Exercise C6. G4.** `operations.md` Gate lists evidence items and a status. Clinical safety owner is `med-dir`. Benefit owner is the client role from C1. Phone channel operator is a client role. The learner does not sign clinical safety as themselves. **Proven** for this course's fictional gate.

## Rubric

Keep the assessment map's four dimensions. Change what they bind to.

| Dimension | Pass line in the rebuilt checks |
| --- | --- |
| Must-mention | Each required claim is present as a structured field or a citation id, not as a unique English phrase |
| Must-not-claim | Banned sentences; a second benefit on the shared reason code; an uncited percentage; urgency assigned by the assistant; patient data on `ext-large`; roadmap opening on `p-triage` or `vendor-bot`; the learner named as clinical-safety owner |
| Traceability | Every metric and every score cites a pack id or a `work/evidence` id that exists |
| Boundary | Clinician owns urgency; coordinator required where earlier modules required it; service identity is not staff |

Foundation failures still block a distinction, as the assessment map says. Advanced slices, not foundation: a second event version, a copilot-ignored scenario written up, sensitivity on one assumption ("if phone-only share is lower than the skew suggests, the callback roster changes"). Sensitivity is **Proven** in the Service Manual and **Emerging** as a graded slice here. Do not make it the pass line.

The checker prints miss sentences in course language, as it does now, without printing lags, counts, hashes, or attack text. Hidden corpus rows are not echoed. A watermark still fails closed.

`chk-readout` remains a file. The assessment map can say the facilitator sheet is used only when a cohort is in the room, and the file rubric is the self-paced equivalent. Do not pretend a markdown file is a live steering conversation.

## Solution approach the chapters should withhold

The solution copy, opened after the checks, can show:

- `accept` implemented as a kind comparison.
- `consume` implemented as a pass-through of id and topic with `kept` true.
- `apply` implemented as same consultant, entered after published, status still cancellable, leave id not seen.
- `clock` implemented as `referred_at`.
- `handoff` implemented as a field copy when the refusal predicates are clear, and a refusal object otherwise.
- `first` implemented as the first id whose sheet marks `open`, after blockers have forced `open` false.
- `evidence` implemented as `med-dir` at G4 only.
- A memo that cites the reconciliation id and the clock id, drops one ledger line, opens on `p-clock`, names client owners, and refuses triage.

Showing that list in the student chapter is the current failure mode. The student chapter shows the defect, the fixture shape, and the command. The solution chapter shows the implementation.

## Self-paced instructional design

Sequence inside a lesson stays linear. 5A before 5B before 5C, because the memo cites the earlier evidence. Do not preview 5C's decision inside 5A's chapter. The current chapter 00 lists every miss, including the proposal misses, before the learner has seen the ledger. That list belongs in the finish chapter as feedback, not in the background as a spoiler.

Interviews stay. They are the one place a persona may state a fact ("empty is not a handoff," "late leave creates `session.cancelled`"). The notes the learner writes must record the fact in their own rows, and the checker looks for the fact id the persona released, which is the pattern `test_m04_l05.py` already uses (`handoff-summary`, late leave). The chapter does not paste the note.

The demo may still print the finance question and withhold the answer. 5C is where the learner answers it from the ledger. If the answer is pasted in an earlier chapter, delete that paste.

A stuck learner gets the miss sentence and the fixture name. They do not get the filled function in the error text. The solution copy remains the debrief, as the course's contract says.

Time: structure A is three sittings. Say so in the module page. Do not invent a clock. Structure B is one sitting only if B1–B2 are six calls and C4 is short. If pilots show learners skipping B2, split anyway.

Language: the student voice of the existing chapters is concrete and repetitive for a reason. Keep that voice. Cut the repetition that exists to stop people pasting the wrong block, because the filled block will no longer be on the page.

## What not to assess

Do not score a live call. Do not score accent, empathy, or clinical correctness of a diagnosis. Do not ask the learner to invent a containment rate. Do not ask them to copy a McKinsey percentage. Do not grade the attack wording. Do not require a second human to mark the memo. The hostile card is a file in the pack, released when the memo exists, the way interviews are released now.

File 05 records what this costs and what to delete first.
