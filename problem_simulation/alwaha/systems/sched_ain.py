"""sched-ain. No intraday API. A missed night leaves yesterday's slots."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "sched-ain",
        "missed-night",
        ["night:2027-01-11"],
        ["facility", "night", "slots"],
    )
