"""hr. Leave is entered after the session is published."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "hr",
        "leave-after-publish",
        ["clinician:h-wadi-endo"],
        ["clinician_id", "session_id", "leave_on"],
    )
