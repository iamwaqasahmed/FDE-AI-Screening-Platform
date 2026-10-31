# Lesson catalog

`commands()` in `src/access/round2/lesson_feeds.py` adds nine January 2027 events (`cmd-r2c-`, streams `r2c-`). This file does not copy them into `student_pack/extracts`. Hijri dates are not added.

| Lesson | Evidence that already exists | Evidence these commands add | Access path |
| --- | --- | --- | --- |
| INV-01 | Boards, the three logs, and the assistant wait of 0. | None for the clock binding. | `student_pack/extracts/boards.json`, `hospital.json`, `channel.json`, `payer.json`, `assistant_screen.json` |
| INV-02 | Letter with clinical wording. Emergency utterance on `REF-3304`. Payer timeout on `REF-2290` with no window. | None. | `student_pack/extracts/hospital.json`, `channel.json`, `payer.json`, `assistant_screen.json` |
| INV-03 | `APR-4417` in the letter. Two offers of `slot-v3` on `REF-5510`. The channel utterance is not a handset delivery. | None for a document-sourced id or a second offer. | `student_pack/extracts/hospital.json`, `channel.json`, `assistant_screen.json` |
| INV-04 | Two dispatches of `sms-4417`. Poison file `cedar-poison-2026`. Saturday file `cedar-2027-01-09`. File night before coverage. `THR-17` repeats that night pattern. `INT-17` cancels earlier than the file and at a later revision. `CUR-4` is cancel-then-text. `channel.json` already has `ProviderAccepted` then `HandsetDelivered` for `LEG-2201`, without `handset_delivered` on those rows. | `ProviderAccepted` then a later `HandsetDelivered` for `R2C-HAND`. `handset_delivered` is false on the accept and true on the handset event. | Existing rows: `student_pack/extracts/channel.json`, `hospital.json`. `R2C-HAND` is not in those files. |
| INV-05 | Hours at 21:00 superseded and 17:00 in force. A winter copy whose stored hash does not match its body. Unauthorized circular. French text still on the summer close. Quotation. Leaflet. `documents.json` also has `leg-dms-draft`, status draft, for Cedar Ridge. `curriculum_gaps.md` still says no draft row. | `DocumentChanged` `dms-draft-fraser`, status draft, audience public, a Fraser Burnaby hours sentence. The body is in the feed. There is no hint field. | Existing rows: `student_pack/extracts/documents.json`. `dms-draft-fraser` is not in that file. |
| INV-06 | `calibration.json` still contains `pass`. | None. | `student_pack/extracts/calibration.json` |
| INV-07 | Host CPU 12 and latency 80 with status green. Served hours are `2026-summer`. Shadow write recorded. | None. | `student_pack/extracts/host.json`, `served_document.json`, `shadow.json` |
| INV-08 | Letter, national-id file, quotation, wage note, leaflet. Call records for `us-west-2` / `us-east-1` and a matching `ca-central-1` pair. Both return HTTP 200. | None. | `student_pack/extracts/calls.json`, `byte_index.json`, `documents.json`. The id file is `student_pack/bytes/national_id.txt`. |
| INV-09 | `PERMIT-12` lodged in Vancouver and stamped in Washington. Board label `since_lodged`. | None. | `student_pack/extracts/boards.json`, `hospital.json`, `channel.json` |

## Feeds

`feeds()` keys: `draft_docs`, `cascade_read_model`, `fraser_feed`, `cedar_feed`, `delivery_split`, `leave`. Each value is a list of student-visible payloads. None of these lists are written to `student_pack/extracts` by this module.

`draft_docs` shows `dms-draft-fraser`.

`cascade_read_model` shows `ReadModelServed` for `cascade-seattle`: clinic name `Cascade day clinic`, rev 1. The later `ReferralCorrected` on stream `r2c-cascade-read` names `Cascade endocrine` and is not in this list.

`fraser_feed` is `FeedExported` for `fraser-burnaby` ref `R2C-FR` on `r2c-export-fraser`. `cedar_feed` is `FeedExported` for `cedar-ridge` ref `R2C-CD` on `r2c-export-cedar`. Neither list includes the other ref.

`delivery_split` lists the accept and the later handset event for `R2C-HAND`.

`leave` lists a `DeskSession` at 08:10 and a later `LeavePosted` at 09:05 for clinician `clin-r2c-endo`, ref `R2C-LEAVE`, both on the local morning of 2027-01-18 in `America/Vancouver`. Hospital `LeavePosted` for `org-leave` already mentions a desk session in prose. It is not this pair. Legacy desk sessions are a different morning and a different ref.
