"""Apply session.cancelled once. A failed SMS releases the hold."""

from __future__ import annotations

import sms


def _prepare(db) -> None:
    db.execute(
        "create table if not exists deliveries ("
        "event_id text primary key, bookings integer not null, sms integer not null, "
        "state text not null, hold text not null)"
    )
    db.commit()


def _store(db, event_id: str, stored: dict) -> dict:
    db.execute(
        "insert into deliveries (event_id, bookings, sms, state, hold) values (?, ?, ?, ?, ?)",
        (event_id, stored["bookings"], stored["sms"], stored["state"], stored["hold"]),
    )
    db.commit()
    return {"event_id": event_id, **stored}


def apply(db, event: dict, faults: dict) -> dict:
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
