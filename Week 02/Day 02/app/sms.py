"""Send one SMS. A rejected receipt does not count as sent."""

from __future__ import annotations


def send(booking_id: str, faults: dict) -> dict:
    if faults.get(str(booking_id)) == "reject":
        return {"ok": False, "body": ""}
    return {"ok": True, "body": f"Your booking {booking_id} has a new time."}
