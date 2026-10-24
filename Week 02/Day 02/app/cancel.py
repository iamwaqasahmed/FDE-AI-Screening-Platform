"""Apply every delivery, including a repeat. A failed send leaves the hold."""

from __future__ import annotations

import sms


def _prepare(db) -> None:
    db.execute(
        "create table if not exists deliveries ("
        "event_id text primary key, bookings integer not null, sms integer not null, "
        "state text not null, hold text not null)"
    )
    db.commit()


def apply(db, event: dict, faults: dict) -> dict:
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
