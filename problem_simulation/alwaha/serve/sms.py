"""SMS send. A rejected receipt is not a sent message.

send() returns ok false when the fault table marks that booking as reject. Every other booking returns ok true.
"""

from __future__ import annotations


def send(booking_id: str, faults: dict) -> dict:
    """Return ok false for a rejected booking, and ok true otherwise.

    The reject fault means the carrier refused the message, so this call is not a sent message.
    """
    # A reject fault is a carrier refusal, not a delivered message.
    if faults.get(booking_id) == "reject":
        return {"ok": False}
    return {"ok": True}
