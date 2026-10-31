---
id: WIKI-EVENTS
title: Event names the projectors already keep
date: 2027-01-06
type: wiki
author: Bobbi Tran
systems:
  - hospital
  - channel
  - payer
access: student
---

# Event names the projectors already keep

I am Bobbi Tran. I keep the three logs for Northline Access Collaborative. This page is dated 6 January 2027. It records the type strings the projectors already keep when they read `var/log.sqlite` and write the three projection files. The writer and the projectors run as local Python in the `access` package on the desk machine in Vancouver. The durable log is `var/log.sqlite`. The projection files are `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. Nothing on this page opens a remote account. The files stay on this machine.

There are three append-only logs. Their tables are `log_hospital`, `log_channel`, and `log_payer`. They share one SQLite file and they do not share a table. A command names its authority, and that name chooses the table. There is no foreign key from one log to another. `append_all` can commit a batch inside one transaction, and each command in the batch still lands on the one table its own authority names. A command that tries to install one shared clock is rejected before a row is stored. Each stored event keeps the `occurred_at` string that arrived with it.

`project_all` opens the log, calls `read_log` for hospital, then channel, then payer, and closes the log connection before it writes any projection. Each call returns that one table ordered by `seq`. The projector does not union the tables and does not sort them by `occurred_at`. A referral string that appears on more than one log becomes more than one document, in more than one file.

## Names already on the walks

These are the type strings I am listing because the running walks already keep them. The list is a list of names.

- RequestAccepted
- CoverageDecided
- CacheStored
- SlotFiled
- DocumentChanged
- HandsetDispatch
- DeskSession

`RequestAccepted`, `HandsetDispatch`, and `DeskSession` are channel types. The channel walk stores each of them as an event document. `CoverageDecided` is a payer type. The payer walk stores it as a coverage document. `CacheStored` and `SlotFiled` are hospital types. The hospital walk stores `CacheStored` as an eligibility-cache document and stores `SlotFiled` as a mart document followed by a nightly-file document. `DocumentChanged` is a hospital type. The hospital walk stores it as an event document, with the payload nested on that document.

Unknown types are still stored. The writer does not keep an allow-list of type strings. A command whose authority is `hospital`, `channel`, or `payer` is appended when the inbox key, the clock check, and the unique keys allow it, whatever string sits in `type`. The projector then keeps that row. A hospital type other than `SlotFiled` and `CacheStored` becomes one event document. Every channel type becomes one event document, including a channel type that is not in the list above. A payer type other than `CoverageDecided` becomes one event document. The type string is copied onto the event document. The payload is copied onto the event document. The row is not dropped because the type was unfamiliar to the branch that builds a mart, a cache, or a coverage document.

These further type strings already appear in the history and are stored by that path. They are examples of stored types. They are not a second clock, and they are not a closed catalog.

- LetterStored
- ReferralAccepted
- Lodged
- Stamped
- WebhookAttempt
- ReturnPosted
- SlotOffered
- DeskNote
- ReplicaCursor
- ReplicaExport
- QueueDepth
- PhoneRecorded
- PhoneFiled
- SchemaEpoch
- ClinicNoted
- SourceRowMigrated

Any other type string an authority sends is stored the same way when the insert succeeds. The log row keeps `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. The projection keeps `kind`, `type`, `ref`, `occurred_at`, and `payload` on the event document.

## What an event document holds

The pass-through document is the same shape on all three walks. `kind` is the string `event`. `type` is the event's type string. `occurred_at` is the event's `occurred_at`. `ref` is the payload's `ref` when that value is present, and otherwise the event's `stream_id`. `payload` is the payload object. The projector does not attach `seq` to the JSON. A reader who needs append order reads the log, ordered by `seq` on that one table.

`LetterStored` takes this path on the hospital walk. The opening letter for `REF-4417` is hospital type `LetterStored`, command `cmd-letter-4417`, `occurred_at` `2027-01-09T18:02:00Z`, stream revision 3. The payload carries `ref` `REF-4417`, the letter text, and `audience` `clinician`. The projection stores those keys under `payload` on an event document. It does not become a mart row.

## RequestAccepted

`RequestAccepted` is stored on `log_channel` and projected into `channel.sqlite` as `kind` `event`. The type string remains `RequestAccepted`. The opening command is `cmd-request-4417`, `occurred_at` `2027-01-09T08:14:00Z`, stream `REF-4417`, stream revision 1. The payload on that command carries:

- `ref`
- `utterance`
- `handset_delivered`
- `channel`
- `desk_region`

On that opening row the utterance is `booked at Cedar Ridge tonight`, `handset_delivered` is false, `channel` is `phone`, and `desk_region` is `BC`. Another `RequestAccepted` row can carry further keys. The channel row for `REF-8801` carries utterance `still waiting`, `handset_delivered` false, `channel` `web`, and `desk_region` `WA`, with `occurred_at` `2027-01-20T16:00:00Z`. The late row `R2F-LATE` carries `person_id`, `recorded_on`, and `reason` beside `ref`. The projector copies the payload it finds. It does not add a key the command omitted, and it does not build a mart from a channel event.

## HandsetDispatch

`HandsetDispatch` is stored on `log_channel` and projected as `kind` `event` with the type left as `HandsetDispatch`. The payload keys I see on the `REF-4417` dispatches are:

- `ref`
- `idempotency_key`
- `attempt`
- `status`

Command `cmd-dispatch-1` is `occurred_at` `2027-01-11T22:10:00Z`, stream `REF-4417`, stream revision 2, attempt 1, status `dispatched-unacked`, idempotency key `sms-4417`. Command `cmd-dispatch-2` is `occurred_at` `2027-01-11T22:16:00Z`, stream revision 3, attempt 2, status `redelivered`, the same idempotency key. Both rows are kept. A later `HandsetDispatch` in the replica history also carries `file_id` and `transcripts`. Those keys stay inside `payload` on the event document when that command sent them.

## DeskSession

`DeskSession` is stored on `log_channel` and projected as `kind` `event` with the type left as `DeskSession`. The payload keys on the opening desk command `cmd-desk-session` are:

- `session_id`
- `token_subject`
- `factor`
- `desk_region`

That row is `occurred_at` `2027-01-09T08:10:00Z`, stream `desk-8841`, stream revision 1, session `sess-8841`, token subject `member-bc-4417`, factor `screen-code-then-sms`, desk region `BC`. Legacy desk rows of the same type also carry `screen_code`, and one of them carries `ref`. The event document holds the payload that was appended. `DeskNote` is a different type. It is still stored, on the channel walk, as an event document. It is not folded into the `DeskSession` document.

## CoverageDecided

`CoverageDecided` is stored on `log_payer`. The payer walk tests the type. When the type is `CoverageDecided`, the walk appends one document with `kind` `coverage`. The columns are:

- `kind`, the string `coverage`
- `ref`, from the payload
- `answer`, from the payload
- `effective_from`, from the payload when the key is present, otherwise null
- `effective_to`, from the payload when the key is present, otherwise null
- `currency`, from the payload when the key is present, otherwise null
- `occurred_at`, from the event

The opening command `cmd-cover-4417` stores `answer` `yes`, `effective_from` `2027-01-12T00:00:00Z`, `effective_to` `2027-04-12T00:00:00Z`, `currency` `CAD`, and `member_region` `BC`, with event time `2027-01-08T16:00:00Z`. The coverage document receives `kind`, `ref`, `answer`, the two window fields, `currency`, and `occurred_at`. `member_region` stays on the log payload. It is not a column of the coverage document.

A timeout is a `CoverageDecided` row whose `answer` is `timeout` and whose payload omits the window keys. Command `cmd-timeout-2290` for `REF-2290` stores `answer` `timeout` and `currency` `USD` at `2027-01-09T19:40:00Z`. The coverage document has `answer` `timeout`, `effective_from` null, `effective_to` null, and `currency` `USD`. The null pair is the empty window stored from that payload. The payer walk does not read the hospital cache while it builds this document.

A payer type other than `CoverageDecided` is still stored. It becomes `kind` `event` in `payer.sqlite`, with `type`, `ref`, `occurred_at`, and `payload`. `PhoneFiled` is one such payer type. It remains an event document.

## CacheStored

`CacheStored` is stored on `log_hospital`. The hospital walk appends one document. `kind` is `eligibility_cache`. The columns are:

- `kind`, the string `eligibility_cache`
- `ref`
- `eligible`
- `window_present`
- `occurred_at`, from the event

The opening command `cmd-cache-4417` is `occurred_at` `2027-01-09T21:00:00Z`, stream revision 1, `eligible` true, `window_present` false, and a `source` string. The cache document receives `kind`, `ref` `REF-4417`, `eligible` true, `window_present` false, and `occurred_at` `2027-01-09T21:00:00Z`. The `source` string stays on the log payload. The cache document does not receive `answer`, `effective_from`, `booking_date`, `wait_days`, `file_id`, or `trailer_ok`. Those columns are produced on other documents, from the events that carry them.

## SlotFiled

`SlotFiled` is stored on `log_hospital`. Cedar Ridge has no slot API. A nightly file from that clinic is still a hospital command. The hospital walk appends two documents from one `SlotFiled` event, in this order: the mart document, then the nightly-file document. It does not also append a pass-through event document for that same event.

The mart document has `kind` `mart`, `ref` from the payload, `booking_date` from the payload, and `wait_days`. The integer written into `wait_days` is 0. The mart document does not receive `file_id`, `site`, `trailer_ok`, `clinic`, or `state`.

The nightly-file document has `kind` `nightly_file`, `ref`, `file_id`, `site`, and `occurred_at` from the event. `booking_date` stays on the mart document. When the payload contains the key `trailer_ok`, the nightly-file document also receives `trailer_ok`, `trailer_count`, and `body_count`. When the payload has no `trailer_ok` key, those three fields are absent from the nightly-file document.

The opening `SlotFiled` is command `cmd-slot-4417`, `occurred_at` `2027-01-11T21:00:00Z`, stream revision 2. The payload carries `ref` `REF-4417`, `site` `cedar-ridge`, `file_id` `cedar-2027-01-11`, `clinic` `ENDO-CLN`, `booking_date` `2027-01-11`, and `state` `WA`. It has no `trailer_ok`. The mart document is `kind` `mart`, `ref` `REF-4417`, `booking_date` `2027-01-11`, `wait_days` 0. The nightly-file document is `kind` `nightly_file`, `ref` `REF-4417`, `file_id` `cedar-2027-01-11`, `site` `cedar-ridge`, `occurred_at` `2027-01-11T21:00:00Z`. `clinic` and `state` remain on the log payload. A `SlotFiled` that does send a trailer, such as the poison batch with `trailer_ok` false, `trailer_count` 12, and `body_count` 11, copies those three fields onto the nightly-file document.

`SlotOffered` is a different hospital type. Unknown types are still stored, and `SlotOffered` is stored as `kind` `event`. It does not take the mart and nightly-file branch. That branch runs only when the type string is `SlotFiled`.

## DocumentChanged

`DocumentChanged` is stored on `log_hospital` and takes the event path. The document in `hospital.sqlite` has `kind` `event`, `type` `DocumentChanged`, `ref`, `occurred_at`, and `payload`. When the payload has no `ref`, `ref` on the event document is the `stream_id`. Hours streams use the document id as `stream_id`. The hours payload carries `doc_id` and does not carry `ref`, so the event document's `ref` is that stream id.

Payload keys that the hours commands store are `doc_id`, `version`, `status`, `audience`, `close_local`, `timezone`, `language`, `body`, and `content_hash`. The summer hours command `cmd-hours-old` is `occurred_at` `2026-06-01T00:00:00Z`, stream `hours-cedar`, stream revision 1, version `2026-summer`, status `superseded`, `close_local` `21:00`, timezone `America/Los_Angeles`. The winter hours command `cmd-hours-new` is `occurred_at` `2027-01-10T00:00:00Z`, stream revision 2, version `2027-winter`, status `in_force`, `close_local` `17:00`, the same timezone. Both rows remain. Other `DocumentChanged` payloads omit `close_local` and `timezone` and still carry `doc_id`, `version`, `status`, `audience`, `language`, `body`, and `content_hash`. A quotation payload can also carry `quote_id`, `supplier_id`, `amount`, `currency`, `site`, `packet_ref`, and `ref`. A contract payload can carry `contract_id`. The event document nests whatever object was stored.

The student pack later copies `DocumentChanged` payloads into `student_pack/extracts/documents.json` and adds `occurred_at` on each object. That file is a view of those payloads. The hospital projection still has the event document with the payload nested. Both are produced from the hospital log. The channel log and the payer log are not read while the hospital walk builds the `DocumentChanged` event document.

## How a walk moves

Inside one projection file, documents follow the `seq` order of that one log. For `SlotFiled`, the mart document is inserted immediately before the nightly-file document of that same event. Loading `rows` from the projection returns the documents in insert order. `occurred_at` on a document is the text from the event that produced it. The hospital letter for `REF-4417` has `occurred_at` `2027-01-09T18:02:00Z` and a later `seq` than the slot whose `occurred_at` is `2027-01-11T21:00:00Z`, because the letter command is later in the append order of `log_hospital`. The projector copies each string onto its own document. It does not rewrite one event's `occurred_at` with another event's `occurred_at`.

`seq` on a log table is the rowid of that table. `log_hospital`, `log_channel`, and `log_payer` each have their own rowid space. The projector never writes `seq` into the JSON. Sorting documents from three files by the `occurred_at` strings builds an order the projector does not write. The office week at the Vancouver desk is Monday through Friday, America/Vancouver. Cascade Seattle and Cedar Ridge use America/Los_Angeles. Cedar Ridge files at night, including weekends. Those facts are about the organizations. They are not a column the projector adds, and they are not a ranking of the type names above.

The local HTTP process is separate from the projector. `python -m access serve` binds `127.0.0.1` and port 8088 unless `--port` is set. It reads JSON under `student_pack/extracts`. It does not append to the logs, and it does not open the projection files to answer a request. After `python -m access init` or `reset`, the pack's `hospital.json`, `channel.json`, and `payer.json` hold the same objects the projector wrote. A student who wants one log's documents can open those files or call `GET /extracts/hospital`, `GET /extracts/channel`, and `GET /extracts/payer`. The type string on an event document is the type that was stored. Unknown types are still stored, on the log and on the event document, with the payload that arrived.
