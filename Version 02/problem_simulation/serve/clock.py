"""The simulated clock and the outage windows it falls into, taken from the simulation timeline."""

from __future__ import annotations

from datetime import date, datetime

OUTAGE_WORDS = ("outage",)


def outage_windows(system: str) -> list[tuple[str, date, date, str]]:
    from simulation.world.timeline import happenings

    return [
        (item.ref, item.start, item.end, item.title)
        for item in happenings(system=system, kind="incident")
        if item.end is not None and any(word in item.title.lower() for word in OUTAGE_WORDS)
    ]


def active_outage(system: str, clock: datetime) -> tuple[str, date, date, str] | None:
    day = clock.date()
    for window in outage_windows(system):
        _, start, end, _ = window
        if start <= day < end:
            return window
    return None


def iso(moment: datetime) -> str:
    return moment.replace(microsecond=0).isoformat()
