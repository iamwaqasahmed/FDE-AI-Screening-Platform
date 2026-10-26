"""eref. The patient API hides pending. Return reasons cite the template version.

fault() returns that hidden-pending defect. The affected key is the pending status. The clean columns are the status and the template version.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the referral fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "eref",
        "pending-hidden",
        ["status:pending"],
        ["status", "template_version"],
    )
