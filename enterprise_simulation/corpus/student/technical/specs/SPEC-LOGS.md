---
id: SPEC-LOGS
title: Append-only log tables
date: 2026-10-15
type: specification
author: Bobbi Tran
systems:
  - hospital
  - channel
  - payer
access: student
---

# Append-only log tables

I am Bobbi Tran. I keep the logs for Northline Access Collaborative. This specification is the contract of the writer that is running on the desk machine in Vancouver. The date on the file is 15 October 2026. The writer is local Python in the `access` package. It uses the standard-library `sqlite3` module. The durable file is `var/log.sqlite` under the `enterprise_simulation` directory. Nothing in this specification opens a remote account, and the file is not deployed to one. When someone asks where a row lives, the answer is that SQLite file on this machine.

The desk clock on the wall is America/Vancouver. Cascade Seattle and Cedar Ridge keep America/Los_Angeles. Fraser Burnaby keeps America/Vancouver. Harbor Coverage writes its own time on its own commands. Those names are the times people already put on a command. The database does not keep a second clock that converts them.

## The file and the tables

`init_db` creates the file when the path is absent. The parent directory is created with the file. A second call, when the path already exists, returns immediately and leaves the bytes unchanged. The connection sets `PRAGMA foreign_keys = ON`. The schema that follows does not contain a `REFERENCES` clause, so that pragma does not link one log to another.

The file holds four tables. `inbox_done` records a command the writer has already accepted. Its columns are `command_id TEXT PRIMARY KEY` and `event_id TEXT NOT NULL`. The other three tables are the logs. Their names are fixed:

| Authority on the command | Table |
| --- | --- |
| `hospital` | `log_hospital` |
| `channel` | `log_channel` |
| `payer` | `log_payer` |

Hospital work from Cascade Seattle, Cedar Ridge, and Fraser Burnaby is appended to `log_hospital`. Cedar Ridge has no slot API. A nightly file from that clinic is still a hospital command, stored on `log_hospital`. Channel work from the Vancouver desk is appended to `log_channel`. Harbor Coverage is appended to `log_payer`. A command whose authority is any other string is rejected with `unknown authority` before a log row is inserted.

Each log table uses the same column list:

| Column | Declared type | Constraint |
| --- | --- | --- |
| `seq` | `INTEGER PRIMARY KEY` | row identity of that table |
| `event_id` | `TEXT NOT NULL` | `UNIQUE` |
| `type` | `TEXT NOT NULL` | |
| `occurred_at` | `TEXT NOT NULL` | |
| `stream_id` | `TEXT NOT NULL` | |
| `stream_rev` | `INTEGER NOT NULL` | unique together with `stream_id` |
| `payload` | `TEXT NOT NULL` | JSON text |

The pair `(stream_id, stream_rev)` is unique inside one table. The same `stream_id` characters may appear on another log. Revision 2 on `log_hospital` is the second stored revision of that stream on the hospital table. It does not count channel rows that happen to use the same characters. There is no foreign key from a hospital row to a channel row, or from a payer row to either of the others. A referral string copied into more than one payload is text that each organization typed. The schema does not check that another log contains a matching row.

## Command fields

A command is one Python dictionary. The writer reads these fields, in this order.

`command_id` is the inbox key. The writer selects `event_id` from `inbox_done` where `command_id` matches. When a row is already there, the writer returns that `event_id` and does not insert again.

`authority` is `hospital`, `channel`, or `payer`. It chooses the table. It is not stored as its own column. It is an input to the event hash, described below.

`payload` is a JSON object. The writer rejects the command when the payload contains the key `canonical_at`. It also rejects the command when `type` is the string `SetCanonicalTime`. The exception text is `a shared clock is not a command`. The check is the presence of the key, and it is an exact match on the type string. A shared instant for every authority is not a command this writer accepts. Each stored event keeps the `occurred_at` string that arrived on that command.

`type` is stored in the `type` column. `occurred_at` is stored in the `occurred_at` column as text. The writer does not parse it as a civil time, does not attach a zone, and does not replace it with a clock reading of its own. `stream_id` is stored as text. `stream_rev` is stored as an integer. The writer applies `int` to the value on the command before the insert and before the hash.

The payload column is `json.dumps` of the payload object with object keys sorted. That text is what a later read parses back into an object. Event types the logs already carry include `RequestAccepted`, `HandsetDispatch`, `DeskSession`, `CoverageDecided`, `CacheStored`, `SlotFiled`, `LetterStored`, and `DocumentChanged`. The writer does not keep a private list of allowed type strings. Any other type is appended when the authority, the clock check, and the unique keys allow it.

## One transaction

`append` takes one command. `append_all` takes a list. Both start with `BEGIN IMMEDIATE`. `append_all` inserts every command in the list inside that single transaction, then commits. Each command still lands on the one table its own authority names. The transaction makes the batch durable together. It does not merge the three tables, and it does not stamp one instant onto every row in the batch. When any insert raises, the writer rolls the transaction back and raises again. A command id that was only inserted inside the failed batch is not left behind in `inbox_done`. A command id that was committed by an earlier call remains.

On a new command the writer builds an identity object with `authority`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. It encodes that object as UTF-8 JSON with sorted keys and with a comma and a colon as the only separators, then hashes the bytes with SHA-256. The hex digest is `event_id`. `seq` is not an input to the hash. `command_id` is not an input to the hash. The insert names `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. It does not supply `seq`. After the log insert, the writer inserts `command_id` and `event_id` into `inbox_done`.

A replay of a `command_id` already in the inbox returns the original `event_id` and writes no second log row. A different `command_id` whose identity object hashes to an `event_id` that is already unique on the table fails the unique constraint on `event_id`. A repeated `(stream_id, stream_rev)` on the same table fails that unique constraint. Both failures roll back the transaction that contains them.

## What delete does

Each log table has two triggers, created with the table. Their names are `{table}_no_update` and `{table}_no_delete`, so the hospital triggers are `log_hospital_no_update` and `log_hospital_no_delete`, and the channel and payer tables have the same pair under their own table names.

The update trigger is `BEFORE UPDATE`. Its body is `SELECT RAISE(ABORT, 'log rows are append-only')`. An `UPDATE` against `log_hospital`, `log_channel`, or `log_payer` aborts. The statement does not change `type`, `occurred_at`, `payload`, or any other column. The row remains as it was inserted.

The delete trigger is `BEFORE DELETE`. Its body is the same `RAISE(ABORT, 'log rows are append-only')`. A `DELETE` that would remove a row from one of the three log tables aborts. The database reports that message. The row stays in the table, with the same `seq`, the same `event_id`, and the same payload text. Delete does not compact `seq`, and it does not free the `event_id`. A person who opens the file in a SQLite browser and issues a delete against a log table gets the abort. The supported way to record a later fact is a new command with a new `stream_rev` on that stream. The earlier row stays.

`inbox_done` does not have these triggers. The append-only rule in this specification is the pair of triggers on `log_hospital`, `log_channel`, and `log_payer`. The write path does not delete inbox rows. Replaying a command id reads the inbox and returns the stored event id.

## Why seq is not a clock

`seq` is the integer primary key of one log table. In SQLite that column is the rowid of that table. The insert omits it, so SQLite assigns it when the row is inserted into that table. The first row in an empty log table receives `seq` 1. The next successful insert on that same table receives the next rowid. `log_hospital`, `log_channel`, and `log_payer` each have their own rowid space. The number 40 on the hospital table and the number 40 on the payer table are two counters. They are not two readings of one clock, and they are not one shared sequence with a gap where the other authority inserted.

`seq` is append order on that table. It is assigned from the insert, not from `occurred_at`. The writer never copies `occurred_at` into `seq`, and it never derives `occurred_at` from `seq`. `occurred_at` remains the text the command brought. A row with a higher `seq` on one table can carry an earlier `occurred_at` string than a row with a lower `seq` on that same table, because the authority wrote the time and the log appended when the command was accepted.

The opening hospital stream `REF-4417` is a concrete case of that split. The cache command is stored with `occurred_at` `2027-01-09T21:00:00Z` and `stream_rev` 1. The slot command is stored with `occurred_at` `2027-01-11T21:00:00Z` and `stream_rev` 2. The letter command is stored with `occurred_at` `2027-01-09T18:02:00Z` and `stream_rev` 3. In the history list the letter is appended after the slot, so its `seq` on `log_hospital` is later than the slot's `seq`, while the letter's `occurred_at` is the earlier of the two strings. Reading `seq` as the time of the letter would contradict the string the hospital put on the letter. The hash of the letter does not contain `seq`, so the identity of the letter is the authority, the type, the `occurred_at` string, the stream, the revision, and the payload.

There is no column that lines the three logs up. Sorting rows from all three tables by `seq` builds a list the store does not keep. Sorting them by `occurred_at` builds a different list the store also does not keep. `read_log` returns one authority, ordered by `seq` on that authority's table. A weekend file from Cedar Ridge and a Friday channel row are on different tables. Their sequence numbers are not a shared timeline, and the office week Monday through Friday is not a column on the log.

The writer also refuses the command that would install one shared instant. A payload key `canonical_at`, or a type `SetCanonicalTime`, raises `a shared clock is not a command` and inserts nothing. The package that computes `event_id` takes no wall-clock reading and no random bytes. Times on the rows are the strings the commands already carried. `seq` cannot be that shared instant, because it is a per-table rowid, it is outside the hash, and a later rowid can store an earlier authority time.

## Reading rows back

`read_log` takes an authority name and selects `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload` from that authority's table, ordered by `seq`. The payload text is parsed as JSON before the row is returned. The function reads one table per call. It does not union the three logs and it does not sort them by `occurred_at`.

`python -m access init` and `python -m access reset` delete the generated `var` directory on this machine and write it again from the history the program carries. They are local commands. They do not open an account. After either command, the three log tables are again the append-only record described here, and `seq` on each table is again the insert order of that rebuild.
