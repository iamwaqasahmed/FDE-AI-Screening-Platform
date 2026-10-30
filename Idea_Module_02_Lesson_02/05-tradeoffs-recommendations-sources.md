# 05 — Tradeoffs, recommendations, and sources

## Recommendation

Rebuild `rel-m02-l02` in place. Keep `chk-journey`, the secret-hiding style, the synthetic generators, the five roles, and the rule that the mart figure is not the desk's number. Replace the paste climax with three graded artifacts: an integration decision (webhook inbox versus CDC versus snapshot), a loss record for the HL7 translation, and a data contract whose time anchor is honest about `p-clock`.

The alternative — a new lesson inserted before Lesson 3 — costs a release id, a curriculum-map edit, and a second setup chapter, and it leaves the current paste in the path so students still "learn" feeds by transcribing `cancel.py`. In-place rebuild is the smaller change to the story and the larger change to the pedagogy. Prefer it.

## Deletions

Delete these. They are in the student path today, and they work against the thesis.

| Delete | Why |
| --- | --- |
| The finished `intake.py`, `cancel.py`, and `mart.py` blocks in chapters 06 and 08 | The lab is transcription. The crash window and the contract never get written by the student |
| "Paste the block again" as the recovery path | It confirms the answer key lives in the chapter |
| Chapter 08's sample data row, including the wait cell | The checker hides the figure. The chapter publishes one profile's number |
| The sentence that the date column *is* the clock, with no bias clause | It grades the student for endorsing the biased anchor |
| `letter` as a required registry field that the code then strips | It confuses the canary with the contract. Keep the canary out of band |
| Ungraded `feed-lines.md` as the only HL7 activity | Sequence order is the point, and an ungraded scratch file does not make it |
| A WhatsApp definition that omits 24 hours, who opens the window, and "accept is not delivery" | The public rule is specific. The packet is vaguer than Meta's page |
| `rebooked` as a patient state the worker never stores, unless it is marked as copy | Two vocabularies with no map |
| `dms.md` as "not today's check" with no other sentence | It invites a false identity between the document feed and CDC. Replace with one sentence that separates them, and do not build either |
| Trainer-only ownership of the mapping loss and of the access manager's desk line | Those are the lesson, and they are currently after the answer key |
| Any impulse to add a live Kafka, a Debezium container, a dbt project, or a WhatsApp Business app | Experimental relative to the outcome. The fixtures can carry the failure |
| Grading the student on naming `ZSS`, `sub_specialty`, `thyroid`, or `priorityHint` | The existing tests exist so the lesson cannot leak them. Teach the loss as a count |

Keep these, or the rebuild will throw out the part that already works.

| Keep | Why |
| --- | --- |
| `chk-journey` re-runs the worker | A handwritten trace cannot pass |
| Failure text that does not echo secrets | This is the right assessment design |
| Duplicate event id returns the first outcome | The happy path of the inbox |
| Rejected SMS releases the hold; no slot escalates | Real compensation and a real refusal to invent capacity |
| Unknown compatible field does not fail the event | Matches a tolerant reader under a backward-compatible add |
| Subscription text before mart text | Stops the warehouse from driving the workflow |
| Watermark file must not sit in `work/` | Module 1 assistant-use rule, still loaded |
| SMS without a national id | Channel content rule, still too easy to skip |
| Zone rows for the engine and the worker | The boundary is real; it is just not sufficient |
| HL7 demo stdout limited to the two order lines | Protects the canary and still shows order |
| One person, five roles, no timetable | The course's instructional constraint |
| Lesson 3's ownership of receipt *timing* | This lesson hands off an outbox. It does not absorb the clock pin |
| Booking from chat still waits | Feeds are not the booking product |

## Adds

Add a decision memo, an inbox that commits before the send, a crash fixture, a breaking schema fixture, a shared-id-across-sources fixture, a WhatsApp policy function with open window, closed window, missing template, and missing opt-in, a contract with owner, grain, biased anchor, and a ban, a two-row mart so grain is visible, and a loss count on the mapping row. Add checker lines listed in the assessment file. Add two short partner pages (acknowledgement levels, customer service window) written in the course's voice so a student is not sent out to assemble policy mid-lab.

Add facilitator readings, not student installations: Confluent compatibility modes, CloudEvents `source` + `id`, HL7 `CA` versus `AA`, FHIR rest-hook handshake, Meta's service-message page, Richardson's outbox, Azure's inbox, Debezium's one-paragraph definition, dbt's contract limits, PayPal's business-name and transform-description fields.

## Tradeoffs

**In-place rebuild versus a new lesson.** In-place keeps `rel-m02-l02` and Lesson 3's "tomorrow the receipt follows the case clock." The student chapter gets harder, which is the point, and the current paste-pass rate goes away. Facilitators who liked a quiet lab will see more `the worker did not run` from real syntax errors. The finish table has to stay kind. A new lesson would let the old day remain a gentle introduction. That gentleness is the defect. Do not preserve it beside the real day. People will stop at the paste.

**Grade the contract as prose versus as warehouse DDL.** Prose (or a tiny YAML the checker parses for headings) fits one person and no dbt install. DDL would prove the shape and still miss the lie, which is the dbt limitation this lesson exists to show. Prose can be gamed with the right nouns. The checker should require the nouns *and* the negative (the date start is booking, the figure is not the baseline, a row is not a person) the way knowledge.md already requires `book` and `not` or `once`. A student who writes only "booking_date" fails the new clause even though they would pass today.

**Implement the inbox versus narrate it.** Narration is what the current chapter does, and the crash window survives. Implementation in a few dozen lines is within the course's Python. The tradeoff is support load. Mitigate with a table schema in the chapter and a sealed `sms.py`. Do not mitigate by pasting `apply`.

**Teach FHIR Subscriptions in full versus one picture.** A full Subscription resource, topic, filter, and handshake is a different course. One picture stops the homemade webhook from being the only pattern the student ever sees. The lab stays on local JSON. Students who already know FHIR are not blocked; students who do not are not certified.

**Teach HL7 segment grammar versus acknowledgement meaning.** Grammar leaks the canary and consumes the day. Acknowledgement meaning transfers to webhooks and to WhatsApp's accept-versus-delivery split. Choose meaning. Facilitators who want a segment exercise can do it orally on the demo output without new files.

**CDC as a lab versus CDC as a rejected option.** Installing Debezium would be current and impressive and would miss `referral.submitted`. Rejecting it in a memo is the FDE skill. The cost is a student who thinks they "didn't do CDC." The decision page's done line says a written rejection is the work. That has to be visible in the student README or the day will feel unfinished to people who equate learning with running a broker.

**Exactly-once as a goal.** Kafka can dedupe producer retries inside a session and can do exactly-once between topics. SMS and WhatsApp cannot be pulled inside that transaction. Claiming end-to-end exactly-once is the experimental mistake. The lesson claims exactly-once *local* effects under at-least-once delivery, and it shows the leftover hazard when the send is outside the commit. That is the honest line in Richardson and in the Azure inbox note.

**Semantic layer as the fix for `p-clock`.** A governed metric that defines wait from `booking_date` makes every tool agree on the undercount. Agreement is the failure mode. The Google and PayPal case study claims high accuracy when an assistant is grounded in Looker definitions. Even if that claim were independently replicated, it would measure fidelity to the definition, not fidelity to the desk. Do not cite it as evidence that a semantic layer would have saved Al-Waha. Cite dbt's validation list as evidence that execution checks do not ask the operational question. The contract's job is to make the bias visible, not to bless a metric store.

**Channel coverage versus time.** Adding WhatsApp policy lengthens the day. Cutting it leaves a word the syllabus already promised and a partner the systems note already specifies. Grade four rows of a pure function. That is shorter than the current paste chapter and it teaches the rule. SMS remains the channel with a body sentence, so the national-id check stays.

**Poison-message isolation versus a harsh checker.** Today's broad exception is simple and punishes a typo and a poison event the same way. Isolation is more production-like and more code in the harness. Do it in the harness, not as student work. The student only has to catch inside the loop if the redesign chooses that. Prefer harness isolation so the lab does not become an exercise in `try/except` theater.

**Module 3 boundary.** Grain is mentioned so the contract is not "one row, one patient." The merge algorithm is not taught. If this lesson starts matching people, it steals `p-waitlist` and risks the mother-and-newborn trap without the later scaffolding. One extra CSV row is the whole addition.

## New lesson opportunities

Do not spawn these as mandatory siblings unless the in-place day will not fit. Order of value:

1. **Stay inside Lesson 2.** The contract, the inbox, and the channel gate are one engagement day. Splitting them drops the trap back into a label.
2. **Lesson 3 already exists.** Point its background at the outbox: accepted is not delivered, receipts duplicate, a fixed sleep is the wrong clock. That is a paragraph, not a new release. If Lesson 3 cannot absorb it, the receipt lesson is the spawn, and it should not re-teach webhooks.
3. **Schema evolution workshop, optional, only if Lesson 1's FHIR break and this registry still feel like two anecdotes.** A thirty-minute addendum: backward versus breaking, on the same JSON. Not a new module. **Emerging** as a separate lesson, **proven** as a section.
4. **Do not spawn a CDC module.** A Debezium practicum is experimental for this audience and this laptop constraint. A later elective for engineers who already run Kafka is a different product.
5. **Do not spawn a WhatsApp certification lesson.** Policy rows are enough. Template category prices change and do not belong in a durable chapter.
6. **Module 3 Lesson 1 remains the identity lesson.** The forward pointer in the contract is the joint. A new "semantic layer" module would repeat `p-clock` with more YAML. Resist it. One contract, next to the feed that finally has `occurred_at` for the referral, is the place the lie becomes obvious: the event has a time, the extract has a different time, the assistant must pick.
7. **A later design readout** (Module 2 Lesson 5 or the Module 1 steering habit) can require the decision memo's rejection of the mart as baseline. If no readout cites `p-clock`, teams will quietly put the figure back into the value case. That is a checklist line on an existing readout, not a new class.

## Risks

The rebuilt checker is stricter. Budget a facilitator pass on the new fixtures with both profiles, because the wait integer and the canary move with the seed, and a chapter that hardcodes either will rot. The current chapter's hardcoded extract row is the example of that rot.

Loose text checks will pass a memo that says "CDC" and "not" in unrelated sentences. Pair each cue with the system id in a window of a few lines, and keep a negative fixture in `test_m02_l02_checks.py` the way replay and trusted-mart already have negative tests.

Students may write the wait integer into the contract while explaining the ban ("the figure 14 is wrong"). The checker then fails them for doing the thing the sentence forbids. Say in the chapter: name the column, do not write the cell. That instruction exists today and is easy to miss because the cell is on the same page. Removing the sample row is the real fix.

Hidden-field tests scan only the root README and templates. After the rebuild, extend the scan to student chapters so a future paste of `sub_specialty` fails CI. Do not extend it to the solution's trainer notes if those notes must name the field for facilitators. Keep trainer notes out of the student tree, as they are now.

## Sources

Pages used in the research file. Vendor self-reports are not independent measurements.

Schema compatibility. Confluent, current platform docs. https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html and https://docs.confluent.io/platform/current/schema-registry/develop/api.html

AsyncAPI specification (v3.1.0 document) and Kafka bindings tutorial. https://github.com/asyncapi/spec/blob/v3.1.0/spec/asyncapi.md and https://www.asyncapi.com/docs/tutorials/kafka/bindings-with-kafka

CloudEvents 1.0.2 and the CNCF graduation announcement (25 January 2024). https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md and https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/

HL7 acknowledgement codes, ACK guidance, MSH-15 and MSH-16, choreography. https://terminology.hl7.org/CodeSystem-v2-0008.html and https://confluence.hl7.org/spaces/CONF/pages/256183953/HL7+V2+ACK+Guidance and https://hl7.org/documentcenter/public/wg/conf/HL7MSH.htm and https://confluence.hl7.org/spaces/CONF/pages/324961644/ACK+Choreography+Patterns

FHIR R5 Subscription and channel types. https://www.hl7.org/fhir/R5/subscription.html and https://hl7.org/fhir/R5/valueset-subscription-channel-type.html

WhatsApp service messages (page updated 21 May 2026) and template fundamentals. https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages and https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/

Transactional outbox. https://microservices.io/patterns/data/transactional-outbox.html and https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

Idempotent consumer and inbox. https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer

Kafka delivery semantics and the idempotent producer limit. https://kafka.apache.org/39/design/design/ and https://kafka.apache.org/44/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html

Anti-corruption layer and gateway. https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer and https://martinfowler.com/articles/gateway-pattern.html

Debezium overview and connectors. https://debezium.io/documentation/reference/stable/ and https://debezium.io/documentation/reference/stable/connectors/index.html

dbt model contracts, constraints, semantic models, validations. https://docs.getdbt.com/docs/mesh/govern/model-contracts and https://docs.getdbt.com/reference/resource-properties/constraints and https://docs.getdbt.com/docs/build/semantic-models and https://docs.getdbt.com/docs/build/validation

PayPal data-contract template and data-mesh post. https://github.com/paypal/data-contract-template and https://developer.paypal.com/community/blog/the-next-generation-of-data-platforms-is-the-data-mesh/

Open Data Contract Standard via the Data Contract CLI. https://cli.datacontract.com/open-data-contract-standard

Looker and PayPal case study, cited only as a vendor claim about fidelity to a governed definition. https://cloud.google.com/customers/paypal-looker-mcp

Course materials used as the object of study, not as external evidence: `course_design/module-02.md`, `course_design/slides/module-02-lesson-02.md`, `instructional/curriculum-understanding-map.md`, `instructional/student-journey/lessons/m02_l02.md`, the Module 2 Lesson 2 student and solution chapters, `problem_simulation/alwaha/engagement/m02_l02.py`, `problem_simulation/alwaha/check/journey_m02.py`, `problem_simulation/alwaha/check/notes_w2.py`, `problem_simulation/tests/test_m02_l02.py`, `problem_simulation/tests/test_m02_l02_checks.py`, `problem_simulation/design/02-real-problems.md` (`p-clock`), and `problem_simulation/design/04-systems-and-environments.md`.
