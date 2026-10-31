# Curriculum data availability

Checked on 30 October 2026 after `python -m access init` printed 949 events. The student pack was opened on disk. `GET /health`, `GET /extracts/boards`, and `GET /ref/REF-4417` were called on a local server. `/ref/REF-4417` returned 34 hits. The pack text did not contain `dec-accept`, `dec-clinical`, `refused`, `APR-9991`, or `sms-holdout`.

There is one module, the engagement. Access for every lesson is the student pack and the local HTTP view. Ground truth for grading stays in `sealed.py`, `sealed_release.py`, and `sealed_holdouts.py`. Those modules are not copied into the pack.

| Lesson | Problem the student meets | Data that is present | Where | How a student reaches it |
| --- | --- | --- | --- | --- |
| INV-01 | The mart wait is 0 and the label is about the request | Boards, hospital mart, channel request, payer window, sponsor note | `extracts/boards.json`, `hospital.json`, `channel.json`, `payer.json`, `sponsor.json` | Pack files, `GET /extracts`, `GET /ref/REF-4417` |
| INV-02 | One urgency field on the assistant screen | Letter text with clinical wording, emergency utterance, return, payer timeout with no window | Hospital letter, channel `REF-3304`, payer `REF-2290`, `assistant_screen.json` | Same |
| INV-03 | A schema-shaped id inside the letter | `APR-4417` in the letter, two `SlotOffered` rows for `REF-5510`, utterance not delivered | Hospital and channel extracts, assistant screen | Same |
| INV-04 | Two texts, a bad trailer, a weekend file | `sms-4417` twice, poison trailer, Saturday file `cedar-2027-01-09`, file night before coverage, cancel-then-text, closure dates | Channel, hospital nightly files, curriculum events | Same. Office week in `organization.json` is Monday–Friday |
| INV-05 | A true quotation of the wrong document | Statuses `draft`, `in_flight`, `in_force`, `superseded`, `unauthorized`. Draft ids `leg-dms-draft` and `dms-draft-fraser`. Hash mismatch on `hours-cedar-copy` | `extracts/documents.json`, `asks.json` | Same |
| INV-06 | The calibration file still carries the label | `calibration.json` rows include `pass`. A channel note has scores 0.5002 vs 0.5000 at n 9 | `extracts/calibration.json`, channel extract | Same |
| INV-07 | The host is green and the served hours are old | `host.json` green, `served_document.json` version `2026-summer`, `shadow.json` wrote a slot | Those three extracts | Same |
| INV-08 | A successful call is not permission to upload | Letter, `bytes/national_id.txt`, quotation, wage, leaflet, two call records | `byte_index.json`, `calls.json`, `bytes/national_id.txt`, audit copy to `us-east-1` | Same |
| INV-09 | A second desk with different nouns | `PERMIT-12` lodged in Vancouver and stamped in Washington | Boards, channel `Lodged`, hospital `Stamped` | Same |

Round-2 rows that are also on the base log:

| Evidence | Records |
| --- | --- |
| Site feeds | `extracts/site_feeds.json`. Cascade read model shows "Cascade day clinic" at rev 1. The later correction is on the hospital log and is not in that feed list |
| Fraser and Cedar exports | Separate feed lists. They do not contain each other's refs |
| Delivery split | `ProviderAccepted` then `HandsetDelivered` for `R2C-HAND` |
| Correlated cohort | 124 commands inside the 949. BC phones in that cohort use 604 |
| Deeper case | `R2E-9`: booked utterance, office list marks 2027-02-15 closed, file that night, coverage from 2027-02-20 |
| Timelines | Phone stored as digits and later as dashed. Source row `S-14` on both `R2F-14` and `R2F-99`. A March event recorded in November |
| Locale examples | BC postal `V6B 2W9` with rejected ZIP `98101`. CAD and USD coverage rows. A spreadsheet UTC stamp that dropped the offset |
| Operations | Quotation `QUO-18420` with supplier `SUP-14` on the document and `SUP-14B` on the invoice note |
| Cross-system ids | `R2D-7` uses desk id `MBR-R2D-7` and hospital id `MRN-R2D-7` |

Counts from the generated extracts: hospital rows 394, channel rows 357, payer rows 236, documents 11.

Scenario datasets are not in the base pack. `python -m access scenario --name replay-storm` and `--name partial-write` each rebuilt, then `init` restored 949 events. Older overlay names remain `partner-outage` and `hours-served-stale`.

The larger workload is a separate file, `var/workload.jsonl`, 1040 commands, seed `20270110`. Its summary is `var/workload_summary.json`: 400 channel, 320 hospital, 320 payer, 269 yes, 29 no, 22 timeout, and 0 BC rows with a 206 phone. It is not mounted on the student HTTP view. `var/stress.jsonl` is a further 2000 `StressTick` rows from `round3.scale`, also outside the pack. Appending those 2000 on a temporary database took 0.162 seconds.

Round 3 on the base log, after the mart field `booking_date_only` was removed from student extracts:

| Evidence | What was checked |
| --- | --- |
| Inlet merger | `inlet-2026-11-02` and `cedar-r3a-2026-11-02` for the same person after `ClinicMerged` |
| Monthly volume | `extracts/monthly_volume.json`, 24 months. 2026-01 WA requests 498, 2026-07 WA requests 238. Assumption check returned no problems |
| Identity graph | `extracts/identity_graph.json`, 9 edges. Phone `604-555-2770` remains on the earlier wrong chart and on the later split |
| Contract MA-2024 | Version 1 body, a later superseded status, a printed copy labeled version 2 whose hash is of the version 1 body, a December `recorded_on` for the August amendment |
| Replicas | cedar-copy cursor 14 and cascade-copy cursor 10. Same file, amount 90, currencies USD and CAD |
| Ledger | `R3F-LEDGER` board shows 18420 USD. The payer row shows 18420 CAD. The comparison is not labeled in the pack |
| Governance | Channel consent true for screen text, hospital consent false for the letter, copy to `ca-central-1` with no reviewer |

Hijri dates are not generated. That deviation is recorded in `docs/decisions.md`. The student package `repair` is not in the tree. The pack was searched after this init and did not contain `booking_date_only`, `dec-accept`, `dec-clinical`, `refused`, `root_cause`, `answer_key`, or `correct_currency`.
