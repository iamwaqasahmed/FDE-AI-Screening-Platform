"""Replace the schedule even when the night file is missing.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

apply_file drops yesterday. A missing night returns None. While
this shell is the file that runs, the journey check says a missed
night cleared the slots.
"""

from __future__ import annotations


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    """Drop yesterday and keep only a file that arrived.

    previous is the file already held. arrived is the night drop.
    None means the night did not arrive. previous is ignored. A
    missing night clears the schedule.
    """
    del previous
    if arrived is None:
        return None
    return arrived
