"""bi. The wait clock starts at booking_date. People are counted as rows.

fault() returns that warehouse defect. The affected keys name the booking-date column and the row count. The clean columns are the person id and the wait figure.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the bi fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "bi",
        "booking-date-clock",
        ["column:booking_date", "count:rows"],
        ["person_id", "wait_days"],
    )
