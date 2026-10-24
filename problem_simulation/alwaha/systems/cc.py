"""cc. About the reason code GEN, and notes that hold PHI. disposition arrives in 2025."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "cc",
        "reason-gen",
        ["reason:GEN", "note:phi"],
        ["disposition", "summary"],
    )
