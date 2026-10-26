"""sms. Receipts arrive late and duplicated. Foreign numbers fail quietly.

fault() returns that receipt defect. The affected keys are the duplicate receipt and the foreign number. The clean columns are the booking id and the status.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the SMS fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "sms",
        "receipt-late-duplicate",
        ["receipt:duplicate", "number:foreign"],
        ["booking_id", "status"],
    )
