---
id: WIKI-PHONE
title: Phone field, digits then dashes
date: 2026-06-02
type: wiki
author: Harper Singh
systems:
  - channel
  - payer
access: student
---

# Phone field, digits then dashes

I am Harper Singh. I am the integration engineer on the Vancouver desk. This note is dated 2 June 2026. Today the channel log received a phone row whose form is dashed. The earlier phone rows on the same person are still the digits rows that were appended in 2025. Digits then dashes. Old rows are not rewritten.

The store is the local file `var/log.sqlite` on this machine. There are three append-only logs, `log_hospital`, `log_channel`, and `log_payer`. They do not share a table, and there is no foreign key from one to another. A shared-clock command is rejected. The phone commands in this note landed on the channel log and the payer log. I am not opening a remote account to read them. `read_log` for `channel` returns the channel rows ordered by `seq`. `read_log` for `payer` returns the payer rows ordered by `seq`. The local HTTP reader, when it is running, binds `127.0.0.1` and serves extracts. It does not rewrite a log row. This note is about the rows the writer stored.

The person id on every phone command below is `p-r2f-2701`. The field name on every phone command below is `phone`. The digit string is `6045552701`. The dashed string is `604-555-2701`. The digit string is ten digits with no hyphen. The dashed string is those same digits with a hyphen after `604` and a hyphen after `555`.

## Digits, first

The first phone command in this history is a channel `SchemaEpoch`. The command id is `cmd-r2f-schema-1`. The authority is `channel`. The type is `SchemaEpoch`. The `occurred_at` text is `2025-01-15`. The stream id is `r2f-schema`. The stream revision is 1. The payload is:

- `person_id` `p-r2f-2701`
- `field` `phone`
- `form` `digits`
- `example` `6045552701`

The example is the digit string. The form word is `digits`. This row is the schema epoch for the digits form. It is stream revision 1 on `r2f-schema`.

The next phone command is a channel `PhoneRecorded`. The command id is `cmd-r2f-phone-digits`. The authority is `channel`. The type is `PhoneRecorded`. The `occurred_at` text is `2025-04-11T17:20:00Z`. The stream id is `r2f-phone`. The stream revision is 1. The payload is:

- `person_id` `p-r2f-2701`
- `field` `phone`
- `form` `digits`
- `phone` `6045552701`

The `phone` value is the digit string `6045552701`. The form word is `digits`. This is the on-file channel row for the digits form. It is stream revision 1 on `r2f-phone`.

The next phone command is a payer `PhoneFiled`. The command id is `cmd-r2f-payer-digits`. The authority is `payer`. The type is `PhoneFiled`. The `occurred_at` text is `2025-04-11T19:05:00Z`. The stream id is `r2f-member`. The stream revision is 1. The payload is:

- `ref` `R2F-2701`
- `person_id` `p-r2f-2701`
- `field` `phone`
- `form` `digits`
- `phone` `6045552701`

This payer row is the copy of the digits number. It carries `ref` `R2F-2701` in addition to the phone fields. It lives on `log_payer`, stream `r2f-member`, stream revision 1. The channel digits row lives on `log_channel`. They are two inserts on two tables. They share the digit string `6045552701` and the form word `digits` because both payloads were written that way. The schema does not link them with a foreign key.

Append order for the digits half is the schema epoch, then the channel `PhoneRecorded`, then the payer `PhoneFiled`. That is digits, stored before any dashed phone command in this history.

## Dashes, after

The dashed schema epoch was appended later. The command id is `cmd-r2f-schema-2`. The authority is `channel`. The type is `SchemaEpoch`. The `occurred_at` text is `2026-06-01`. The stream id is `r2f-schema`. The stream revision is 2. The payload is:

- `person_id` `p-r2f-2701`
- `field` `phone`
- `form` `dashed`
- `example` `604-555-2701`

The example is the dashed string `604-555-2701`. The form word is `dashed`. This is a new row. Stream revision 2 is a new `stream_rev` on `r2f-schema`. The revision 1 row, with form `digits` and example `6045552701`, is still in `log_channel`. The writer inserted revision 2. It did not update revision 1.

Today's on-file dashed row is a channel `PhoneRecorded`. The command id is `cmd-r2f-phone-dashed`. The authority is `channel`. The type is `PhoneRecorded`. The `occurred_at` text is `2026-06-02T16:40:00Z`. The stream id is `r2f-phone`. The stream revision is 2. The payload is:

- `person_id` `p-r2f-2701`
- `field` `phone`
- `form` `dashed`
- `phone` `604-555-2701`

The `phone` value is `604-555-2701`. The form word is `dashed`. This is the row dated today. It is stream revision 2 on `r2f-phone`. The revision 1 row on that same stream is still the digits `PhoneRecorded` from `2025-04-11T17:20:00Z`, with `phone` `6045552701` and form `digits`.

Digits then dashes. The digits schema epoch is stream revision 1. The dashed schema epoch is stream revision 2. The digits `PhoneRecorded` is stream revision 1. The dashed `PhoneRecorded` is stream revision 2. The payer `PhoneFiled` row is still the digits payload. This history does not contain a second payer command that stores `604-555-2701`. The payer table still has stream `r2f-member` at stream revision 1 with form `digits` and phone `6045552701`.

## Old rows are not rewritten

A log row is inserted once. The update trigger on `log_channel` is `log_channel_no_update`, `BEFORE UPDATE`, and it aborts with the text `log rows are append-only`. The same abort is on `log_payer` under the name `log_payer_no_update`. An `UPDATE` that tried to change the revision 1 payload from `6045552701` to `604-555-2701` would abort. The revision 1 payload would remain the digits payload that was inserted. The delete trigger aborts the same way, with the same text. Deleting the digits row is not how the dashed row was stored. The dashed row is a later insert with a new `command_id` and a new `stream_rev`.

I read `log_channel` after today's append. Ordered by `seq`, the phone-related channel rows from this history are:

- `cmd-r2f-schema-1`, type `SchemaEpoch`, `occurred_at` `2025-01-15`, stream `r2f-schema`, stream revision 1, form `digits`, example `6045552701`
- `cmd-r2f-phone-digits`, type `PhoneRecorded`, `occurred_at` `2025-04-11T17:20:00Z`, stream `r2f-phone`, stream revision 1, form `digits`, phone `6045552701`
- `cmd-r2f-schema-2`, type `SchemaEpoch`, `occurred_at` `2026-06-01`, stream `r2f-schema`, stream revision 2, form `dashed`, example `604-555-2701`
- `cmd-r2f-phone-dashed`, type `PhoneRecorded`, `occurred_at` `2026-06-02T16:40:00Z`, stream `r2f-phone`, stream revision 2, form `dashed`, phone `604-555-2701`

Four channel rows. Two streams. Each stream has revision 1 and revision 2. Revision 1 on each stream is still the digits payload. Revision 2 on each stream is the dashed payload. The `seq` values are whatever rowids `log_channel` assigned when those inserts happened, among the other channel inserts. I am not treating those rowids as a clock shared with `log_payer`. The payer row is on the other table.

On `log_payer` the phone row from this history is still one row:

- `cmd-r2f-payer-digits`, type `PhoneFiled`, `occurred_at` `2025-04-11T19:05:00Z`, stream `r2f-member`, stream revision 1, `ref` `R2F-2701`, form `digits`, phone `6045552701`

That payload text is the text written in April 2025. Today's channel insert did not open `log_payer` and did not change that payload. Old rows are not rewritten. The digits payer row is an old row. It is still digits.

Replaying a command id returns the original `event_id` and does not write a second row. Sending `cmd-r2f-phone-digits` again returns the event id already stored for that command id. It does not replace the digits payload with the dashed string. Sending `cmd-r2f-phone-dashed` again returns the event id of today's row. It does not erase the digits row. A new command id that reused stream `r2f-phone` at stream revision 1 would fail the unique pair `(stream_id, stream_rev)` on `log_channel` and roll back. The way the dashed form was stored was stream revision 2, command id `cmd-r2f-phone-dashed`, a new insert.

`event_id` is the SHA-256 hex of the identity object: authority, type, `occurred_at`, `stream_id`, `stream_rev`, and payload. `seq` is not in the hash. `command_id` is not in the hash. The digits `PhoneRecorded` and the dashed `PhoneRecorded` have different `occurred_at` values, different `stream_rev` values, and different payloads, so they are two event ids and two rows. The digits payload still contains the key `phone` with the value `6045552701` and the key `form` with the value `digits`. The dashed payload contains the key `phone` with the value `604-555-2701` and the key `form` with the value `dashed`. The schema epoch rows use `example` rather than `phone`. The digits epoch's `example` is still `6045552701`. The dashed epoch's `example` is `604-555-2701`.

## What the projector does with these types

`SchemaEpoch`, `PhoneRecorded`, and `PhoneFiled` are type strings the writer stored. The channel projector stores every channel event as `kind` `event`, with `type`, `ref`, `occurred_at`, and `payload`. `SchemaEpoch` and `PhoneRecorded` take that path. Their payloads have no `ref`, so `ref` on the event document is the stream id, `r2f-schema` or `r2f-phone`. The payload object still holds `person_id`, `field`, `form`, and either `example` or `phone`. The payer projector stores a type other than `CoverageDecided` as `kind` `event`. `PhoneFiled` takes that path in `payer.sqlite`. Its payload has `ref` `R2F-2701`, so the event document's `ref` is `R2F-2701`, and the payload still holds the digits phone. Unknown types are still stored. These three type strings are stored. Building the projection again reads the log as it is, including the digits rows and the dashed rows. The projector does not update the log while it writes the projection files.

The student extracts `channel.json` and `payer.json` are copies of those projection documents after a build. `GET /extracts/channel` and `GET /extracts/payer` return those arrays from `student_pack/extracts`. `GET /ref/R2F-2701` hits the payer `PhoneFiled` document because that document's `ref` and its payload `ref` are `R2F-2701`. The channel `SchemaEpoch` and `PhoneRecorded` payloads have no `ref`. On those event documents the projector sets `ref` from the stream id, so the schema documents carry `ref` `r2f-schema` and the phone documents carry `ref` `r2f-phone`. A lookup for `R2F-2701` does not select the channel documents. A lookup for `r2f-phone` selects the `PhoneRecorded` documents. A lookup for `r2f-schema` selects the `SchemaEpoch` documents. `person_id` and `phone` stay inside the payload. The ref route does not match on those keys. A reader of the channel extract sees two `PhoneRecorded` event documents when the pack was built from the log that contains both revisions, and one `SchemaEpoch` for digits and one `SchemaEpoch` for dashes.

## The strings side by side

Digits, stored first:

- schema example `6045552701`, form `digits`, `2025-01-15`, command `cmd-r2f-schema-1`
- channel phone `6045552701`, form `digits`, `2025-04-11T17:20:00Z`, command `cmd-r2f-phone-digits`
- payer phone `6045552701`, form `digits`, `ref` `R2F-2701`, `2025-04-11T19:05:00Z`, command `cmd-r2f-payer-digits`

Dashes, stored after:

- schema example `604-555-2701`, form `dashed`, `2026-06-01`, command `cmd-r2f-schema-2`
- channel phone `604-555-2701`, form `dashed`, `2026-06-02T16:40:00Z`, command `cmd-r2f-phone-dashed`

The phone commands store `person_id`, `field`, `form`, and the number under `example` or `phone`. They do not store a spreadsheet source field. I am writing what the log has after today's append.

Old rows are not rewritten. The 2025 digits rows remain in the tables with the payloads listed above. The dashed rows are additional appends. Digits then dashes is the order of those appends: digits in January and April 2025, dashes on 1 June 2026 and on 2 June 2026. This note is the integration record of that order on the day the dashed `PhoneRecorded` was stored.
