---
id: WIKI-EXTRACTS
title: Student pack extracts and the local read URLs
date: 2027-01-11
type: wiki
author: Bobbi Tran
systems:
  - local-read-api
  - hospital
  - channel
  - payer
access: student
---

# Student pack extracts and the local read URLs

I am Bobbi Tran. This page is the list of extract files a student can open, the fields on the five files named below, and the local read URLs that return them. The date is 11 January 2027. The files are written on the desk machine by `python -m access init` or `python -m access reset`. They sit under `student_pack/extracts` in `enterprise_simulation`. The reader that serves them is local Python. `python -m access serve` binds `127.0.0.1` and port 8088 unless `--port` sets another port. On start it prints `http://127.0.0.1:<port>/extracts`. It does not bind a public interface, and it does not open a remote account.

The reader lists `*.json` in `student_pack/extracts`, sorts the paths, and parses each file as UTF-8 JSON. The key is the stem, the file name with `.json` removed. Each request reads the directory again. The reader does not open `var/log.sqlite`. It does not open `var/proj/hospital.sqlite`, `channel.sqlite`, or `payer.sqlite`. It does not append to the logs. There is no shared clock on this process. The three logs remain the append-only tables in `var/log.sqlite`. This process answers from the JSON files.

`student_pack/sponsor.json`, `student_pack/organization.json`, and `student_pack/README.md` sit beside the extracts directory and are not part of the bundle. Files under `student_pack/bytes/` are not part of the bundle. The reader does not import the sealed release module or the sealed holdout module. A file that is not in `student_pack/extracts` is not served.

## File names under the extracts directory

The five files this page lists field by field are:

- `hospital.json`
- `channel.json`
- `payer.json`
- `boards.json`
- `documents.json`

The stems are `hospital`, `channel`, `payer`, `boards`, and `documents`. After init or reset, the same directory also contains these stems, and the reader returns them with the same routes: `asks`, `assistant_screen`, `audit`, `byte_index`, `calibration`, `calls`, `desk`, `focus`, `host`, `identity_graph`, `legacy_desk`, `monthly_volume`, `served_document`, `shadow`, and `site_feeds`. Adding another JSON file in the directory adds another key on the next GET. Removing a file removes its key.

`hospital`, `channel`, and `payer` are the projected document lists copied from `var/proj/hospital.sqlite`, `channel.sqlite`, and `payer.sqlite`. `documents` is built from hospital event documents whose `type` is `DocumentChanged`: each object is that document's `payload` with `occurred_at` copied onto it. `boards` is a list of three objects written directly into `boards.json`. The other stems are the other JSON files in the folder. `GET /extracts` returns them together. It does not filter by referral.

## Read URLs

The process implements `GET`. A success sends status 200 and `Content-Type: application/json`. The handler does not write a request log line. With the default port, the read URLs are:

- `http://127.0.0.1:8088/`
- `http://127.0.0.1:8088/health`
- `http://127.0.0.1:8088/extracts`
- `http://127.0.0.1:8088/extracts/hospital`
- `http://127.0.0.1:8088/extracts/channel`
- `http://127.0.0.1:8088/extracts/payer`
- `http://127.0.0.1:8088/extracts/boards`
- `http://127.0.0.1:8088/extracts/documents`
- `http://127.0.0.1:8088/ref/<ref>`

`GET /` and `GET /health` return the JSON object `{"status":"up"}`. The status field on that object is the string `up`. A path that is not exactly `/` or exactly `/health` does not take this branch. `/health/` is not this route.

`GET /extracts` returns one JSON object, the whole bundle. Each key is a stem. Each value is the JSON value parsed from that file. A file that holds a list comes back as a JSON array. Key order inside an object follows the order in the file. The route is an exact path match. `/extracts/` is not this route. It falls through to the single-extract rule with an empty name.

`GET /extracts/<name>` returns the one bundle value whose key equals `<name>`. The name is the path text after `/extracts/`, with a query string removed if a `?` is present. The name is compared as that text. The reader does not strip a trailing slash, and it does not decode a percent-encoded character before the comparison. `GET /extracts/hospital` returns the hospital array. `GET /extracts/channel` returns the channel array. `GET /extracts/payer` returns the payer array. `GET /extracts/boards` returns the boards array. `GET /extracts/documents` returns the documents array. `GET /extracts/hospital?verbose=1` uses the name `hospital`, because the query is cut off before the lookup. The body of a hit is that one JSON value. It is not wrapped in an envelope.

When the name is not a key in the bundle, the response is status 404 with an empty body and no `Content-Type`. An unknown stem is a miss. The route does not create a file to satisfy a miss.

`GET /ref/<ref>` returns one JSON object with `ref` and `hits`. The referral text is the path after `/ref/`, with a query string removed. An unknown referral is still status 200, with `hits` an empty list and `ref` set to the text that was asked for. A hit is `{"extract": <stem>, "row": <row>}`. Hits are collected by walking the bundle in sorted stem order, and by walking each file in its stored order. The walk treats a JSON array as a list of objects. It treats a JSON object as a candidate row, and it also walks nested objects and nested arrays, except that it does not descend into a property named `payload`. A nested `payload` stays visible on the row that contains it.

A row matches when `ref` equals the requested text, or `stream_id` equals it, or `stream_ref` equals it, or `stream` equals it when `stream` is a string, or `stream` is an object whose `ref` equals it, or `payload` is an object whose `ref` equals it. Other strings on the row do not match. A referral that appears only inside a letter's prose is not a hit. `GET /ref/REF-4417` returns the hits whose fields name `REF-4417`, each labeled with the extract stem it came from. `GET /ref/REF-2290` returns the hits for that referral, including the coverage row whose `answer` is `timeout`. The route does not join those hits into one object. The list is the matches.

Any other path is status 404 with an empty body. The handler defines `GET` and does not define a post, put, patch, or delete method. Those methods are not routes that append a log command or edit an extract.

## Fields on hospital.json

`hospital.json` is a JSON array. Each element is one projection document. The `kind` string tells which field set is on that element.

A document with `kind` `mart` has these fields:

- `kind`
- `ref`
- `booking_date`
- `wait_days`

`wait_days` is the integer the hospital projection writes beside `booking_date`. On the mart documents this projection writes, that integer is 0. The mart document does not include `file_id`, `site`, `trailer_ok`, `clinic`, `state`, `eligible`, `window_present`, `answer`, or `currency`.

A document with `kind` `nightly_file` has these fields:

- `kind`
- `ref`
- `file_id`
- `site`
- `occurred_at`

When the hospital payload contained the key `trailer_ok`, the same document also has `trailer_ok`, `trailer_count`, and `body_count`. When the payload had no `trailer_ok` key, those three fields are absent. `booking_date` is not a field on the nightly-file document. The opening nightly file for `REF-4417` stores `file_id` `cedar-2027-01-11`, `site` `cedar-ridge`, and `occurred_at` `2027-01-11T21:00:00Z`.

A document with `kind` `eligibility_cache` has these fields:

- `kind`
- `ref`
- `eligible`
- `window_present`
- `occurred_at`

`eligible` and `window_present` are separate booleans. The opening cache for `REF-4417` stores `eligible` true and `window_present` false, with `occurred_at` `2027-01-09T21:00:00Z`.

A document with `kind` `event` has these fields:

- `kind`
- `type`
- `ref`
- `occurred_at`
- `payload`

`type` is the hospital type string, such as `DocumentChanged` or `LetterStored`. `payload` is the object stored on the log. `ref` is the payload `ref` when present, otherwise the stream id.

## Fields on channel.json

`channel.json` is a JSON array. Every element is an event document. The fields are:

- `kind`, the string `event`
- `type`
- `ref`
- `occurred_at`
- `payload`

`type` is the channel type string. `RequestAccepted`, `HandsetDispatch`, `DeskSession`, `DeskNote`, `WebhookAttempt`, and any other channel type that was appended appear here as `type`, with the payload nested. The opening `RequestAccepted` payload for `REF-4417` carries `ref`, `utterance`, `handset_delivered`, `channel`, and `desk_region`. A `HandsetDispatch` payload carries the keys that command stored, including `idempotency_key`, `attempt`, and `status` on the `REF-4417` dispatches. A `DeskSession` payload carries `session_id`, `token_subject`, `factor`, and `desk_region` on the opening desk row. The channel file does not contain `kind` `mart`, `nightly_file`, `eligibility_cache`, or `coverage`.

## Fields on payer.json

`payer.json` is a JSON array. A document with `kind` `coverage` has these fields:

- `kind`
- `ref`
- `answer`
- `effective_from`
- `effective_to`
- `currency`
- `occurred_at`

`answer` is the string the payer stored. `effective_from` and `effective_to` are the window strings when the payload had those keys, and null when it did not. `currency` is the code when the payload had it, and null when it did not. The opening coverage row for `REF-4417` stores `answer` `yes`, `effective_from` `2027-01-12T00:00:00Z`, `effective_to` `2027-04-12T00:00:00Z`, `currency` `CAD`, and `occurred_at` `2027-01-08T16:00:00Z`. The coverage row for `REF-2290` stores `answer` `timeout`, `currency` `USD`, `occurred_at` `2027-01-09T19:40:00Z`, and null for `effective_from` and `effective_to`. `member_region` is on the log payload of those commands and is not a field of the coverage document.

A payer document whose type was not `CoverageDecided` has `kind` `event` and the fields `type`, `ref`, `occurred_at`, and `payload`.

## Fields on boards.json

`boards.json` is a JSON array of three objects. Every object has these fields:

- `ref`
- `label_id`
- `label_text`
- `board_name`
- `board_value`
- `board_as_of`
- `currency_context`

The three objects stored in the file are these.

The object with `ref` `REF-4417` has `label_id` `since_you_asked`, `label_text` `Days since you asked Northline`, `board_name` `facility_mart`, `board_value` 0, `board_as_of` `2027-01-11`, and `currency_context` `CAD member, WA site`.

The object with `ref` `REF-8801` has `label_id` `since_facility_accepted`, `label_text` `Days since Cascade accepted the referral`, `board_name` `facility_mart`, `board_value` 13, `board_as_of` `2027-02-02`, and `currency_context` `USD`.

The object with `ref` `PERMIT-12` has `label_id` `since_lodged`, `label_text` `Days since the application was lodged`, `board_name` `records_counter`, `board_value` 19, `board_as_of` `2027-03-20`, and `currency_context` `CAD`.

`board_value` is an integer field on each object. `board_as_of` is the date string on that object. `currency_context` is the text on that object. `board_name` is `facility_mart` on the first two objects and `records_counter` on the third. Other referrals in `hospital.json` and `payer.json` have no object in this file. `GET /extracts/boards` returns the array of three. `GET /ref/REF-4417` includes the boards object whose `ref` is `REF-4417` when the walk reaches `boards`. Mart `wait_days` remains a field on mart documents in `hospital.json`. Board `board_value` remains a field on objects in `boards.json`.

## Fields on documents.json

`documents.json` is a JSON array. There is no `kind` field and no `type` field on these objects. Each object is a `DocumentChanged` payload plus `occurred_at`.

Fields that the document commands store, and that therefore appear on these objects, include:

- `doc_id`
- `version`
- `status`
- `audience`
- `language`
- `body`
- `content_hash`
- `occurred_at`

Hours rows also carry `close_local` and `timezone` when the payload had them. The `hours-cedar` row at stream revision 1 stores version `2026-summer`, status `superseded`, `close_local` `21:00`, timezone `America/Los_Angeles`, and `occurred_at` `2026-06-01T00:00:00Z`. The `hours-cedar` row at stream revision 2 stores version `2027-winter`, status `in_force`, `close_local` `17:00`, the same timezone, and `occurred_at` `2027-01-10T00:00:00Z`. The copy `hours-cedar-copy` stores its own `body` and its own `content_hash`.

A row includes a further key when that payload had it. Quotation rows can include `ref`, `packet_ref`, `quote_id`, `supplier_id`, `amount`, `currency`, and `site`. Contract rows can include `contract_id`. Status strings present on document commands include `in_force`, `superseded`, `unauthorized`, and `in_flight`. `audience` values on those commands include `public`, `procurement`, and `payroll`. `language` values include `en` and `fr`. If a key is absent on a particular object, that payload did not store it. `GET /extracts/documents` returns this array. `GET /ref/<ref>` hits a document object when the object has a `ref` equal to the request. A document whose only identifier is `doc_id` is opened from `GET /extracts/documents` by reading `doc_id`.

The five files and the read URLs above are the ones this page is for. The logs stay in `var/log.sqlite`. The reader returns the JSON that is in `student_pack/extracts` at the time of the GET.
