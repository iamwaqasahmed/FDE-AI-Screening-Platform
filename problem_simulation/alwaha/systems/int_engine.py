"""int-engine. One mapping drops the sub-specialty. Debug logs include PHI since CHG-2025-118.

fault() returns that mapping defect. The affected keys are the dropped sub-specialty and the change that left PHI in the debug logs. The clean columns are the message, the specialty, and the sub-specialty.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the integration-engine fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "int-engine",
        "dropped-subspecialty",
        ["map:subspecialty", "change:CHG-2025-118"],
        ["message_id", "specialty", "sub_specialty"],
    )
