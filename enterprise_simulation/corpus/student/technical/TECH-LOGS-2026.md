---
id: TECH-LOGS-2026
title: Hospital, channel, and payer logs
date: 2026-10-01
type: wiki
author: Harper Singh
systems:
  - hospital
  - channel
  - payer
  - local-read-api
access: student
---

This is the integration note for the logs Northline is running. I am Harper Singh. This is my last edit before I leave the integration seat. The Vancouver desk, Cascade Seattle, Cedar Ridge, Fraser Burnaby, and Harbor Coverage all write through the same machine, and the machine keeps their words apart.

## Three logs

There are three append-only logs. Their names are hospital, channel, and payer. They share one SQLite file, `var/log.sqlite`, and they do not share a table. The tables are `log_hospital`, `log_channel`, and `log_payer`. A command names its authority. The writer accepts only those three names. A command for any other authority is rejected before a row is stored.

`append_all` writes a history inside a single transaction. Each command in that history still lands on the one table its authority names. The transaction makes the batch durable together. The schema has no foreign key from a hospital row to a channel row, or from a payer row to either of the others. A reference string may be copied into more than one payload because each organization typed the same referral code. That repetition is text. The database does not declare it as a key, and it does not check that the other log contains a matching row.

## Append-only rows

Each log row holds `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. `seq` is the primary key of that table. `event_id` is unique. The pair `stream_id` and `stream_rev` is unique inside the same table. The payload is stored as text. Update and delete are blocked by triggers. Both abort. A correction is a later append with a new `stream_rev` on that stream. Replaying a `command_id` that the inbox has already accepted returns the original `event_id` and does not write a second row.

A command that tries to install one shared clock is rejected. The writer refuses a payload that carries a shared instant for every authority, and it refuses a command whose type exists only to set that shared instant. Each stored event keeps the time that arrived with it.

## Authority time

`occurred_at` is the time that authority wrote on the event. The hospital log keeps hospital time. The channel log keeps channel time. The payer log keeps payer time. Those strings are not converted onto one another when they are appended. The desk in Vancouver works in America/Vancouver. Cascade Seattle and Cedar Ridge work in America/Los_Angeles. Harbor Coverage records its own decision time. The log stores the string the command brought. It does not keep a second column that lines the three logs up.

The same `stream_id` text can appear on two logs. Each log has its own `stream_rev` sequence. Revision 2 on the hospital log is the second hospital append for that stream. It says nothing about how many channel rows use the same characters.

## Event names on the logs

These event names exist on the logs. The list is the set I am handing to the next integration engineer. Other type strings are also appended when an authority sends them. The names below are ones a reader will find.

`RequestAccepted` is a channel event. The payload carries the referral, the utterance, whether the handset was delivered, the channel, and the desk region.

`HandsetDispatch` is a channel event. The payload carries the referral, an idempotency key, the attempt number, and a dispatch status.

`DeskSession` is a channel event. The payload carries the session id, the token subject, the factor the desk used, and the desk region.

`CoverageDecided` is a payer event. The payload carries the referral, the answer, the effective window when Harbor sent one, and the currency when Harbor sent one.

`CacheStored` is a hospital event. The payload carries the referral, `eligible`, and `window_present`.

`SlotFiled` is a hospital event. Cedar Ridge has no slot API. The hospital log records the nightly file here. The payload carries the referral, the site, `file_id`, and `booking_date`. When the file included a trailer, the payload also carries `trailer_ok`, `trailer_count`, and `body_count`.

`DocumentChanged` is a hospital event. The payload carries the document id, version, status, audience, and body. Hours sheets also carry a local close and a timezone name on that payload.

## Sequence

Sequence is append order, not a shared timeline. `seq` counts inserts on that one table. The next hospital append receives the next hospital `seq`, whatever `occurred_at` says. A row with a higher `seq` can carry an earlier authority time than the row above it, because the authority wrote that time and the log appended when the command arrived. Reading `seq` across hospital, channel, and payer as if the three numbers were one clock misreads the file. Sorting the three logs by `occurred_at` builds an order the store does not keep. Each log's sequence is the order of its own appends.

## Projections

`project` reads one log at a time. It writes three stores, and each store is built from one log only: `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. Each store is a single table of JSON documents. The projector replaces the file it is writing. It does not join the other logs while it writes.

From the hospital log, a `SlotFiled` event becomes two documents. The mart document keeps `kind`, `ref`, `booking_date`, and `wait_days`. The projector writes `wait_days` as 0 beside the booking date taken from that payload. The nightly-file document keeps `kind`, `ref`, `file_id`, `site`, and the event's `occurred_at`. Trailer fields are copied only when the hospital sent them. A `CacheStored` event becomes an eligibility-cache document with `ref`, `eligible`, `window_present`, and `occurred_at`. Every other hospital event is passed through with its type, referral, authority time, and payload.

The channel projection passes each channel event through in the same shape: type, referral, authority time, and payload. `RequestAccepted`, `HandsetDispatch`, and `DeskSession` stay events. They are not folded into the hospital mart.

The payer projection turns `CoverageDecided` into a coverage document with `ref`, `answer`, `effective_from`, `effective_to`, `currency`, and `occurred_at`. A timeout is stored with a null window. The effective-from and effective-to fields are null on that row. The answer remains the timeout the payer recorded.

## Local read API

The desk reads extracts through a local HTTP process. `python -m access serve` binds `127.0.0.1` and port 8088 unless another port is given. It reads every JSON file under `student_pack/extracts`. It does not append to the logs, and it does not open the projection files to answer a request.

`GET /` and `GET /health` return a small JSON object whose status field is up. `GET /extracts` returns the whole bundle. The keys are the file names without the `.json` suffix. `GET /extracts/<name>` returns that one file. An unknown name is a 404. `GET /ref/<ref>` returns the rows whose ref matches, as an object with the ref and a list of hits. Each hit names the extract and the row. Responses use `Content-Type: application/json`. Any other path is a 404.

The extracts a new hire opens are the JSON the reader serves. The logs remain the append-only record. The projections are the per-log documents described above. The reader is a view over the extract files. When those three disagree in a way that matters to a screen, the disagreement is in the bytes. This page records how the bytes are stored.

I will not be here to revise the page after this week. The rules above are the ones the process is running.
