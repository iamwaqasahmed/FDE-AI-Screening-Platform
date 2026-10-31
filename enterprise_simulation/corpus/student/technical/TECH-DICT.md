---
id: TECH-DICT
title: Data dictionary for the extracts
date: 2027-01-05
type: data-dictionary
author: Jordan Hale
systems:
  - hospital
  - payer
  - documents
  - boards
access: student
---

This dictionary is for a new hire in records at Cascade Seattle. I am Jordan Hale. The files below are the ones you can open on your first week. They sit in the student extracts, and the local reader returns the same JSON. The pages here define the columns those files already contain. A column that is absent on a particular row was not stored for that row.

You will see the same referral code on a mart row, a nightly file, a cache row, and a coverage row. Each of those rows has the columns of its own kind. Read the kind, then read the columns listed for that kind. The dictionary does not add fields.

## Mart

Mart rows live in the hospital extract. `kind` is the string `mart`. These are the columns on that row.

`kind` marks the document as a mart row so you can separate it from a nightly file or a cache row in the same file.

`ref` is the referral code stored on the mart.

`booking_date` is the date stored from the hospital slot filing. It is a calendar date, written as year, month, and day.

`wait_days` is the integer stored beside `booking_date`. The hospital projection writes this figure when it builds the mart. On the extracts you can open, the stored integer is 0.

A mart row does not carry the nightly file's trailer fields, the cache flags, or the payer answer. Those live on their own rows. When you are asked for the mart, quote `ref`, `booking_date`, and `wait_days` from the row whose `kind` is `mart`.

## Nightly file

Nightly-file rows live in the hospital extract. `kind` is the string `nightly_file`. Cedar Ridge is a nightly file site. The file is how that clinic's slot arrives.

`kind` marks the document as a nightly file.

`ref` is the referral code stored on the file row.

`file_id` is the identifier of the file the hospital recorded. You will see values such as `cedar-2027-01-11` and older cedar file names. Use the string as an identifier. Two rows can mention related work and still carry different `file_id` values. One clinic can also reuse a file id on a later replay. Read the id that is on the row in front of you.

`site` is the site code stored on the file, such as `cedar-ridge`.

`occurred_at` is the timestamp stored on the nightly-file row. It is copied from the hospital event that filed the slot.

`trailer_ok` is present when the hospital sent a trailer with the file. It is a boolean. `true` means the hospital marked the trailer acceptable. `false` means the hospital marked the trailer unacceptable. When `trailer_ok` is present, the row also has `trailer_count` and `body_count`. `trailer_count` is the count in the trailer. `body_count` is the count in the body. When the hospital did not send a trailer, those three fields are absent. Do not fill them with a zero to make the row look complete. Absence is the stored state.

A nightly file can be recorded on a weekend. The row still uses the columns above. The office week of the Vancouver desk is not a column on this document.

## Eligibility cache

Cache rows live in the hospital extract. `kind` is the string `eligibility_cache`.

`kind` marks the document as a cache row.

`ref` is the referral code stored on the cache.

`eligible` is a boolean. `true` means the cache stored the member as eligible. `false` means the cache stored the member as not eligible.

`window_present` is a boolean beside `eligible`. `true` means a window was stored on the cache. `false` means a window was not stored on the cache. The two booleans are separate columns. A row can have `eligible` true and `window_present` false. Read both.

`occurred_at` is the timestamp stored on the cache row.

The cache row does not include `effective_from`, `effective_to`, or `currency`. Those columns belong to coverage.

## Coverage

Coverage rows live in the payer extract. `kind` is the string `coverage`. Harbor Coverage writes these.

`kind` marks the document as coverage.

`ref` is the referral code stored on the coverage row.

`answer` is the payer answer stored on the row. The values you will see are `yes`, `no`, and `timeout`.

`effective_from` is the start of the window when the payer stored one. On a timeout the field is null. That null is the empty window.

`effective_to` is the end of the window when the payer stored one. On a timeout the field is null.

`currency` is the currency code stored on the payer row. You will see `CAD` and `USD`. Read the code on the row.

`occurred_at` is the timestamp stored on the coverage row.

A timeout row still has `kind`, `ref`, `answer`, `currency`, and `occurred_at`. The window columns are null. A `yes` or `no` row carries the window the payer sent, as timestamps, along with the currency the payer sent.

## Documents

Document rows live in the documents extract. They are a list. There is no `kind` column. A document is one version of one document id, with the text and the hash stored beside it.

`doc_id` is the document identifier. Several rows can share a `doc_id` when more than one version was stored. `hours-cedar` is one such id. Read `version` to tell the rows apart.

`version` is the version string stored on that row.

`status` is the status stored on that row. Values present in the extract include `draft`, `in_flight`, `in_force`, `superseded`, and `unauthorized`.

`audience` is who the document addresses. Values include `public`, `clinician` on letters held in the hospital events, and on these rows `public`, `procurement`, `payroll`, and `finance`.

`language` is the language code stored on the row, such as `en` or `fr`.

`body` is the text stored on the row.

`content_hash` is the hash string stored with that body.

`occurred_at` is the timestamp stored on the document row. One contract row stores a date without a time portion. Read the string that is there.

Some rows carry extra columns because that document had them. `close_local` is a local close time, such as `21:00` or `17:00`, on hours sheets that stored one. `timezone` is the timezone name stored on that sheet, such as `America/Los_Angeles`. Quotation rows may include `amount`, `currency`, `quote_id`, `supplier_id`, `site`, `packet_ref`, and `ref`. Contract rows may include `contract_id`. If a column is not on the row, it was not stored. The hours copy and the hours sheet can both be in the file as separate `doc_id` values. Compare `body` and `content_hash` on the row you opened.

## Boards

Board rows live in the boards extract. They are a short list. Each row is one labeled number.

`ref` is the referral or case code stored on the board row.

`label_id` is the identifier of the label printed for that row.

`label_text` is the words of the label stored on the row.

`board_name` is the name of the board. Values in the file include `facility_mart` and `records_counter`.

`board_value` is the number stored on that board row. It is an integer. It is a different column from mart `wait_days`. Read it from the board row.

`board_as_of` is the date string stored on the board row, written as year, month, and day.

`currency_context` is the text stored on the board row about the currency setting of that line. Examples in the file include `CAD member, WA site`, `USD`, and `CAD`. Quote the text on the row.

The board list you can open has one row for `REF-4417`, one for `REF-8801`, and one for `PERMIT-12`. Other referrals in the hospital and payer extracts do not have a board row in this file. When you need a board value, look here. When the referral is absent, say the boards extract has no row, and continue with the mart, nightly file, cache, coverage, or document that does.

## How to look something up

Start from the referral code. In the hospital extract, collect every row with that `ref` and group them by `kind`. Read mart columns only on `mart`, nightly columns only on `nightly_file`, and cache columns only on `eligibility_cache`. In the payer extract, read coverage columns on `coverage`. In the documents extract, match `doc_id` or a `ref` when the document stored one. In the boards extract, match `ref` and then read `board_name`, `board_value`, `board_as_of`, and `currency_context`.

The local reader can return one extract by name, or the rows whose ref matches across the bundle. Either way you get these columns. Write them down as stored. A new hire's first week is reading, filing the column names above, and asking records when a row uses a field this dictionary already defines.
