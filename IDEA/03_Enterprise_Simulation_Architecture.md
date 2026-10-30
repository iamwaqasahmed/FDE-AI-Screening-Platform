# 3 — Simulation architecture

Package name: `access`. Standard-library SQLite. Three operating-system processes. The package imports no cloud SDK and no model client.

## Processes

| Process | Writes | Does not |
| --- | --- | --- |
| `append` | One of `log_hospital`, `log_channel`, `log_payer`, and that log’s outbox, in one transaction | Cross-log keys, wall-clock timestamps, update, delete |
| `project` | One store per authority: `var/proj/hospital.sqlite`, `channel.sqlite`, `payer.sqlite` | Read another authority’s log |
| `serve` | An inbox file, then a projection read on localhost | An “episode” route that joins the three logs into one timeline |

`check` is a fourth program. It opens sealed gold and the student’s binding. It does not open a socket and it does not call a model.

A reversal is a new event on the log that owned the earlier event. Student commands enter the inbox and become events only inside `append`.

## Gold

Written before any sentence is rendered. It contains:

- Persons, with links the student must not invent: a mother and a newborn who share a contact and are not one person; twins; a reused identifier; Hijri civil dates and Gregorian dates.
- The `promise` table: which authority a given screen may cite.
- Decision owners: who may write `dec-clinical`, `dec-route`, `dec-cover`, `dec-slot`.
- Document facts: status, audience, language, content hash. A body can change under the same version id. The hash changes.
- The fault schedule. Graded faults are fixed: the same body every time, no random delay.
- Claim versus record tags for interview sentences.

There is no column `true_wait`, no `canonical_at`, and no view that unions the three logs. A KPI that drops its authority fails, including a single reconciled number. The legal shared value is the string `refused`.

The public reference is `REF-4417`. It is printed on the extracts. Gold for it is four events:

| Log | Type | Time on that log | Decision |
| --- | --- | --- | --- |
| `log_payer` | `CoverageDecided` | 2027-01-08 16:00Z | `dec-cover`: yes from 2027-01-12 through 2027-04-12 |
| `log_channel` | `RequestAccepted` | 2027-01-09 08:14Z | `dec-accept`. Utterance says the visit is booked tonight. No handset delivery |
| `log_hospital` | `CacheStored` | 2027-01-09 21:00Z | None. Keeps `eligible: true` and drops the coverage window |
| `log_hospital` | `SlotFiled` | 2027-01-11 21:00Z | `dec-slot`. File `ain-2027-01-11` |

The file night is before coverage starts, so `dec-cover` is false at that instant. The cache is not `dec-cover`. The utterance is not `dec-slot`. The mart stores booking date 2027-01-11 and `wait_days` 0. That is the hospital formula. Patient wait starts at `dec-accept`. These instants are gold. They do not appear in the student chapter.

The student tree does not contain `gold/`.

## What serve returns

Five extracts and a sponsor note that demands one number. A form whose labels are filled and whose times are empty. No route that books Ain from a sentence. No route that returns one episode.

Projections may lag. The hospital’s cached `eligible: true` is a fact about the cache. It is not `dec-cover`. A channel utterance that says a visit was booked is not `dec-slot`. The mart’s figure can match the hospital’s booking-date formula exactly.

## Checks

The student’s binding is applied to:

1. The practice log, which the demo can pass with a naive patch.
2. A hidden holdout.
3. A second mini-world: different nouns, same relationship.

One miss fails the specification. The miss names the broken relationship and does not print the gold value. A missing file fails. A field named `pass` on an input row is ignored. Copied numbers fail because holdout numbers differ.

Resubmission is allowed. It does not add a tenth investigation.

## What the simulator refuses

A live model in the grader. A public sandbox as the world. A cloud account that stores gold. An offensive range. Physiology or a clinical device. Rewriting a committed event. A fourth world process that is a broker or a FHIR server. Those protocols appear as projections and files when an investigation needs them.

## Operator note

An operator may run the same three processes once per submission in a disposable environment. If that run’s manifest differs from the laptop hash, the run is discarded. Students do not deploy gold.
