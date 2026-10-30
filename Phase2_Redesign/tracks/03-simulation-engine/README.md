# Simulation engine

Build specification for the Al-Waha simulator. This track does not change `problem_simulation/`, the lesson packs, or any `Idea_*` folder. Implement the package beside the current generator, then point the existing entry points at it.

The course already has `python -m alwaha.worldbuild` (seed to pack), `python -m alwaha.serve` (stateful mocks), and `python -m alwaha.check` (pass or fail on mock end state, answer withheld). Keep that contract. Replace the hidden shape: one event log, one projection per system, gold graphs written before any generated sentence, faults that are constants on the graded path, and a student who attaches to a hospital that is already running and already wrong.

## The three processes

One Python package, `alwaha.sim`. A supervisor starts three operating-system processes. They do not share a write connection.

| Process | Module | Writes | Reads |
|---|---|---|---|
| `append` | `python -m alwaha.sim.append` | The event log, the outbox, and (build mode only) gold | Inbox of commands |
| `project` | `python -m alwaha.sim.project` | One store per system | Outbox, in `seq` order |
| `serve` | `python -m alwaha.sim.serve` | Inbox files only | That system's projection, then the fault gate |

`python -m alwaha.sim up` is the supervisor. It is not a fourth world. `python -m alwaha.check` is a pure function over gold, a projection frozen at a sequence number, and the student's artifact. Detail is in [01-engine.md](01-engine.md).

Default store is SQLite through the stdlib `sqlite3` module. Docker is optional and is allowed to run Postgres only. The event bytes are the same in either store.

## Build order inside one release

1. Write gold graphs (identity, policy binding, procurement, fault schedule, fact specs). Hash them.
2. Compile history into the log from those graphs and the release calendar. Commit each event in the same transaction as its outbox row.
3. Project every system to the release cursor. Fail the build if a projection disagrees with the gold graph filtered by that system's view manifest.
4. Only then render Arabic and English from the fact specs. Freeze the bytes into the pack.
5. Restore that snapshot in `sim up`. The student work tree is the previous release's adapters, already pointed at the ports.

[02-gold-and-faults.md](02-gold-and-faults.md) specifies the files, the reversal events, and the grade abort rules. [03-inherit-dont-greenfield.md](03-inherit-dont-greenfield.md) specifies the snapshot, the inherited tree, and `advance`.

## What the running system already contains

History from 8 January 2023 through the release's case instant is already in the log when the port opens. Nakhl's MRNs, Safra's reversed merge, Wadi's clinic-code change, Ain's nightly file, a 48-hour insurance snapshot, a document search that returns drafts, and a GPU order that misses 8 February 2027 are rows in those projections. A later release appends a `DecisionReversed` event. It does not edit the earlier decision.

## Package map

Target under 200 lines per file. One concern per file. Split a system file by event family when it grows past that.

```
alwaha/sim/
  up.py                      # supervisor only
  append/pipeline.py         # gold, gate, compile, commit, then render
  append/commit.py           # log + outbox + inbox_done, one transaction
  gold/identity.py
  gold/policy.py
  gold/procurement.py
  gold/faults.py
  gold/facts.py
  gold/manifest.py
  log/event.py               # canonical bytes, sha256
  log/sqlite.py
  log/postgres.py            # optional; same SQL
  release/calendar.py
  release/decisions.py       # DecisionRecorded, DecisionReversed
  project/relay.py
  project/manifest.py
  project/<system>.py        # one file per system id in design/04
  fault/grade.py             # abort unless toxicity is 1 and jitter is 0
  fault/effects.py
  serve/app.py
  serve/inbox.py
  serve/routes.py
  check/compare.py           # no model import
  render/phrase.py           # after the gold gate; not on the grade path
  feed/synthea_rates.py      # optional; hash-pinned CSV only
```

`alwaha.sim` must not import `boto3`, a Synthea jar, a LocalStack client, or an HTTP client aimed at a public FHIR host. A unit test imports the package with those modules blocked.

## Acceptance tests

- Same profile, seed, and release: SQLite and Postgres produce the same event-hash manifest.
- `UPDATE` or `DELETE` on `log` raises.
- Render refuses to start when the gold manifest is missing.
- Kill `project` after it applies an event and before it stores the cursor. Restart. The projection hash matches a clean run.
- At `rel-m03-l03`, an in-flight referral still carries the criteria hash from its start event.
- `alwaha.check` exits before scoring when any graded fault has toxicity other than 1 or jitter other than 0.

## Documents

| File | Contents |
|---|---|
| [01-engine.md](01-engine.md) | Processes, log, outbox, projections, local runtime, optional AWS |
| [02-gold-and-faults.md](02-gold-and-faults.md) | Gold-before-text, fault schedule, reversals, deterministic checks |
| [03-inherit-dont-greenfield.md](03-inherit-dont-greenfield.md) | Snapshot restore, inherited adapters, advancing a release |
| [04-sources.md](04-sources.md) | Primary sources and the three refused cores |
