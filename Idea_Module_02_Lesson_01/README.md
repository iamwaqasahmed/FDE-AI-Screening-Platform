# Module 02 Lesson 01 — research dossier

This folder is an independent curriculum proposal for Module 2, Lesson 1 (Sign-in, release `rel-m02-l01`). It does not replace the student copy, the solution copy, the facilitator slides, or the grader. No file outside this folder was changed. A facilitator can read it beside the live lesson and decide later whether to adopt any of it.

The lesson that exists today is a real piece of teaching. A learner leaves with a patient who can open `/chat`, a coordinator who can open `/console`, a SQLite session row, a status answer that still calls the Module 1 tool named `status`, and a sprint that puts client generation before booking. Booking does not happen. The checks `chk-auth` and `chk-journey` pass on that result, and the journey check is limited to the status question. Those facts are worth keeping. They are also smaller than the sentence the syllabus uses for the day: authentication for a patient-access assistant.

## Thesis

Generating a client from a changed OpenAPI file is integration hygiene. Patient access needs step-up authentication, caregiver delegation, broken-object-level authorization tests, and a FHIR facade over a versioned hospital information system.

The current lab does the hygiene well and the identity work on paper. `generate.py` scans the new `his-wadi.yaml` for lines that start with `- name:`, writes the first name into `FIELD`, and the hand-written client still sends `clinicCode`, which the new spec dropped in favour of `clinic`. The demo prints two lines and hides the field name. That is a sound contract-drift exercise. It is not SMART on FHIR, it is not OpenID Connect, and it is not a level of assurance in the sense NIST or ISO use. The identity note `loa.md` is copied into `knowledge.md`. The shell that actually signs people in is already finished in the packet, and the chapters tell the learner to leave `auth.py`, `session.py`, and `server.py` unchanged.

## What was read

Student chapters `00-background` through `08-finish`, the student README, the packet shell (`client.py`, `generate.py`, `auth.py`, `session.py`, `flow.py`, `his.py`, `contract.py`, `server.py`), `his-wadi.yaml`, `iam.yaml`, `loa.md`, and `fhir-v2.md`. Solution chapters `01-what-done-is` through `06-trainer`, plus the finished knowledge page. Facilitator sources: `course_design/module-02.md` Lesson 1, `course_design/slides/module-02-lesson-01.md`, `course_design/roles-and-delivery.md`, and `instructional/curriculum-understanding-map.md` (the Sign-in section and the classroom-day pairing). Grader sources: `problem_simulation/alwaha/engagement/m02_l01.py`, `problem_simulation/alwaha/check/auth.py`, `problem_simulation/alwaha/check/journey.py`, `problem_simulation/tests/test_m02_l01.py`, `problem_simulation/tests/test_m02_l01_checks.py`, and the design notes in `08-live-services.md`, `11-eval-and-hardness.md`, `10-release-schedule.md`, and `traceability/module-02-trace.md`.

External sources are limited to pages fetched for this dossier. The load-bearing ones are the SMART App Launch 2.2.0 authorization and scope pages, RFC 9700 (OAuth 2.0 Security Best Current Practice, January 2025), the OAuth 2.1 Internet-Draft `draft-ietf-oauth-v2-1-16`, OpenID Connect Core 1.0, NIST SP 800-63-4 (July 2025), the ISO/IEC 29115:2013 catalogue page and the public preview of that standard, the HL7 FHIR Patient and Appointment definitions, the OWASP Session Management Cheat Sheet, OWASP API1:2023 on broken object level authorization, the Saudi National Single Sign-On service page and the SDAIA Nafath user guide, and the Synthea synthetic-patient project. URLs are collected in `05-tradeoffs-recommendations-sources.md`. Nothing here relies on a blog paraphrase of those documents.

## What this folder does not do

It does not edit the course. It does not publish a new OpenAPI file into `packet/`. It does not weaken `chk-auth` or `chk-journey`. It does not tell a learner how to break an API. The authorization section describes a defensive test with two synthetic patients whose identifiers are already in the fixture: the cross-patient read must come back empty or refused. It does not describe searching for identifiers, scripting enumeration, or bypassing a control.

Nafath is described from the National Platform service page and the SDAIA user guide. The classroom mock must not call the live national service, must not ask for a national id or Iqama, and must not store a PIN. The pattern (a request number on the relying party, confirmation in a trusted app, then a PIN) is the teaching object. The national system stays outside the lab.

## How the papers divide the work

Read them in order.

`01-existing-lesson-evaluation.md` says what the live lesson actually teaches, what the checks actually grade, and where the facilitator design notes promise a delegate and a step-up that this release does not grade. It names what to keep, including the hidden-field demo, the service-token refusal, the status tool, and the rule that booking waits.

`02-industry-research.md` is the descriptive survey: SMART on FHIR, OAuth 2.0 as tightened by RFC 9700, OAuth 2.1 as a draft, OpenID Connect claims that carry assurance, NIST’s split of identity proofing, authentication, and federation, ISO/IEC 29115’s four levels and weakest-phase rule, the Nafath sign-on pattern, FHIR Patient and Appointment, server-side sessions, and object-level authorization as a test objective. Each technology is marked Proven, Emerging, or Experimental.

`03-redesign-architecture-and-simulation.md` puts those sources on the Al-Waha mocks. It specifies the facade, the session row, the step-up gate, the caregiver grant, the datasets, and the named failures. It compares three buildable alternatives and two that this course should not build.

`04-exercises-assessment-instruction.md` turns that architecture into self-paced chapters, new lessons, deletions from the current paste path, and checks that still fit a learner who holds all five hats. Booking still does not complete. Feeds still come after sign-in. The classroom pairing in the understanding map is treated as a constraint, not as a timetable.

`05-tradeoffs-recommendations-sources.md` records the costs, the recommended sequence, and the URLs.

## The change in one sitting

Keep a short hygiene prefix on `rel-m02-l01`: the v1 client fails, the generated client reads the referral, both pages open, the service token is refused, the Module 1 status tool answers, booking is refused. Stop treating that prefix as the identity lesson.

Add two self-paced lessons before Feeds, still with no clock:

- Assurance and the session. The session id is independent of the subject. A booking attempt at the opening assurance level is held with an explicit step-up result. A local mock plays the Nafath-shaped confirmation (number match, then a second factor) without a national id. The learner writes a one-page map from the cluster’s `loa-1` / `loa-2` onto NIST IAL, AAL, and FAL, and onto an ISO 29115 level, including the rule that the achieved level is the weakest phase.
- Whose chart. Two synthetic patients, one caregiver, one expired grant and one live grant. A FHIR R4 facade in front of the versioned HIS returns Patient and a proposed Appointment. A defensive test fails if patient A’s token can read patient B’s referral. The status question still uses the Module 1 tool after the facade read succeeds. No Appointment is moved to `booked`.

Feeds (`rel-m02-l02`) opens when the second lesson’s foundation check passes. Module 4 keeps the fuller delegate and break-glass grade. The early lesson is the first meeting with those ideas, so the later check is not a surprise vocabulary test.

## Self-paced rule

The live course already has no timetable. Chapters are numbered. Finish checks gate the next lesson. One person holds lead, AI or data, application, product, and architect. A later release can make an earlier choice incomplete. This proposal keeps that shape. It does not add a sprint clock, a cohort calendar, or a requirement that five people be in the room. “New lessons” here means more numbered student folders the same reader walks in order, after this lesson’s checks and before Feeds. Optional advanced chapters, where they exist, open only after the foundation check is green, which is the pattern the understanding map already uses on the data module.

The understanding map pairs `rel-m01-l05` and `rel-m02-l01` as one classroom day. Adding two lessons of substance means that pair can no longer be “score the proof, then also finish identity.” The recommendation is to let the proof-and-hygiene pair stay one sitting, and to let assurance and object-level checks be the next self-paced sitting, still before webhooks. That is a scope change for facilitators who planned Feeds on the same day. It is not a schedule.

## Maturity labels

These labels are used the same way in every paper.

**Proven** means a published specification or an operational practice a hospital integration team can be held to, with a stable document a learner can open. SMART App Launch 2.2.0, OAuth 2.0 plus RFC 9700, OpenID Connect Core 1.0, PKCE (RFC 7636), NIST SP 800-63-4, ISO/IEC 29115:2013, FHIR R4 Patient, server-side sessions as described by OWASP, and object-level checks as an API security test objective are in this class. Nafath as a national sign-on service is operationally proven. Wiring this classroom to it is not.

**Emerging** means a finished or late specification whose adoption in hospital patient access is uneven, or a draft the IETF itself says must not be cited as a standard. OAuth 2.1 (`draft-ietf-oauth-v2-1-16`, September 2026, expires 7 March 2027) is emerging. SMART’s granular `.cruds` scopes are published and still coexist with version-1 `.read` and `.write`. FAPI 2.0, DPoP (RFC 9449), and token exchange (RFC 8693) for a caregiver acting on behalf of a patient are emerging options for a later advanced chapter, not for the foundation check.

**Experimental** means a design this course should mention in a reading and should not grade. Verifiable credentials as the step-up, continuous access evaluation to revoke a session when a grant expires mid-conversation, GNAP, and FHIR R5 appointment recurrence are in this class for Al-Waha in 2027. SMART’s conformance page already marks `associated_endpoints` experimental; the lab should not depend on it.

## Datasets, failures, and deletions in short

The dataset is a tiny synthetic bundle, `ds-sign-in`, authored for the pack so the seed and the watermark stay deterministic. It holds two Patient resources, one RelatedPerson, two Consent resources (one expired), two Appointment resources in `proposed`, and the existing referral scenario. Synthea is the method citation for “synthetic, not real.” The pack does not download a population. National identifiers do not appear. The status scenario’s watermark stays in the packet and fails the check if it is copied into `work/`, as it does today.

Named failures the simulator should be able to show, each as a grader message that does not reveal the secret it is protecting: contract drift on the removed HIS field; a service client accepted as the patient; a cross-patient read that returns a chart; a booking attempt that skips step-up; an expired caregiver grant that still reads; a session id equal to the subject; a scope wider than the status task; an implicit-grant response type accepted by the mock; a custom issuer pair presented as if it were a discovery document.

Deletions, argued in the later papers: the graded paste of the booking sentence as the only assurance evidence; calling a line scan a generated OpenAPI client without saying so; calling `x-issuer` plus `x-token-endpoint` a discovery document; teaching `session_id = subject` and `alwaha_session={sub}` as the finished session design; the learner-facing name “FHIR v2” for a document that is not a FHIR resource; the booking gate that looks for the letters in the word “book”; the facilitator sentence that `chk-auth` already grades an expired delegate, unless the check is extended to do that.

## Who this is for

A course owner deciding whether Lesson 1 stays a contract lab. A facilitator who already knows the paste blocks and wants to know what a later editor must not “helpfully” add to the student pages (the understanding map’s warning about traps applies in reverse here: the trap is good; the missing identity work should be added beside it, not instead of the hidden field). A later author writing Feeds, who needs the word “session” to keep meaning a sign-in row on this lesson and a clinic session on the next. The learner does not receive this folder.
