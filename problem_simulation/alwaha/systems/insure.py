"""insure. The eligibility snapshot can be 48 hours old. rel-w4d4 is a gateway outage."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "insure",
        "stale-snapshot",
        ["eligibility:48h", "outage:rel-w4d4"],
        ["person_id", "class", "as_of"],
    )
