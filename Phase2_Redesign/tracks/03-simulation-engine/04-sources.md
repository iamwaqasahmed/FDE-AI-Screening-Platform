# Sources

Primary sources for the engine, then the three products this design refuses as the core. Course files (`problem_simulation/design/`, the current `alwaha` package, the cross-cutting simulation notes) are the system this spec extends. They are not external evidence.

## Primary

### 1. Event log as the system of record

Martin Fowler, "Event Sourcing", 12 December 2005.

https://martinfowler.com/eaaDev/EventSourcing.html

Every change is an event stored in apply order for the life of the state. He lists complete rebuild (discard state, replay onto empty), temporal query (state at a time by replaying up to an event), and replay to correct a past event. This engine uses the first two. A stakeholder reversal is a later event, not a rewrite of an earlier one, so the third facility is deliberately unused. Complete rebuild is `project` deleting one system's store and replaying the log prefix. Temporal query is the release cursor.

### 2. Working copies, and replay that stays local

Martin Fowler, "What do you mean by Event-Driven?", 7 February 2017.

https://martinfowler.com/articles/201701-event-driven.html

The event log is the source of truth and the system state is derived. A version-control log is his example: the editor can use a working copy and ignore the commits. Different working copies may use different schemas. Replay does not have to be asynchronous; a local commit is synchronous. Replay becomes unsafe when results depend on calls to outside systems. Schema change of events over time is a real cost.

Taken literally: Nakhl, Safra, Wadi, Ain, `insure`, and `dms` are working copies. `project` performs no network IO. Partners are projections plus a fault table, so a rebuild does not call a payer or a public sandbox. Event types are added per release; old rows stay.

### 3. Read models per question

Greg Young, *CQRS Documents*, chapter "CQRS and Event Sourcing" (the 2010 PDF collected on the CQRS site).

https://cqrs.wordpress.com/documents/cqrs-and-event-sourcing-synergy/

https://cqrs.wordpress.com/wp-content/uploads/2010/11/cqrs_documents.pdf

Young's split: the domain consumes commands and produces events; the read model consumes events and produces the objects clients actually query. The write side stores events, so it does not also keep a relational current-state model. A query such as "everyone named Greg" is impossible against the log alone; that is what the read model is for. He also notes the relay problem between the two sides.

Taken literally: `append` is the domain. Each file under `project/` is a read model with an impedance mismatch that is the point (Wadi's codes, Ain's file, the insurance lag). The outbox is the relay. Students query ports, never `GetById` on the log.

### 4. One transaction for the event and the handoff

Chris Richardson, "Pattern: Transactional outbox".

https://microservices.io/patterns/data/transactional-outbox.html

A command that updates state and publishes a message cannot use 2PC across a database and a broker safely. Write the message into an outbox table in the same transaction as the state change. A separate relay publishes afterwards. The relay can publish a message more than once if it crashes after the send and before it records that fact. Consumers must be idempotent. Order follows the transaction order.

Taken literally: the state change is the log insert. The same transaction inserts the outbox row and `inbox_done`. `project` is the relay. Idempotency key is `event_id`. No broker is required, which keeps the process count at three. Outbox rows are retained so the course does not take on the delete-churn cost of a high-volume outbox.

The AWS Prescriptive Guidance page describes the same pattern with SQS and is not a dependency:

https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

### 5. Fault vocabulary, with the random draws left out

Shopify, Toxiproxy README and `toxics/latency.go`.

https://github.com/shopify/toxiproxy/blob/main/README.md

https://github.com/Shopify/toxiproxy/blob/main/toxics/latency.go

Toxics are directional (`upstream` or `downstream`). `toxicity` is the fraction of connections affected and defaults to 1. Latency is `latency` ± `jitter` milliseconds. The latency implementation adds `rand.Int63n(jitter*2) - jitter` when jitter is positive. The stub applies the toxic when `rand.Float32() < toxicity`. Disabling the proxy is the documented way to take a service down. With no toxics, overhead is well under a millisecond, so the idea fits a laptop.

Taken literally: the graded schedule stores toxicity as the integer 1 and jitter as the integer 0, and `fault/effects.py` is a pure table. The engine does not shell out to the Go proxy on the grade path, because those two `rand` calls are unseeded. Practice sleep uses the stored `latency_ms`. `alwaha.check` aborts if a graded row breaks the two integers.

### 6. A fresh dependency per run, then delete it

Testcontainers, "Getting Started".

https://testcontainers.com/getting-started/

Start real services in containers for a test, wait until they are ready, run, then destroy containers, volumes, and networks, including after a hard kill (their Ryuk sidecar). Ports are mapped to random host ports so parallel runs do not collide. Each pipeline gets its own set, so one run's data does not leak into the next.

Taken literally: the required isolation is a new `var/<submission_id>/` and a delete at the end. Postgres, when an author sets `ALWAHA_LOG_URL`, is the one container, image `postgres:16-alpine`, digest pinned, random host port, destroyed after the grade. The student's hospital is not a long-lived shared database.

## Refused as the core

### Synthea

MITRE Synthea, "Recreating a Dataset".

https://github.com/synthetichealth/synthea/wiki/Recreating-a-Dataset

A matching population needs the same commit, the same `-s` seed, the same clinician seed `-cs`, the same reference date `-r`, and the same end date `-e`. Unset, seed becomes `System.currentTimeMillis()`, and reference date and end date become the day of the run. A longer end date adds events and can change fields such as whether a condition is still active. Time zone changes exported timestamps. The default export is a longitudinal FHIR chart per person (`exporter.fhir.export`, transaction bundle), which is one complete record rather than Nakhl versus Safra versus a nightly file.

Optional feeder, and only this: `feed/synthea_rates.py` may read one CSV whose sha256 is a constant in that file, produced offline by a pinned Synthea commit, and may expose integer specialty rates to the demand compiler. The grade does not execute Synthea. FHIR bundles from Synthea are not an input. If the CSV is absent, demand uses the course tables.

### LocalStack

LocalStack, "Auth Token".

https://docs.localstack.cloud/aws/getting-started/auth-token/

An auth token is a mandatory credential to start the LocalStack container. The partners in this course are hospitals, national identity, SMS, WhatsApp, insurance, documents, and a file drop. An AWS-shaped control plane would be a second enterprise. The engine has no LocalStack module. The optional AWS deployment in [01-engine.md](01-engine.md) runs these three Python processes and, if wanted, RDS. It does not emulate AWS APIs for the student.

### Public FHIR sandbox

The public HAPI server is a shared voluntary host (`http://hapi.fhir.org`, R4 base `http://hapi.fhir.org/baseR4`). MITRE's FHIR-for-research notes describe it that way and show Synthea bundles posted to a local `hapiproject/hapi` container instead:

https://mitre.github.io/fhir-for-research/modules/synthea-test-server

A public server has no Al-Waha log, no release cursor, and no per-submission discard. An empty local HAPI would teach the wire format and would still be one database pretending to be every hospital. Wadi's wire format is `project/wadi.py` writing JSON from the log. Document history is the event stream for that document, which the route can list. The binding decision stays in `policy.json`.

## What the engine refuses to simulate

Recorded here so the process list in [01-engine.md](01-engine.md) stays closed.

- A live or hosted model inside `alwaha.check`, including a model asked to judge citations, prose, or privacy.
- Synthea charts, LocalStack, and `hapi.fhir.org` as the world the student inherits.
- Unseeded jitter or a toxicity coin-flip on a graded run.
- Wall-clock "today" as the simulation end, or instance NTP as `occurred_at`.
- A shared mutable world left behind for the next submission.
- An offensive cyber range beside the scripted threat rows.
- Physiology, a complete chart, or any output that could be read as clinical advice.
- Real payer, WhatsApp, national-identity, or GPU-vendor sandboxes.
- The student's framework choices. The contract and the mock end state are the graded surface.
- A rewrite of a committed event when a stakeholder reverses a decision.
- A message broker, an AWS SDK, or a FHIR server process as a required fourth process.
