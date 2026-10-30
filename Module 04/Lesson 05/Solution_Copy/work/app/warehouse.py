"""The referral clock is the referred date.

The warehouse feed has two dates on one row. booking_date is when
the slot was booked. referred_at is when the referral was written.
The clock for this connection is the referral. The booking column
is later, and it is not returned.
"""


def clock(row: dict) -> str:
    """Return the referred date. Leave the booking column unread.

    A missing referred date is an empty string.
    """
    # booking_date is on the row and is intentionally not this clock.
    return str(row.get("referred_at") or "")
