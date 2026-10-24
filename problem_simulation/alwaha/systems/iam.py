"""iam. Leavers and a role change keep access. svc-integration is a directory admin."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "iam",
        "stale-staff-access",
        ["staff:leaver", "staff:role-change", "svc-integration"],
        ["staff_id", "role", "closed"],
    )
