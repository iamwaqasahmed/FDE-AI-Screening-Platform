---
id: WIKI-ERRORS
title: Delete, shared clock, and command replay
date: 2026-11-12
type: wiki
author: Bobbi Tran
systems:
  - hospital
  - channel
  - payer
access: student
---

# Delete, shared clock, and command replay

I am Bobbi Tran. I keep the logs on the desk machine in Vancouver. This page records what the writer does when a statement tries to delete a log row, when a command tries to install a shared clock, and when a command id is sent again. The date on the page is 12 November 2026. The writer is local Python in the `access` package. It uses the standard-library `sqlite3` module. The file is `var/log.sqlite` under `enterprise_simulation`. The process does not open a remote account. A row lives in that file on this machine.

The file holds `inbox_done` and three log tables. `inbox_done` has `command_id` as its primary key and `event_id` as a second column. The log tables are `log_hospital`, `log_channel`, and `log_payer`. A command's `authority` must be `hospital`, `channel`, or `payer`. That string selects the table. It is not stored as its own column. Each log table has the columns `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. `seq` is the integer primary key. `event_id` is unique. The pair `stream_id` and `stream_rev` is unique inside one table. There is no foreign key from one log table to another. `PRAGMA foreign_keys = ON` is set on the connection, and the schema contains no `REFERENCES` clause, so the pragma does not link the tables.

`append` takes one command. `append_all` takes a list. Both start with `BEGIN IMMEDIATE`. `append_all` runs every command in the list inside that transaction and then commits. When any step raises, the writer rolls the transaction back and raises again. A command id inserted only inside the failed batch is not left in `inbox_done`. A command id committed by an earlier call remains.

## Delete a log row

Each log table is created with two triggers. The names are `{table}_no_update` and `{table}_no_delete`. On the hospital table the delete trigger is `log_hospital_no_delete`. On the channel table it is `log_channel_no_delete`. On the payer table it is `log_payer_no_delete`.

The delete trigger is `BEFORE DELETE`. Its body is `SELECT RAISE(ABORT, 'log rows are append-only')`. A `DELETE` aimed at `log_hospital`, `log_channel`, or `log_payer` reaches that trigger before the row is removed. SQLite aborts the statement. The database reports the text `log rows are append-only`. The row stays in the table. Its `seq` stays. Its `event_id` stays. Its `type`, `occurred_at`, `stream_id`, `stream_rev`, and payload text stay. The delete does not compact `seq`. The delete does not free the `event_id`. A later insert on that table receives a new rowid. The aborted delete does not make the old rowid available by removing the row, because the row is still there.

A delete that names one `seq`, a delete that names one `event_id`, and a delete that names a `stream_id` all hit the same trigger when they target one of the three log tables. The trigger is on the table, not on a column. Opening the file in a SQLite browser and issuing `DELETE FROM log_hospital` aborts the same way. Issuing `DELETE FROM log_channel WHERE stream_id = 'REF-4417'` aborts the same way. Issuing `DELETE FROM log_payer WHERE event_id = ?` aborts the same way. After the abort, `read_log` for that authority still returns the row, ordered by `seq` with the other rows of that table.

The update trigger is `BEFORE UPDATE` and raises the same text, `log rows are append-only`. An `UPDATE` that tries to change `type`, `occurred_at`, `payload`, `stream_rev`, or any other column on the three log tables aborts. The row remains the inserted row. I am recording that here because the trigger is created in the same statement block as the delete trigger. The delete path and the update path both stop inside SQLite before the row changes.

`inbox_done` does not have `no_update` or `no_delete`. The append-only triggers are the pairs on `log_hospital`, `log_channel`, and `log_payer`. The write path in `append` and `append_all` does not issue a delete against `inbox_done`. A replay reads `inbox_done` and returns the stored `event_id`. It does not remove the inbox row.

The projector's replacement of `var/proj/hospital.sqlite`, `channel.sqlite`, and `payer.sqlite` unlinks those projection files and creates new databases. That unlink is not a `DELETE` against `log_hospital`, `log_channel`, or `log_payer`. The log triggers do not run during a projection write. When the projection run finishes, the log rows are the rows that were read. `python -m access init` and `python -m access reset` remove the generated `var` directory on this machine and write it again from the history the program carries. That is a directory replacement followed by new inserts. It is not a `DELETE` statement against a live log table, and it does not pass through `log_hospital_no_delete`.

The local HTTP process defines `GET`. It does not define a delete method, and it does not open `var/log.sqlite`. An HTTP request to `127.0.0.1` does not remove a log row. The behavior in this section is the SQL trigger on the three log tables.

## A shared-clock command

`_insert` handles one command inside the caller's transaction. It reads `command_id` first. When `inbox_done` already has that `command_id`, it returns the stored `event_id` and does not look at the rest of the command. When the command id is new, it reads `authority`. An authority other than `hospital`, `channel`, or `payer` raises `ValueError` with the text `unknown authority`. No log row is inserted. No inbox row is inserted. `append` or `append_all` rolls the transaction back and raises that error again.

When the authority is one of the three names, the function reads `payload`. The shared-clock check is next. The command is rejected when the payload contains the key `canonical_at`. The command is rejected when `type` is the string `SetCanonicalTime`. Either condition is enough. The exception is `ValueError` with the text `a shared clock is not a command`. The check is the presence of the key `canonical_at`. It is an exact match on the type string `SetCanonicalTime`. A payload that has the key raises even when the value under the key is null, a string, or an object. A type string that is not exactly `SetCanonicalTime` does not trip the type half of the check. A type `SetCanonicalTime` raises even when the payload has no `canonical_at` key.

The raise happens before `event_id` is computed and before the `INSERT` into the log table and before the `INSERT` into `inbox_done`. The rejected command adds no row. Because `append` and `append_all` wrap the work in `BEGIN IMMEDIATE`, the exception rolls that transaction back. In `append_all`, a shared-clock command in the middle of the list rolls back the earlier commands of that same batch as well. Those earlier commands were not committed. Their command ids are absent from `inbox_done` after the rollback. Command ids committed by a previous call stay in `inbox_done`, and their log rows stay.

A stored event keeps the `occurred_at` text the command brought. The writer does not parse that text as a civil time, does not attach a zone, and does not replace it with a reading of its own. The hash that becomes `event_id` includes `authority`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. It does not include a shared instant, because a command carrying `canonical_at` or typed `SetCanonicalTime` never reaches the hash. `seq` is not an input to the hash. `command_id` is not an input to the hash. The package that computes the hash takes no wall-clock reading and no random bytes.

The desk clock on the wall is America/Vancouver. Cascade Seattle and Cedar Ridge keep America/Los_Angeles. Fraser Burnaby keeps America/Vancouver. Harbor Coverage writes its own time on its own commands. Those strings can appear in `occurred_at` when an organization put them on a command. They are the text of that command. They are not a `canonical_at` key, and they are not a `SetCanonicalTime` command. Sending the key, or sending that type, is the case this section describes: the writer raises, the transaction rolls back, and the three log tables are unchanged by that command.

## Replay a command id

On a command whose `command_id` is already in `inbox_done`, `_insert` selects `event_id` and returns that string. It does not insert a second log row. It does not insert a second inbox row. It does not compute a new hash. The caller of `append` receives the original `event_id`. The caller of `append_all` receives that same `event_id` in the list of ids, in the position of the replayed command.

The select sees rows inserted earlier in the same open transaction. If `append_all` is given the same `command_id` twice in one list, the first copy inserts the log row and the inbox row, and the second copy finds the inbox row and returns the `event_id` without a second insert. The commit then keeps one log row and one inbox row. If the `command_id` was committed by an earlier call, a later `append` of that same id returns the original `event_id` and writes nothing. The existing log row stays as it was inserted, including its `seq`.

The replay return happens before the authority check and before the shared-clock check. The function returns the stored `event_id` from the inbox row it found. It does not compare the new command's payload with the stored payload before returning.

A different `command_id` is not a replay. The function builds an identity object with `authority`, `type`, `occurred_at`, `stream_id`, `stream_rev` coerced with `int`, and `payload`. It encodes that object as UTF-8 JSON with sorted keys and with a comma and a colon as the only separators, then hashes the bytes with SHA-256. The hex digest is `event_id`. The insert writes `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `json.dumps` of the payload with sorted keys. It omits `seq`, so SQLite assigns the rowid. Then it inserts `command_id` and `event_id` into `inbox_done`.

When that new `command_id` hashes to an `event_id` that is already unique on the table, the insert fails the unique constraint on `event_id`. When the new command repeats a `(stream_id, stream_rev)` pair already stored on the same table, the insert fails the unique constraint on that pair. Both failures raise. `append` or `append_all` rolls the transaction back. The failed command leaves no log row and no inbox row from that attempt. A unique failure is a different outcome from a replay. A replay of a known `command_id` returns the original `event_id` and commits cleanly when the rest of the batch also succeeds. A new `command_id` that collides on `event_id` or on `(stream_id, stream_rev)` rolls back.

`read_log` after a successful replay shows the original row once. The `seq` values on that table are the insert order of the rows that were actually inserted. The replay does not add a row, so it does not advance `seq`. The payload text of the original row remains the JSON stored at insert time. A person who sends `cmd-request-4417` again receives the `event_id` stored for that command id. `log_channel` still has one row for that command. The channel projection, the next time it is built, still has one event document from that row, because the projector reads the log and the log has one row.

The three cases on this page are the three outcomes of the code that is running. A delete of a row in `log_hospital`, `log_channel`, or `log_payer` aborts with `log rows are append-only` and leaves the row in place. A new command whose payload contains `canonical_at`, or whose type is `SetCanonicalTime`, raises `a shared clock is not a command` and inserts nothing. A repeated `command_id` returns the original `event_id` and does not write a second row.
