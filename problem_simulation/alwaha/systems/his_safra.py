"""his-safra. A merge was applied and later reversed. SIU messages arrive out of order.

fault() returns that merge defect. The affected keys are the reversed merge and the SIU sequence. The clean columns are the person and the sequence.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the his-safra fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "his-safra",
        "merge-reversed",
        ["merge:p-000005", "siu:sequence"],
        ["person_id", "sequence"],
    )
