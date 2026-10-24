"""sms. Receipts arrive late and duplicated. Foreign numbers fail quietly."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "sms",
        "receipt-late-duplicate",
        ["receipt:duplicate", "number:foreign"],
        ["booking_id", "status"],
    )
