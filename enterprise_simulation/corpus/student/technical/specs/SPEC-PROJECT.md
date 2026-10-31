---
id: SPEC-PROJECT
title: Per-log projection into three stores
date: 2026-10-15
type: specification
author: Bobbi Tran
systems:
  - hospital
  - channel
  - payer
access: student
---

# Per-log projection into three stores

I am Bobbi Tran. This specification describes the projector that runs beside the three logs. The date is 15 October 2026. The projector is local Python in the `access` package. It reads `var/log.sqlite` and writes three SQLite files under `var/proj/`. It uses the standard-library `sqlite3` and `json` modules. It does not open a remote account. The logs stay the append-only record. The projection files are a derived copy that the projector is allowed to replace.

`project_all` opens the log, calls the log reader three times, and closes the log connection before it writes any projection. The three calls are `read_log` for `hospital`, then `channel`, then `payer`. Each call returns that one table ordered by `seq`. The projector does not union the tables, does not sort them by `occurred_at`, and does not join a hospital row to a channel row or a payer row while it writes. A referral string that appears in more than one log becomes more than one document, in more than one file, because each file is built from its own list.

## The three files

The output paths are `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. For each path the projector creates the parent directory, deletes the file when it already exists, and opens a new database. Each database has one table, `rows`, with one column, `doc TEXT NOT NULL`. Each insert stores one JSON object in `doc`. There is no second table of indexes, and there is no foreign key to the log. Replacing the file is the whole update. The projector does not append a correction into an old projection file, and it does not delete rows inside a file it is keeping. The next run unlinks the file and writes a fresh one from the current log.

The log triggers that abort delete apply to `log_hospital`, `log_channel`, and `log_payer`. They do not apply to these projection files, because the projector removes the file from the directory and creates a new database. A projection run does not issue `DELETE` or `UPDATE` against the logs. When the run finishes, the log rows are the rows that were there at the read.

JSON object keys are written in the order the projector builds the dictionary. A later reader that loads `doc` and parses it sees those keys. The student pack copies the same objects into `student_pack/extracts/hospital.json`, `channel.json`, and `payer.json` after a build. This specification is about how the objects are produced. The HTTP reader, specified separately, serves the extract files. It does not open `var/proj` to answer a request.

## How a nightly file row is produced

The hospital walk looks at `type` on each hospital event, in `seq` order.

When the type is `SlotFiled`, the projector appends two documents, in this order. The first is the mart document. The second is the nightly-file document. Both come from that one hospital event. No channel event and no payer event is consulted.

The mart document has `kind` set to `mart`. `ref` is copied from the payload. `booking_date` is copied from the payload. The mart stores a wait beside a booking date: the same document holds `wait_days` beside `booking_date`. The integer written into `wait_days` is 0. The mart document does not receive `file_id`, `site`, `trailer_ok`, `clinic`, or `state`. Those keys are not mart columns.

The nightly-file document has `kind` set to `nightly_file`. The columns it always receives from a `SlotFiled` event are:

| Column | Source |
| --- | --- |
| `kind` | the string `nightly_file` |
| `ref` | payload `ref` |
| `file_id` | payload `file_id` |
| `site` | payload `site` |
| `occurred_at` | the event's `occurred_at`, not a payload field |

`file_id` is the file identifier the hospital put on the command. It is copied as text. The projector does not rewrite it from `booking_date` and does not rewrite it from `seq`. `booking_date` is not a column on the nightly-file document. It stays on the mart document produced from the same event.

`trailer_ok` is copied only when the payload contains the key `trailer_ok`. When that key is present, the projector also copies `trailer_count` and `body_count` from the payload onto the nightly-file document. The three fields arrive together. When the payload has no `trailer_ok` key, the nightly-file document is stored without `trailer_ok`, without `trailer_count`, and without `body_count`. The projector does not invent a trailer boolean for a file that did not send one.

Other payload keys on `SlotFiled` stay on the log. They are not added to the mart document and they are not added to the nightly-file document. The opening `SlotFiled` for `REF-4417` is an example. Its payload carries `ref` `REF-4417`, `site` `cedar-ridge`, `file_id` `cedar-2027-01-11`, `clinic` `ENDO-CLN`, `booking_date` `2027-01-11`, and `state` `WA`. It has no `trailer_ok`. The event `occurred_at` is `2027-01-11T21:00:00Z`. The mart document produced from it is `kind` `mart`, `ref` `REF-4417`, `booking_date` `2027-01-11`, `wait_days` 0. The nightly-file document is `kind` `nightly_file`, `ref` `REF-4417`, `file_id` `cedar-2027-01-11`, `site` `cedar-ridge`, `occurred_at` `2027-01-11T21:00:00Z`. `clinic` and `state` remain on the hospital log payload. Cedar Ridge can file at night, including a weekend. The row is still these columns. The Vancouver office week is not a column on the document.

A `SlotFiled` event does not also produce a pass-through event document. The two documents above are the whole projection of that type.

## How a cache row is produced

When the hospital type is `CacheStored`, the projector appends one document. `kind` is `eligibility_cache`. The columns are:

| Column | Source |
| --- | --- |
| `kind` | the string `eligibility_cache` |
| `ref` | payload `ref` |
| `eligible` | payload `eligible` |
| `window_present` | payload `window_present` |
| `occurred_at` | the event's `occurred_at` |

`eligible` is the boolean the hospital stored. `window_present` is the boolean stored beside it. They are separate columns. A cache row can hold `eligible` true and `window_present` false. The projector copies both values from the payload. It does not read a payer coverage document while it builds the cache row, and it does not fill `effective_from` onto the cache row. `effective_from` is a coverage column, produced from the payer log in the payer file.

Extra payload keys on `CacheStored` are not copied. The opening cache for `REF-4417` carries `eligible` true, `window_present` false, and a `source` string. The cache document receives `kind`, `ref` `REF-4417`, `eligible` true, `window_present` false, and `occurred_at` `2027-01-09T21:00:00Z`. The `source` string stays on the log payload.

The cache document does not receive `answer`, `file_id`, `trailer_ok`, `booking_date`, or `wait_days`. Those columns belong to the coverage row, the nightly-file row, or the mart row.

## How a coverage row is produced

The payer walk is separate. The projector reads `log_payer` only. When the type is `CoverageDecided`, it appends one document. `kind` is `coverage`. The columns are:

| Column | Source |
| --- | --- |
| `kind` | the string `coverage` |
| `ref` | payload `ref` |
| `answer` | payload `answer` |
| `effective_from` | payload `effective_from` when the key is present, otherwise null |
| `effective_to` | payload `effective_to` when the key is present, otherwise null |
| `currency` | payload `currency` when the key is present, otherwise null |
| `occurred_at` | the event's `occurred_at` |

`answer` is the string the payer stored on that command. The opening coverage command for `REF-4417` stores `answer` `yes`, `effective_from` `2027-01-12T00:00:00Z`, `effective_to` `2027-04-12T00:00:00Z`, and `currency` `CAD`, with event time `2027-01-08T16:00:00Z`. The coverage document receives those fields. `member_region` is on that command's payload and is not a column of the coverage document. It stays on the log.

A timeout is a `CoverageDecided` command whose payload has `answer` `timeout` and does not include `effective_from` or `effective_to`. The projector still emits a coverage document. `answer` is `timeout`. `effective_from` is null. `effective_to` is null. That null pair is the empty window. `currency` is copied when the payer sent it. The timeout command for `REF-2290` stores `answer` `timeout` and `currency` `USD` at `2027-01-09T19:40:00Z`, without a window. The coverage document has a null `effective_from` and a null `effective_to`. The projector does not borrow a window from a hospital cache row. The cache row and the coverage row are produced from different logs, into different files.

`wait_days`, `booking_date`, `eligible`, `window_present`, `file_id`, and `trailer_ok` are not columns of the coverage document. `eligible` and `window_present` are cache columns. `file_id` and `trailer_ok` are nightly-file columns. `wait_days` and `booking_date` are mart columns. A coverage row that needs to be read is read from `payer.sqlite`, by `kind` `coverage`.

## Every other event

A hospital event whose type is neither `SlotFiled` nor `CacheStored` becomes one document with `kind` `event`. The document carries `type`, `ref`, `occurred_at`, and `payload`. `ref` is the payload's `ref` when that value is present, and otherwise the event's `stream_id`. `LetterStored` and `DocumentChanged` take this path. Their payloads, including letter text or document fields, are nested under `payload` on the hospital event document. They do not become mart rows, nightly-file rows, or cache rows.

Every channel event takes the event path. `kind` is `event`. `type`, `ref`, `occurred_at`, and `payload` are stored. `RequestAccepted`, `HandsetDispatch`, and `DeskSession` remain events in `channel.sqlite`. The channel projector does not build a mart, a nightly file, or a coverage row. A channel utterance stays inside the channel payload.

A payer event whose type is not `CoverageDecided` takes the same event path in `payer.sqlite`. Only `CoverageDecided` becomes `kind` `coverage`.

The order of documents inside one file follows the `seq` order of that log, and, for `SlotFiled`, the mart document is inserted immediately before the nightly-file document of that same event. Loading `rows` without an `ORDER BY` returns the documents in insert order, which is that walk. The projector does not attach `seq` to the JSON. A reader who needs append order of the log reads the log. A reader who needs `wait_days`, `booking_date`, `eligible`, `window_present`, `file_id`, `trailer_ok`, `answer`, or `effective_from` reads the document of the matching `kind` in the file this specification assigns to that column.
