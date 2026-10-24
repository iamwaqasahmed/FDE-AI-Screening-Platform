"""int-engine. One mapping drops the sub-specialty. Debug logs include PHI since CHG-2025-118."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "int-engine",
        "dropped-subspecialty",
        ["map:subspecialty", "change:CHG-2025-118"],
        ["message_id", "specialty", "sub_specialty"],
    )
