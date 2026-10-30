# 02 — Industry research

This note compares durable execution, messaging patterns, referral standards, Saudi business calendars, and human approval with the intake lesson. Claims below are tied to pages fetched for this packet. No performance numbers are invented. Where a vendor's guarantee is narrow, the narrowness is the finding.

## Durable execution, and the exactly-once boundary

Durable execution means the program's progress is stored, so a crash resumes from recorded steps instead of starting the business effects again. Three products document that idea differently. A fourth approach, plain transactional messaging, does not resume Python functions. It stores rows and messages.

### Temporal

Temporal's activity documentation says activities should be idempotent because they may run more than once. Completed activities are not re-executed on workflow replay. An activity is recorded in history only when it returns or errors. If the worker finishes the activity and crashes before telling the server, the activity is retried. Temporal's recommended idempotency key for a downstream call is the workflow run id plus the activity id, and the downstream service is what enforces the key, not the activity function.

The same page states the boundary in one sentence: for an activity whose retry policy allows retries, Temporal guarantees the activity will be observed as completed exactly once, and the activity may still be executed multiple times and may partially complete more than once. That is the exactly-once myth in the vendor's own words. "Observed once" is a history fact. "Executed once" is a side-effect fact. Hospital holds, bookings, and SMS sends are side effects. They need their own keys.

Temporal's approval pattern treats a person as a waited state. The workflow blocks on `workflow.wait_condition` until a signal brings the decision or a timeout fires. While it waits, the worker is idle. The timer lives in the server's store and survives worker restarts. The signal carries the decision, the approver, and comments. A query can read status without changing it. The pattern's own trade-off list says an external system must send the signal, a maximum wait must be chosen, and large approval payloads grow the history.

That pattern is the picture of `approval.held`: the hold is an activity, and Lesson 4's coordinator turn would be the signal. The picture fits in a paragraph. The server does not fit in this morning. The classroom map spends the next half-day on the agent.

**Maturity.** Replay plus at-least-once activities is a documented production model. Requiring the server and SDK here is an emerging teaching choice.

### Restate

Restate's key-concepts page describes a journal of steps. After a crash, replay skips completed steps and resumes. Handlers wrap non-deterministic work, including HTTP and database calls, in `ctx.run` (or the language equivalent) so the result is stored. Without that wrapper, replay would repeat the call and could see a different result.

Ingress idempotency is a header, `Idempotency-Key`. After the call completes, Restate keeps the response for 24 hours by default, and a second call with the same key in that window returns the stored response. The retention is tunable. From Restate 1.7 the ingress can attach its own keys so one in-flight retry is safe; those keys do not dedupe distinct client calls. The caller still supplies `event_id` when the business rule is permanent.

Calls proxied through Restate are documented as not duplicated, and side effects still belong inside `ctx.run`. A hold that commits at the hospital before the journal entry lands is the same crash Temporal describes. A replay next week sits outside the default 24-hour window. `pol-sla.md` has no such expiry. A Restate default would weaken the lesson's event-id rule unless retention is raised and the chapter says the number.

**Maturity.** Emerging. The journal and the header are documented and concrete. The retention default is a reason not to treat Restate as a drop-in for the lesson's permanent event-id rule without saying the number.

### DBOS

DBOS checkpoints workflow inputs and step outputs in Postgres. Recovery restarts the workflow with the checkpointed inputs and, before each step, returns the stored output if one exists. The architecture page requires the workflow function to be deterministic given the same arguments and step results, and it requires steps to be idempotent because a crash during a step retries the step. Once a step is checkpointed, it is not run again.

The Python transactions tutorial narrows exactly-once to the application database. A datasource transaction records its outcome in the same database transaction. On replay, DBOS returns the stored result and does not re-execute that function. A plain step can still run twice if the process crashes after a commit and before the checkpoint. A hold on `his-wadi` is not a write in that database, so it still needs an idempotency key. DBOS is the product closest to "Postgres, and no extra cluster." It is still a library, a system database, and a determinism rule. The lesson's harness can show the atomic write without the library.

**Maturity.** Emerging as a product. The exactly-once claim is proven only inside the sentence the tutorial uses: the same database transaction as the checkpoint. Treating that sentence as a guarantee for Ain, Wadi, or `eref` would be experimental.

### Plain transactional messaging

Chris Richardson's transactional outbox stores the outgoing message in the same database transaction as the business row. A relay publishes it. Benefits on the page: no two-phase commit across database and broker, the message goes out if and only if the transaction commits, and broker order follows application order. The relay can publish twice if it crashes after the send and before it records that fact. Consumers store message ids. Richardson's saga note pairs the outbox with a broker that delivers at least once.

This is the pattern the lesson can simulate without a new server. A referral row and an outbox row commit together. A second delivery of `event_id` finds the id and writes nothing. A crash between hold and commit is visible because the hold mock counts calls. The relay's duplicate publish is the replay scenario the day already has.

**Maturity.** Proven as a pattern. Richardson documents the duplicate-publish issue rather than claiming exactly once. That honesty is what the student should copy.

### What "exactly once" is allowed to mean in this course

Use three sentences, and no fourth.

1. A recorded step can be observed once in a history or a journal (Temporal, Restate, DBOS checkpoints).
2. A database transaction can commit a business write and a durability row once (DBOS datasource transactions, and the outbox insert).
3. An external hospital call can be made safe under repeats only if the hospital, or a key store in front of it, treats the key as a duplicate. Temporal says the key is enforced by the called service. The outbox page says the consumer tracks ids because the relay can publish twice.

A slogan that the intake worker is exactly once because it uses a framework is experimental. The lesson should not grade that slogan.

## Messaging patterns that already match the nine scenarios

Hohpe and Woolf, *Enterprise Integration Patterns* (2003), with the pattern statements on enterpriseintegrationpatterns.com, name the lesson's bugs more precisely than "workflow."

**Idempotent receiver.** The problem statement: a sender may send once and the receiver may still see the message more than once. The solution is a receiver that can safely receive the same message multiple times, either by dropping duplicates or by making the effect itself idempotent. The lesson's replay scenario is the first of those. The in-memory set is a teaching model of de-duplication for one pass. The production receiver stores the id.

**Dead letter channel.** When the messaging system cannot or should not deliver a message, it moves the message to a dead letter channel. The site's SQS example uses a receive count and a limit, then moves the message. Hohpe's conversation-pattern introduction says a consumer that retries a poison message will keep crashing the provider, so retries must be limited. The lesson's `retries: 2` and the `dead-letter` scenario are that limit. The missing piece is the channel: the event itself, the reason, and a later decision to replay or discard. A boolean on a log row is the record that the event was not applied. It is not yet a channel.

**Claim check.** Store a bulky payload and pass a key. These letters are one sentence, so size is not the pressure. Classification is. Lesson 1 watermarks one letter. A claim check would leave the letter in the zone that may hold it and put a document key on the event. The log would not contain the letter. Name the pattern. Do not build the store on this day. The watermark rule is the form the student already practices.

**Process manager versus choreography.** Hohpe's process manager keeps the sequence and chooses the next step from intermediate results. The flow is hub-and-spoke. He warns that a process manager can become the default for every integration problem, can hide the real rule, and can bottleneck. Richardson splits sagas into orchestration, where a coordinator sends commands, and choreography, where each participant reacts to events. Intake needs one row a coordinator can read, so it is a process manager's job. Choreography would scatter hold, release, and dead letter. The lesson keeps one process, `wf-intake`, and does not grow a general engine.

**Resequencer, sequence, and correlation.** The pattern list next to the process manager includes a resequencer: related messages arrive out of order and must be applied in sequence. On this stream the higher sequence wins the letter and the earliest `occurred_at` starts the clock. Those are two positions in one ordered list. The order pair shares 12 January 2027, so a due date cannot reveal a clock taken from the wrong event. The chapter should say the two positions out loud. A second pair on two dates would repeat the holiday case. `referral_id` correlates the pair. `event_id` is the delivery. The starter counts events per referral and conflates them. The reference worker separates them. One id used for both opens a second approval on the order pair, or drops a real correction as if it were the replay.

## Referral standards, at the altitude of this day

The lesson's event is an invented `referral.submitted`. Two real families sit behind it. The student should hear the names and the boundary. The student should not parse HL7.

**HL7 v2.** The v2.4 patient-referral chapter defines `REF^I12` as a message from one provider to another about a patient, with demographics and clinical information. `ORM` is an order, a different event. An Australian HL7 v2 note draws the operational line: an order usually stays inside one enterprise, and the ordering provider keeps the plan of treatment; a referral transfers some or all of that responsibility, and the receiving provider may place further orders. Al-Waha intake is that second case. Responsibility moves when a person decides. Booking from the letter would treat the referral as an order the sender still controls.

**FHIR.** BSeR uses `ServiceRequest` as the referral and `Task` as fulfillment. The task points at the initiator, the recipient, and the service request, and it changes when the request is sent, accepted, or completed. The FHIR v5.0.0 task-status value set has twelve codes, from `draft` and `requested` through `on-hold`, `failed`, and `completed`. It is maturity level 3 and Trial Use. `approval.held` maps to a task that is `requested` and waiting on a person. It is not `accepted` and not `completed`. Twelve statuses do not fit in a boolean.

**In-force criteria.** FHIR `PlanDefinition.status` is `draft`, `active`, `retired`, or `unknown`. `effectivePeriod` is when the content is meant to be used, and the spec's example is a plan for 2016 published in 2015. The lesson has status and no period and no pin. The production rule is to store the active document whose period contains the start. A later activation of v4 leaves that stored id alone. Module 3 grades the citation. This day can grade the stored id.

One paragraph in the words chapter is enough. `referral.submitted` is the cluster's event. A v2 shop would send `REF`. A FHIR shop would send a `ServiceRequest` and track the person with a `Task`. A draft definition is not the rule.

## Business calendars in Saudi Arabia

The pack's weekend is Friday and Saturday. The working-day names are Sunday through Thursday. That matches the civil-service rule, and it is why the Monday–Friday starter is the trap.

The Ministry of Human Resources and Social Development's English text of the Implementing Regulation for Human Resources in the Civil Service says, in Article 10, that official working days are from Sunday to Thursday. Article 127 lists the weekend as Friday and Saturday of each week. It lists National Day as 23 September, with an observed day when that date falls on Friday or Saturday: the preceding Thursday if National Day is a Friday, the following Sunday if it is a Saturday. It lists Eid al-Fitr from 25 Ramadan through 5 Shawwal, and Eid al-Adha from 5 Dhul-Hijjah through 15 Dhul-Hijjah. Article 128 says a single working day between two official holidays is itself a holiday. Article 11 sets ordinary government hours at seven hours, from 07:30 to 14:30, and Ramadan hours at five hours, from 10:00 to 15:00.

The national portal page carries the royal-decree wording: official working days run Sunday through Thursday, and Friday and Saturday replace Thursday and Friday as the weekly holidays. Reuters dates that switch to 23 June 2013. The regulation is the rule the calendar file should be read against.

The ministry's labor-law page is a different regime: at most eight hours a day or forty-eight a week, and in Ramadan at most six hours a day or thirty-six a week. Friday is the weekend for workers and may be replaced for some work after notice to the labor office. A cluster can have civil-service staff, contracted staff, and shift rosters together. The SLA clock in `pol-sla.md` counts working days. Ramadan shortens a day for those regimes. It does not remove a Sunday–Thursday date from a two-day count. A business-hour SLA would need the Ramadan timetable. This policy does not. One sentence in the student chapter should say so, so a careful reader does not skip Ramadan dates that are still working days.

Article 127 states the two Eids in Hijri. Umm al-Qura is the Kingdom's Hijri calendar. Its FAQ says religious dates follow that calendar's astronomical calculations and can differ by a day where the crescent is sighted. The worker's rule is the one the lesson already uses: `holidays` is a list of Gregorian dates, updated when an announcement is made. Computing Eid inside `add_working_days` is the wrong design. The pack's three March 2027 dates are fixtures. This research does not call them an announced Eid. National Day's observed-day rule and Article 128's bridge day become concrete dates before they enter that list. The worker skips dates it is given. It does not encode Article 127. An ungraded question can ask where 23 September would sit if it fell on a Friday.

**Maturity.** The Sunday–Thursday civil-service week is proven for this client's SLA story. A single coded Hijri engine is experimental. Ramadan hour tables are proven as regulation and out of scope for a day-count function.

## Human approval as a state

A boolean `approved` collapses four different situations the course already separates: waiting (`approval.held`), a tool that is not allowed to run until an id exists (Lesson 4's `approval: true` on `slots.book` and `referral.return`), a dead letter that never opened an approval, and a duplicate that is flagged and still waiting. Lesson 4 also uses `pending` for an approval id that has not been decided, and it fails a return that leaves without a coordinator. The pieces are in the course. They are easy to flatten into one flag because the tool catalog's field is named `approval` and its type is boolean.

The production object is a row: state name (`approval.held` or `dead-letter`), one approval id from the system of record or none, hold (`none`, `open`, or `released`), `booked` false, the pinned criteria id, and the coordinator as the actor being waited on. Accepted and returned belong to a later policy. This day does not perform them.

Temporal's approval pattern adds a timeout. This policy does not say what happens if the coordinator never acts. An auto-return would break the acceptance line. The state stays `approval.held` until a later lesson's signal. A timeout is a future case with its own sentence. FHIR task status is the vocabulary for a later integration lesson. The mapping sentence for this day is short: `approval.held` is a task waiting for a performer. It is not `accepted` and not `completed`.

**Maturity.** Human tasks as first-class workflow states are proven in business-process practice. Temporal's signal-and-wait is a proven description of how a durable engine implements that wait, and an emerging dependency if this lesson tried to host it. A boolean on a tool catalog is a useful gate and a bad model of the referral. Teaching the boolean as the workflow would be experimental.

## What this research says the lesson may touch

Hands-on, in the existing Python harness: the calendar file, sequence versus delivery, a persisted idempotency key, in-force versus draft, a pin of the criteria id, duplicate-still-held, hold and release, a retry budget, a dead-letter row, and `approval.held` with an id that the mock returns.

Name-only, in a comparison card of about a page: Temporal's "observed once, executed more than once," Restate's journal and 24-hour idempotency retention, DBOS's exactly-once inside one database transaction, the outbox's duplicate publish, Hohpe's process manager and his warning against using it for everything, claim check for the letter, `REF^I12` versus an order, FHIR `Task` status, and the Hijri announcement rule.

Out of the lesson: installing any of the three engines, parsing HL7, calling a model, booking, computing Ramadan hours into the due date, and encoding Article 127 in the counter.
