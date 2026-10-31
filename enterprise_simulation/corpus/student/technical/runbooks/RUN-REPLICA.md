---
id: RUN-REPLICA
title: Cursor figures and amount 90 on the two copies
date: 2027-01-19
type: runbook
author: Bobbi Tran
systems:
  - hospital
  - channel
  - local-read-api
access: student
---

# RUN-REPLICA

I am Bobbi Tran. I keep the three logs. This note is what I saw on 19 January 2027 when I opened the hospital log for referral `R3E-SYNC` and wrote down the replica cursors, and then the two export rows that both carry amount 90. Cascade Seattle and Cedar Ridge are different sites. The copy names on these rows are `cascade-copy` and `cedar-copy`. I am writing the figures that were on the rows. The logs are still the three append-only tables in `var/log.sqlite`. I did not update them to produce this note, and I did not delete anything. Delete is rejected. There is no shared clock. No account is open. These copies are rows on the hospital log on the desk machine. They are not servers I deployed anywhere.

The desk in Vancouver works Monday through Friday, America/Vancouver. Cedar Ridge is in Washington, America/Los_Angeles, and files at night, including weekends. The rows below use the `occurred_at` strings that were stored with them. I am not lining those strings up with the channel log and calling the mixture the order of the morning. I read the hospital table for the hospital rows, and I read the channel table for the channel rows. That is the same reading I wrote for new hires on 1 November 2026.

## How I opened the file

`log_hospital`, `log_channel`, and `log_payer` share `var/log.sqlite` and do not share a table. There is no foreign key from one to another. A referral string can appear in more than one payload. `R3E-SYNC` appears on hospital rows and on channel rows. Each table has its own `seq`. I stayed inside one table at a time.

The local HTTP process serves extracts. `python -m access serve` binds `127.0.0.1` and port 8088 unless another port is given. It reads JSON under `student_pack/extracts`. It does not append, and it does not open the projection files to answer `GET /extracts` or `GET /ref/<ref>`. I used the log for the figures in this note. The projections, when they are built, are built one log at a time into `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. A projection is not a merged clock.

A command that tries to install one shared clock is rejected. I did not send one. The `occurred_at` values below are the strings on the rows I read.

## The file these copies name

On the hospital log, stream `r3e-sync`, a `SlotFiled` row is stored with `occurred_at` `2027-01-18T21:00:00Z`, stream revision 1. The payload I read carries referral `R3E-SYNC`, file id `cedar-r3e-2027-01-18`, site `cedar-ridge`, clinic `ENDO-CLN`, state `WA`, `trailer_ok` true, `trailer_count` 8, and `body_count` 8. The booking date stored on that payload is `2027-01-18`. I am copying those fields because they were on the slot row. The cursor rows and the export rows name that same file id and that same source stream.

Cedar Ridge has no slot API. The hospital log records the nightly file as an append. I am not describing a second system in another account. The file id is text on the payload.

## The two cursors

Both cursor rows are hospital events of type `ReplicaCursor`. Both name source stream `r3e-sync` and file `cedar-r3e-2027-01-18`. Each sits on its own stream, at stream revision 1. The payload field I copied is `seq_caught`. These are the two numbers I saw.

On `cedar-copy` I saw 14. The command id on that row is `cmd-r3e-cursor-cedar`. The stream id is `r3e-cedar-copy`. The `occurred_at` string is `2027-01-18T22:10:00Z`. The replica field is `cedar-copy`. `seq_caught` is 14.

On `cascade-copy` I saw 10. The command id on that row is `cmd-r3e-cursor-cascade`. The stream id is `r3e-cascade-copy`. The `occurred_at` string is `2027-01-18T22:16:00Z`. The replica field is `cascade-copy`. `seq_caught` is 10.

I wrote 14 beside cedar-copy and 10 beside cascade-copy because that is how the rows were stored when I looked. The two timestamps are the timestamps on those two rows. I am leaving the two numbers as two numbers. Chris Pell asked me, in the hallway, which figure the finance pack should treat as the one that counts. I told Chris I would write down what I saw. This note is that writing. The hospital `seq` of each row is the append counter on `log_hospital` only. `seq_caught` is a field inside the payload. I am not adding those payload numbers to the table's `seq`, and I am not subtracting them.

## Amount 90, two currencies

Both export rows are hospital events of type `ReplicaExport`. Both name source stream `r3e-sync` and file `cedar-r3e-2027-01-18`. Each is stream revision 2 on the same replica stream as the cursor I listed above. Both payloads carry amount 90. The currencies on amount 90 are the two codes I saw on those two rows.

On `cedar-copy` the export command is `cmd-r3e-export-cedar`, `occurred_at` `2027-01-19T14:40:00Z`, amount 90, currency `USD`.

On `cascade-copy` the export command is `cmd-r3e-export-cascade`, `occurred_at` `2027-01-19T14:46:00Z`, amount 90, currency `CAD`.

Amount 90 is on both rows. `USD` is the currency code on the cedar-copy export. `CAD` is the currency code on the cascade-copy export. Harbor Coverage is the payer, and Harbor rows can carry CAD or USD on the payer log. These two amount-90 rows are on the hospital log, on the replica streams, not on `log_payer`. I am not moving them onto a payer row in order to make one code. I am not editing either payload. Update is rejected. Delete is rejected. A later append would be a new event if an authority sent one. I am not sending one in this note.

Jordan Hale has the records seat at Cascade Seattle. Sam Nguyen sends the Cedar Ridge night file. I have not asked either of them to replace a currency code. The two codes are in the log as two appends. Both shapes of the amount sit beside the same digits, 90, with different currency text. I will hand Chris both lines: amount 90 with `USD` on cedar-copy, and amount 90 with `CAD` on cascade-copy.

## Channel rows I also copied

I opened `log_channel` separately. Two `HandsetDispatch` rows share idempotency key `r3e-sms-1` and file id `cedar-r3e-2027-01-18`, on stream `r3e-handset`.

Attempt 1, command `cmd-r3e-handset-1`, status `sent`, `occurred_at` `2027-01-19T15:02:00Z`. The transcript stored on that row is "Northline visit filed at Cedar Ridge."

Attempt 2, command `cmd-r3e-handset-2`, status `redelivered`, `occurred_at` `2027-01-19T15:08:00Z`. The transcript stored on that row is "Northline visit booked at Cedar Ridge."

I copied both transcripts. They are different sentences on two appends that reuse one idempotency key. The channel log kept both. I did not delete the first dispatch. A `QueueDepth` row, command `cmd-r3e-queue-depth`, at `2027-01-19T15:20:00Z`, records visible backlog 120, oldest age 5400 seconds, and consumer alive true.

A `DeskNote` on stream `r3e-desk`, command `cmd-r3e-desk-note`, at `2027-01-19T15:26:00Z`, stores this sentence: "The morning board was printed from cascade-copy." I copied the sentence because it was the note on the row. The note names a print source. The cursor figures I wrote above are the `seq_caught` values 14 and 10. The export currencies I wrote above are `USD` and `CAD` on amount 90. The note is an additional channel append. I am including it so the channel reading is complete for this referral on this day.

## What I am leaving in the book

A new hire who opens this referral should be able to find, on the hospital log, cedar-copy at 14 and cascade-copy at 10, and amount 90 in `USD` on cedar-copy and amount 90 in `CAD` on cascade-copy, with the file id `cedar-r3e-2027-01-18` on those payloads. They should be able to find the two handset transcripts and the desk-note sentence on the channel log. They should read each log on its own `seq`.

The local reader can return matching rows for `R3E-SYNC` through `GET /ref/R3E-SYNC` when the extracts contain them. The reader is a view over JSON files. It is not a writer, and it is not a shared clock. If the extract and the log differ for a field, write down which one you opened. I opened the log for the numbers in this note.

I will keep both cursor numbers in the IT book as 14 and 10, and both currencies on amount 90 as `USD` and `CAD`, attached to the copy names on the rows. Anyone who wants a single figure can read this page and still has both. I am the person who keeps the logs. The rows stay append-only whether or not a board later prints one of the sentences I copied.
