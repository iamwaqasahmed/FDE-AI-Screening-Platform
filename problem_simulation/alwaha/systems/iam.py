"""iam. Leavers and a role change keep access. svc-integration is a directory admin.

fault() returns that stale-access defect. The affected keys are the leaver, the role change, and the integration service. The clean columns are the staff id, the role, and whether the account is closed.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the identity fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "iam",
        "stale-staff-access",
        ["staff:leaver", "staff:role-change", "svc-integration"],
        ["staff_id", "role", "closed"],
    )
