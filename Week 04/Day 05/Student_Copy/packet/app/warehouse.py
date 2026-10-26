"""Read the booking date.

This is the starter. It returns booking_date, the day the slot was
booked. That day is later than the day the referral was written.
The finished module returns referred_at instead.
"""


def clock(row: dict) -> str:
    """Return the booking date and ignore the referred date.

    A missing booking date is an empty string.
    """
    # referred_at is the other column. This starter does not return it.
    return str(row.get("booking_date") or "")
