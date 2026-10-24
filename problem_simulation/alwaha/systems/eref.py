"""eref. The patient API hides pending. Return reasons cite the template version."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "eref",
        "pending-hidden",
        ["status:pending"],
        ["status", "template_version"],
    )
