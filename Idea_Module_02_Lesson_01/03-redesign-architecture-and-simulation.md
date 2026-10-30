# Redesign: architecture and simulation

This paper specifies a simulation that can sit beside the current `rel-m02-l01` pack. It does not change that pack. The assistant still answers one status question with the Module 1 tool. Booking still does not write a booked appointment. The new machinery is a facade, a session store with its own identifier, a step-up gate, a caregiver grant, and a set of defensive checks. Three alternatives are specified far enough to build. Two further alternatives are specified far enough to reject.

## What the simulation is protecting

Al-Waha’s patient-access assistant runs in `zone-private` for `h-wadi`. `his-wadi` remains the system of record for the referral and, later, for slots. The assistant is a relying party. It should not hold the HIS dialect in the chat process as if that dialect were the clinical API. The identity provider remains the cluster `iam` mock. A national sign-on is represented only as a scripted confirmation inside that mock. The consent service from the live-services design, which already stores grants by patient and actor and can expire, becomes visible on this lesson in miniature. The integration client `svc-integration` remains a client-credentials principal. The canary stays in the scenario file and stays out of `work/`.

The status path is unchanged in outcome. A patient at the opening assurance level asks where the referral is. The facade reads the HIS through a versioned adapter. The adapter that matches interface version 2 succeeds. The adapter pinned to the removed field fails, and the demo may still show that failure without naming the field. On success, `contract.reply` records the tool `status`, cites the facade’s stable name, and copies count, state, and facility from the scenario. A message that asks to book does not book. The difference from today is the reason the gate gives. Today the gate looks for the letters of the word “book” in the message. In the redesign the gate looks at the session’s authentication class. A low class returns a step-up-required result and `booked` false. A high class, on this release, still returns “booking is a later day,” because the slot write is out of scope. The learner can see that assurance was checked and that the write still did not happen. String matching can remain as a regression the suite must not use as the control.

## Alternative A — Proven profile (recommended)

The facade exposes a FHIR R4 base, for example `/fhir/R4`, with Patient read and search, Appointment search, RelatedPerson read, and Consent read. SMART App Launch 2.2.0 is the authorization profile: authorization code, S256 PKCE, `aud` set to that base, scopes `launch/patient`, `patient/Patient.rs`, and `patient/Appointment.rs`. Staff use the same authorization server with OpenID Connect and a role claim, and they do not receive `launch/patient` for the console. The backend client uses `client_credentials` and a system scope that the facade’s policy refuses for patient-compartment reads. This matches SMART’s statement that system scopes are limited by client policy, and it matches the existing design sentence that the passing read uses the patient token.

The HIS stays behind the facade with two adapters. Version 1 sends the removed field and is the failing demo. Version 2 sends `clinic` and is the live adapter. The OpenAPI files remain the adapter contracts. A small generator may still emit the version-2 client that the adapter uses internally. The chat process calls the facade, not that client. Learners who only need hygiene run the generator and the demo. Learners who are on the identity lessons never edit the HIS client as their main task.

The session row lives in SQLite, still the application database, not in `his-wadi`. Columns: `session_id` (random, at least 64 bits of entropy, not equal to `subject`), `subject`, `role`, `aal` (the authentication class of this session), `ial` (the proofing class recorded for the subject, which does not rise during the session), `auth_time`, `expires`. The cookie is `HttpOnly`, `SameSite=Lax`, and `Secure` when the page is served on HTTPS. The local HTTP lab on 127.0.0.1 may omit `Secure` only if the check’s fixture says so, and the knowledge note must say that the deployed cookie in `zone-private` sets `Secure`. Regeneration happens at sign-in and again when step-up succeeds. Idle timeout is short enough to observe in a test by moving the case clock, which the cluster already has. Absolute timeout is recorded and not left infinite.

Step-up is an OpenID Connect transaction. The opening login yields an ID Token whose `acr` is the low class, mapped in a local note to the cluster word `loa-1`, to NIST AAL1, and to an ISO 29115 level no higher than LoA2. The subject’s proofing note may already say the national-id check has not been done. When the patient asks to book, the assistant calls the authorization server again with `max_age=0` and an essential `acr` for the high class. The mock does not perform cryptography beyond what the fixture needs. It displays a two-digit request code and expects the learner’s client, or the scripted runner, to submit that same code plus a second-factor flag. That is the Nafath-shaped confirmation: number match, then a PIN-equivalent flag, with no national id field on the form. Success writes a new session id, a new `auth_time`, and the high AAL. The IAL moves to the higher class only if the fixture says this subject was proofed, which is the “checked against nid” idea expressed as a proofing event the mock has already recorded, not as a number the learner types. Failure leaves the old session and returns step-up required. Booking remains a later day even after success.

Delegation uses RelatedPerson and Consent in the bundle. The caregiver’s session has their own subject. The Consent names the patient, the caregiver, the scope `view`, and a period. The facade allows a Patient read when the caller is the patient, or when the caller is the caregiver and the Consent period contains the case-clock time. An expired Consent refuses. A book scope is present on a second Consent so the product page can say the grant exists, and the facade still refuses to create an Appointment, because booking waits. Token exchange is not required in this alternative. The server compares session subject, patient id, and Consent. An advanced chapter may add RFC 8693 later.

Object-level tests are part of the pack, authored as expected outcomes. They are described in the exercises paper. The simulator’s job is to make the wrong policy fail those tests and the right policy pass them, without printing the other patient’s identifier in the failure text.

This alternative reuses `chk-auth` and `chk-journey` only if their pass meaning is versioned. Safer: keep today’s checks green on the hygiene prefix, and add `chk-auth-stepup` and `chk-auth-object` for the new lessons. The hardness table can then stop claiming that `chk-auth` on `rel-m02-l01` already includes an expired delegate.

## Alternative B — Emerging profile

Alternative B keeps the facade, the session row, the two patients, and the Consent period from Alternative A. It changes the token profile toward specifications that are real and not yet the default in a typical hospital portal.

The authorization server follows RFC 9700 and is configured as a subset of FAPI 2.0: confidential client only, pushed authorization requests, and sender-constrained access tokens via DPoP. The browser never sees the access token. A small backend-for-frontend holds it, which is also what the OWASP session sheet prefers over `localStorage`. Step-up still uses `acr` and `max_age`. The caregiver path uses token exchange so the HIS adapter receives an actor token that names both the caregiver and the patient. OAuth 2.1 is the reading target, not the graded target, because `draft-ietf-oauth-v2-1-16` expires and is not an RFC. The graded wire captures are RFC 6749 plus RFC 9700 plus the FAPI features the mock actually implements.

This alternative is the right advanced chapter for architects who will meet national or financial-grade gateways. It is the wrong foundation for a room that includes readers who are not application engineers. DPoP and pushed authorization requests add moving parts before the learner has a stable picture of patient context. The simulation cost is a second token endpoint behaviour and a proof-of-possession check the status tool does not need. Recommend it as an optional chapter after Alternative A’s foundation check is green, in the same self-paced way Module 3 opens advanced files after the finish check.

## Alternative C — Experimental reading, not a lab

Alternative C replaces the step-up mock with a verifiable credential the patient presents, or with a continuous-evaluation event that revokes the session when Consent expires mid-chat. Both are legitimate research topics. Neither is how `iam` is described in this course, and neither is how the Nafath user steps are published. A verifiable-credential lab would invent an issuer, a wallet, and a presentation the rest of the modules never reuse. A continuous-evaluation lab would grade event delivery that Lesson 2 is supposed to introduce with webhooks. FHIR R5 Appointment recurrence and SMART’s experimental `associated_endpoints` fall in the same bin: available to mention, not available to require.

The experimental paper the learner may read is one page: these designs exist, they are not this release, and the foundation remains authorization code, server-side session, and a Consent period checked at request time. No check goes red because a learner skipped the page.

## Alternatives to reject

**Hygiene plus a paragraph.** Keep `generate.py` as the climax and add a SMART definition to the words chapter. The checks stay substring checks on `loa-2` and `database`. This preserves the green path and leaves the thesis untouched. The design notes will continue to promise a delegate the grader does not see. Reject it as the destination. The hygiene prefix may remain as the first hour.

**Live Nafath.** Redirect the sign-in button to the national service. The official service is for individuals using government and private platforms. This repository is a training simulation with watermarked fictional records. A live redirect would ask real people for real identifiers. The published pages do not provide a student client id. Reject it. The number-match mock in Alternative A is the furthest the lab should go.

## Datasets

The pack ships `ds-sign-in`, a single FHIR R4 Bundle authored by the course, not a Synthea population download. Synthea is the method reference: synthetic patients, FHIR R4 export, no real person’s record, seedable runs. The course already depends on deterministic seeds and a per-profile canary. A generated population would fight both. The bundle is small enough to read aloud.

Contents, all fictional, all free of national ids:

- `Patient/pt-a` and `Patient/pt-b`, each with an MRN identifier in a system URI under the fictional cluster, an active flag, and a name that does not match a real patient. No photo, no address, no phone.
- `RelatedPerson/cg-a` linked to `pt-a` with a caregiver relationship code drawn from the FHIR valueset, named as a role, not as a biography.
- `Consent/grant-live` for `cg-a` on `pt-a`, scope view, period covering the case date 17 January 2027.
- `Consent/grant-expired` for the same pair, scope view, period ended before the case date. The defensive test uses this row. The live grant is the passing row. They are different Consent ids so the learner does not edit a date in place to cheat both tests.
- `Appointment/ap-a` for `pt-a` with status `proposed`. `Appointment/ap-b` for `pt-b` with status `proposed`. Neither is `booked`.
- The existing referral scenario row, still outside the Bundle if the watermark must stay in `status.json`. The facade joins `ref-status` to `pt-a` inside the hidden gold, not inside the learner-visible letter field.

Actors in the identity fixture, extending today’s list rather than replacing the patient and the coordinator:

- Patient A at low AAL, subject distinct from the session id the store will mint.
- The same patient after the scripted step-up, high AAL, proofing flag set in the fixture.
- Caregiver, subject `cg-a`.
- Coordinator and the other staff roles already in `loa.md`.
- Service client `svc-integration`.
- A foreign role, as today’s check already uses.

The request-code fixture is a pair of two-digit codes. One is the code the mock displays. One is a decoy. The runner submits the displayed code. The file does not contain a PIN, a national id, or a biometric sample. Profiles `practice` and `small` differ by canary and by the status count, as they do now. They share the same clinical story so the lesson text stays stable.

A learner who wants more FHIR volume may be pointed at Synthea’s documentation and at the public SMART developer sandbox as optional reading. Those corpora are not copied into `packet/`. They include far more resource types than this lesson grades, and a US census demographic default is the wrong population story for Al-Waha even though the records are synthetic.

## Named failures

Each failure is a switch or a fixture the grader can select. The message names the class of miss and does not name the other patient, the removed field, the canary, or the assurance string the learner was supposed to write.

`f-contract`. The HIS adapter sends the removed field. The read fails. The facade’s Patient read is not attempted. This is today’s demo, kept on the adapter.

`f-deputy`. The status call is made with the integration client. The facade refuses. The patient-token call for `pt-a` succeeds. Today’s sign-in refusal of the service token remains. This failure adds the read path the design note already describes.

`f-bola`. Patient A’s token, patient B’s referral or Appointment id, both ids from the fixture. The response is a refusal or an empty search. The body must not contain patient B’s MRN. The swapped call, patient B reading patient B, succeeds. Removing the compartment check turns the test red.

`f-stepup`. A booking-intent call on the low-AAL session returns step-up required and does not write an Appointment. After the scripted number match, the same intent returns the later-day refusal and still does not write `booked`. A regression that treats any non-empty `loa` as permission to book fails `f-stepup`.

`f-grant`. The caregiver session with `grant-expired` reads `pt-a` and is refused. The caregiver session with `grant-live` reads `pt-a` and succeeds. The caregiver reads `pt-b` and is refused. The expired grant must not be repairable by a stale cache; if the consent service’s stale-cache switch from the live-services design is turned on, the test expects the facade to consult the current period, not the cache. That switch can wait for the advanced chapter so the foundation stays one defect at a time.

`f-session`. A store that sets `session_id` equal to `subject` fails. A cookie that lacks `HttpOnly` fails when the test inspects the local server’s `Set-Cookie`. A second sign-in that keeps the old session id fails the regeneration check.

`f-scope`. A client that requests `patient/*.cruds` for the status app fails the scope note. The permitted set is Patient read and Appointment read. This is a written artifact plus a fixture the mock grants. The mock refuses to issue the wider set to the status client.

`f-implicit`. A client that sends `response_type=token` is rejected by the mock. The failure message says the implicit response type is rejected. It does not explain how to intercept a fragment.

`f-discovery`. A token flow page that only names the two extension URLs, and a client that does not read `authorization_endpoint` and `code_challenge_methods_supported` from the local smart-configuration fixture, fails the architect check. The fixture is a file in the packet, served at a path on the mock.

`f-facade`. A chat process that calls the HIS path directly, skipping the facade, fails the journey even if the body keys match version 2. The status citation is the facade. The adapter log may show the HIS call. The learner-visible contract is FHIR.

These failures are deterministic under the case clock and the profile seed, consistent with the fault-switch rule already written for Module 2 contract tests.

## How this sits with later lessons

Feeds still own webhooks, HL7 v2 messages, and `session.cancelled` as a clinic session. The sign-in session id must not be reused as that event’s identifier. The facade’s Appointment search returns `proposed` only, so Lesson 2 does not inherit a booked slot. Lesson 3’s caregiver usability script can use `cg-a` and the live grant, which means the script stops being the first time the word caregiver appears. Lesson 5 still must not promise a live slot at Ain. Module 4 still grades break-glass, deletion, and the hidden attack set. The early object-level tests are positive and negative fixtures, not that attack set. Module 3’s person-level identity work is untouched: two Patient resources are two people here, and a mother and a newborn are not introduced.

The simulation’s modularity follows the current shell. One module mints sessions. One module decides chat versus console. One module is the facade policy. One module is the HIS adapter. One module is the status contract. `generate.py` stays on the adapter side. None of these modules need to know Nafath’s name. The assurance note maps the mock’s classes to the national pattern in prose. The code sees `aal` values.

## Maturity of the simulation itself

Alternative A is a Proven composition: each part has a stable specification, and the composition is ordinary integration work. Alternative B is Emerging because FAPI 2.0 and DPoP are specified and heavier than the foundation. Alternative C is Experimental and stays a reading. The rejected pair are not maturity levels. They are mismatches with the thesis or with the rule that this course uses fictional records.
