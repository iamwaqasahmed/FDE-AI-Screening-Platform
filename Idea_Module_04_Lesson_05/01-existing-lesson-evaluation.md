# 01 — Existing lesson evaluation

Release `rel-m04-l05`. Student title: The proposal. Facilitator title: Integration and the proposal. Curriculum-map title: Connect, and propose. The three names already show the compression. This evaluation reads the student chapters `00` through `09`, the solution chapters and the worked `work/` files, `course_design/module-04.md`, `course_design/slides/module-04-lesson-05.md`, `instructional/curriculum-understanding-map.md`, `course_design/assessment-map.md`, `course_design/roles-and-delivery.md`, `problem_simulation/design/traceability/module-04-trace.md`, `problem_simulation/design/10-release-schedule.md`, the check modules, `m04_l05_rules.py`, and `problem_simulation/tests/test_m04_l05.py`.

## What the lesson claims

`course_design/module-04.md` assigns three syllabus outcomes to this single lesson.

1. Integrate AI applications with enterprise platforms, authentication services, databases, messaging systems, and business applications.
2. Design production-ready architectures that are secure, reliable, and maintainable.
3. Prioritize use cases by business value, technical feasibility, implementation effort, and organizational impact, then produce a roadmap, an execution plan, and success metrics.

The objective sentence is narrower and better: HR leave cancels a session, the contact center receives a handoff, and `rcp/proposal.md` can be presented. Concepts named for teaching before the lab: remaining integrations, stage gate G4, adoption, success metrics. The trace file adds an advanced layer the student lab does not run: `int-engine` bridging HL7 and FHIR, a schema registry, insurance, and a document-management change feed. The lesson's own advanced layer, in the module note, is "schema-registry tolerance" and "the phone-only adoption channel."

Roles, from `roles-and-delivery.md`: the lead reads out; the AI engineer brings success metrics; the application engineer owns the contact-center handoff; the product manager owns ranking and roadmap; the architect owns both architecture documents. The student background says one person holds all five. That constraint is real and should stay.

Assessment placement: `rcp/proposal.md` is scored by `chk-m04-l05-rcp` inside the discovery and architecture components as rehearsal practice. It is not the later 25 percent Real Client Project. `chk-readout` sits in the 10 percent executive-communication component. The map says that check uses a facilitator sheet filled during steering. The self-paced path grades `readout.md`, `retro.md`, and `knowledge.md` instead. The module-4 individual lab on the assessment map is "one attack from the dev sample that the guardrail stops." Lesson 5 is where that lab is wired, as `personal.py`.

Prior knowledge the map requires: every earlier week; `p-clock` first in the finished ranking; identity as the dependency of the waitlist; the value model; the requirements from Module 3 Lesson 5; the drill from Lesson 4. The proposal's client remains Al-Waha. A later real client is out of these folders.

## What the learner actually does

Chapters 00 through 04 are reading, a demo, and two interviews. Chapter 03 walks twenty pack files. The chapter also prints the file contents, so the walk is a search for a token (`connected`, `cc`, `evt-extra`, `call-empty`, `published`, `referred_at`, `p-triage`, `phone-only`, `clinical-safety`, `G4`, `twice`). The interesting facts are already on the page: one handoff summary is empty; leave `entered_at` is after `published_at`; `p-triage` carries blocker `pol-clinical-safety` and `p-clock` does not; the readiness skew is `phone-only` at `phc-rim`; the clinical-safety cell is empty at gate G4; steering asks which benefit is counted twice.

The demo command prints one line, `Which benefit is counted twice?`, and withholds the answer. The interviews then give the operational answers in the clear. The access manager says a handoff with no summary is not a handoff. The enterprise architect says leave entered after publish creates `session.cancelled`, and the warehouse feed is the BI mart. Chapter 08 pastes those sentences into the notes the integrate check reads.

Chapters 05 through 08 are replacements. The sprint paste is an eight-step order: requests, sign-in, bus, handoff, leave, warehouse, ranking, proposal. Chapter 06 pastes the filled `signin`, `bus`, `handoff`, `leave`, and `warehouse` modules and their tests. Chapter 07 pastes `rank`, `gates`, and `personal`. Chapter 08 pastes the deployment architecture, the operations plan, the proposal, the readout, the retro, and both interview notes. The proposal paste is the text that later appears in `Solution_Copy/work/rcp/proposal.md`. The search instruction under that paste is the check: find `Al-Waha`, then `not the value model`, then `p-clock`, then `same calls`, then `site-b`, then `phone-only`. Chapter 09 runs five checks. The local suite is eight unit tests that match the pasted fixtures.

A learner who follows the paste instructions passes. A learner who writes a sharper handoff briefing, a ranked portfolio with effort and feasibility, or a benefits register with a baseline and a target will fail unless the required tokens also appear in the required sections.

## What each check actually scores

### Integrate (`chk-m04-l05-integrate`)

Staff sign-in: `kind == staff` is accepted; a service actor must not come back as staff. The pack row is `svc-integration` with role `admin`. The defect is real: a machine identity sits in the staff directory. The function does not look at audience, expiry, step-up, or whether this actor may cancel a session. Authentication as an enterprise topic was Module 2 Lesson 1. This lesson confirms a role bit after the drill.

Bus: an event with a field outside `{id, session, topic}` must be kept, and every `session.cancelled` must be kept. That is Postel's rule plus "do not drop the one event this consumer exists to see." It is not a schema registry. There is no second version, no compatibility mode, and no consumer contract shared back to a producer.

Handoff: a non-empty `summary` must be copied and must not be refused; a blank summary must be refused and must not carry an agent id or an invented summary. The pack has two calls. One summary is "Referral status, still pending." The other is empty. The check never asks whether the non-empty summary tells a human what the caller wants, what was already tried, what is unresolved, or which referral it is. A twenty-second briefing and a one-line subject pass the same way. The product failure the thesis names is invisible to the grader.

Leave: the first leave row, applied to a session built from that row, must return status `cancelled` and event `session.cancelled`. Those are two misses, and the lesson is right to keep them apart from the knowledge-file miss. The reference function in `m04_l05_rules.py` also refuses a different consultant and a leave entered before publish. The graded pack has one row, so those negatives are ungraded. There is no duplicate delivery, no appointment already in `arrived`, no patient notification, and no slot released. The trace's HL7/FHIR bridge is not in the lab.

Warehouse: `clock` must return `referred_at`, not `booking_date`. This is a measurement definition stuffed into an integration function. It matters because a wait metric that starts at booking hides the queue the proposal claims to attack. The lesson never asks the learner to use the clock inside a metric.

Notes and sprint are graded on this check too: access-manager notes must contain the word summary; architect notes must miss neither leave, `session.cancelled`, nor `bi`; `sprint.md` must open with the requests. Gold is unused. A lag or a count is not printed. That restraint is worth keeping.

### Operations (`chk-m04-l05-ops`)

`architecture-deploy.md` passes when Zones contains `zone-private`, `zone-hospital`, and `zone-public`; Flows contains `cc`, `bi`, `hr`, and `bus`; Boundary contains "clinician" and "urgency". The solution text does that in nine lines. It does not show a failure mode, a data class, or what happens when `site-a` is dead (that was Lesson 4). `operations.md` passes when Owners and Incident are non-empty, RACI contains `med-dir`, and Gate contains `g4` and `checklist`. `gates.evidence` must return `{cell: med-dir, gate: G4}` for the go-live item. Any other gate leaves the cell blank, but the graded item is the G4 row.

G4 in `gates/stage-gate.md` is the course's own go-live gate, one of G0 intake, G1 risk tier, G2 DPIA, G3 pilot, G4 go-live, G5 post-launch. Those names are a teaching sequence. They are not the UK government's gateway review numbers. Teaching them as if they were an external standard would be a false claim. The empty clinical-safety cell is the right defect. Filling it with the string `med-dir` is the whole of the evidence. A go-live pack would also name residual risk, rollback, who is on call, and who owns the benefit after the team leaves. None of that is scored.

### Proposal (`chk-m04-l05-rcp`)

Section rules, from the check:

- Client must contain "al-waha".
- Ranking must contain "not the value model" and at least one dependency pair (`p-waitlist`/`identity`, `p-dna`/`identity`, `p-status`/`identity`, or `p-bounce`/`criteria`).
- Roadmap's earliest problem id must not be empty, `p-triage`, or `vendor-bot`.
- Metrics must contain `site-b` and some problem id, and must not contain the digits `70`.
- Plan must contain "same" and "call", which the solution satisfies with "the same calls".
- Adoption must contain `phone-only`, `phc-rim`, and `readiness`.
- A banned sentence fails the document.
- `rank.first` must return an id in the open-id list. The open list is every row whose blocker list is empty, in file order. The first is `p-clock`.

The syllabus asked for value, feasibility, effort, and organizational impact. The code sorts on none of those. The dot-vote disagreement is a sentence the chapter tells the learner to paste. The double count is the word "same" beside the word "call", not a reconciliation of two ledger lines against one stream of calls. Success metrics "you measured" means "name `site-b` and a problem id, and do not type 70." `test_m04_l05.py` keeps a phone-only count and the benefit answer out of the lesson pages. The check then cannot see a measured baseline, because no baseline is allowed to appear as a number the page might leak. The authoring constraint and the learning goal are in conflict, and the keyword check resolves it by dropping the measurement.

### Readout (`chk-readout`)

The readout must mention a clinician and urgency, keep patient data off the external model, fill gold sections (ranking with a real first problem and a dependency, handoff summary, `session.cancelled`, the double-counted benefit, the phone-only channel), keep an ask log, and cite a source. `knowledge.md` line 1 must contain `session.cancelled`. Line 2 must open on a problem other than `p-triage` and `vendor-bot` and must mention a dependency. Retro needs Keep, Drop, and Open. The solution readout is a heading plus one sentence per question on `steer-m04-l05`. The steering card is five questions. The chapter pastes the five answers. The assessment map's facilitator sheet is not what a solo learner experiences.

### Individual (`chk-individual-m04-l05`)

`personal.stop` blocks family `atk-direct` and never sets `booked`. The attack wording stays in the pack and must not be copied. As a regression of Lesson 1, the idea is sound: a direct attack still must not book on the last day. As the capstone's individual evidence, it does not touch handoff quality, leave, benefits, or the proposal. It consumes one of the six pastes in chapter 07.

## The traps are the lesson's best design

Two traps are named on the slide: a roadmap that starts with `p-triage`, and a handoff with no summary. The release schedule adds cancellations that ignore consultant leave. The miss list in chapter 00 is longer and mostly right as a defect catalogue: service token accepted as staff; bus drops an unknown field; bus misses `session.cancelled`; late leave leaves the session published; leave emits no cancel; warehouse clock starts at booking; ranking follows the dot-vote; metrics were not measured; adoption misses phone-only; the two savings are treated as separate; urgency leaves the clinician; patient data rides `ext-large`.

**Proven** as teaching problems. Each one is a false move a team on this engagement can actually make. Clinical urgency stays with a clinician. The sponsor sentence (an AI front desk that books, reschedules, answers, and chases, live before Ramadan) is not the plan. `p-triage` stays blocked. Identity remains the dependency of the waitlist. Ain stays on a nightly file. Those boundaries are the course's accumulated judgment, and the proposal is where they should be defended.

The failure is the path. Chapter 00 lists the miss sentences. Chapter 03 shows the rows. The interviews speak the rule. Chapter 07 states that `first` returns `p-clock` and that `evidence` names `med-dir`. Chapter 08 pastes the proposal that already reconciles the two savings. The demo asks the finance question and the paste answers it. A trap that includes its own answer key does not trap.

## Where the thesis holds

The capstone compresses four practices into one paste day.

**Contact-center integration.** The learner confirms a handoff function. They do not sit with a call, decide assist versus containment, or write the briefing a coordinator reads before they speak. The access manager's second answer, in chapter 03, says a large share of calls are people asking for referral status. That is a demand fact. It never becomes a measured baseline in the metrics section. The metrics paste says "`p-status` is a measured contact-center demand" without a measure.

**HR events.** One comparison of two timestamps, same consultant, status cancelled, topic `session.cancelled`. The scheduling consequence (slot freed, patient told, duplicate event ignored, in-progress visit left alone) is absent. The course's own reference code knows two negative cases the grader never feeds.

**Operations.** Zone names, four flow tokens, a boundary sentence, an owner line, `med-dir`, and the word checklist. Lesson 4 already drilled failover. This document does not absorb that drill into an operating picture. Incident is "the Lesson 2 replay" plus a dashboard list.

**Executive proposal.** Six headings, about twenty lines, every load-bearing phrase supplied by the chapter. No benefits register, no baseline, no target, no owner of the benefit after exit, no optimism check, no sensitivity, no "what would falsify this." The Working Backwards press release and the Amazon narrative, opened in file 02, are both harder than this page, and both are still shorter than a business case. The gap is evidence, not length.

Adoption is one channel sentence: phone callback for phone-only patients at `phc-rim`, because the readiness file says so. There is no owner who will place those calls after the forward-deployed engineer leaves, no script, and no distinction between patients who cannot use the app and coordinators whose job is the app. GDS assisted digital, opened for file 02, is the analogue for the patient side only.

## What is already strong

The pack discipline is strong. Interviews have scripts. The demo withholds the answer even though the paste later reveals it. Counts and the attack text stay out of chapters, and `test_m04_l05.py` enforces that. Miss sentences are specific and are not collapsed when two failures travel together (bus pair, leave pair, gates pair). The clinical boundary is on the readout and on the architecture. The proposal cannot change client. The ranking helper and the prose roadmap can disagree, and both are checked, so a prose claim that opens on `p-clock` with a helper that still returns `p-triage` fails. That split is worth keeping when the helper stops being "first unblocked row."

The solution copy is an example, and its readme says wording can differ when the behaviors hold. The checks are stricter than that sentence. Wording can differ only inside a section that still contains the tokens. A reviser who believes the solution readme will be surprised by `rcp_m04_l05.py`.

Self-paced instruction is explicit: one person, five hats, `work/` only, packet left closed, solution closed until checks pass. The chapter machinery (picture versus paste, search the saved file, do not repair indentation by hand) is careful about a failure mode this course has clearly hit. It is also how the answer key is delivered. The instructional problem is not that the steps are fussy. The problem is that the steps replace the judgment.

## Syllabus lines with no practice

| Claim | What is practiced |
| --- | --- |
| Authentication services | A kind flag on two actors |
| Databases | A warehouse row's date field |
| Messaging | Keep unknown fields; keep one topic |
| Business applications | Copy a summary; cancel on a late leave |
| Value, feasibility, effort, impact | File order among unblocked ids |
| Success metrics the team measured | `site-b` and a problem id; digit ban |
| Adoption | Three tokens and the words "phone callback" |
| Schema-registry tolerance | One extra field on one event |
| HL7/FHIR bridge | Named in the trace, absent from the lab |

**Proven** keep: the defect list, the clinical boundary, the blocked triage problem, the referral clock as a definition, the service-versus-staff split, the two-part leave miss, the author rule that hides seed counts. **Emerging** inside the current course: using a keyword rubric as a stand-in for a steering conversation. It is reliable and gameable. **Experimental** relative to the syllabus: claiming enterprise integration and a full prioritization method from these eight short functions.

## Implications for a redesign

Grade the decision the learner makes from the pack, not the paragraph the chapter supplies. Move the attack lab off the critical path of the proposal or keep it as an ungraded regression. Feed the leave function the negative rows the reference code already understands. Score a handoff on a fielded briefing, and score a proposal on citations to measurements that exist in the pack under ids, so the lesson can still avoid printing a bare count in prose. The next file records the external practice those changes should follow. The structures are in file 03.
