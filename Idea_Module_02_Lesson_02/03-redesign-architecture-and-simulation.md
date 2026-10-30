# 03 — Redesign, architectures, and simulation

The rebuilt day still ends with intake from `eref`, a cancellation worker on the dev namespace, and a mart the desk does not trust. The student produces three decisions a paste cannot fake: which pipe each system uses, what the HL7 translation is allowed to drop, and a data contract that states the mart's bias. Code remains small. The checker remains the judge.

## The systems already in the case

The facilitator systems note already assigns a pipe. The lesson should use that assignment instead of one webhook story for everything.

| System | What it actually is | Pipe that fits | Why the others fail |
| --- | --- | --- | --- |
| `eref` | Referral system the cluster owns. Domain event `referral.submitted` | Webhook or FHIR-style rest-hook, consumer inbox | CDC would emit row images and miss the business moment. Polling is the path Lesson 2 retires |
| `h-nakhl`, `h-safra` | HL7 v2 SIU, out of order at Safra | Feed into `int-engine`, enhanced-mode accept versus application ack, explicit loss log | A webhook assumes HTTP and a JSON contract they do not publish. CDC assumes a database log the cluster may not be allowed to read |
| `h-wadi` | FHIR on the private zone | Emerging: R5 rest-hook. Today: the cancellation events the pack already has | Forcing HL7 onto the one FHIR hospital reverses Lesson 1 |
| `sched-ain` | Nightly full file, last file wins | Snapshot poll with a freshness SLA | A webhook cannot appear inside a file that arrives once a night |
| `bi` mart | Extract whose clock starts at `booking_date`; rows are not people | Snapshot poll, read under a contract, never a command | Subscribing to a dashboard does not create a system of record |
| `sms` | Partner send, receipts late and duplicated | Outbox plus receipt, idempotent send key | Exactly-once is not on offer |
| `wa` | Business API, template and 24-hour window | Same outbox, different policy gate | Copying the SMS sentence into free text after the window is a policy failure |
| `dms` | Document versions and a circulars feed | Leave it for the corpus lesson | It is not Debezium |

`p-clock` stays the semantic defect. The approach that fits it, in the problem table, is corrected SQL and no model. This lesson does not correct the SQL. It writes the contract that forbids the assistant, the sprint, and the business case from using the figure as the baseline. Fixing the warehouse is a later, named piece of work, owned by `bi`, not by the front-desk worker.

## Three architectures

### A — Domain-event subscription and a transactional inbox

**Proven. This is the default for `eref` and for `session.cancelled`.**

`eref` commits its own transaction and then POSTs a CloudEvents-shaped JSON body: `source` (a URI for `eref`), `id` (today's `event_id`), `type` (`referral.submitted`), `specversion`, and a data object limited to the registry. The worker verifies the signature the pack will invent as a shared header (a static fixture secret is enough; do not design a novel crypto scheme in the chapter). It inserts an inbox row keyed by `source` + `id` in the same SQLite transaction as the local referral row. Duplicate key returns the stored result and responds with success so the sender can stop. Unknown data keys are listed on the result and not stored. A missing required field quarantines the event: stored as rejected, not silently given an empty `referral_id`.

The cancellation worker uses the same inbox. The booking transition commits *before* `sms.send` or the WhatsApp policy function. The send is an outbox row (`pending`, then `accepted` or `rejected`). A crash before commit retries the whole transition once. A crash after commit returns the row and does not send a second time. A partner reject runs a second transaction that releases the hold, and a replay of that event returns `compensated` rather than sending again.

FHIR rest-hook is this architecture with a notification Bundle, a handshake, and HTTPS. Show the handshake once, then keep the lab on local JSON. **Emerging** only as the live binding for `h-wadi`. The inbox itself is proven.

### B — Log-based change data capture

**Proven for databases that expose a log. The wrong default for this lesson's two events.**

Debezium records row-level changes in commit order. A connector on a hospital scheduling database the cluster is allowed to read would show inserts and updates without anyone writing a webhook. Consumers still see at-least-once delivery when the sink retries, so the inbox does not disappear. What disappears is the business vocabulary. A change to a row is not `referral.submitted` and not "the clinic session was cancelled." Someone still maps the row image into those types. That mapper is another anti-corruption layer, with its own loss log.

In the memo the student rejects B for `eref`, because the domain event already exists, and rejects it for `sched-ain`, because a nightly file is not a log. A hands-on Debezium lab is **experimental** here: it needs a broker and it teaches operations the checker cannot see. One paragraph of the Debezium overview is the reading. The words chapter states that the document change feed and a database change stream share an English word and are different pipes. Do not point B at `dms`.

### C — Snapshot poll with a watermark and a contract

**Proven. This is the mart, and it is still the right read after webhooks arrive.**

The old `readReferral` poll is retired because `eref` can push and the poll hid the business event behind "ask again." The mart cannot push a truthful event. It is an extract. `sched-ain` is the same shape: last file wins, a missed night leaves yesterday. The consumer stores the file's timestamp or a checksum and an explicit freshness statement ("this extract's `booking_date` values are the warehouse clock as of the file, and they are not referral time"). Polling here is not a legacy smell. Calling it legacy is how a team ends up treating the CSV as a stream.

The worker may read the extract only after the subscription exists, which the current sprint already requires. The read returns the contract verdict, not a trusted wait. An assistant that wants "how long has this referral waited" computes from `referral.submitted` `occurred_at` when that event has been stored, and says "unknown" when it has not. It does not fill the gap with `wait_days`.

### Comparison

| Question | A. Webhook + inbox | B. CDC | C. Snapshot poll |
| --- | --- | --- | --- |
| Fits | `eref`, clinic-session events, later a `h-wadi` rest-hook | A source database with a log and no events | `bi` mart, `sched-ain` nightly file |
| Ordering | Not given by HTTP. Use the sequence field, and do not let file order win | Commit order per table, still not domain order | Last file wins. Stale on purpose |
| Duplicates | Normal. Inbox on `source` + `id` | Normal at the sink. Inbox still required | The same extract arrives again. Checksum, do not apply twice as two people |
| Schema change | Registry compatibility on the subject | Connector schema history. A column add is a row-image change, not a decision | Contract diff. A renamed column fails the poll |
| Failure the student must see | Crash between side effect and commit | Mapping a row image into a domain event and losing a column | A fresh file that still uses the biased clock |
| What the lesson does | Implement | Reject in writing, with a reason | Implement the contract, not a new poller for `eref` |

A fourth pattern, HL7 enhanced acknowledgements, is not a rival to A–C. It is the reliability story inside the engine that feeds A. Commit accept means "safe storage, you may stop sending." Application accept means "the mapped event was applied." The engine may `CA` when the raw SIU is durable and withhold `AA` when the mapping dropped a qualifier or the sequence is older than the one already applied. The student labels a three-row fixture. They do not encode MSH.

## Anti-corruption layer

**Proven pattern. One place in the lab.**

`int-engine` translates HL7 into the cluster's event shape. Fowler's test: HL7 segment names are a foreign vocabulary, so a translation is justified. `eref`'s field names are the cluster's own registry, so the worker conforms.

The layer's graded output is a loss record the checker can see without printing the hidden token:

- source facility and sequence;
- whether file order and sequence order disagree;
- a count of raw qualifiers that the mapped object does not carry;
- the reply the engine would owe: accept-level only, or application-level as well.

The hidden field name and the hidden segment value stay out of `work/` prose, matching `test_m02_l02.py`. The student writes "the mapped event is smaller than the raw message by one qualifier" because the fixture's mapped object has fewer keys than `raw`. That is observable without naming the secret. The facilitator gold still knows which qualifier. The failure text stays generic: `the mapping loss was not recorded`, `file order was treated as clinical order`.

The layer does not book and does not call a model. Translation stays in the layer; booking policy stays in the worker. An LLM that invents the missing qualifier is **experimental** and repeats the `p-slots` and `p-triage` mistake. Zone placement stays: engine in `zone-hospital`, worker in `zone-private`. A mapped event with a loss flag is not a complete clinical fact.

## Channel policy

**Proven rules, local fixtures.**

`channel.decide(now, last_inbound, template_id)` returns `sms`, `wa_session`, `wa_template`, or `escalate`. The clock is the case clock Lesson 3 will pin. Two instants are enough. An inbound two hours ago allows a WhatsApp session text, and SMS stays allowed. An inbound thirty hours ago, or none, rejects free text; a registered template id writes `wa_template`; a missing template escalates. The SMS sentence must not be copied into that free-text slot. Opt-in false escalates on both channels. The fixture carries the flag. The chapter invents no consent statute. A partner reject uses the existing compensate path, with the reason kept so Lesson 3 can tell a template failure from a window failure. Outbox `accepted` is not `delivered`. The student does not sleep.

The 24-hour figure is Meta's, copied onto the fictional partner page. The words chapter defines three different sessions: the customer service window, yesterday's sign-in, and the clinic block. The patient line still says a booking moved, with no ten-digit id and no wait figure. A figure in `sms.md` fails. Today the figure is banned only from `mart.md` and from cancellation rows.

## The data contract is the climax

**The habit is proven. A full ODCS toolchain is emerging and optional.**

`work/contract.md` (or a short YAML if the facilitator prefers ODCS headings) for the wait extract, written by the student, graded as text plus one function `mart.read` that returns the contract verdict. Required clauses:

| Clause | What a passing answer says | What still fails |
| --- | --- | --- |
| Owner | `bi` publishes the extract. The desk does not | Naming `eref` or the assistant as owner |
| Grain | A row is a row in the extract. It has not been shown to be one person | "One row, one patient" with no other source |
| Time anchor | The date column is when the warehouse starts the clock, and that start is booking, not referral | Calling the date column the true wait, or copying the wait cell into the note |
| Authority | Not a system of record for waiting. `p-clock` is the reason, named as the finding from Module 1, not as a percent | Using the figure in `sprint.md`, `sms.md`, or the patient states |
| Allowed use | An operator may see that a number was published | The assistant telling a patient the number |
| Freshness | The file is a snapshot. A newer referral event can exist that the file does not contain | Treating the file as a subscription |
| Classification | Same zone rules as the rest of the pack. The note carries no national id and no watermark | Pasting the webhook file into `work/` |

`mart.read` returns `authoritative: false`, the anchor name, and `reason: biased_anchor`. The wait cell may appear only as `published_claim`. Any graded markdown that contains the integer fails. Keep `trusted` and `clock` for one checker release if needed, then drop `clock`, because that key taught the wrong sentence.

dbt is the reading, not the runtime. A name-and-type contract would accept this CSV and would still accept the lie. The student does not install dbt. Identity stays in Module 3. A second row with the same `person_key` makes "one row, one person" false. The student does not merge rows. The mother-and-newborn trap stays later.

## Synthetic data

Keep every current generator in `alwaha.engagement.m02_l02`: webhook with canary letter and extra field, three cancellations plus the no-slot event, HL7 rows, seed-derived wait. Add fixtures that are still synthetic and still free of real identifiers.

| Fixture | What it adds | Secret rule |
| --- | --- | --- |
| `referral.submitted.v2.json` | Optional field that the v2 registry lists, absent on v1 | Student accepts v1 and v2. A replay of the same `source`+`id` does not create two referrals |
| `referral.submitted.break.json` | Required field removed or renamed | Quarantine. Do not store a partial as success |
| `cancel-crash.json` | A delivery record that was sent and not committed, represented as an outbox `pending` with no inbox row, then a replay | One send in the final trace |
| `wa-window.json` | `last_inbound` inside and outside 24 hours, template present and absent, opt-in false | Closed window plus free text fails |
| `waitlist-grain.csv` | Two rows, same person key, different dates | Contract must not say one row is one person |
| `int-engine` loss row | Raw object with one more key than `mapped` | Loss count is 1. The key's name stays out of student prose |
| Duplicate receipt | Two SMS receipts for one outbox id | Lesson 3's problem, planted here as a row the outbox ignores the second time |

The practice profile and any other profile differ by canary, as they do now. The wait integer moves with the seed. Chapters show headers and the column roles, not a sample number. The demo still prints only the two order lines.

No live WhatsApp, no live broker, no PHI. The partner is a Python function with a fault file, which is what `sms.py` already is. Extend it. Do not network.

## Production scenarios the simulation should force

Each line is a checker phrase that names the behavior and hides the secret. Existing passes stay: replay after a commit books once; a compatible unknown field is ignored and not stored; SMS reject releases the hold in a transaction the replay can see; no slot escalates with no send; the watermark file and the canary value stay out of `work/`. `letter` stops being a required business field.

New failures the paste never reaches:

| Situation | Pass |
| --- | --- |
| Crash: outbox `pending`, inbox row absent, then a replay | One send |
| Same id, different `booking_id` | Quarantine. CloudEvents reuses `id` for a resend of the same event |
| SIU sequence 2 then 1 | Applied sequence is 2. File order loses |
| Mapped object smaller than raw | Loss count recorded. No invented qualifier and no model |
| Raw message stored, mapping still open | The note marks accept-level only. No MSH bytes |
| Required field removed | Quarantine, not an empty id |
| Two sources, one `event_id` | Both stored. The key is the pair |
| WhatsApp window closed | Free text refused. A template id writes a template row. No template escalates |
| Opt-in false | Escalate even if the window is open |
| Outbox `accepted`, no receipt | Not described as delivered. `states.md` says what `notified` means |
| Wait figure in SMS, sprint, or contract | `wait number was used as truth` |
| Contract says the figure is the baseline, or that a row is a person | Those clauses fail |
| Referral `occurred_at` is later than the extract | Freshness clause: the assistant does not prefer the file |
| Bad fixture signature | Rejected, not stored. A string compare, not a new cryptosystem |
| One handler raises | That event is `failed`. Later events still run. Today's broad `except` in `journey_problems` turns any exception into `the worker did not run` for the whole submission. Isolate that in the harness |

Edge states worth a line in the facilitator guide, not a new feature: heartbeat missed (FHIR), TTL exceeded so a WhatsApp send is dropped, receipt arrives twice, Hijri dates on Nakhl (Module 3 and the calendar lesson, do not solve here), MRN reuse (identity lesson). Name them as out of scope so the student does not "handle" them with a guess.

## What the simulation is not

It is not a cluster deploy. `namespace.yaml` and `compose.yaml` stay as maps of where the worker would sit. It is not a Kafka course. It is not a WhatsApp Business Account. It is not a dbt project. It is not the lesson that corrects the warehouse SQL. The decision memo ends with "bi owns the SQL change; we will not quote the extract in the value case." That sentence is the FDE move `p-clock` asked for, and it is available to one person at a laptop.
