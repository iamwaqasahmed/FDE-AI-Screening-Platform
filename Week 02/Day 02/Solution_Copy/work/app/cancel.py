"""Apply session.cancelled once. A failed SMS releases the hold.

Chapter 06 replaces work/app/cancel.py with this file.
The packet copy stays the shell that books every delivery.

A repeated event id returns the stored row and does not book
again. A rejected receipt stores compensated, releases the hold,
and books nothing. A delivery with no slot stores escalated,
sends no SMS, and books nothing.
"""

from __future__ import annotations

import sms


def _prepare(db) -> None:
    """Create the deliveries table when this database does not have it.

    One row per event id. insert below refuses a second row for
    the same id, which is how a replay keeps the first counts.
    """
    db.execute(
        "create table if not exists deliveries ("
        "event_id text primary key, bookings integer not null, sms integer not null, "
        "state text not null, hold text not null)"
    )
    db.commit()


def _store(db, event_id: str, stored: dict) -> dict:
    """Insert one delivery row and return it with the event id.

    stored already has the state, the counts, the hold, and the
    body. This function does not add a booking of its own.
    """
    db.execute(
        "insert into deliveries (event_id, bookings, sms, state, hold) values (?, ?, ?, ?, ?)",
        (event_id, stored["bookings"], stored["sms"], stored["state"], stored["hold"]),
    )
    db.commit()
    return {"event_id": event_id, **stored}


def apply(db, event: dict, faults: dict) -> dict:
    """Apply one cancellation, or return the row already stored for this id.

    A second call with the same event id returns the stored counts
    and an empty body. It does not call sms.send again.

    When slot is false, the row is escalated: no booking, no SMS,
    and no hold.

    Otherwise sms.send uses the booking id and the fault file.
    An accepted receipt stores notified, one booking, and one SMS.
    A rejected receipt stores compensated, zero bookings, zero
    SMS, and a released hold.
    """
    _prepare(db)
    event_id = str(event["event_id"])
    existing = db.execute(
        "select bookings, sms, state, hold from deliveries where event_id = ?",
        (event_id,),
    ).fetchone()
    if existing is not None:
        return {
            "event_id": event_id,
            "bookings": int(existing[0]),
            "sms": int(existing[1]),
            "state": existing[2],
            "hold": existing[3],
            "body": "",
        }
    if not event.get("slot", True):
        return _store(db, event_id, {"state": "escalated", "bookings": 0, "sms": 0, "hold": "none", "body": ""})
    sent = sms.send(str(event["booking_id"]), faults)
    if sent["ok"]:
        stored = {"state": "notified", "bookings": 1, "sms": 1, "hold": "none", "body": sent["body"]}
    else:
        stored = {"state": "compensated", "bookings": 0, "sms": 0, "hold": "released", "body": sent["body"]}
    return _store(db, event_id, stored)
