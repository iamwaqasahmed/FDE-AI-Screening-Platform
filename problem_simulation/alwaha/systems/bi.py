"""bi. The wait clock starts at booking_date. People are counted as rows."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "bi",
        "booking-date-clock",
        ["column:booking_date", "count:rows"],
        ["person_id", "wait_days"],
    )
