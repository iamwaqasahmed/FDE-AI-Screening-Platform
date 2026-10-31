---
id: SPEC-HOURS-DOCS
title: Hospital document fields
date: 2026-01-09
type: specification
author: Harper Singh
systems:
  - hospital
  - documents
access: student
---

# Hospital document fields

I am Harper Singh. I am the integration engineer for the hospital document store. This specification records the fields a hospital document row carries. The date is 9 January 2026. The store is the hospital log on the desk machine, table `log_hospital`, in the local SQLite file `var/log.sqlite`. A document change is a command with authority `hospital` and type `DocumentChanged`. The writer is local Python. It does not open a remote account. This page is about the fields on the document. It describes `status`, `audience`, `version`, the hash, and `body` as the hospital stores them.

A document command uses the same command envelope as any other hospital command: `command_id`, `authority`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. The document fields live in the payload. `stream_id` is the document id for the hours sheets and for the other documents that use the document id as their stream. `stream_rev` is the revision of that stream on `log_hospital`. A new revision is a new append. The log triggers abort update and delete, so a later status is a later row, and the earlier row remains with the payload it had when it was inserted. `occurred_at` is the time string on that command. It is the hospital's time for that append. It is not a clock shared with the channel log or the payer log.

The documents extract is a list built from these events. Each list element is the payload with `occurred_at` from the event copied onto the object. A reader of `documents.json` sees the fields below as properties of that object. A reader of the hospital projection sees the same payload nested under an event whose `type` is `DocumentChanged`. The field names are the same in both places.

## Body

`body` is the document text stored on that row. It is a string. The hospital stores the characters that were on the command. Hours sheets, leaflets, quotations, wage notes, and contract text are all stored in this field when the command is a `DocumentChanged`. The body is the text a reader quotes when they are quoting the document. It is not the version string, and it is not the hash. Two rows can carry related words and still be two bodies. The field to read is the `body` on the row in front of you.

The body is also the only input to the hash procedure below. Punctuation, spaces, and letter case are part of the body. A body that differs by a single character is a different byte string when it is hashed.

## Version

`version` is the version string stored on that row. It is text, not a numeric counter. The hospital has stored version strings such as `1`, `2`, `2026-summer`, `2027-winter`, `2027-01-draft`, `q-2027`, and `w-4`. The version identifies which writing of a document id the row claims to be. Several rows may share a `doc_id`. `version` is how those rows are told apart when their document ids match. The version is not fed into the hash. Changing the version string, and leaving the body the same, does not by itself change the digest the hash procedure computes from the body. The row still stores whatever `version` the command carried, beside whatever `body` the command carried.

`stream_rev` is the append revision on the hospital stream. It is not `version`. A row can have `stream_rev` 1 and a version string that is not `1`. Read both fields as they are stored. The unique pair on the log is `(stream_id, stream_rev)`. The version string is payload.

## Audience

`audience` is the audience string stored on that row. It names who the document addresses. Values the hospital document rows store include `public`, `procurement`, `payroll`, and `finance`. A hours sheet that was stored for the public page carries `audience` `public`. A quotation stored for procurement carries `procurement`. A wage note carries `payroll`. A contract document carries `finance`. The field is that string on the row. It does not select a second body. The body on the same row is the text stored for the audience stored on that row.

Language is a separate field, `language`, stored beside audience when the command included it. Values include `en` and `fr`. A French hours sheet is its own document id and its own body. Audience and language are two columns. This specification's required audience field is `audience`.

Some document rows also carry `close_local` and `timezone` because the hours command included them. `close_local` is a local time string such as `21:00` or `17:00`. `timezone` is a zone name such as `America/Los_Angeles`. Those keys are present on the hours rows that stored them. They are absent on a document command that did not include them. Absence means the command did not store the key. The hash procedure does not read `close_local` or `timezone`.

## Hash

The hash field on the row is `content_hash`. It is a string of hexadecimal characters stored in the payload next to `body`. The hospital's digest of a body is SHA-256 over the UTF-8 bytes of that body alone. The encoder uses the body string as it is stored. The digest does not include `version`. It does not include `status`, `audience`, `language`, `doc_id`, `close_local`, `timezone`, or `occurred_at`. Two bodies with the same characters produce the same digest. A version change that does not change the body does not change that digest.

The value kept on the row is the `content_hash` string on the document command. The default recording path sets that string to the digest of the body on the same command. The column and the body are still two fields. A reader who wants the digest of the stored body hashes `body` with the procedure above. A reader who wants the hash the row is holding reads `content_hash`. This specification defines both: the procedure that reduces a body to a digest, and the field the hospital stores under the name `content_hash`.

Contract text uses the same pair. The contract document `MA-2024` stores `body` and `content_hash` on each `DocumentChanged` row, with `version` beside them. The hash procedure is the same SHA-256 of the body. The contract id and the audience `finance` are stored on the row and are outside the hashed bytes.

## Status

`status` is the status string stored on that row. It is payload text. The hospital stores several status strings on document rows. Two of the statuses the hospital stores are superseded and in-force. On the row, superseded is the string `superseded`, and in-force is the string `in_force`.

`in_force` is a status the hospital stores. A document command whose payload says `in_force` is inserted with that string in `status`. The row keeps `in_force` for as long as the row remains. A later append does not rewrite it. Contract version `1` of `MA-2024` is stored on a `DocumentChanged` row with status `in_force`. Hours commands also store `in_force` on rows whose payload uses that string. The field on each of those rows is the string `in_force`.

`superseded` is a status the hospital stores. A document command whose payload says `superseded` is inserted with that string in `status`. The row keeps `superseded`. The hospital also stores a status note, type `StatusNoted`, whose payload carries `status` `superseded` for a version of a document id. That note is its own event. It does not delete the earlier `DocumentChanged` row and it does not change the earlier row's payload. Both the status string on a `DocumentChanged` payload and the status string on a `StatusNoted` payload are strings the hospital has stored. `superseded` is one of those strings.

Other status strings the hospital stores on document rows include `draft`, `in_flight`, and `unauthorized`. A Fraser draft hours document is stored with `draft`. A French hours document is stored with `in_flight`. A circular is stored with `unauthorized`. Each of those is the `status` on its own row, in the same field as `in_force` and `superseded`. The field does not hold a list. One row holds one status string, the one on its command.

A single `doc_id` can accumulate more than one row. Each row has its own `version`, its own `status`, its own `audience`, its own `body`, and its own `content_hash`. One row for a document id can store `superseded` while another row for the same document id stores `in_force`. The hours document id `hours-cedar` is stored that way: a row whose `version` is `2026-summer` carries status `superseded`, and a row whose `version` is `2027-winter` carries status `in_force`. Each row also has its own `body`, its own `content_hash`, its own `audience`, and its own `close_local`. Reading the status means reading the row. The summer row's status is the string on the summer row. The winter row's status is the string on the winter row.

Quotation rows and some contract rows carry extra columns such as `amount`, `currency`, `quote_id`, `contract_id`, and `site` when the command included them. Those columns do not replace `status`, `audience`, `version`, `content_hash`, or `body`. When a column is missing on a row, that command did not store it.

The log appends these payloads in the order the commands are accepted. `seq` on `log_hospital` is that append order. `occurred_at` is the time string on the command and can differ in order from `seq`. A document dated on the payload's own terms is still the row that was inserted. Rebuilds of the local file, through `python -m access init` or `reset`, write the same document commands again from the history the program carries. They rewrite the local SQLite file on this machine. They do not open an account, and they do not collapse two statuses into one row.

This specification is the field list for that store. `status` holds the stored status, including the stored values `superseded` and `in_force`. `audience` holds the stored audience. `version` holds the stored version string. `content_hash` holds the stored hash. `body` holds the stored text. A row is complete as stored when those fields that the command included are the fields on the row.
