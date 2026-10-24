"""phc-templates. The pack still emits criteria v3 fields after the v4 draft exists."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "phc-templates",
        "criteria-v3-after-draft",
        ["template:crit-v3"],
        ["criteria_version"],
    )
