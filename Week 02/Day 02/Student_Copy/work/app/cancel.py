"""Apply every delivery, including a repeat. A failed send leaves the hold.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

Each call books again, even when the same event id was already
stored. A failed SMS still leaves the hold open. A delivery with
no slot is booked the same way. The journey check names those
three misses while this shell is the file that runs.
"""

from __future__ import annotations

import sms


def _prepare(db) -> None:
    """Create the deliveries table when this database does not have it.

    One row per event id. The columns are the counts and the state
    the check reads: bookings, sms, state, and hold. insert or
    replace in apply overwrites that row on a repeat.
    """
    db.execute(
        "create table if not exists deliveries ("
        "event_id text primary key, bookings integer not null, sms integer not null, "
        "state text not null, hold text not null)"
    )
    db.commit()


def apply(db, event: dict, faults: dict) -> dict:
    """Book this delivery, then add to the counts if it was seen before.

    The previous row is read only so its counts can grow. The event
    id is not a reason to stop. sms.send decides whether the text
    counts. The hold is always stored as open, including when the
    receipt was rejected and including when the event has no slot.
    The state is always notified.
    """
    _prepare(db)
    event_id = str(event["event_id"])
    row = db.execute(
        "select bookings, sms from deliveries where event_id = ?",
        (event_id,),
    ).fetchone()
    bookings = 0 if row is None else int(row[0])
    texts = 0 if row is None else int(row[1])
    sent = sms.send(str(event["booking_id"]), faults)
    bookings += 1
    if sent["ok"]:
        texts += 1
    db.execute(
        "insert or replace into deliveries (event_id, bookings, sms, state, hold) values (?, ?, ?, ?, ?)",
        (event_id, bookings, texts, "notified", "open"),
    )
    db.commit()
    return {
        "event_id": event_id,
        "state": "notified",
        "bookings": bookings,
        "sms": texts,
        "hold": "open",
        "body": sent["body"],
    }
