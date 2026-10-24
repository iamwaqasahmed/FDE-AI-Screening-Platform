"""his-safra. A merge was applied and later reversed. SIU messages arrive out of order."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "his-safra",
        "merge-reversed",
        ["merge:p-000005", "siu:sequence"],
        ["person_id", "sequence"],
    )
