"""nid. Check-digit failures, a visitor-to-Iqama lag, and a late death flag."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "nid",
        "identity-lag",
        ["nid:p-000009", "visitor:p-000003", "death:p-000010"],
        ["person_id", "national_id"],
    )
