"""cc. About the reason code GEN, and notes that hold PHI. disposition arrives in 2025.

fault() returns that reason-code defect. The affected keys are the GEN reason and the note that holds PHI. The clean columns are the disposition and the summary.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the contact-center fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "cc",
        "reason-gen",
        ["reason:GEN", "note:phi"],
        ["disposition", "summary"],
    )
