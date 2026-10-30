# Engine

## Processes

`python -m alwaha.sim up --profile practice --release <id>` starts three processes and waits until every projector cursor equals that release's sequence number. Then it opens ports.

**append** is the only writer of domain facts. Build mode (`ALWAHA_ROLE=facilitator`) writes gold, compiles history, and commits it. Runtime mode opens the log with append-only semantics and commits inbox commands. It has no HTTP port. A student-role process refuses `--mode build`.

**project** tails the outbox. It writes `var/proj/<system>.sqlite` and nothing else. It does not read another system's file. It does not call the network. Replay is a local function of a log prefix (Fowler, 2017: replaying a log that calls external systems is the failure mode to design out).

**serve** speaks the interfaces the course already publishes: FHIR for `his-wadi`, HL7 files and feeds for Nakhl and Safra, the nightly file for `sched-ain`, REST for `eref`, `nid`, `sms`, `wa`, `insure`, `dms`, `consent`, `proc`. Each route loads one projection, passes the call through the fault gate, and returns that result. The only write serve performs is an inbox file: temp, fsync, rename.

Existing commands stay as wrappers.

| Command today | Wrapper |
|---|---|
| `python -m alwaha.worldbuild` | `append --mode build`, then `project` to the release cursor, then render |
| `python -m alwaha.serve` | `sim up` |
| `python -m alwaha.check` | `check.compare` against the pinned snapshot |

## Two layers, one runtime truth

Gold graphs are the authoring form. They are written first and they are what the grader compares against. The event log is the runtime source of truth. Historical events are a pure compilation of the gold graphs plus the release calendar. After the snapshot is taken, a new fact exists only if `append` committed an event.

Projections are working copies with different schemas (Fowler, 2017). They are disposable. Delete `var/proj/<system>.sqlite`, restart `project`, and the bytes return. The log is not disposable.

A build test, run before render, asserts for every system:

```text
project(log[:release_seq], manifest[system]) == gold.view(system, release)
```

`gold.view` drops fields the manifest drops, applies case-clock lag, and renames codes. A mismatch fails the build. The rendered leaflets are not an input to this test.

## Event envelope

```text
seq          integer, assigned inside the commit transaction
event_id     sha256 of canonical(type, occurred_at, release_id, stream_id, stream_rev, payload)
type         string
occurred_at  case clock, RFC3339, suffix Z, never the wall clock
release_id   rel-m01-l01 … rel-m04-l05
stream_id    aggregate, e.g. decision/dec-v4-scope, referral/<id>, person/<gold id>
stream_rev   1..n inside that stream
payload      object, no prose
```

Canonical bytes: UTF-8, object keys sorted, separators `,` and `:`, no floats. Money, toxicity, and durations are integers (millis, basis points, or a currency minor unit). `event_id` does not include `seq`, so a rebuild produces the same ids. A duplicate `event_id` or a duplicate `(stream_id, stream_rev)` aborts the transaction.

`occurred_at` for history is taken from the case calendar: start 8 January 2023, engagement open 10 January 2027, sponsor date 8 February 2027. The compile step has no `datetime.now()` call. An import test greps the package for `datetime.now`, `time.time` used as a timestamp source, and `random.random`. The fault sleeper in practice mode is the one allowed `time.sleep`, and graded mode does not use it.

## Transaction

Chris Richardson's outbox, with Greg Young's simplification: the write model is the event, so the "business row" and the message are the same fact written twice in one transaction (once in `log`, once in `outbox`). There is no second current-state table on the write side.

```sql
CREATE TABLE log (
  seq INTEGER PRIMARY KEY,
  event_id TEXT NOT NULL UNIQUE,
  type TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  release_id TEXT NOT NULL,
  stream_id TEXT NOT NULL,
  stream_rev INTEGER NOT NULL,
  payload TEXT NOT NULL,
  UNIQUE (stream_id, stream_rev)
);
CREATE TABLE outbox (
  seq INTEGER PRIMARY KEY REFERENCES log(seq),
  event_id TEXT NOT NULL UNIQUE
);
CREATE TABLE inbox_done (
  command_id TEXT PRIMARY KEY,
  event_id TEXT NOT NULL
);
CREATE TRIGGER log_append_only BEFORE UPDATE ON log
BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER log_no_delete BEFORE DELETE ON log
BEGIN SELECT RAISE(ABORT, 'append-only'); END;
```

`commit.py` runs, in one `BEGIN IMMEDIATE`:

1. If `command_id` is already in `inbox_done`, return the stored `event_id`.
2. Insert the log row and the outbox row.
3. Insert `inbox_done`.

Do not delete outbox rows. The projector cursor is the consumer mark. A relay that crashes after the projection applies and before the cursor advances will deliver again. Each handler is idempotent on `event_id`, and the apply plus the cursor update commit in one transaction on that system's own database. That is the at-least-once behavior Richardson documents, handled without a broker.

Postgres uses the same statements. `log/postgres.py` is loaded only when `ALWAHA_LOG_URL` is set. Unset means SQLite. The manifest hash is over event bytes, so the store is invisible to the grade.

There is no two-phase commit and no required Kafka, Redis, or NATS process. A broker would be a fourth moving part and would not change the event bytes.

## View manifests

`project/manifest.py` holds one `View` per system. The projector file may not widen it.

```text
View
  system     his-wadi | his-nakhl | his-safra | sched-ain | eref | nid |
             sms | wa | insure | dms | consent | proc | catalog | phc-templates | …
  keeps      field names this store may contain
  drops      canonical_person_id, gold_cluster, vendor_queue, fault_id, …
  lag        case-clock duration subtracted from the release as_of
             insure: 48 hours; nid death flag: the seeded lag; others: 0
  ignores    event types this system deliberately does not apply
             catalog ignores CodeRetired, so END-01 stays listed
  wire       fhir-r4 | hl7v2 | file | json
  nulls      forbidden; a dropped field is an absent key
```

Wadi's FHIR resources are produced by `project/wadi.py` from events. The file maps a stream to a resource type and writes JSON. It does not run a FHIR server. History for a document is the set of events on that `stream_id`, which is what a client walks. Search returns drafts, unauthorized copies, and superseded leaflets because those events were projected, and the binding decision is not a column the search route sorts to the top.

`sched-ain` has no port for booking. Its projection is a directory of nightly files. A missed night repeats the previous file, which is a compiled event (`NightMissed`), not a missing job.

Lag is computed from `occurred_at` and the release `as_of`. It is not a race between threads. Two machines at the same release see the same insurance snapshot.

## Fault gate

`fault/effects.py` implements the Toxiproxy vocabulary: `latency`, `timeout`, `reset`, `slow_close`, `bandwidth`, `disabled`. Shopify's latency toxic draws an unseeded `rand.Int63n` when jitter is positive, and toxicity is an unseeded `rand.Float32()` draw. The graded gate does not call that code.

```text
effect(call, schedule) -> latency_ms | timeout | reset | disabled | pass
```

On the graded schedule every row has toxicity integer `1` and jitter integer `0`, so the function is a table lookup on `(partner, release, match)`. Practice `sim up` may `time.sleep` for `latency_ms` so a person feels the delay. `ALWAHA_CLOCK=case`, which `alwaha.check` always sets, skips the sleep and returns the same body and status. The check compares bytes and effect kind. It does not compare wall duration.

`fault/grade.py` runs first inside `alwaha.check`. Any graded row with toxicity other than 1 or jitter other than 0 aborts the score with the check id only.

## Commands from the student

A booking, a send, or a purchase acknowledgement the student initiates:

1. `serve` writes `inbox/<command_id>.json` and returns `202` with that id, or the stored result when `inbox_done` already has it.
2. `append` validates the command against the log prefix (idempotency key, referral start hash, Ain file-only rule).
3. The commit is either the domain event or a `CommandRejected` event. Rejection is replayable. It is not a log line that only existed in memory.

Scripted grade journeys use the same inbox. The driver is `check`, the path is `serve`, and the expected end state was hashed at pack build.

## Local runtime

| Piece | Required |
|---|---|
| CPython with stdlib `sqlite3` | yes |
| Docker | no |
| Postgres 16 | only if `ALWAHA_LOG_URL` is set |
| AWS account, LocalStack, public FHIR host | no |
| GPU, WhatsApp, payer, or national-id sandbox | no |

Practice ports are constants in the committed `ports.json` so the inherited adapters resolve without a rewrite. If a port is taken, `serve` exits and names the port. It does not pick another one. The grading service writes a per-submission `ports.json` with ephemeral ports, because parallel submissions cannot share a port. The event hash does not include the port.

Disposable Postgres, when an author opts in, follows the Testcontainers lifecycle: start `postgres:16-alpine` on a random host port, wait until ready, run the submission, destroy the container and its volume even if the process is killed. Pin the image digest in `log/postgres.py`. The core grade path never starts that container. SQLite files for a submission live under `var/<submission_id>/` and are deleted at the end of the grade.

## What an AWS deployment of the simulator would add

This is a deployment of the three processes, not of the student's assistant. The student's `POST /v1/chat` still runs where the student runs it. The grader sends scripted journeys at that contract and reads artifacts.

| Laptop | Same three processes on AWS | Why it is optional |
|---|---|---|
| SQLite file | RDS Postgres, same schema, digest-pinned major version | Event bytes already match across stores. RDS adds a bill and a network hop. |
| `var/<submission_id>/` deleted at the end | One task per submission, disk destroyed after the check | Needed only when many grades run at once. A laptop grades one submission at a time. |
| Fixed or ephemeral localhost ports | Private IP of that task, still written to a `ports.json` the driver reads | An ALB would add a shared front door. One team's booking must not be visible to the next. |
| In-process fault table | The same function inside the task | AWS Fault Injection Simulator draws its own failures. That breaks toxicity 1 and jitter 0. |
| Case clock in the log | Case clock in the log | Instance NTP is not `occurred_at`. |

A cloud run is accepted when its event-hash manifest equals the laptop manifest for that seed and release. A difference means the cloud run is discarded. The package import graph does not include `boto3`. A task definition, if someone writes one later, is a shell around `python -m alwaha.sim up` and a `DATABASE_URL`. It is not on the path that produces a score on a student machine.

## Module boundaries

The supervisor, the commit, each gold file, each system projector, the fault table, and the comparer are separate modules so a change to Wadi's FHIR mapping does not reopen the insurance lag or the grade function. Shared code is `log/event.py` (canonical bytes) and `project/relay.py` (cursor and redelivery). World constants stay in `gold/` and `release/`. `check/compare.py` receives paths and returns pass or fail. It does not import `render/phrase.py`.

`feed/synthea_rates.py` is the only optional feeder. It reads one CSV checked into the facilitator tree, checks a pinned sha256, and returns integer rates to the demand compiler. Missing file: the compiler uses the course demand tables. The module has no subprocess call and no FHIR types. LocalStack and a public FHIR sandbox have no module.
