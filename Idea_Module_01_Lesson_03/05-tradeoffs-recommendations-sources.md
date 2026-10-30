# 05 — Tradeoffs, recommendations, and sources

## Recommendation

Teach `wf-intake` as a policy-correct process with one durable transaction, not as a tour of workflow servers. The student lab is plain transactional messaging: a referral row, a stored `event_id`, and an outbox row commit together; the hospital mock honors an idempotency key; a crash between hold and commit is graded; the in-force criteria id is pinned at start. Temporal, Restate, and DBOS stay on a comparison card that quotes their own limits. The workflow still stops at `approval.held`. It still does not book. Ain still has no slot API.

That choice fits a self-paced forward-deployed lesson whose next chapter is an agent, and whose classroom form shares a day with that agent. It also fits the checks the course already trusts. `chk-events` grades behavior and hides the answer. The redesign adds cases. It does not replace the grader with an essay about frameworks.

## What is in the lesson, and what is name-only

| Idea | Where it lives | Maturity for this course |
| --- | --- | --- |
| Sunday–Thursday SLA calendar, holidays as data | Student edits `add_working_days` | Proven |
| Sequence versus file order, event id versus referral id | Student edits grouping and sort | Proven |
| In-force status versus higher draft, id pinned at start | Student edits selection; gold checks the pin | Proven practice, new scenario |
| Duplicate flagged, still held, not booked | Student edits the flag | Proven for this case |
| Hold, release on failure, no book, Ain queued is not booked | Student edits effects | Proven for this case |
| Retry budget then dead-letter record | Student edits effects; channel is named in the note | Proven pattern, small record |
| `approval.held` as a state with an id from the mock | Note plus log | Proven workflow practice |
| Transaction plus outbox plus crash | Given store, graded crash | Proven pattern, small harness |
| Temporal replay, at-least-once activities, approval signal | Comparison card | Proven product, name-only here |
| Restate journal, idempotency header, 24-hour default retention | Comparison card | Emerging, name-only |
| DBOS checkpoint, exactly-once inside the application database | Comparison card | Emerging, name-only |
| Saga as one compensation for the hold | The release row | Proven pattern, narrow scope |
| Choreography across services | Not built | Name-only, and a poor fit |
| Claim check for the letter | Note, plus the log must not copy the letter | Proven pattern, store not built |
| HL7 `REF^I12`, FHIR `ServiceRequest` and `Task` | One paragraph | v2 proven, FHIR Task Trial Use |
| Hijri computation, Ramadan hour arithmetic, National Day encoder | Reading only | Proven as regulation, experimental as code in this worker |
| LLM extraction or an orchestration-framework install | Deleted from the claim | Experimental for this day |

## Tradeoffs among the four runtimes

**Plain transactional messaging** makes the commit boundary visible. A student can see the three writes and the crash. It does not give timers that survive for weeks, a query API for a waiting workflow, or replay of a Python stack. Lesson 4's agent is still a Python program that reads a row. That is the integration this course needs. The cost is that someone may leave thinking a SQLite file is a workflow product. The card exists so they do not.

**Temporal** gives the best published account of the human wait and the best warning about exactly-once. The activity page says the activity is observed completed exactly once and may execute multiple times. The approval pattern blocks on a signal with a timeout and keeps the timer in the server. Those two pages are the reading. The cost of making Temporal the lab is operational and conceptual at once: a server, a worker, deterministic workflow code, and activity timeouts, on a day whose traps are Friday and a draft PDF. Students would debug the SDK while the calendar bug waited. The idempotent hold would still have to be written, because Temporal does not make `his-wadi` idempotent.

**Restate** gives a journal and a one-line idempotency header, which maps cleanly onto `event_id`. The documented default retention is 24 hours. The lesson's policy has no such expiry. Using Restate without raising that number would make a next-day replay of the same event id start a second intake. That is a sharp teaching point and a bad default for a graded lab. Name it. Do not install it.

**DBOS** gives exactly-once execution for a function whose writes commit in the same database transaction as the durability record. The Python tutorial says replay returns the stored result and does not re-execute that function. A hold that leaves the process and hits another system is outside that sentence. DBOS would also add decorators and a system database the student must not confuse with `eref`. The visible SQL transaction teaches the same atomicity with less vocabulary. Prefer that.

Hohpe's process-manager warning applies to all three products and to a home-grown engine. A process manager can implement almost any integration and can hide the actual rule. The actual rules here are the calendar, the sequence, the criteria status, the missing Ain API, and the human state. A framework chapter that never mentions Friday has failed the client.

## Saga scope, stated narrowly

A full saga that cancels the referral when the hold fails would accept a business decision the policy reserves for a coordinator. The compensation in this lesson undoes the hold only. The referral stays in `approval.held`. Richardson's orchestration-versus-choreography split is why this stays a single process: the coordinator needs one row. Choreographed consumers for hold, criteria, and duplicate would make "where is this referral" a log search. That design is a poor fit for intake and a possible fit for side effects after a decision, which is Lesson 4's SMS, not this morning's work.

Garcia-Molina and Salem introduced sagas as long-lived transactions made of shorter ones with compensations. The course can cite that origin and teach from Richardson's pages. It should not assign the 1987 paper.

## Clinical policy and calendars, stated narrowly

Pinning `crit-endo-v3` is the whole versioning lab. FHIR `PlanDefinition.effectivePeriod` explains why a published draft can exist beside an active document. The student does not create a FHIR resource. Module 3 remains the citation lesson.

The calendar worker trusts a list. The Ministry of Human Resources and Social Development's civil-service regulation is why the list says Sunday–Thursday and why Friday is the trap. The same regulation's Ramadan hours, Eid bounds in Hijri, National Day observed-day rule, and bridge day are real, and they belong in a reading box. Encoding them is how a small function becomes a calendar product. Umm al-Qura is the citation for "do not compute the crescent in the worker." The pack's March 2027 dates stay unlabeled fixtures.

Labor-law hours and the substitutable Friday are the reason the SLA calendar is not a clinic roster. Shift services can be open on an SLA weekend. The worker must not infer "closed clinic" from "non-working SLA day." Ain is unheld because the release has no slot API, which is a different fact from the weekend.

## Human state across Lesson 3 and Lesson 4

Lesson 3 ends in `approval.held` with one id and `booked` false. Lesson 4's catalog marks some tools `approval: true`, meaning they require that id, and it keeps a pending id for a return that a coordinator has not decided. The risk is vocabulary. If students learn "approval" as the boolean on the tool, they will think the intake state is a flag the agent flips. The intake note should carry one sentence into the next morning: the tool flag asks whether an id is required; the referral row says whether a person has been asked and has not yet answered. Timeouts that auto-accept or auto-return are out of policy. Temporal's timeout path is described as what a later policy would have to write, not as behavior the worker grows on its own.

## Explicit deletions

1. Delete the full correct-file paste from the student chapter.
2. Delete placeholder lines as a passing `knowledge.md`.
3. Delete the facilitator claim that the day integrates LLMs and an orchestration framework.
4. Delete the in-flight word search as the sole proof of versioning, and replace it with the pin scenario when the course is edited.
5. Delete approval ids minted in the worker, and return them from the mock.
6. Delete the in-memory set as the definition of idempotency. Keep it only as the starter bug's opposite in a single pass, then persist the key.
7. Do not delete the Friday trap, the quiet check messages, the watermark, the order pair, the draft criteria, the duplicate-still-held rule, the Ain rule, or the split between compensate and dead letter.
8. Do not add booking, an Ain API, auto-accept, auto-return, a required workflow server, a Hijri library, or an LLM extractor.

## New lesson, and lessons not to add

Add no new release between Lesson 3 and Lesson 4. Add a packet page, `patterns.md`, inside this lesson's reading. Add an optional ungraded seminar after Lesson 4, with no release id, that maps the held state to a Temporal signal and a FHIR task status. That seminar is the place for screenshots of vendor docs if an instructor wants them. It is not a gate.

Do not add a "workflow platforms" module in front of the agent. The agent lesson is where a waited approval earns its keep, because a book tool can run too early. Students who have seen `approval.held` as a row will understand that bug. Students who have spent a day installing Temporal will understand a different bug.

If a later cohort already runs Temporal at work, the comparison card is the adaptation, not a fork of the lab. They can annotate which activity would wrap `hold`. They still implement the calendar and the pin in Python. The gold file does not import their cluster.

## Risks if the redesign is done badly

A crash harness that is flaky will train students to rerun the check. The driver should be deterministic: a fault name that raises after the hold call, then a second invocation in the same grader process. No sleep, no port, no timeout race.

A pin scenario that prints `crit-endo-v3` in the failure text will leak the answer the current tests carefully withhold. The message stays `criteria moved after start`.

A comparison card that cheers for one vendor will undo the exactly-once section. Quote the limit next to the feature. Temporal's limit is multiple execution. Restate's limit is retention. DBOS's limit is the database boundary. The outbox's limit is a relay that can publish twice.

A store module that the student must write will swallow the calendar. Give the store. Grade the policy functions.

## Sources

Pages below were used as the evidence for this packet. Pattern statements and vendor guarantees are theirs. The Al-Waha pack remains fiction.

### Durable execution and exactly-once

- Temporal, "Activity Definition," idempotency and the observed-once sentence: https://docs.temporal.io/activity-definition
- Temporal, Python error-handling guidance on at-least-once activities and idempotency keys: https://docs.temporal.io/develop/python/best-practices/error-handling
- Temporal, "Approval Pattern": https://docs.temporal.io/design-patterns/approval
- Temporal, human-in-the-loop document approvals, on the durable wait: https://docs.temporal.io/guides/reliable-document-approvals
- Restate, "Key Concepts," journal and duplicate requests: https://docs.restate.dev/foundations/key-concepts
- Restate, HTTP idempotency key and 24-hour retention: https://docs.restate.dev/services/invocation/http
- Restate, service configuration, idempotency retention default: https://docs.restate.dev/services/configuration
- DBOS, "Architecture," checkpoints, determinism, and idempotent steps: https://docs.dbos.dev/architecture
- DBOS, Python "Transactions & Datasources," exactly-once for the application database: https://docs.dbos.dev/python/tutorials/transaction-tutorial

### Messaging

- Chris Richardson, "Pattern: Transactional outbox," including duplicate publish: https://microservices.io/patterns/data/transactional-outbox.html
- Chris Richardson, "Pattern: Saga," orchestration and choreography: https://microservices.io/patterns/data/saga.html
- Gregor Hohpe and Bobby Woolf, Idempotent Receiver: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html
- Dead Letter Channel: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html
- Claim Check: https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html
- Process Manager, including the warning and the Step Functions example: https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html
- Hohpe, conversation introduction, on poison messages and limited retries: https://www.enterpriseintegrationpatterns.com/patterns/conversation/Introduction.html

The saga idea originates with Hector Garcia-Molina and Kenneth Salem, "Sagas," SIGMOD 1987. This packet teaches from Richardson's exposition and does not assign the paper. The ACM record is https://dl.acm.org/doi/10.1145/38713.38742.

### Referral standards

- HL7 v2.4 chapter 11, `REF^I12` patient referral, as rendered at https://www.hl7.eu/HL7v2x/v24/std24/ch11.htm
- HL7 Australia v2 working group note on referral versus order: https://hl7.org.au/archive/hl7v2wg/7-Patient-Referral_2623498.html
- HL7 FHIR US BSeR, workflow management resources (ServiceRequest and Task): https://hl7.org/fhir/us/bser/WorkflowManagementResources.html
- FHIR task-status value set, twelve codes, maturity level 3, Trial Use: https://hl7.org/fhir/valueset-task-status.html
- FHIR PlanDefinition, status and effectivePeriod: https://hl7.org/fhir/plandefinition.html

### Calendars

- Ministry of Human Resources and Social Development, Implementing Regulation for Human Resources in the Civil Service (English PDF), Articles 10, 11, and 127: https://www.hrsd.gov.sa/sites/default/files/2023-04/Implementing%20Regulation%20for%20Human.pdf
- HRSD, labor-law working hours, Ramadan cap, and Friday weekend that can be substituted: https://www.hrsd.gov.sa/en/care-about-you/health-and-safety
- National portal, "Friday and Saturday weekend holidays," decree wording: https://my.gov.sa/en/news/6250
- Reuters, 23 June 2013, on the switch to a Sunday–Thursday working week: https://www.reuters.com/article/world/saudi-arabia-changes-its-working-week-to-sunday-thursday-idUSDEE95M055/
- Umm al-Qura calendar FAQ, astronomical dates and possible one-day difference where the crescent is sighted: https://www.ummulqura.org.sa/ar/faq

### Course artifacts this packet read

Student chapters `00` through `08`, the solution knowledge and trainer chapters, `course_design/module-01.md` Lesson 3, `course_design/slides/module-01-lesson-03.md`, the curriculum map section "Lesson 3 — Intake workflow," the packet policy, calendar, criteria, contract, and workflow shells, and `problem_simulation/tests/test_m01_l03.py`, `test_m01_l03_checks.py`, `m01_l03_worker.py`, and `m01_l03_calendar.py`. Those files are the lesson. They are not external evidence. This folder does not modify them.
