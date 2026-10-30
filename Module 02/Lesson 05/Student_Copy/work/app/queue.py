"""Book a slot at every hospital.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

book ignores the facility and the fault. It returns booked for
every call. While this shell is the file that runs, the journey
check says a live slot was promised.
"""

from __future__ import annotations


def book(facility_id: str, fault: str = "") -> str:
    """Return booked and ignore every argument.

    facility_id is the hospital. fault is empty for a normal
    booking, or live-slot for the fault. Neither is used. Ain
    is booked the same way as every other hospital.
    """
    del facility_id, fault
    return "booked"
