# 02 — Industry research

Sources below were opened. Figures that a vendor states about itself are marked as that vendor's claim. No throughput, latency, or adoption rate is invented. Where a page was a search hit and the body was read from that capture, the URL is the one on the page.

The course's legal setting is fictional. Nothing here maps Al-Waha onto a Saudi regulator. WhatsApp's rules are Meta's platform rules for a real API the fiction is allowed to imitate.

## Schema registry and compatibility

**Proven.** Confluent's schema-evolution document defines the compatibility types Schema Registry enforces when a new schema is registered for a subject. `BACKWARD` (the default) means a consumer on the new schema can read data written with the latest registered schema, not necessarily every older one. `BACKWARD_TRANSITIVE` extends that to all registered versions. `FORWARD` means a consumer still on the last schema can read data the new schema writes. `FULL` requires both directions against the latest schema; `FULL_TRANSITIVE` requires both against every registered version. `NONE` turns the check off. The stated reason for the default is operational: with backward compatibility you can rewind a consumer to the beginning of a topic; forward compatibility does not promise that old messages are readable, and it asks the producer to anticipate later readers.

https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

The API reference lists the same seven modes and repeats the rewind rationale: https://docs.confluent.io/platform/current/schema-registry/develop/api.html

Against the lesson's markdown table: an allow-list that ignores unknown keys is closer to a reader that tolerates a producer adding a field. It is not a compatibility *gate*. The gate refuses to register a breaking schema. The lesson's `topics.md` has a version column stuck at `1` and a parser that never reads it. Adding `priorityHint` to the fixture and ignoring it is one legal evolution (a new optional field, consumer not yet upgraded). Removing `referral_id` would be a break. The current `accept` would store an empty id and fail later with `the referral was not recorded`, which is an outcome check, not a compatibility check. Teaching the modes means the student picks `BACKWARD` or `BACKWARD_TRANSITIVE` for `referral.submitted` and says which edits are legal: add an optional field with a default, do not rename `patient_key` in place, do not drop a field a rewound consumer still expects.

Avro, Protobuf, and JSON Schema do not implement those words identically. The lesson should use the compatibility decision and keep the JSON payload the pack already has. A markdown cell is not a registry.

## AsyncAPI

**Proven as a specification, emerging as something this cluster would publish.** AsyncAPI describes event-driven APIs: channels, messages, and protocol bindings. The Kafka binding can name a schema registry URL and a vendor (`confluent`, `apicurio`, and others) on the server, and can name topic settings on the channel. The specification text is the source of truth for the document shape.

https://github.com/asyncapi/spec/blob/v3.1.0/spec/asyncapi.md

https://www.asyncapi.com/docs/tutorials/kafka/bindings-with-kafka

`eref.yaml` is OpenAPI, which fits `readReferral` and the call that registers a subscription. It is a poor home for "this body is `referral.submitted`, owner `eref`, and a replay keeps `source` + `id`." The student reads a short AsyncAPI channel and names the contract fields. Generating another client repeats Lesson 1. A live Kafka binding is out of scope.

## CloudEvents

**Proven.** CloudEvents is a CNCF specification for common event metadata. The project graduated on 25 January 2024. Spec 1.0.2 requires every event to carry `id`, `source`, `specversion`, and `type`. Producers must make `source` + `id` unique per distinct event. A re-send caused by a network error may reuse the same `id`. Consumers may treat identical `source` and `id` as duplicates. `type` should be prefixed with a reverse-DNS name so the owner of the semantics is visible. All implementations must support JSON.

https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md

https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/

The lesson dedupes on `event_id` alone. Fixtures do not collide, so the bug is latent. CloudEvents namespaces the pair. Two hospitals and `eref` are three sources. An `event_id`-only inbox will merge distinct occurrences, or split one replay if a broker rewrites the id. The redesign keys `source` + `id` and keeps `event_id` as the id half. Students do not adopt a CNCF SDK. `specversion` versions the envelope, not the payload. The lesson's single version cell conflates them.

## HL7 v2 acknowledgements

**Proven standard, taught here at the level of the two replies, not at the level of a parser.** HL7's acknowledgement code system `v2-0008` distinguishes original-mode application replies (`AA`, `AE`, `AR`) from enhanced-mode accept replies (`CA`, `CE`, `CR`) and enhanced-mode application replies (again `AA`, `AE`, `AR`).

https://terminology.hl7.org/CodeSystem-v2-0008.html

The HL7 Conformance work group's ACK guidance states the enhanced-mode rule in plain language: a positive accept acknowledgement means the receiver has committed the message to safe storage and the sender need not resend; an application acknowledgement may follow later with the result of processing. Commit reject (`CR`) and commit error (`CE`) are accept-level failures (for example an unacceptable message type, version, or processing id, or a sequence-number error). The MSH fields that select the mode are MSH-15 (accept acknowledgement type) and MSH-16 (application acknowledgement type). If both are omitted, original-mode rules apply. The condition table on the MSH definition includes `AL` (always), `NE` (never), `ER` (error or reject only), and `SU` (success only).

https://confluence.hl7.org/spaces/CONF/pages/256183953/HL7+V2+ACK+Guidance

https://hl7.org/documentcenter/public/wg/conf/HL7MSH.htm

The choreography page shows the three patterns: accept only (`MSH-15=AL`, `MSH-16=NE`), application only, and both.

https://confluence.hl7.org/spaces/CONF/pages/324961644/ACK+Choreography+Patterns

This is the sentence the HL7 demo does not teach. Sorting by sequence decides which schedule row stands. The acknowledgement decides whether Nakhl is allowed to stop transmitting. A worker that returns success because it appended a file has sent something like `CA` and has not sent `AA`. The course's out-of-order SIU pair is the right fixture. The redesign adds one question: after you persist the raw message and before you trust the mapping, which reply are you sending? Students do not build an MLLP listener. They label a fixture.

Original mode's subtlety belongs in a facilitator note, not a graded parser: HL7's own control-chapter discussion says the standard does not require the receiver to finish database work before acknowledging, only to accept responsibility at the same integrity as its other input. A queue can be a commit. That is why "we returned OK" is not "the slot moved."

## FHIR Subscriptions

**Proven as a specification. Emerging as the default in an estate that still emits v2.** FHIR R5 `Subscription` asks a server to notify a subscriber when a `SubscriptionTopic` matches, with optional filters. The core channels are `rest-hook` (HTTPS POST of a notification Bundle), `websocket`, `email`, and `message`. For rest-hook the server starts the subscription at `requested`, POSTs a handshake, and moves to `active` only after the endpoint accepts it. Errors on the handshake move it to `error`. Heartbeats and `event-notification` follow. The security note says implementations should refuse plain HTTP.

https://www.hl7.org/fhir/R5/subscription.html

https://hl7.org/fhir/R5/valueset-subscription-channel-type.html

Put next to this lesson, `subscribeReferralSubmitted` is a homemade rest-hook without a handshake, without a heartbeat, and without a Bundle. That is allowed in a fiction. The student should see the standard shape once, then implement the local JSON event, so the day does not become an FHIR certification. Hospitals on HL7 v2 stay behind the engine. `his-wadi` is already the FHIR house, on the private zone, and Lesson 1 just moved its spec. A rest-hook from `h-wadi` is the emerging path. Pretending Nakhl will emit R5 this week is the wrong case.

R4 servers use the R5 backport channel guide. That page is a facilitator answer, not the lab: https://hl7.org/fhir/uv/subscriptions-backport/2024Jan/channels.html

## WhatsApp: templates and the 24-hour window

**Proven platform policy.** Meta's service-message document, updated 21 May 2026, states:

- Service messages are free-form and do not need template pre-approval.
- They can be sent only inside a customer service window.
- The window is a 24-hour timer that starts when the WhatsApp user messages or calls the business. A further user message or call resets it to 24 hours.
- When the window is closed, the only option is a pre-approved template.
- Messages go only to users who have opted in.
- The Messages API success response means the request was accepted. It does not mean the message was delivered. Delivery status arrives on a messages webhook.
- A burst of sends is not guaranteed to arrive in request order. The documented way to force order is to wait for `delivered` before the next send.
- Undelivered messages are retried until a time-to-live. The page's default is 30 days for non-authentication messages and 10 minutes for authentication templates. Past the TTL, treat the message as dropped if no `delivered` status arrived.

https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages

Template fundamentals: outside the window, templates are the only message type, they are reviewed, and a template that is not `APPROVED` cannot be sent. A creation-rate cap on that page is a product limit, not a hospital volume, and the lab should not chase it. https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/

The course's `wa.md` uses "session window" without a duration and without saying who opens it. "Session" is already overloaded: yesterday's sign-in session, today's clinic session, and this window. The words chapter separates the first two. It should name the third as the customer service window and state the 24 hours, because that number is Meta's, not a case invention.

Category (utility versus marketing versus authentication) matters for a booking notice. A cancellation or a new time is a utility intent. The lab does not need the price list. It needs the rule that a closed window rejects free text like the SMS fault rejects `bkg-2`, and that an approved template is a different send. Pricing pages change; the window rule is the stable teaching object. Do not copy currency amounts into the student pack.

A business-initiated template does not, on the service-message rules above, replace the user action that opens the window. The student policy is: if the last inbound is inside 24 hours, free text is allowed; if not, send only a registered template id; if the template is missing or the partner rejects it, escalate the way no-slot escalates. Do not fall through to free text.

## Transactional outbox, inbox, at-least-once

**Proven.** Chris Richardson's transactional-outbox pattern: the service writes the business change and the message row in one database transaction; a relay publishes afterward. The relay can publish twice if it crashes after the broker accepts and before it marks the row sent. Consumers must be idempotent. He notes that consumers usually already must be, because brokers deliver more than once.

https://microservices.io/patterns/data/transactional-outbox.html

AWS's note states the same dual-write failure, the same duplicate risk, and the same consumer rule, and it says not to emit on rollback. SQS standard queues are cited there as at-least-once. FIFO is a different product, not a proof that `eref`'s HTTP webhook is exactly-once. https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

Azure's idempotent-consumer pattern is the consumer twin. Record a stable id. If the id is present, acknowledge and stop, optionally returning the previous outcome (which is what the lesson's replay path does). The failure window is check-then-act: process the message, crash before recording the id, redeliver, process again. The fix they name is the inbox: write the deduplication marker and the business effect in one transaction. On redelivery either the marker is there and the work is skipped, or the transaction never committed and the work is safe to repeat.

https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer

Kafka's design document states the three guarantees: at most once (loss, no redelivery), at least once (no loss, possible redelivery), exactly once. It warns that many exactly-once claims do not survive producer failure, consumer failure, or multiple processes. A producer that retries without knowing whether the first attempt committed is at least once. The idempotent producer, since 0.11, dedupes those retries inside a session. The KafkaProducer javadoc for 4.4 says application-level resends are not covered, and that idempotence is per session unless a transactional id spans sessions. Exactly-once between topics is not exactly-once into SMS.

https://kafka.apache.org/39/design/design/

https://kafka.apache.org/44/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html

On `cancel.py`, the stored-row return is the inbox fast path. Send-then-insert is Azure's failure window, and the send cannot sit in the SQLite transaction. Commit the inbox and the booking, then send, then record the receipt. Compensate a reject in a later transaction a replay can see. A crash after the send and before the receipt row is the leftover hazard: either the partner dedupes on a key, or the lesson shows the hazard. The `sms` export already says receipts are late and duplicated. Lesson 3 owns timing. This lesson owns "the send is not the commit."

Standing up Kafka to perform exactly-once is **experimental** for this course. The design document's warning is the lesson.

## Anti-corruption layer

**Proven.** Eric Evans named the anti-corruption layer. Microsoft's architecture note quotes that origin and states the use: a facade between subsystems that do not share semantics, so one model does not leak into the other. It adds cost, latency, and an operational surface, and it is the wrong tool when the models already match. Fowler's gateway article (10 August 2021) makes the same split: a gateway translates a foreign vocabulary; translating a widely understood vocabulary only because a team dislikes the names is a mistake. He points at the DDD choice between Conformist and anti-corruption layer.

https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer

https://martinfowler.com/articles/gateway-pattern.html

`int-engine` is that layer for HL7. The mapped object keeps a specialty and drops the raw extra segment. The loss is the layer's behavior, and today only the trainer file records it. `eref`'s JSON is the cluster's own event. The worker should conform to that contract, not invent a second referral model. `registry.keep` is a partial conformist reader. Stripping `letter` after it was allowed is not translation; it is a canary. The redesign splits those.

Debezium is the CDC reference, and it is a different pipe. The project describes itself as recording all row-level changes in each table, in the order they occurred, for applications to read. Connectors include PostgreSQL, Oracle, SQL Server, Db2, and others. Incubating connectors are called out as not a compatibility promise.

https://debezium.io/documentation/reference/stable/

https://debezium.io/documentation/reference/stable/connectors/index.html

A row image is not a domain event. "A column in `referral` changed" is not `referral.submitted`. CDC is the right proposal when the hospital will not emit an event and will allow a log reader. It is the wrong proposal for Nakhl's HL7 socket, and it is the wrong reading of the packet file `dms.md`. In this course `dms` is the document system (versions, audiences, a change feed of circulars). Teaching it as Debezium would corrupt the later corpus lesson.

## Data contracts, and semantic layers that lie

Three artifacts, three strengths.

**Proven inside dbt, and limited to shape.** With `contract.enforced: true`, every column needs a `name` and a `data_type`. The build preflight checks that the query matches, then the DDL carries those names and types. Contracts apply to SQL models materialized as table, view, or qualifying incremental. They do not apply to Python models, ephemeral models, sources, seeds, or snapshots. Views can declare types and cannot declare constraints. On many warehouses a constraint can be stored and still not enforced. dbt recommends contracts on public models.

https://docs.getdbt.com/docs/mesh/govern/model-contracts

https://docs.getdbt.com/reference/resource-properties/constraints

The Semantic Layer's published validations check that the YAML parses, that the semantic graph respects its own rules (for example one primary entity, metric configuration), and that the generated SQL executes against columns that exist. That is governance of the *declaration*. It does not include a check that the measure matches the operational meaning.

https://docs.getdbt.com/docs/build/validation

https://docs.getdbt.com/docs/build/semantic-models

**That gap is the lie.** A semantic model can be valid, unique, and executed, and still define waiting as the interval from `booking_date`. Every dashboard then agrees. Agreement is not truth. `p-clock` is this failure in the case: the mart is internally consistent and operationally early. Google's PayPal and Looker case study claims that grounding an assistant in Looker's semantic layer produced near-100% accuracy versus AI-to-SQL that guesses column names. That sentence is the vendor's case study, not an independent measurement, and it answers a different question (did the model use the governed definition) than the question this lesson grades (is the governed definition the wait the desk means).

https://cloud.google.com/customers/paypal-looker-mcp

**Proven as a PayPal practice.** Their Apache-2.0 template is a producer-consumer agreement: fundamentals, schema, quality, SLA, security, stakeholders. Columns carry a business name, a logical type beside the physical type, a classification, and a plain-language transform. The data-mesh post says each quantum has contracts for the user relationship, the model, and the SLA. Those description fields are what a type contract lacks: `wait_days` can be an integer and still count from booking.

https://github.com/paypal/data-contract-template

https://developer.paypal.com/community/blog/the-next-generation-of-data-platforms-is-the-data-mesh/

**Emerging as a cross-vendor file format.** The Open Data Contract Standard, maintained by Bitol under the Linux Foundation AI and Data umbrella, is a YAML document for structure, semantics, quality, ownership, servers, and SLA properties. The Data Contract CLI documents `v3.2.0` as the version `datacontract init` writes, and it can lint, diff, and test a contract against a live source. No adoption count is cited here because this research did not find a neutral census worth repeating.

https://cli.datacontract.com/open-data-contract-standard

For the lesson, ODCS is a reasonable file shape if the facilitator wants one YAML. It is not required. A short contract in the course's own headings (owner, grain, time anchor, source of record or not, classification, what an assistant may say) will teach the same idea with less tooling. Mark a full ODCS toolchain **emerging** and optional. Mark the *habit* of writing the time anchor and the ban **proven**, because PayPal's template and dbt's own limits both point at it, and because `p-clock` is already the case.

## What not to import

Do not import a benchmark of webhook QPS, a "percent of hospitals on FHIR," or a Schema Registry market share. Those numbers were not taken from the pages above. Do not import WhatsApp prices. Do not treat Kafka exactly-once as a property of `sms.send`. Do not call `dms` CDC. Do not teach the student to build an HL7 parser that echoes `ZSS` or the dropped field name into a graded page: the existing tests forbid that leak, and the redesign can grade the *fact of a loss* without printing the hidden token.
