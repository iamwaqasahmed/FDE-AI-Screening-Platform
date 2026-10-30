# Tradeoffs, recommendations, and sources

This paper closes the dossier. It states the recommendation, the costs of accepting it, the costs of the alternatives, the deletions, and the sources a later editor can open. It assumes the evaluation, the industry survey, the architecture, and the exercise plan in the other files.

## Recommendation

Keep Module 2, Lesson 1 as a contract-hygiene lab on `rel-m02-l01`. Add two self-paced lessons, `rel-m02-l01a` and `rel-m02-l01b`, before Feeds. Build Alternative A from the architecture paper: FHIR R4 facade, SMART App Launch 2.2.0 code flow with S256 PKCE, server-side session ids, OpenID Connect `acr` and `max_age` for step-up, a local number-match mock shaped like the published Nafath steps, RelatedPerson plus Consent for the caregiver, and defensive fixture tests for the other patient’s chart. Leave OAuth 2.1, FAPI 2.0, and DPoP as optional advanced reading after the foundation check. Leave verifiable credentials, continuous evaluation, and FHIR R5 recurrence as a single experimental page with no check. Do not connect the lab to live Nafath. Do not grade the current paste blocks as evidence of identity engineering.

The thesis this serves: generating a client from a changed OpenAPI file is integration hygiene. Patient access needs the step-up, the grant, the object-level tests, and the facade.

## Tradeoffs of the recommended path

**Time against the classroom pair.** The understanding map puts score-the-proof and sign-in on one classroom day, and puts Feeds on the next pair. S1 fits the current day. S2 and S3 do not. Facilitators either extend the self-paced gap before Feeds or they drop Feeds later in the module and compress Lesson 3. The recommendation is to extend the gap. Feeds teach transport. Transport of referrals before the reader can bind a token to a patient teaches the wrong dependency. The cost is a longer Module 2 and a map edit. The cost of not paying it is a Module 4 access check that introduces delegation as if it were new, after the learner has deployed an assistant that could read by identifier.

**Gold stability.** Later tests call `write_m02_l01` and expect `m02_l01_gold.json` to carry the removed field, the live field, the roles, and the status row. New behaviour belongs on new release ids. The cost is two more packs and two more check commands. The benefit is that today’s green line keeps its meaning. Reusing `chk-auth` for step-up would make every existing passing work folder fail, including the solution copy, and would make the phrase “partial” in the finish chapter false in a new way.

**Facade versus direct HIS.** A facade adds a component the deploy lesson must eventually health-check. The current journey health already lists `his-wadi` and `iam`. Adding the facade as a dependency is honest and is another failure point. The benefit is that interface version 3 can change the HIS query name without teaching the chat process a new field list. The hygiene demo still shows the broken adapter, so the trap does not move into a slide.

**Assurance vocabulary.** Teaching IAL, AAL, FAL, and ISO LoA beside `loa-1` and `loa-2` adds words a mixed room did not ask for. The words chapter is already long. The benefit is that `loa-2` “checked against nid” stops being stored in the same column as a one-time code. A learner who only memorizes two bullets will pass S1 and fail S2’s must-mention list, which is the point. The mitigation is the map template: three rows, one weakest-phase sentence, no essay.

**National pattern without a national connection.** Some readers will want the real app, because the client is imagined in Saudi Arabia and the official service is the one hospitals’ patients already use. The tradeoff is pedagogical sharpness against a hard boundary. The published steps (request number, app confirmation, PIN, and a separate biometric path; an alternate Absher password plus OTP) are enough to see that authenticators differ in class. A live integration is not described as a student API on the pages fetched here, and it would collect real identifiers. The mock is less impressive and is the correct scope.

**Caregiver earlier than Module 4.** Lesson 3 already has a caregiver usability script. Module 4 grades expired grants and break-glass. Introducing Consent in S3 makes Lesson 3 a continuation and Module 4 a hardening pass. The risk is that S3’s simple period check is copied forward as if it were the whole of access governance. The mitigation is a sentence in the S3 finish chapter: break-glass, deletion, and the hidden attack set are a later module; this lesson only shows a grant period and a patient compartment.

**Self-paced load.** One person holds five hats across three lessons. That is the course’s existing rule, applied to more chapters. The risk is a reader who stalls on S2’s session code. The mitigation is the same as today’s shell: the check fails with a chapter pointer, `prepare_work` restores the starter, and the starter for S2 includes a failing session module with one function to replace, not a blank file. The course’s preference for modular files applies: session minting, cookie flags, facade policy, and HIS adapter stay separate modules so no function becomes the whole lesson.

## Tradeoffs of the other alternatives

**Alternative B, the Emerging profile,** buys sender-constrained tokens and a caregiver token that names both parties. It spends the reader’s attention on DPoP and pushed authorization requests. For a status read on a private-cloud mock, bearer tokens inside a backend that the browser does not script are enough to satisfy RFC 9700’s main lesson for this audience. FAPI 2.0 is the right citation when the booking write eventually crosses a high-value boundary. Doing it before the first correct session id inverts the difficulty. Offer it after S2’s foundation check, ungraded or graded only as an advanced slice that a simpler method is allowed to skip. The hardness note’s pattern is that advanced slices exist so a simpler method fails them. Use that pattern if Alternative B becomes a slice: a bearer token replayed from another client fails the DPoP slice; the foundation stays green without DPoP.

**Alternative C, the experimental reading,** costs one page and avoids a lab the rest of the course cannot maintain. The loss is currency. A 2027 reader may meet wallets and continuous evaluation in a vendor slide. The one-pager should say they are outside this assistant’s identity provider. Expanding them into a lab would create a second identity stack beside `iam`, which the design notes do not contain.

**Hygiene plus a paragraph** costs nothing and changes nothing. It is the right choice only if the course owner explicitly narrows the syllabus sentence to “adapt a client and open two pages.” The slides currently say to teach OIDC, roles, the assistant contract, and FHIR versions before the lab. The lab can carry roles and the contract. It cannot carry OIDC or FHIR versions while the identity file is two extension URLs and the record file is one query parameter. Either the slides shrink or the lab grows. This dossier grows the lab, in extra lessons, so the slides can stay true.

**Live Nafath** fails the fictional-record rule and the evidence rule. The sources describe user experience. They do not give this course a client registration. There is no partial version that “just uses a test national id.”

## Deletions

These are deletions from the taught design and from the graded path. They are not deletions of history from facilitator notes.

The graded paste blocks for sprint, states, token flow, and knowledge, as the identity evidence. Templates and a must-mention check replace them.

The claim that `x-issuer` and `x-token-endpoint` constitute a discovery document. A smart-configuration fixture replaces it.

The finished-state claim for a session id equal to the subject and a cookie equal to the subject. S1 may still show that row so the current check remains true. S2 treats it as the failing fixture `f-session`.

The learner-facing name FHIR v2 for a non-FHIR document. The HIS version and the FHIR release are named separately. The removed field stays hidden in learner-facing failure text.

The message-text scan as the booking authorization control. Step-up and “later day” become different results.

The facilitator line that this release’s `chk-auth` includes an expired delegate, unless a future editor actually adds that case to this check. The accurate line is the finish chapter’s word, partial, plus the status-only journey.

The instruction that every identity behaviour already in `auth.py` is out of bounds for the whole of sign-in. It stays out of bounds on S1. S2 and S3 have modules the learner is expected to change.

Nothing in this list deletes the demo, the canary, the service-token sign-in refusal, the cross-page refusal, the status tool, or the rule that booking does not complete.

## What to leave for later modules

HL7 v2 feeds, webhooks, and the clinic-session event stay on Feeds. Receipt timing and the caregiver usability script stay on Lesson 3, now able to cite `cg-a`. Deploy stays the first place a real `Secure` cookie on a private-cloud URL is probed. Ain stays file-only. Person matching across rows stays the data module. Break-glass, DPIA, and deletion stay Module 4. This split is a tradeoff against completeness. S3 will feel unfinished to a reader who wants the caregiver to book. That feeling is the same one the current lesson creates on purpose, and it should remain. The new lessons explain the gate. They do not open it.

## Proven, Emerging, Experimental, applied to the decision

Grade Proven behaviour: authorization code, PKCE S256, no implicit grant, no password grant, server-side session with regeneration and `HttpOnly`, FHIR R4 Patient and proposed Appointment, patient compartment, Consent period, service client refused as a patient, NIST’s three assurance families as vocabulary, ISO’s four-level scale and weakest-phase rule as vocabulary, Nafath’s published steps as a described pattern.

Offer Emerging behaviour after the foundation: SMART granular scope syntax beyond the two scopes the status app needs, FAPI 2.0, DPoP, token exchange for the caregiver, OAuth 2.1 as a draft to watch. The draft fetched here expires 7 March 2027, which is inside the case year. A lesson that treats it as stable will go stale on a known date. RFC 9700 is the stable security citation and already says 2.1 will incorporate it.

Mention Experimental behaviour once: verifiable credentials, continuous access evaluation, GNAP, R5 recurrence, SMART experimental endpoints. No fixture, no check, no must-mention.

## Risks if the recommendation is adopted badly

A facade that is only a renamed HIS path, still requiring `clinic` as a query string, would keep the naming problem. The Patient resource has to be a Patient resource.

A step-up that sets a column the learner edits by hand, with no mock confirmation, would recreate the paste problem. The number match has to be an event the runner performs.

A BOLA chapter that asks the reader to try identifiers until one works would cross the line this dossier set. Fixture ids, expected refusal, no hunting.

An assurance map that declares the cluster “NIST AAL2 compliant” or “ISO LoA3 certified” would overclaim. The map is a translation for a fictional provider. NIST is a US publication. ISO 29115’s detailed criteria are not reproduced here. Nafath is not a NIST deployment.

A dataset that imports Synthea’s default Massachusetts population would add US-census demographics and dozens of unused resource types, and would fight the canary. The hand-authored bundle is the dataset. Synthea is the citation for the method.

## Sources

All of these were opened while writing this dossier. Catalogue pages and standards previews are cited for what they state in public. Paywalled bodies were not reconstructed.

SMART App Launch 2.2.0, launch and authorization, including PKCE S256, `aud`, and `state`: https://www.hl7.org/fhir/smart-app-launch/app-launch.html

SMART App Launch 2.2.0, scopes and launch context, including patient, user, and system scopes and the statement that scopes do not replace underlying permissions: https://hl7.org/fhir/smart-app-launch/scopes-and-launch-context.html

SMART App Launch 2.2.0, conformance, including smart-configuration fields and the note that `associated_endpoints` is experimental: https://www.hl7.org/fhir/smart-app-launch/conformance.html

RFC 9700, Best Current Practice for OAuth 2.0 Security, BCP 240, January 2025, including the deprecation guidance on the implicit grant and the resource-owner password grant, and the statement that OAuth 2.1 will incorporate the BCP: https://www.rfc-editor.org/info/rfc9700/

OAuth 2.1 draft `draft-ietf-oauth-v2-1-16`, September 2026, expires 7 March 2027. Internet-Draft, not an RFC: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/

OpenID Connect Core 1.0, incorporating errata set 2, including ID Token claims, `acr`, `amr`, `auth_time`, and the note that ID Token expiry is not the session lifetime: https://openid.net/specs/openid-connect-core-1_0.html

FAPI 2.0 Security Profile, final, high-security OAuth profile following RFC 9700: https://openid.net/specs/fapi-security-profile-2_0-final.html

NIST SP 800-63-4, Digital Identity Guidelines, July 2025, IAL, AAL, and FAL: https://pages.nist.gov/800-63-4/sp800-63.html and the CSRC publication record https://csrc.nist.gov/pubs/sp/800/63/4/final

ISO/IEC 29115:2013, Entity authentication assurance framework, confirmed 2020. Catalogue abstract: https://www.iso.org/standard/45138.html The public preview used for LoA1–LoA3 characterizations and the weakest-phase rule is the sample hosted at https://cdn.standards.iteh.ai/samples/45138/31391aa0c87a48e192194661d81a0dbc/ISO-IEC-29115-2013.pdf The full clause text is not copied into this course.

HL7 FHIR Patient, normative since 4.0.0, current publication page FHIR 5.0.0: https://www.hl7.org/fhir/patient.html R4 reference for the facade fixture: https://hl7.org/fhir/R4/patient.html

HL7 FHIR Appointment, current publication: https://www.hl7.org/fhir/appointment.html R4 reference: https://hl7.org/fhir/R4/appointment.html

OWASP Session Management Cheat Sheet, entropy, cookie flags, regeneration, timeouts: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

OWASP API Security Top 10, 2023, API1 Broken Object Level Authorization, including the prevention paragraph used as the defensive-test objective: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

National Single Sign-On service, National Platform, SDAIA, Nafath application steps: https://my.gov.sa/en/services/119727

SDAIA Nafath platform user guide, including app number-match and the Absher password plus OTP path: https://sdaia.gov.sa/en/Services/ServicesGuidelines/SingleSignontoGovernmentPrivateServices.pdf

SDAIA biometric verification guide for the Nafath app: https://sdaia.gov.sa/en/Services/ServicesGuidelines/BiometricVerificationService.pdf

National Information Center, linked to SDAIA, including the digital-identity task: https://sdaia.gov.sa/en/Sectors/Nic/Pages/default.aspx

Synthea synthetic patient generator, FHIR R4 export, no real patient records. Method citation only: https://synthetichealth.github.io/synthea/ and https://github.com/synthetichealth/synthea

Course files this dossier treated as the system under study, not as external evidence: `course_design/module-02.md`, `course_design/slides/module-02-lesson-01.md`, `instructional/curriculum-understanding-map.md`, the Module 2 Lesson 1 student and solution copies, `problem_simulation/alwaha/engagement/m02_l01.py`, `problem_simulation/alwaha/check/auth.py`, `problem_simulation/alwaha/check/journey.py`, `problem_simulation/tests/test_m02_l01.py`, `problem_simulation/tests/test_m02_l01_checks.py`, `problem_simulation/design/08-live-services.md`, `problem_simulation/design/11-eval-and-hardness.md`, and `problem_simulation/design/traceability/module-02-trace.md`.

## Decision the course owner still has to make

Whether Feeds may open after S1. This dossier says no, except as an explicit syllabus cut that shrinks the slides. Whether new release ids are acceptable. This dossier says yes, because the current gold is a dependency. Whether the expired-delegate sentence in the hardness table is edited to point at S3 and at Module 4, or is implemented inside today’s `chk-auth`. This dossier edits the sentence and implements the case on `rel-m02-l01b`. Those three decisions are enough to start. The generator, the hidden field, and the two pages can stay exactly as they are while the decisions are made.
