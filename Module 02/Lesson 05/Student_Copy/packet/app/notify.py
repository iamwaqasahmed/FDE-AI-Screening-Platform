"""Confirm a slot when the notice fails.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

notify returns booked when the notice was not sent. While this
shell is the file that runs, the journey check says a failed
notice confirmed a slot.
"""

from __future__ import annotations


def notify(status: str, sent: bool) -> str:
    """Confirm a slot when the notice fails.

    status is the booking state. sent is whether the notice left.
    A failed notice returns booked. A notice that was sent returns
    the status it was given.
    """
    if not sent:
        return "booked"
    return status
