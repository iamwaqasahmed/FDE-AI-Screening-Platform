# Student walkthrough

Built with `access.world.build` on a temporary directory. Every field below was read from that `student_pack`.

Files in the pack: `README.md`, `sponsor.json`, `organization.json`, `bytes/national_id.txt`, and `extracts/` (`asks.json`, `assistant_screen.json`, `audit.json`, `boards.json`, `byte_index.json`, `calibration.json`, `calls.json`, `channel.json`, `desk.json`, `documents.json`, `focus.json`, `hospital.json`, `host.json`, `legacy_desk.json`, `payer.json`, `served_document.json`, `shadow.json`).

## INV-01

Opened `extracts/boards.json`. The `REF-4417` row has `label_id` `since_you_asked`, `board_name` `facility_mart`, `board_value` 0, and `board_as_of` `2027-01-11`.

Opened `extracts/hospital.json`. The row with `kind` `mart` and `ref` `REF-4417` has `wait_days` 0 and `booking_date` `2027-01-11`.

Opened `sponsor.json`. Field `text` asks for one wait number on the patient screen.

Opened `extracts/assistant_screen.json`. Field `wait_days` is 0 on `ref` `REF-4417`.

## INV-02

Opened `extracts/hospital.json`. A `LetterStored` payload `text` for `REF-4417` contains `chest pain`. A `FaqBodyStored` payload `body` contains the same phrase. `REF-3304` has a `ReturnPosted` row.

Opened `extracts/payer.json`. The `REF-2290` row has `kind` `coverage`, `answer` `timeout`, `effective_from` null, and `effective_to` null.

Opened `extracts/channel.json`. The `REF-3304` payload `utterance` contains `emergency`.

Opened `extracts/assistant_screen.json`. Field `urgency` is `urgent`.

## INV-03

Opened `extracts/hospital.json`. The `REF-4417` letter payload `text` contains `APR-4417`. Two rows have `type` `SlotOffered` and `ref` `REF-5510`. Both payloads have `version` `slot-v3` (`offer_id` `offer-a`, then `offer-b`).

Opened `extracts/assistant_screen.json`. Field `approval_accepted` is `APR-4417`.

Opened `extracts/channel.json`. The `REF-4417` payload has `handset_delivered` false. Its `utterance` is `booked at Cedar Ridge tonight`.

## INV-04

Opened `extracts/channel.json`. Two payloads on `REF-4417` have `idempotency_key` `sms-4417`: `attempt` 1 with `status` `dispatched-unacked`, and `attempt` 2 with `status` `redelivered`.

Opened `extracts/hospital.json`. A `kind` `nightly_file` row has `file_id` `cedar-2027-01-09`, `ref` `WEEKEND-1`, and `occurred_at` `2027-01-09T21:00:00Z`. That row has no `trailer_ok` field. Another nightly row has `file_id` `cedar-poison-2026`, `trailer_ok` false, `trailer_count` 12, and `body_count` 11.

Opened `extracts/payer.json`. The `REF-4417` coverage row has `answer` `yes` and `effective_from` `2027-01-12T00:00:00Z`.

Opened `organization.json`. Field `office_week` is `Monday through Friday`. Field `note` says clinical sites file at night, including weekends.

Opened `extracts/channel.json`. A `ClosuresAnnounced` payload `dates` lists `2027-01-01` and `2027-02-15`.

## INV-05

Opened `extracts/documents.json`. The `status` values are `superseded`, `in_force`, `unauthorized`, `in_flight`, and `draft`.

`hours-cedar` version `2026-summer` has `status` `superseded` and `close_local` `21:00`. The same `doc_id` version `2027-winter` has `status` `in_force` and `close_local` `17:00`. `circ-unauth` has `status` `unauthorized`. `hours-cedar-fr` has `status` `in_flight` and `language` `fr`. `leg-dms-draft` has `status` `draft`.

`hours-cedar-copy` has `doc_id` `hours-cedar-copy`, `status` `in_force`, `version` `2027-winter`, and a `content_hash` that differs from the SHA-256 of its `body`.

`quote-harbor` has `audience` `procurement`. `leaflet-hours` has `audience` `public`. `wage-band` has `audience` `payroll`.

## INV-06

Opened `extracts/calibration.json`. Each row has a `pass` key. `cal-04` has `pass` false. `cal-07` has `pass` true, `n` 8, `score_a` 0.5001, and `score_b` 0.5.

## INV-07

Opened `extracts/host.json`. `status` is `green`, `cpu_percent` is 12, `latency_ms_p99` is 80, and `host` is `desk-app-3`.

Opened `extracts/served_document.json`. `served_version` is `2026-summer`. `told_doc_id` and `served_doc_id` are `hours-cedar`. `served_close_local` is `21:00`.

Opened `extracts/shadow.json`. `wrote_slot` is true. Field `sentence` is `booked at Cedar Ridge tonight`.

Opened `extracts/hospital.json`. The `REF-4417` row with `kind` `eligibility_cache` has `eligible` true and `window_present` false.

Opened `extracts/assistant_screen.json`. `hours_version_served` is `2026-summer` and `hours_close_local` is `21:00`.

## INV-08

Opened `extracts/byte_index.json`. `name` includes `letter`, `national-id`, `quotation`, `wage`, `leaflet-public`, and `hours-public`. Field `where` points at the hospital letter for `REF-4417`, `bytes/national_id.txt`, document `quote-harbor`, document `wage-band`, document `leaflet-hours`, and document `hours-cedar`.

Opened `bytes/national_id.txt`. The file is present.

Opened `extracts/calls.json`. `call-west` has `payload_kind` `referral-letter`, `endpoint_region` `us-west-2`, `processor_region` `us-east-1`, and `http_status` 200. `call-match` has `payload_kind` `referral-letter`, both regions `ca-central-1`, and `http_status` 200.

## INV-09

Opened `extracts/boards.json`. `PERMIT-12` has `label_id` `since_lodged`, `board_name` `records_counter`, and `board_value` 19.

Opened `extracts/channel.json`. A row with `type` `Lodged` and `ref` `PERMIT-12` has payload `city` `Vancouver` and `region` `BC`.

Opened `extracts/hospital.json`. A row with `type` `Stamped` and `ref` `PERMIT-12` has payload `state` `WA` and `office` `cascade-records`.

## Pack text

A search of every file in the pack found no match for `dec-accept`, `dec-clinical`, or `refused`.

## Gaps

`documents.json` includes `status` `draft` on `leg-dms-draft`.

`organization.json` `office_week` is Monday through Friday. Lesson INV-04 still describes a Sunday through Thursday week.
