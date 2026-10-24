"""consent. An expired caregiver grant is still served from the cache."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "consent",
        "stale-grant-cache",
        ["grant:caregiver-expired"],
        ["patient_id", "actor", "scope", "expires"],
    )
