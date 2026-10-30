# Inherit a running system

The student does not receive an empty repository and a generator command as the assignment. They receive a work tree that already talks to local ports, and a simulator whose hospitals already have four years of fractured state. Their first failing check is against that state.

## What CI publishes per release

For profile `practice` and release `R`, the pack build in [02-gold-and-faults.md](02-gold-and-faults.md) produces a student-facing snapshot and a facilitator-only tree.

Student-facing, inside the lesson pack:

| Path | Role |
|---|---|
| `snapshots/<R>/<system>.sqlite` | Projection at `R`'s cursor. This is the hospital. |
| `snapshots/<R>/lock.json` | Profile, seed, release, `release_seq`, prefix event-hash, per-system projection hash. No payloads and no gold fields. |
| `snapshots/<R>/checkpoint.json` | Header the runtime log copies: `release_seq`, prefix event-hash, `history_start`. |
| `snapshots/<R>/ports.json` | Fixed localhost ports for practice. |
| `inherit/<R>/work/` | Adapters and tests copied from release `R-1`, still aimed at those ports. |
| `packet/release/` | The public files this release adds (OpenAPI, drops, interface notes). |
| `deltas/<later-release>.jsonl` | Events a later `advance` may append: decisions, product changes, partner behavior. No canonical person stream. |

Facilitator-only, absent from the student pack:

| Path | Role |
|---|---|
| `truth/<profile>/<R>/` | Gold graphs and `MANIFEST.sha256`. |
| `eval/<R>/` | Expected end-state hashes of scripted journeys. |
| Assessment snapshots | Other seed, other site names. Built on the grading service. |

`lock.json` carries the facilitator event-hash and the projection hashes. The student machine can recompute the projection hashes from the sqlite files. It cannot recompute the event-hash, because the canonical log stays on the build machine. `checkpoint.json` stores `release_seq` and that prefix hash so runtime appends start after the published world. `his-wadi.sqlite` contains Wadi's MRNs and clinic codes. It does not contain `canonical_person_id`. Opening the file shows the same partial system an integrator would see.

## Boot

```text
python -m alwaha.sim up --profile practice --release rel-m02-l05
```

Student role does the following and then listens:

1. Create `var/` outside the work tree. Do not generate a population.
2. Copy `snapshots/rel-m02-l05/*.sqlite` into `var/proj/`. Refuse to start if a projection hash disagrees with `lock.json`.
3. Create a runtime SQLite log whose first row is the checkpoint: `release_seq` and the prefix event-hash, payload empty. Later commits use `seq` greater than `release_seq`. The canonical history log is not in this pack.
4. Require `release_seq > 0` and `checkpoint.history_start` of 8 January 2023, with `as_of` on or after that date. There is no `--init-empty` flag. A cursor that would open an empty hospital is an error.
5. Start `append --mode runtime`, `project`, and `serve`.
6. Return from `up` when every cursor equals `release_seq` and `/ready` is 200.

If the snapshot is missing, student-role `up` exits. It does not call `worldbuild`. Deleting a projection file and restarting copies the snapshot again. Replay from the canonical log is an author action. Authors rebuild with `python -m alwaha.worldbuild --profile practice --release rel-m02-l05` and the published lock must match. That rebuild is the determinism test. It is not the student's first step.

`/ready` returns the release id. It does not return a fault id or a gold field.

## The work tree they inherit

`inherit/rel-m02-l05/work/` is the previous release's adapters. It already contains a Wadi client, an eref client, an SMS client, and a client that still calls a live slot route for Ain. Its unit tests play cassettes recorded against `rel-m02-l04`. Those tests stay green. The same calls against `serve` are already red, because `dec-ain-slots` has reversed and because the projections contain the standing defects.

The student edits `work/`. They do not edit `snapshots/`. `sim up` will not overwrite `work/`.

At the moment `rel-m02-l05` is listening, the projections already show:

| System | Already true |
|---|---|
| `his-nakhl` | Reused MRNs. A subset of PID dates stored without an era marker. |
| `his-safra` | A merge event and a later reverse. SIU rows are not in `occurred_at` order. |
| `his-wadi` | FHIR JSON from the projector. Encounters before the code event use `END-01`. Later ones use `ENDO-CLN`. No cluster-wide person id. |
| `sched-ain` | A nightly file. The live book route returns the fixed queued body. |
| `eref` | The `pending` key is absent. |
| `insure` | Eligibility whose source event is 48 case-hours behind `as_of`. |
| `dms` | Search hits include the draft and the unauthorized circular. |
| `phc-templates` | v3 fields. |
| `catalog` | `END-01` still defined, because that projector ignores `CodeRetired`. |
| `proc` | The team's GPU buy order, acknowledged late, promised after 8 February 2027. |

Interface notes describe the wire. They do not list this table as a cheat sheet of causes. The causes are the gold graphs.

## A later release while their process is running

```text
python -m alwaha.sim advance --release rel-m03-l03
```

`advance` is a command to the running `append` process. It is not a fourth process and it does not restart `serve`. It appends `deltas/rel-m03-l03.jsonl`, including `DecisionReversed` on `decision/dec-v4-scope`, after checking that file's hash against the pack. Those delta events are the ones student-visible projectors apply. Canonical person events are not in the delta. Projectors catch up. The Wadi port, the document search, and the eref port stay bound. `work/` is left in place.

After the cursors reach the new sequence:

- v4 is in force for `endo`, `ophth`, and `card`
- referrals whose start event carries the v3 hash still carry that hash
- adapters written to the earlier decision now fail the citation check and the in-flight check for different reasons
- the student's own database, if they created one, is theirs; `advance` does not drop it

An advance that would require rewriting a payload already committed is a failed transaction. The student keeps the old behavior until the new events are projected, which is the partial-view lag made operational: `insure` still will not show an eligibility event until 48 case-hours have passed inside the log.

## Grading a submission

The grading service does not attach to the student's `var/`. For each submission it:

1. Creates `var/<submission_id>/`.
2. Restores the assessment snapshot for that release (same three processes, assessment seed).
3. Sets `ALWAHA_CLOCK=case`.
4. Points the journey driver at the student's `POST /v1/chat` and at this submission's `ports.json`.
5. Runs `grade(...)`.
6. Deletes the directory. If Postgres was opted in, it destroys that container.

One submission's hold cannot remain for the next submission, because the next submission is a new directory and a new log prefix. This is the Testcontainers property (a disposable dependency per run, cleaned up after the run, including after a crash) implemented with a directory. The container is optional.

The service returns `check_id` and pass or fail. It does not return `truth/`, the toxic row, or a model explanation.

## What the student is trusted to rebuild

On practice, a second `worldbuild` with seed `20270110` is supposed to match `lock.json`. That is allowed and encouraged for authors, and it is available to a student who wants more rows via the existing `small` or `personal` profile. Those profiles still compile from gold-before-text. They do not author a second hidden truth.

The assessment profile is not in the tree they were given. Reading practice gold, if they have built it locally, is outside the assessment. The score that matters is the fresh assessment world on the grading service.

## Commands the lesson can print

```text
python -m alwaha.sim up --profile practice --release rel-m02-l05
python -m alwaha.sim advance --release rel-m03-l03
python -m alwaha.check --release rel-m03-l03 --work ./work --profile practice
```

`check` on practice uses the practice gold the local build stored, still with toxicity 1 and jitter 0, still without a model. It is the same function the service runs. The profile and the seed differ.
