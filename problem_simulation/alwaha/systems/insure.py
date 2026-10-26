"""insure. The eligibility snapshot can be 48 hours old. rel-w4d4 is a gateway outage.

fault() returns that stale-snapshot defect. The affected keys are the old eligibility snapshot and the outage. The clean columns are the person, the class, and the as-of instant.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the insurance fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "insure",
        "stale-snapshot",
        ["eligibility:48h", "outage:rel-w4d4"],
        ["person_id", "class", "as_of"],
    )
