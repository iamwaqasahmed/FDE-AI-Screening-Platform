---
id: RUN-MIGRATE
title: Phone rows change shape without a rewrite
date: 2026-06-02
type: runbook
author: Harper Singh
systems:
  - channel
  - payer
  - hospital
  - local-read-api
access: student
---

# RUN-MIGRATE

I am Harper Singh, integration engineer at Northline Access Collaborative. I am writing this on 2 June 2026, at the Vancouver desk, just before the phone format change. The office week is Monday through Friday. Today is a Tuesday. The desk clock on the wall is America/Vancouver. This note is about the phone field already stored on the logs, and about the shape new rows will use. It is not a project plan for another system. The logs are here, on this machine, in `var/log.sqlite`.

No account is open. I am not loading a migration job into a remote account, because there is no account, and nothing in this change was deployed. The change is a convention for new appends. The file stays the file. Bobbi Tran keeps the three logs with me while I am still in the integration seat. After I leave, this page is the note I want the next person to have about phones.

## The three tables this change touches

There are three append-only tables: `log_hospital`, `log_channel`, and `log_payer`. A command names its authority. Update is rejected. Delete is rejected. The abort text is that log rows are append-only. A command that tries to install one shared clock is rejected. The writer refuses a payload that carries a shared instant for every authority, and it refuses a command whose type exists only to set that shared instant. Phone text does not become a clock. A phone row keeps the `occurred_at` the command brought, on the table the authority named.

There is no foreign key from the channel phone row to the payer phone row. The same digits can be copied into both payloads because both commands carried them. The schema does not check that the other log matches. I am not adding that check as part of today's change.

The desk reads extracts through the local HTTP process. `python -m access serve` binds `127.0.0.1` and port 8088 unless another port is given. It reads JSON under `student_pack/extracts`. `GET /extracts` returns the bundle. `GET /extracts/<name>` returns one file. `GET /ref/<ref>` returns matching rows. The reader does not append, and it does not rewrite a phone string while it serves. If a clerk refreshes an extract and still sees digits, the digits are what was written into the extract from the log. Refreshing the page is not a rewrite of the old row.

## What is already stored

Phones were stored as digits. The field name is `phone`. The form name on the schema note is `digits`. The example on that note is `6045552701`. The person id on the note is `p-r2f-2701`.

On the channel log, stream `r2f-schema`, command `cmd-r2f-schema-1` is a `SchemaEpoch` at stream revision 1. `occurred_at` is `2025-01-15`. The payload says field `phone`, form `digits`, example `6045552701`.

On the channel log, stream `r2f-phone`, command `cmd-r2f-phone-digits` is a `PhoneRecorded` at stream revision 1. `occurred_at` is `2025-04-11T17:20:00Z`. The payload stores form `digits` and phone `6045552701` for person `p-r2f-2701`.

On the payer log, stream `r2f-member`, command `cmd-r2f-payer-digits` is a `PhoneFiled` at stream revision 1. `occurred_at` is `2025-04-11T19:05:00Z`. The payload stores the same person, the same form `digits`, the same phone `6045552701`, and referral `R2F-2701`. That payer row is its own append. It is not a foreign key back to the channel row. The channel `occurred_at` and the payer `occurred_at` are two strings. I am not sorting the channel log and the payer log together and calling that the moment the number was "really" captured. Each string stays on its own row.

I looked at those three rows this morning. They are still digits. I did not issue an update. An update would be rejected. I did not issue a delete. A delete would be rejected.

## The form new rows use

New rows use dashes. The dashed example I am writing into the convention is `604-555-2701`. The digits `6045552701` and the dashed string `604-555-2701` are the two shapes of this one synthetic member number. The dashed shape puts a hyphen after the area code and after the exchange. The digits shape is the ten digits with no hyphen.

Yesterday, 1 June 2026, the channel log took a second schema append. Command `cmd-r2f-schema-2` is a `SchemaEpoch` on stream `r2f-schema` at stream revision 2. `occurred_at` is `2026-06-01`. The payload says field `phone`, form `dashed`, example `604-555-2701`, person `p-r2f-2701`. That schema row is a new append. It does not edit revision 1. Revision 1 still says `digits` and still shows `6045552701`.

I am writing this note just before the phone format change on the phone rows themselves. The `PhoneRecorded` row that is already on `r2f-phone` is the digits row. New phone rows use dashes. When the next `PhoneRecorded` for this person is appended, its form is `dashed` and its phone text is `604-555-2701`. That next row is a later `stream_rev` on `r2f-phone`. It is not a replacement of revision 1. Anyone who opens the stream after that append will see revision 1 in digits and the later revision in dashes.

Old rows were not rewritten. I want that sentence in the plainest words I have. The digits `PhoneRecorded` stays. The digits `PhoneFiled` on the payer log stays. The digits `SchemaEpoch` stays. I did not run a pass that walks old payloads and inserts hyphens. I will not run one this afternoon. Append-only is the reason, and it is also the choice. A rewrite would be an update. Update is rejected. A rewrite that deleted the digits row and inserted a dashed row under the same identity would still be a delete of the digits row. Delete is rejected. The inbox returns the original event id when a command id is replayed, and it does not write a second row for that same command id. The dashed phone, when it is appended, needs its own command id. Replaying `cmd-r2f-phone-digits` will not turn that row into dashes.

## Both shapes will be in the log

Both shapes will be in the log. After the new rows are appended, a reader who searches payloads for `6045552701` will still find the old rows, and a reader who searches for `604-555-2701` will find the new rows. The channel log will hold both forms. The payer log will still hold the digits filing unless a later payer command appends something else. I am not promising a payer append today. I am promising that I am not rewriting the payer digits row to match the dashed example. Both shapes will be in the log because the old shape remains and the new shape is an additional append.

If you export one stream to a spreadsheet and your sheet shows a single phone column, you have collapsed two stored strings into one display. The log did not collapse them. `6045552701` is the text on the old rows. `604-555-2701` is the text new rows use. Comparing them as equal is a comparison you might do in a notebook. It is not a constraint the table enforces. I am not adding a check that strips hyphens before insert. The payload is stored as it arrived.

Clerks on the desk, including June Lau in member services and Noel Park on the phone bay, will see member numbers that look uneven. Some rows have hyphens. Some rows are ten digits. That unevenness is the stored state after today. I do not want a well-meaning script "cleaning" the file overnight. Cleaning, in this case, means update or delete, and both are rejected. If a script reports that it normalized a thousand phones, it did not normalize these tables. Come and get me, or get Bobbi, before you believe the report.

## What I am not doing with the other logs

Hospital rows are a different authority. A hospital payload can mention a person. Today's phone convention is about the phone field on the channel schema and the phone rows that follow it, plus the payer filing that already copied the digits. I am not opening `log_hospital` to rewrite clinic notes so they display hyphens. Old rows were not rewritten there either. There is no shared clock I can use to say the hospital note and the channel phone "happened at one converted instant." Each row keeps its own `occurred_at`.

Projections are rebuilt from one log at a time. `var/proj/channel.sqlite` comes from the channel log. `var/proj/payer.sqlite` comes from the payer log. `var/proj/hospital.sqlite` comes from the hospital log. When `project` runs, it replaces the projection file it is writing. It does not join the three logs, and it does not hyphenate an old payload during the copy. If the channel projection shows a digits phone document and, later, a dashed phone document, that is because both events are on the channel log. If the payer projection shows digits, that is because the payer row is still digits.

The local reader serves whatever JSON the extract build wrote. It does not have a formatter that prints every phone with dashes for the sake of the screen. When you are asked what the member's phone is, read the row you were asked about and quote the characters on that row. Quote `6045552701` when you are on the digits row. Quote `604-555-2701` when you are on a new dashed row. Say which command id you read. The two strings are both in the story of `p-r2f-2701` once the new row exists. Both shapes will be in the log.

## After I leave the seat

This is the change as it stands on the morning of 2 June 2026, just before new phone rows take the dashed form. Schema revision 2, dated 1 June 2026, already records form `dashed` and example `604-555-2701`. Schema revision 1 still records form `digits` and example `6045552701`. The phone row at `r2f-phone` revision 1 is still `6045552701`. The payer filing is still `6045552701` on `R2F-2701`. Old rows were not rewritten. New rows use dashes. Both shapes will be in the log.

If you are reading this in a later month, do not "finish" the change by editing history. The finished state of an append-only phone field is the presence of both shapes. The digits rows are the record of how the number was stored. The dashed rows are the record of how later commands stored it. I would rather you show a supervisor both strings than show them one string you wish the file contained.
