---
id: WIKI-REPLICAS
title: Replica cursors and the two exports of amount 90
date: 2027-01-19
type: wiki
author: Bobbi Tran
systems:
  - hospital
  - channel
access: student
---

# Replica cursors and the two exports of amount 90

I am Bobbi Tran. I keep the three logs. This page is what I wrote down on 19 January 2027 after I opened `var/log.sqlite` and copied the replica rows for referral `R3E-SYNC`. The copy names on the rows are `cascade-copy` and `cedar-copy`. I am writing the figures that were on the rows. I did not update a row to produce this page, and I did not delete a row. The logs are still `log_hospital`, `log_channel`, and `log_payer` in one local file. There is no foreign key from one table to another. A shared-clock command is rejected by the writer. No remote account is open. These copies are rows on the hospital log on the desk machine.

The desk in Vancouver works Monday through Friday, America/Vancouver. Cedar Ridge is in Washington, America/Los_Angeles, and files at night, including weekends. Cascade Seattle is the hospital in Washington. The `occurred_at` strings below are the strings stored on the rows. I read `log_hospital` for the hospital rows and `log_channel` for the channel rows. Each table has its own `seq`. `seq` on the table is the append counter for that table. The numbers I am calling out from the cursor payloads are the `seq_caught` fields inside those payloads.

The local reader can return matching rows for `R3E-SYNC` through `GET /ref/R3E-SYNC` when the extracts contain them. `python -m access serve` binds `127.0.0.1` and port 8088 unless another port is given. It reads `student_pack/extracts`. It does not append, and it does not open the projection files to answer the GET. I used the log for the figures in this note. When a projection is built, it is built one log at a time into `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. `ReplicaCursor` and `ReplicaExport` are hospital types outside the `SlotFiled` and `CacheStored` branches, so the hospital walk stores them as event documents with the payload nested. They are still stored.

## The slot row these copies name

On `log_hospital`, stream `r3e-sync`, a `SlotFiled` row is stored with command id `cmd-r3e-slot-filed`, `occurred_at` `2027-01-18T21:00:00Z`, and stream revision 1. The payload I read carries:

- `ref` `R3E-SYNC`
- `booking_date` `2027-01-18`
- `file_id` `cedar-r3e-2027-01-18`
- `site` `cedar-ridge`
- `clinic` `ENDO-CLN`
- `state` `WA`
- `trailer_ok` true
- `trailer_count` 8
- `body_count` 8

Cedar Ridge has no slot API. The hospital log records the nightly file as an append. The file id is text on the payload. The cursor rows and the export rows name that same file id and that same source stream, `r3e-sync`.

## cascade-copy seq 10 and cedar-copy seq 14

Both cursor rows are hospital events of type `ReplicaCursor`. Both name source stream `r3e-sync` and file `cedar-r3e-2027-01-18`. Each sits on its own stream, at stream revision 1. The payload field I copied is `seq_caught`. These are the two numbers I saw.

cedar-copy seq 14. On `cedar-copy` I saw 14. The command id is `cmd-r3e-cursor-cedar`. The stream id is `r3e-cedar-copy`. The `occurred_at` string is `2027-01-18T22:10:00Z`. The replica field is `cedar-copy`. `seq_caught` is 14. The payload also carries `ref` `R3E-SYNC`, `source_stream` `r3e-sync`, and `file_id` `cedar-r3e-2027-01-18`.

cascade-copy seq 10. On `cascade-copy` I saw 10. The command id is `cmd-r3e-cursor-cascade`. The stream id is `r3e-cascade-copy`. The `occurred_at` string is `2027-01-18T22:16:00Z`. The replica field is `cascade-copy`. `seq_caught` is 10. The payload also carries `ref` `R3E-SYNC`, `source_stream` `r3e-sync`, and the same file id.

I wrote cedar-copy seq 14 and cascade-copy seq 10 because that is how the rows were stored when I looked. The cedar-copy cursor's `occurred_at` is `2027-01-18T22:10:00Z`. The cascade-copy cursor's `occurred_at` is `2027-01-18T22:16:00Z`. The two timestamps are the timestamps on those two rows. The two `seq_caught` numbers are 14 and 10. I am leaving 14 beside cedar-copy and 10 beside cascade-copy. The hospital `seq` of each row is the append counter on `log_hospital` only. `seq_caught` is a field inside the payload. I copied the payload field. I did not add it to the table's `seq`, and I did not subtract the two payload numbers from each other.

Chris Pell asked me, in the hallway, which figure the finance pack should treat as the one that counts. I told Chris I would write down what I saw. This page is that writing. Jordan Hale has the records seat at Cascade Seattle. Sam Nguyen sends the Cedar Ridge night file. The cursor rows name both copy strings. Both numbers are in the log.

## Amount 90 and the two currency words

Both export rows are hospital events of type `ReplicaExport`. Both name source stream `r3e-sync` and file `cedar-r3e-2027-01-18`. Each is stream revision 2 on the same replica stream as the cursor I listed above. Both payloads carry amount 90. The two currency words on those rows are `USD` and `CAD`.

On cedar-copy the export command is `cmd-r3e-export-cedar`, stream `r3e-cedar-copy`, stream revision 2, `occurred_at` `2027-01-19T14:40:00Z`, amount 90, currency word `USD`. The payload fields are `ref` `R3E-SYNC`, `replica` `cedar-copy`, `source_stream` `r3e-sync`, `file_id` `cedar-r3e-2027-01-18`, `amount` 90, and `currency` `USD`.

On cascade-copy the export command is `cmd-r3e-export-cascade`, stream `r3e-cascade-copy`, stream revision 2, `occurred_at` `2027-01-19T14:46:00Z`, amount 90, currency word `CAD`. The payload fields are `ref` `R3E-SYNC`, `replica` `cascade-copy`, `source_stream` `r3e-sync`, `file_id` `cedar-r3e-2027-01-18`, `amount` 90, and `currency` `CAD`.

Amount 90 is on both rows. `USD` is the currency word on the cedar-copy export. `CAD` is the currency word on the cascade-copy export. Those are the two currency words I read. Harbor Coverage is the payer, and Harbor rows on `log_payer` can carry `CAD` or `USD` on coverage documents. These two amount-90 rows are on the hospital log, on the replica streams. They are not on `log_payer`. I copied them from `log_hospital`. I did not move them onto a payer row. I did not edit either payload. An update of a log row aborts with `log rows are append-only`. A delete of a log row aborts with the same text. The two export rows stay as two appends.

I will hand Chris both lines. One line is amount 90 with the currency word `USD` on cedar-copy. The other line is amount 90 with the currency word `CAD` on cascade-copy. The digits of the amount are 90 on each line. The currency word is the `currency` field on that line. Both lines name file `cedar-r3e-2027-01-18`.

## Channel rows I also copied

I opened `log_channel` separately. Two `HandsetDispatch` rows share idempotency key `r3e-sms-1` and file id `cedar-r3e-2027-01-18`, on stream `r3e-handset`.

Attempt 1 is command `cmd-r3e-handset-1`, stream revision 1, status `sent`, `occurred_at` `2027-01-19T15:02:00Z`. The transcript stored on that row is `Northline visit filed at Cedar Ridge.` The payload carries `ref` `R3E-SYNC`, `file_id` `cedar-r3e-2027-01-18`, `idempotency_key` `r3e-sms-1`, `attempt` 1, `status` `sent`, and `transcripts` holding that one sentence.

Attempt 2 is command `cmd-r3e-handset-2`, stream revision 2, status `redelivered`, `occurred_at` `2027-01-19T15:08:00Z`. The transcript stored on that row is `Northline visit booked at Cedar Ridge.` The payload carries the same `ref`, the same `file_id`, the same idempotency key, `attempt` 2, `status` `redelivered`, and `transcripts` holding the second sentence.

I copied both transcripts. They are different sentences on two appends that reuse one idempotency key. The channel log kept both. The first dispatch is still in the table after the second append. A `QueueDepth` row, command `cmd-r3e-queue-depth`, stream `r3e-queue`, stream revision 1, at `2027-01-19T15:20:00Z`, records `visible_backlog` 120, `oldest_age_seconds` 5400, and `consumer_alive` true. The payload `ref` is `R3E-SYNC`.

A `DeskNote` on stream `r3e-desk`, command `cmd-r3e-desk-note`, stream revision 1, at `2027-01-19T15:26:00Z`, stores this sentence: `The morning board was printed from cascade-copy.` The payload also carries `ref` `R3E-SYNC` and `file_id` `cedar-r3e-2027-01-18`. I copied the sentence because it was the note on the row. The note names a print source. The cursor figures I wrote above are cedar-copy seq 14 and cascade-copy seq 10. The export lines I wrote above are amount 90 with `USD` and amount 90 with `CAD`. The note is an additional channel append. I am including it so the channel reading for this referral on this day includes the sentence that was stored.

## What is on the page

A person who opens this referral on the hospital log can find the `SlotFiled` row for file `cedar-r3e-2027-01-18`, the cedar-copy cursor with `seq_caught` 14, the cascade-copy cursor with `seq_caught` 10, the cedar-copy export of amount 90 in `USD`, and the cascade-copy export of amount 90 in `CAD`. A person who opens the channel log can find the two handset transcripts, the queue-depth payload, and the desk-note sentence. Each log is read on its own `seq`.

The command ids in the order the history lists them are `cmd-r3e-slot-filed`, `cmd-r3e-cursor-cedar`, `cmd-r3e-cursor-cascade`, `cmd-r3e-export-cedar`, `cmd-r3e-export-cascade`, `cmd-r3e-handset-1`, `cmd-r3e-handset-2`, `cmd-r3e-queue-depth`, and `cmd-r3e-desk-note`. Nine commands. Five of them are hospital commands. Four of them are channel commands. None of them is a payer command. None of them carries a `canonical_at` key. None of them is typed `SetCanonicalTime`.

I am the person who keeps the logs. On 19 January 2027 the rows above were the rows I read. cedar-copy seq 14 and cascade-copy seq 10 are the cursor figures. Amount 90 is on both exports. The two currency words are `USD` and `CAD`. The rows stay append-only. This page is the copy of what those payloads contained.
