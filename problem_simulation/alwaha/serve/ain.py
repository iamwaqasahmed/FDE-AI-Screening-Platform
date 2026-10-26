"""sched-ain reference. A miss does not print the clinic code.

book() returns queued for the Ain facility when the fault is not the live-slot value, and booked for every other call. apply_file() keeps the previous file when nothing arrived. notify() leaves a queued status queued. None of these functions return a clinic code.
"""

from __future__ import annotations

AIN = "h-ain"
QUEUED = "queued"
BOOKED = "booked"
FAULT = "live-slot"


def book(facility_id: str, fault: str = "") -> str:
    """Return queued or booked.

    Ain is queued unless the fault is the live-slot value. That fault, and any other facility, is booked.
    """
    # The live-slot fault is the only Ain call that skips the queue.
    if facility_id == AIN and fault != FAULT:
        return QUEUED
    return BOOKED


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    """Return the file that now stands.

    A missing arrival leaves the previous file in place. An arrived dict replaces that file entirely.
    """
    # None means this night's file did not arrive, so the previous file still stands.
    if arrived is None:
        return previous
    return arrived


def notify(status: str, sent: bool) -> str:
    """Return the status left after a notification attempt.

    A queued status stays queued. Any other status is returned unchanged. The sent flag does not change the result.
    """
    # Sending a message does not promote a queued Ain request to booked.
    if status == QUEUED:
        return QUEUED
    return status
