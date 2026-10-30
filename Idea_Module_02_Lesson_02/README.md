# Idea — Module 02 Lesson 02 — Feeds

Research only. Nothing in this folder changes the course. The lesson under study is `rel-m02-l02` (Module 2, Lesson 2 — Feeds). The student pack, the solution pack, `course_design/module-02.md`, `course_design/slides/module-02-lesson-02.md`, the curriculum map, `problem_simulation/alwaha/engagement/m02_l02.py`, and `test_m02_l02*.py` were read and left untouched.

## Recommendation

Rebuild this lesson in place. Keep the trap, the secret-hiding checker, the synthetic fixtures, and the rule that one person holds every role. Delete the paste-the-answer chapters. The graded climax becomes a **data contract for the wait mart**, with an idempotent consumer and a channel policy beside it.

Webhook handlers plus a markdown schema registry under-teach enterprise integration. An FDE on this day decides, per system, among a domain-event subscription, log-based change data capture, and a snapshot poll; puts an anti-corruption layer on HL7; treats at-least-once delivery as normal; and refuses to let `wait_days` become the business baseline. The course already planted that last defect as `p-clock` (the mart starts the clock at booking). The current lab only asks the student to name `booking_date` and to set `trusted` false.

| Maturity | Use it for |
| --- | --- |
| Proven | Transactional inbox, at-least-once plus consumer idempotency, Confluent compatibility modes, HL7 accept versus application acknowledgements, WhatsApp's 24-hour customer service window, dbt contracts as shape guarantees, Evans's anti-corruption layer |
| Emerging | AsyncAPI as the event contract the cluster actually publishes; FHIR R5 Subscriptions as the feed for hospitals that can leave HL7 v2; Open Data Contract Standard as the YAML shape of the mart contract |
| Experimental | A laptop Debezium cluster as the lab; treating a semantic layer as proof the metric is true; an LLM that maps HL7 segments into bookings |

## The six files

| File | Job |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What `rel-m02-l02` teaches, what the checker grades, and where the paste hides the design |
| [02-industry-research.md](02-industry-research.md) | Official sources: schema registry, AsyncAPI, CloudEvents, HL7 acknowledgements, FHIR Subscriptions, WhatsApp policy, outbox and inbox, data contracts |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Three integration architectures, the anti-corruption layer, the mart contract, synthetic fixtures, failures |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Self-paced roles, exercises, checks, and how a solution is allowed to look |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | What to delete, what to add, which lessons to spawn, tradeoffs, links |

## One-page recommendation

**Keep.** `chk-journey` hiding the extra field, the dropped field, the wait figure, the owner, and the watermark. The sprint order (subscription before the mart). Replay of `session.cancelled` as a duplicate `event_id`. A rejected SMS that releases the hold. A cancellation with no slot that escalates and does not book. Zone placement of `int-engine` and `wf-session-cancelled`. The access manager's line that the mart figure is not the desk's number. One person, five roles, no timetable.

**Change the climax.** `mart.py` today returns `{"clock": "booking_date", "trusted": False, "wait": <cell>}` and `mart.md` must contain the column name and must not contain the figure. That passes a student who thinks `booking_date` is a correct start of waiting. `p-clock` says the opposite: the dashboard understates waiting because the clock starts at booking, not at referral, and the fix is corrected SQL, not a model. The contract has to say who owns the extract, the grain, the time anchor, and the prohibition on using the figure as a baseline.

**Change the worker.** The finished `cancel.py` selects a row, calls `sms.send`, then inserts. A crash after the send and before the insert delivers the text twice on replay. Azure's idempotent-consumer note calls that window out, and names the transactional inbox as the fix: business effect and deduplication marker commit together. The lesson's happy-path replay never opens the window.

**Change the feeds story.** `eref` as a webhook is one pipe. HL7 v2 through `int-engine` is a second, and the engine is an anti-corruption layer that drops a segment value (trainer-only `hl7.md`). The `bi` mart is a third: a snapshot, which is why polling stays legitimate there after polling `eref` is retired. The packet's `dms.md` is the document change feed, not database CDC. Say that in the lesson so the word "change feed" does not become a shrug.

**Channel policy is graded or it leaves the day.** Meta's service-message page (updated 21 May 2026) says a user message or call opens a 24-hour window, a later user message or call resets it, and a closed window allows only pre-approved templates. The API's success response means the request was accepted, not that the message was delivered. The course's `wa.md` says "session window" and "registered template" and the checker scores SMS only.

**Do not** add a live broker, a live WhatsApp app, or a Debezium cluster. The synthetic pack can grow a second schema version, a crash fixture, a closed WhatsApp window, and a contract YAML. Lesson 3 already owns receipt timing. This lesson hands it an outbox row and a channel decision.

## What the checker grades today

`chk-journey` re-imports `work/app` and reads the markdown pages. A hand-edited trace does not count. The pass the student chapters currently manufacture is:

- `intake.accept` returns webhook mode, stores `referral_id`, ignores a key the registry does not list, and drops `letter` because that value is the watermark.
- `cancel.apply` returns the stored row for a repeated `event_id`, stores `compensated` and a released hold when `sms.send` rejects `bkg-2`, and stores `escalated` with no booking when `slot` is false.
- `mart.read` names `booking_date` and sets `trusted` false. `mart.md` contains that column name and does not contain the wait integer. The integer is still returned on the trace.
- `sprint.md` mentions a subscription or a webhook before it mentions the mart.
- `states.md` has four patient lines. `zones.md` places `int-engine` in `zone-hospital` and some row in `zone-private`. `sms.md` contains "booking" and no ten-digit run.
- `knowledge.md` has a line with `eref` and a line with `book` plus `not` or `once`.

`journey_m02` treats a true `trusted` flag, or a clock other than the date column, as "wait number was used as truth." The shell's bug and the semantic bug are the same failure string. `p-clock`, in the facilitator problem table, is more specific: the dashboard understates waiting because the clock starts at booking, not at referral, and the fitting fix is SQL, not a model. The student can pass without writing that sentence. Chapters 06 and 08 contain the functions that pass. `prepare_work.py` restores the shells, and the recovery text says to paste again.

The HL7 demo prints two lines and the scratch sheet is ungraded. Solution `hl7.md` records a dropped mapping. Students are told not to write that file. `wa.md` is three sentences and the checker scores SMS. `dms.md` says the change feed is out of scope. In the systems note, `dms` is the document system, not a database log.

## What "data contract" means on this day

A dbt model contract can force column names and types and still accept `wait_days` as an integer. dbt's semantic validations check that the YAML is coherent and that the SQL runs. They do not ask whether the interval matches the desk. PayPal's published contract template has a place the type check lacks: a business name, a transform description, an owner, a classification, an SLA. The rebuilt `contract.md` uses that habit in the course's own headings.

The contract names `bi` as publisher, refuses "one row, one person," names the date column as the warehouse start at booking, forbids the figure as a patient quote and as a value baseline, and says a snapshot is not a subscription. `referral.submitted` carries `occurred_at`. After this lesson the assistant can say the referral time when the event is in the inbox, and "unknown" when it is not. It does not fill the hole with the extract. Module 3 still owns identity matching. This day only makes the false grain visible with a second CSV row.

## Pipes, in one screen

| System | Choice | Maturity of that choice |
| --- | --- | --- |
| `eref`, `session.cancelled` | Webhook, inbox keyed by source and id, send after commit | Proven |
| HL7 from Nakhl and Safra | Anti-corruption layer, loss count, accept-level reply while the mapping is open | Proven pattern. Segment parsing stays out |
| `h-wadi` later | FHIR R5 rest-hook picture, not a second lab | Emerging in this estate |
| Mart and `sched-ain` | Snapshot poll under the contract | Proven. Polling is not retired everywhere |
| Database CDC | Written rejection for `eref` | Proven technology, wrong default here. A Debezium install is experimental for the course |
| WhatsApp | 24-hour window opened by the user; template or escalate when closed; API accept is not delivery | Proven Meta policy, graded as four rows |
| `dms` | Not built | It is the document feed |

## How to read the maturity labels

A label attaches to a practice in this course, not to a vendor. FHIR Subscriptions are a published specification and still an emerging default where hospitals emit HL7 v2. "Experimental" means it should not be the student's critical path. Vendor sentences about their own accuracy, including the Looker and PayPal case study, are quoted in the research file as claims and are not used as evidence that a semantic layer would correct `p-clock`.
