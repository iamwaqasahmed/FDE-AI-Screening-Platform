"""phc-templates. The pack still emits criteria v3 fields after the v4 draft exists.

fault() returns that leftover-criteria defect. The affected key is the old criteria template. The clean column is the criteria version.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the template-pack fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "phc-templates",
        "criteria-v3-after-draft",
        ["template:crit-v3"],
        ["criteria_version"],
    )
