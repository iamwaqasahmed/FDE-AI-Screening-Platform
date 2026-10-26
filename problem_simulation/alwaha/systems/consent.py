"""consent. An expired caregiver grant is still served from the cache.

fault() returns that stale-grant defect. The affected key is the expired caregiver grant. The clean columns are the patient, the actor, the scope, and the expiry.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the consent fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "consent",
        "stale-grant-cache",
        ["grant:caregiver-expired"],
        ["patient_id", "actor", "scope", "expires"],
    )
