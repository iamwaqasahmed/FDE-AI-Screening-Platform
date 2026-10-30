# 4 — Data and systems

## Logs

Each log row has an authority, an event name, a payload, and that authority’s own time. Times are not comparable by sorting all three logs together.

Illustrative event names, stable for the build:

| Log | Events the projectors understand |
| --- | --- |
| `log_channel` | `RequestAccepted`, `WindowOpened`, `WindowClosed`, `ProviderAccepted`, `HandsetDelivered` |
| `log_hospital` | `ReferralAccepted`, `CacheStored`, `SlotFiled`, `DocumentChanged`, `LeavePosted` |
| `log_payer` | `CoverageDecided` |

`RequestAccepted` can carry an utterance. The utterance is not `dec-slot`. `ProviderAccepted` is not `HandsetDelivered`. `CacheStored` can keep a stale eligibility bit and drop the coverage window. `SlotFiled` names a file id. `CoverageDecided` carries `effective_from` and `effective_to`. A file night before `effective_from` is not coverage.

## Projections the student can call

| Id | Authority | Student sees | Withheld |
| --- | --- | --- | --- |
| `his-wadi` | Hospital | A read model, one version behind a correction | The corrected row |
| `his-nakhl`, `his-safra` | Hospital | A feed that can arrive out of order | A later cancel until reconciliation |
| `sched-ain` | Hospital | A nightly file | A slot API. There is not one |
| `eref` | Hospital | Referral events. The patient API can hide `pending` | The coordinator note |
| `dms` | Hospital | Documents with status, audience, language, hash | Drafts are present and must not be cited |
| `mart` | Hospital | A wait figure that matches the receipt formula | The request clock |
| `desk-id` | Desk | A local step-up. Screen code, then a second factor. The session id is not the token subject | A live national identity service. No national id is collected |
| `desk-channel` | Desk | Window open or closed, accept, delivery | Delivery is a separate event |
| `cc` | Desk | A handoff queue | The previous caller. Identity must not stick |
| `cover` | Payer | Yes, no, or timeout | A default of covered |
| `hr` | Hospital | Leave, sometimes after a session started | — |

Nakhl, Safra, Wadi, and Ain cannot read one another.

## Synthetic population

Generated from the gold graph, then rendered to text. The renderer’s bytes are hashed. A model may draft a sentence at pack-build time. The grader never calls one.

Minimum population rules:

- One mother and one newborn who share a phone and are two persons.
- Twins who share a phone and are two persons.
- One reused medical record number, then a replacement pointer.
- Dates as civil Hijri and as Gregorian. The graded converter is the tabular function shipped with the pack. A civil conversion library is named in a reading and is not swapped in silently.
- Documents: one fact, two languages, one translation behind. Status is draft, in force, superseded, or unauthorized.
- Slots: a version. Two offers can hold the same version.
- One public reference id printed on all extracts so the student can see the disagreement. The scoring instants for that id stay in gold.

## Classes of bytes

| Class | Examples | Where it may sit |
| --- | --- | --- |
| Public | Published hours, a public leaflet, a published rubric | Laptop, and an account bucket with a hash |
| Restricted | Referral letter, national id, a supplier quotation, a wage | Laptop only |

The highest class in a mixed object wins. A public FAQ that quotes a letter is restricted.

## What a chapter may contain

Symptoms, contradictory extracts, and a blank binding. After the student saves a prediction, the chapter may name the mechanism on a different object and show one worked procedure. It may not name the graded column, the graded authority, or the holdout instants.
