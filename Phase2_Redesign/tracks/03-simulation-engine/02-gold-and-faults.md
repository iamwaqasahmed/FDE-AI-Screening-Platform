# Gold graphs and fault schedules

## Write order

`append/pipeline.py` runs these steps in order. A later step is a function call that is not registered until the previous step's hash is on disk.

| Step | Output | Allowed to call a model |
|---|---|---|
| 1 | `truth/<profile>/<release>/identity.json` | no |
| 2 | `policy.json` | no |
| 3 | `procurement.json` | no |
| 4 | `faults.json` | no |
| 5 | `facts.json` | no |
| 6 | `MANIFEST.sha256` over steps 1–5 | no |
| 7 | log rows compiled from those files and `release/calendar.py` | no |
| 8 | projections, then the agreement test in [01-engine.md](01-engine.md) | no |
| 9 | `render/` prose plus a sidecar | yes, once, at pack build |

Step 9's sidecar stores `fact_id`, `lang`, `content_hash`, and `prose_hash`. `content_hash` is sha256 of the canonical fact spec plus `lang`. `prose_hash` freezes the bytes that shipped. Checks compare `content_hash`, document id, status, audience, and span. They do not score wording.

The render step opens with `assert_gold_manifest(truth_dir)`. If `MANIFEST.sha256` is absent or does not match the five files, render does not start. If a fact spec's required claims are missing from the draft prose, the pack is not published. Grade time reads the frozen sidecar and does not call the model again.

Draws inside gold builders use `random.Random(profile.seed)` and record the draw count in the manifest. `faults.json` is constants. It does not draw.

## identity.json

Canonical persons, official Arabic name, the seeded Latin spellings, id timeline (visitor number, later Iqama, reused MRN, newborn under the mother's id, twins, late death), and point-in-time clusters. Pairwise labels live here. No export file contains this object. The student link file is scored against a slice of this graph for the release `as_of`. A false merge costs more than a missed link, which the current identity check already implements. The engine's job is to keep the graph off the projection.

## policy.json

For each case date and each document version the binding row is:

```text
doc_id, content_hash, lang, status, effective, sunset,
site | cluster, audience, supersedes
```

The binding function the grader runs, unchanged in meaning from the current corpus rules:

- status is `in_force`
- the case date is inside `effective` and `sunset`
- the site matches, or the document is cluster-wide
- a facility document narrows a cluster document only when the cluster row allows it
- a referral keeps the `criteria_hash` stored on its start event

`policy.json` stores the result of that function per `(case_date, specialty, site)` before any leaflet is phrased. The unauthorized Ramadan circular and the v3/v4 pair are rows with different status. Search on `dms` returns all of them. The check compares the student's citation tuple `(doc_id, content_hash, lang, span)` to the binding row. Failure text contains the check id. It does not contain the hash, the national id, or the clause.

## procurement.json

The vendor queue, other buyers, and the true ship instant stay here. The `proc` projection receives only the team's own order stream: `requested`, `acknowledged` after a seeded lag, `partial` for a seeded short shipment, `frozen` when the case date is inside the Ramadan freeze, `received` when goods arrive. A buy order placed for the 10 January 2027 engagement has `received` after 8 February 2027. Rent is a different SKU whose `received` is inside the engagement. The student artifact fields are `gpu_path` (`rent` or `buy`) and `ready_date`. The comparer checks `ready_date` against the case clock and the projected promised date.

## facts.json

Structured claims for each public leaflet and the clinic-hours family, one object per `(doc_id, lang)`. English and Arabic are two rows that share claim ids. The planted drifts are rows, not accidents of phrasing: the in-force English Ramadan hours, an Arabic circular with the same title and status `unauthorized`, and one Arabic prep leaflet a version behind the in-force English leaflet. Preferred language is a field on some contact projections and absent on others. Absence is a missing key.

## Fault schedule

`faults.json` rows:

```text
fault_id        stable string
partner         insure | nid | sms | wa | maps | …
kind            latency | timeout | reset | slow_close | bandwidth | disabled | duplicate
toxicity        integer 1 on every row a grade will load
jitter_ms       integer 0 on every row a grade will load
latency_ms      integer constant
stream          upstream | downstream
from_release    inclusive
until_release   exclusive, or empty for open-ended
match           object, e.g. {"origin": "phc-rim"}
duplicate_at    list of case-clock offsets in seconds, used when kind is duplicate
```

Graded rows include, as data:

- `insure` reads a projection that already lags 48 case-hours, and `disabled` covers `rel-m04-l04`
- `nid` returns a fixed rate-limit body after a fixed call count in the script; death and id-replacement are late events in the log
- `sms` has `kind=duplicate` with two seeded offsets, so the log contains two receipt events; the check expects one logical send
- maps calls with `origin=phc-rim` have `kind=timeout` and a fixed `latency_ms`; other origins return `ref-travel`
- `sched-ain` does not need a toxic for "no API"; the route is absent; a missed night is `NightMissed`

`alwaha.check` loads this file and aborts if any row in the graded window has `toxicity != 1` or `jitter_ms != 0`. Practice exploration may pass `--demo-jitter` to `sim up`. That flag is rejected by `check.compare`. Jitter, when an author is watching a demo, uses `random.Random(f"{seed}:{fault_id}:{call_id}")` so a demo is repeatable. The score never takes that branch. Shopify's proxy is the vocabulary list, not the library on the grade path, because its jitter and toxicity draws are unseeded.

## Requirement reversals are later events

A stakeholder reversal is a new event on the same `stream_id`. The calendar in `release/decisions.py` is the authoring form. The appender assigns `seq` and `stream_rev`. Authors do not patch an earlier payload.

```text
DecisionRecorded
  decision_id, choice, scope, release_id, prior_event_id empty

DecisionReversed
  decision_id, choice, scope, release_id, prior_event_id, retain
```

Shipped reversals, matching the current release schedule:

| decision_id | Recorded | Reversed | retain |
|---|---|---|---|
| `dec-v4-scope` | `rel-m01-l04`, choice `v4_remains_draft` | `rel-m03-l03`, choice `v4_in_force`, scope `endo`, `ophth`, `card` | `start_criteria_hash` |
| `dec-ain-slots` | `rel-m01-l03`, choice `realtime_slot_expected` | `rel-m02-l05`, choice `file_only`, scope `sched-ain` | `no_intraday_hold` |

`retain=start_criteria_hash` means `project/eref.py`, on `DecisionReversed`, updates the current template pointer and does not rewrite referral streams whose start `seq` is lower. The start event already holds `criteria_hash`. Gold's policy slice at `rel-m03-l03` expects v4 in force for those three specialties and expects in-flight referrals to keep the earlier hash. A check at an earlier release expects v4 still draft. Both expectations are rows computed in step 2, before render.

`advance` appends only events whose `release_id` is the new release. The SQLite triggers in [01-engine.md](01-engine.md) make an update of an old decision a failed transaction. A release pack adds files under that release id. It does not rewrite a pack a previous lesson already graded.

`eref`'s omission of `pending` is a manifest rule with a `visible_from` release set in `release/calendar.py` to the product-change release the corpus already describes. Until that release, the key is absent. After it, the key appears because new events are projected, not because an old JSON file was edited.

## How checks stay deterministic

`check/compare.py` signature:

```text
grade(check_id, release, work_dir, world_dir) -> {check_id, pass|fail}
```

Inputs, and nothing else:

1. Gold files and `MANIFEST.sha256` for that profile and release.
2. The projection directory at `release_seq` after scripted commands, if the check is an end-state check.
3. Structured files under `work_dir` (link file, citation tuples, `gpu_path`, `ready_date`, tool trace, model hash on `reg-models`).

Abort, before assertions, when any of these is true:

- log event-hash disagrees with the published lock
- a projector cursor disagrees with `release_seq`
- a graded fault row is not toxicity 1 and jitter 0
- `ALWAHA_CLOCK` is not `case`
- the sidecar's `content_hash` disagrees with `facts.json`
- the work tree contains an `assessment` profile path

The scripted journey runs through the inbox with the case clock. Expected mock end state (one hold, one booking, one logical message, compensation if the receipt path died, no second booking on replay) is stored as hashes in facilitator `eval/` at pack build, produced by a throwaway run of the same three processes. The student package does not contain `eval/` or `truth/`.

Comparer operations are equality, set precision and recall, and date order. There is no model call, no sampling temperature, and no "does this prose seem right" branch. A facilitator commentary model, if someone runs one while preparing a class, is not an input. Interview scores stay on the scripted must-surface tree. Written templates stay on required fields and must-mention lists compiled at step 2.

Failure text is the check id and pass or fail. Canary strings, attack text, national ids, and the missing fact stay in gold and are not interpolated into the message.

A second `worldbuild` of profile `practice` seed `20270110` through the same release matches `MANIFEST.sha256` and the event-hash lock. The assessment seed is a different profile, built on the grading service, never copied into the participant tree. Assessment renames of sites and date shifts are a pure function applied while gold is written, so a rule hardcoded to a practice site fails the agreement test on assessment.
