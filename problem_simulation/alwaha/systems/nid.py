"""nid. Check-digit failures, a visitor-to-Iqama lag, and a late death flag.

fault() returns that identity-lag defect. The affected keys are the failed check digit, the visitor whose id lagged, and the late death flag. The clean columns are the person and the national id.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the national-id fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "nid",
        "identity-lag",
        ["nid:p-000009", "visitor:p-000003", "death:p-000010"],
        ["person_id", "national_id"],
    )
