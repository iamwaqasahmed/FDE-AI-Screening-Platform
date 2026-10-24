"""SMS send. A rejected receipt is not a sent message."""

from __future__ import annotations


def send(booking_id: str, faults: dict) -> dict:
    if faults.get(booking_id) == "reject":
        return {"ok": False}
    return {"ok": True}
