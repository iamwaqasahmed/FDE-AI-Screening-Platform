"""sched-ain. No intraday API. A missed night leaves yesterday's slots.

fault() returns that missed-night defect. The affected key is the night that did not arrive. The clean columns are the facility, the night, and the slots.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the Ain scheduling fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "sched-ain",
        "missed-night",
        ["night:2027-01-11"],
        ["facility", "night", "slots"],
    )
