---
id: RUN-LOGS
title: How a new hire reads the three logs
date: 2026-11-01
type: runbook
author: Bobbi Tran
systems:
  - hospital
  - channel
  - payer
  - local-read-api
access: student
---

# RUN-LOGS

I am Bobbi Tran. I keep the three logs for Northline Access Collaborative. This note is for a new hire in IT on the Vancouver desk, written 1 November 2026. It is about how to read `var/log.sqlite`. Read it beside Harper Singh's page, Hospital, channel, and payer logs, dated 1 October 2026. Harper described the file before leaving the integration seat. I am describing the same file as you will open it on the desk machine.

The desk is in Vancouver, British Columbia. The office week is Monday through Friday. The desk clock on the wall is America/Vancouver. Cascade Seattle and Cedar Ridge use America/Los_Angeles. Fraser Burnaby uses America/Vancouver. Harbor Coverage is the payer and records its own time on its own rows. Those clocks belong to the people and the sites. They are not a second database.

## The file

The live record is one SQLite file, `var/log.sqlite`, on this machine. There is no shared clock. No account is open, and this file was not deployed to a remote account. When someone asks where the logs live, the answer is that path on the desk machine. When someone asks for a console in another account, there is no console, because the account is not open.

`append_all` writes history inside a single transaction. Each command in that history still lands on the one table its authority names. The transaction makes the batch durable together. It does not merge the authorities into one table, and it does not stamp one instant onto every row in the batch.

## Three tables

The file has three log tables. Their names are `log_hospital`, `log_channel`, and `log_payer`. A command names its authority, and the authority is one of hospital, channel, or payer. The writer accepts only those three names. A command that names any other authority is rejected before a row is stored. Hospital work from Cascade Seattle, Cedar Ridge, and Fraser Burnaby is appended on `log_hospital`. Channel work from the Vancouver desk is appended on `log_channel`. Harbor Coverage is appended on `log_payer`.

There is no foreign key from a hospital row to a channel row, or from a payer row to either of the others. A referral code can be copied into more than one payload because each organization typed the same characters. That repetition is text. The database does not declare it as a key, and it does not check that the other log contains a matching row. When you see the same referral on two tables, you are seeing two appends that happen to carry the same text. You are not seeing a join the schema enforces.

## What a row holds

Each log row holds `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. `seq` is the primary key of that table. It counts inserts on that table alone. `event_id` is unique on that table. The pair `stream_id` and `stream_rev` is unique inside the same table. The payload is stored as text. The same `stream_id` characters can appear on two logs. Each log has its own `stream_rev` sequence. Revision 2 on the hospital log is the second hospital append for that stream. It says nothing about how many channel rows use the same characters.

`occurred_at` is the time that authority wrote on the event. The hospital log keeps hospital time. The channel log keeps channel time. The payer log keeps payer time. Those strings are not converted onto one another when they are appended. The log stores the string the command brought. It does not keep a second column that lines the three logs up. A row can carry a full instant, and another row can carry a calendar date, because that is what the command brought. You read the string that is stored.

A command that tries to install one shared clock is rejected. The writer refuses a payload that carries a shared instant for every authority, and it refuses a command whose type exists only to set that shared instant. Each stored event keeps the time that arrived with it. If a new hire tries to "put the day on one clock" by writing a shared instant back into the file, the writer rejects that command. The three tables stay three tables.

## Append only

The tables are append-only. Update is rejected. Delete is rejected. Triggers on each log table abort both. The abort tells you that log rows are append-only. A correction is a later append with a new `stream_rev` on that stream. The earlier row stays in the table, with the payload it had when it was inserted. Replaying a `command_id` that the inbox has already accepted returns the original `event_id` and does not write a second row. You do not delete the first row to make the replay fit. The replay is the same event.

I want that sentence to be the one you remember on a bad afternoon. Delete is rejected. If a clerk asks you to remove a row because the story on the screen feels messy, you refuse the delete. You can append another event if an authority sends a later command. You cannot reach into `log_hospital`, `log_channel`, or `log_payer` and erase the earlier one. I have watched people open a SQLite browser and hover over a delete button. The button is not the log. The trigger is the log.

## Sequence and the order of the day

Sequence is append order on one table, not a shared timeline. The next hospital append receives the next hospital `seq`, whatever `occurred_at` says. A row with a higher `seq` on that table can carry an earlier authority time than the row above it, because the authority wrote that time and the log appended when the command arrived. Reading `seq` on hospital, then `seq` on channel, then `seq` on payer, as if the three numbers were one counter, misreads the file. The number 40 on the hospital table and the number 40 on the payer table are two counters that happen to display the same digits.

Do not sort the three logs together and call that the order of the day. I will say it the way I say it at the desk. Take the hospital rows, the channel rows, and the payer rows, sort them by `occurred_at` or by `seq` into one list, and you have built an order the store does not keep. That sorted list is a spreadsheet you made. It is not the day. The order of appends on `log_hospital` is the hospital order. The order of appends on `log_channel` is the channel order. The order of appends on `log_payer` is the payer order. Cedar Ridge files at night, including weekends, and the Vancouver office week is still Monday through Friday. A weekend file does not become an office-day row because you sorted it next to a Friday channel event. Each log's sequence is the order of its own appends.

When you explain a referral to Morgan Ibarra or to Dana Okonkwo, bring the three readings separately. Say which table you opened. Say the `seq` you saw on that table. Say the `occurred_at` string on that row. Then open the next table and do it again. If they ask you for one timeline, repeat the instruction: do not sort the three logs together and call that the order of the day.

## Projections

`project` reads one log at a time. It writes three stores, and each store is built from one log only: `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. Each store is a single table of JSON documents. The projector replaces the file it is writing. It does not join the other logs while it writes. Opening a projection is not opening a merged day. The hospital store is hospital documents. The channel store is channel documents. The payer store is payer documents.

From the hospital log, a slot filing becomes a mart document and a nightly-file document. The mart document keeps a wait figure beside the booking date taken from that payload. The projector writes that wait figure as 0. Trailer fields are copied onto the nightly-file document only when the hospital sent them. A cache event becomes an eligibility-cache document. A payer timeout is stored with a null window. The effective-from and effective-to fields are null on that row. The answer remains the timeout the payer recorded. Those are properties of the projection. They are not a sort of the three logs.

## Local read

The desk reads extracts through a local HTTP process. `python -m access serve` binds `127.0.0.1` and port 8088 unless another port is given. It reads every JSON file under `student_pack/extracts`. It does not append to the logs, and it does not open the projection files to answer a request.

`GET /` and `GET /health` return a small JSON object whose status field is up. `GET /extracts` returns the whole bundle. The keys are the file names without the `.json` suffix. `GET /extracts/<name>` returns that one file. An unknown name is a 404. `GET /ref/<ref>` returns the rows whose ref matches, as an object with the ref and a list of hits. Each hit names the extract and the row. Responses use `Content-Type: application/json`. Any other path is a 404.

The extracts a new hire opens are the JSON the reader serves. The logs remain the append-only record. The projections are the per-log documents described above. The reader is a view over the extract files. When the extract, the projection, and the log disagree in a way that matters to a person on the phone, the disagreement is in the bytes you can open. This page records how those bytes are stored. It does not tell a board which of the three authority times it is allowed to print. I keep the logs. Dana's office keeps the boards. I will show you the row. I will not sort the three logs into their slide.

## A first afternoon

On your first afternoon, find the file. List the table names and confirm you see `log_hospital`, `log_channel`, and `log_payer`. Read a handful of rows from one table, ordered by `seq` on that table. Read `occurred_at` as text. Read the payload as text. Then close that result and open the next table. Write down three short notes, one per table. If your notes have become one sorted column, start again.

Try nothing destructive. An update will be rejected. A delete will be rejected. A shared-clock command will be rejected. A replay of a command id you already have returns the original event id. If you need a fresh generated tree, `python -m access init` and `python -m access reset` rebuild local state on this machine from the history the program carries. They are local commands. They do not open an account.

That is the reading. Three tables. Append only. Delete is rejected. No shared clock. The local HTTP process serves extracts. And once more, because this is the mistake I most want you to avoid: do not sort the three logs together and call that the order of the day.
