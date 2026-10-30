# Exercises, assessment, and self-paced instruction

This paper turns the recommended architecture into lessons a single reader can walk, in order, with no timetable. The five hats stay. The checks stay outcome-based. Booking still waits. The paste blocks that currently are the identity lesson are deleted as graded evidence. The hygiene demo stays.

## Lesson sequence

Three self-paced lessons replace the idea that `rel-m02-l01` is the whole of sign-in. They are still one person’s work. A cohort that rotates hats does not need to be in the room. Feeds stay closed until the third lesson’s foundation check prints passed.

**Lesson S1 — The contract.** Same release id `rel-m02-l01`, shortened. Purpose: the HIS interface changed; a client pinned to the removed field fails; a client aligned with the spec reads the referral; the patient and the coordinator can open the assistant; the status tool answers; booking is not performed. This is today’s lab with the identity paste reduced to a pointer at the next lesson. Chapters stay numbered. Setup, the role, the words needed for the demo, the notice, the generator, the two pages, the finish checks. `chk-auth` on this lesson keeps today’s meaning and today’s name, and the facilitator map stops saying it includes a delegate. `chk-journey` stays status-only.

**Lesson S2 — Assurance and the session.** New folder, new release id proposed as `rel-m02-l01a` so `write_m02_l01` and its gold file stay stable for later tests. Purpose: the session id is not the subject; a low authentication class cannot pass the booking gate; a scripted number-match raises the class; the learner maps cluster words onto NIST and ISO levels. The status question still works. No Appointment is booked.

**Lesson S3 — Whose chart.** Proposed release `rel-m02-l01b`. Purpose: the facade returns FHIR Patient and a proposed Appointment; patient A cannot read patient B; an expired caregiver Consent cannot read patient A; a live Consent can; the integration client cannot. The Module 1 status tool still produces the pending sentence after the facade read. Booking remains a later day even for the high class and the live grant.

A course owner who will not add folders before Feeds can fold S2’s foundation into S1 and hold S3 as advanced chapters that open after S1’s finish check, required before Module 4 and recommended before Feeds. The recommended path is the three folders. Feeds move referral content. A reader who subscribes to webhooks before they can say which patient a token may read will treat authorization as a later patch. The understanding map’s classroom pair, proof then sign-in, can absorb S1. S2 and S3 are the next self-paced sitting. That is more work than the current evening. It is the work the syllabus line already names.

## Deletions from the instruction

Delete the graded paste of `sprint.md`, `states.md`, `token-flow.md`, and `knowledge.md` as the evidence of identity understanding. The current blocks are correct sentences. They are also the answer key printed above the check. A template with headings may remain. The learner writes the sentences after the shell run. The check looks for the presence of a claim the run made true, and a wrong claim fails without printing the expected level, as today’s knowledge miss already does.

Delete the words-chapter sentence that the issuer and token endpoint extensions are the discovery document. Replace it with a local smart-configuration fixture and a sentence that discovery is that document.

Delete the instruction to treat `session_id` equal to the subject as the finished row. The four names in today’s `COLUMNS` may remain on S1 so the current check stays green. S2 introduces the new columns and fails `f-session` if the id equals the subject.

Delete the learner-facing title “FHIR v2” for the HIS file. The notice can say “HIS interface version 2” and can say that FHIR R4 is the facade in S3. Facilitator notes may mention the old title so existing test names stay intelligible. Do not delete the trap. The hand-written client still sends the removed field. The demo still hides the name.

Delete the booking control that searches the patient message for the word “book” as the assurance mechanism. A regression test may keep a case whose text contains those letters and whose class is high, and may require that the later-day refusal still happens because booking is out of scope, not because the letters matched. The step-up result is reserved for the low class.

Delete the staff-role and service-token behaviour from the “do not edit” list only on S2 and S3, where the new modules are the ones the learner may change. On S1 the shell stays pre-built, which is appropriate for a contract lab.

Do not delete: the watermark rule, the closed `problem_simulation/build` folder, the solution-copy-after-pass rule, the five hats, the status tool, the approval left at `later`, the two-page server, the rule that a miss does not echo a secret, or the warning that Lesson 2’s `session.cancelled` is a clinic session.

## Lesson S1 exercises

The reader still does all five hats, and the hats are now matched to actions that are small enough to be real.

The lead writes `sprint.md` in their own words after reading the notice. The check requires a generate-or-align step before any booking sentence. It does not require the pasted paragraph. A one-line sprint fails if booking is first.

The application hat runs the generator, runs the demo, and opens both pages. They do not edit `auth.py`. They record the two demo lines on the worksheet the checks do not grade.

The AI hat runs the status question and confirms `tool_trace` contains `status`, `booked` is false, and the citation is present. They do not retune a model.

The product hat writes four states they observed: signed out, patient chat, staff console, booking refused. The booking row may say the reason is “later,” because step-up is the next lesson. The check looks for the patient, the coordinator, and a booking row that is not enabled.

The architect writes where the session row was written, naming the application database, and names `svc-integration` as a client that did not open a page. The deeper token story is S2.

Finish checks are today’s `chk-auth` and `chk-journey`, with knowledge reduced to two lines the learner composes: booking did not happen; the session row is in the application database. The `loa-2` substring moves to S2 so S1 does not grade a level the learner did not exercise.

## Lesson S2 exercises

Prior knowledge is S1’s green checks, the zones page, and the split between waitlist identity and sign-in identity.

The product hat drafts the state table again with two patient states: opened at the low class, and stepped up. The copy for a booking attempt at the low class is the step-up-required sentence the contract returns. The copy after step-up is still the later-day sentence. The hat is graded on whether a stranger can tell those apart.

The architect reads the local discovery fixture and writes `token-flow.md` with the authorization endpoint, the token endpoint, PKCE S256, and the session cookie’s `HttpOnly` flag. They write the assurance map: cluster `loa-1` and `loa-2`, NIST IAL versus AAL versus FAL, ISO’s weakest-phase rule, and a short description of the Nafath-shaped number match as the high-class authenticator in the mock. The page cites the National Platform and the SDAIA guide as readings. It does not include a national id. The check looks for the three NIST family names, the phrase that the overall level follows the weakest phase, and the words application database. It does not look for a pasted paragraph. A page that calls the two extension fields “the discovery document” fails `f-discovery`.

The application hat changes the session module and the sign-in handler. The new row uses an id the test can see is not the subject. Sign-in regenerates it. Step-up regenerates it again. The handler sets `HttpOnly`. The mock step-up endpoint shows a request code from the fixture. The runner submits it. The hat does not implement a password grant or an implicit response. A unit test in the pack rejects `response_type=token` via `f-implicit`.

The AI hat keeps the status tool on the low-class session. They add one assertion: a booking-intent message at low class does not add a book tool and does not set `booked`. They do not add a model.

The lead’s sprint puts discovery and session regeneration before step-up, and step-up before any booking write. The write itself stays in the later section.

Foundation check `chk-auth-stepup` runs `f-stepup`, `f-session`, `f-implicit`, and `f-discovery`. A miss does not print the expected `acr` value. Advanced, optional after the foundation passes: read the FAPI 2.0 abstract and answer, in `knowledge.md`, whether this client is public or confidential and where the access token lives. The expected answer for the foundation is a server-side session and a token that the browser script does not store. The advanced chapter may introduce DPoP as Emerging and must not be required for Feeds.

## Lesson S3 exercises

Prior knowledge is S2’s session and the Module 1 rule that a tool does not book from a sentence in a letter.

The dataset chapter asks the reader to open `ds-sign-in` and list resource types. They should find two Patient resources, one RelatedPerson, two Consent resources, two Appointment resources. They should find no national id. They should find both Appointments at `proposed`. A short `patients.md` names who may view `pt-a`: the patient, and the caregiver only while the live Consent’s period contains the case date. This is the product hat’s artifact.

The application hat implements the facade policy module: compartment check, Consent period check against the case clock, refusal of the integration client on patient reads, and a translation from the version-2 HIS referral to the status fields the contract already copies. The HIS adapter stays the generated client. The chat path calls the facade. `f-facade` fails a direct HIS call from chat.

The architect draws the zone crossing: browser to assistant, assistant to facade, facade to HIS, facade to consent. The integration client is on the facade edge and does not become the patient’s `sub`. The drawing is `token-flow.md` extended, not a new notation language.

The AI hat confirms the status tool still runs after a successful facade read, and that a cross-patient read does not call the tool with the other patient’s row. The citation remains the clinical source the contract names. They record that the model does not decide authorization.

The lead adds the object-level tests to the definition of done and sequences them before Feeds. The tests are provided as runners. The learner’s job is to make them pass and to watch one of them fail when they temporarily remove the compartment comparison. The temporary removal is a local edit they revert. The chapter does not ask them to craft a request against an unknown id.

Foundation check `chk-auth-object` runs `f-bola`, `f-grant`, `f-deputy`, and `f-facade`, plus the status journey so the Module 1 tool cannot be dropped. `f-scope` grades the architect’s scope sentence and the mock’s refusal to issue `patient/*.cruds` to this client. Advanced, after the foundation: the consent stale-cache switch, and a one-page note on token exchange as an Emerging way to carry caregiver and patient together. Module 4 remains the grade for break-glass and for the hidden attack set.

## Assessment rules

Checks stay automatic and secret-preserving. Written pages use must-mention lists computed from the world, which is the hardness note’s existing rule. Spoken readouts are out of scope until the module’s lesson 5.

Must-mention on S2: session id distinct from subject; regeneration at sign-in; `HttpOnly`; low class versus high class; IAL, AAL, and FAL as three selections; weakest phase; booking not performed. Must-not-claim: that the national service was contacted; that a national id was stored; that OAuth 2.1 is a published RFC; that the HIS query parameter is a FHIR Patient element; that the high class books a slot today.

Must-mention on S3: two patients; caregiver; expired grant refused; live grant allowed for view; service client refused on the patient read; Appointment status `proposed`; status tool still used. Must-not-claim: that unpredictable ids are a substitute for the check; that a SMART scope by itself authorizes every id; that the caregiver may book today; that patient B’s chart was shown.

Rubric for the prose, three levels, applied by the same style of must-mention grader the course already wants, not by a model judge. Foundation: the run is green and the page contains the must-mention items and none of the must-not-claim items. Missing either fails. Advanced: the optional chapter’s artifact exists and names the Emerging spec without making it a dependency of the foundation. There is no score for prose style.

The personal-world lab for the module stays at lesson 5. These lessons do not add `chk-individual`. A reader working alone is already the default.

## Self-paced mechanics

Each lesson’s background states the carry-forward from the previous finish, the five hats, and the rule that the next folder stays closed. Chapters are numbered. A failed check points at a chapter and does not reveal the gold string. `prepare_work` restores shells. The learner does not repair Python indentation by hand, which is the current recovery rule and should survive.

There is no hour estimate in the learner pages. Facilitator notes may say S1 is the current lesson’s length minus the identity paste, and that S2 and S3 are each a full sitting for a reader who is new to OAuth. Those notes are planning aids. They are not a clock in the student copy. A reader who passes S1 and pauses for a week resumes at S2 without a penalty. A later lesson may still invalidate a choice, as the background chapters already warn. If S3’s facade citation replaces a direct `his-wadi` citation, the journey gold for S1 should keep the old citation so S1 remains reproducible. S3’s gold carries the facade citation. Releases stay append-only, which is how `write_m02_l01` currently leaves earlier gold files alone.

Optional readings sit after the foundation check: RFC 9700 sections on implicit grant and password grant, summarized by the chapter in a few sentences plus the URL; the SMART scope page; NIST SP 800-63-4’s assurance-level section; ISO’s catalogue abstract; the Nafath service page and the SDAIA user guide; the OWASP session sheet’s entropy and cookie sections; the OWASP API1 page’s prevention paragraph. Experimental reading is the one page in the architecture paper. None of these readings are fetched live during the check. The packet may include a short excerpt only where the licence allows. NIST pages and RFC pages may be linked. ISO 29115’s full text is not copied into the packet. The learner’s map uses the preview’s published statements: four levels, weakest phase, and the LoA1–LoA3 characterizations the preview states. LoA4 is named as the top of the scale without invented criteria.

## What the learner leaves with

After S1: the current carry-forward, minus the claim that they engineered assurance. After S2: a session row that can survive a step-up, a map a DPO could read, and a booking gate that asks for a higher class and then still waits. After S3: a facade, two synthetic patients, a caregiver whose expired grant fails in public, and a status answer that still comes from the Module 1 tool. The next background, Feeds, can say those sentences and then define `session.cancelled` as a clinic session so the collision is explicit on the morning it matters.

## Instruction tone

Keep the current voice: one reader, concrete commands, failure table, solution closed until the finish chapter says the checks passed. Do not add a persona that role-plays an attacker. The defensive tests are runners with fixture ids. The chapter says what a red test means and which module to look at. It does not say how to craft a bypass. Caregiver is a product scenario the usability lesson already wanted, introduced here as a grant with a period, not as a story about deceiving staff.
