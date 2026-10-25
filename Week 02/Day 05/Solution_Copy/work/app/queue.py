"""Queue a booking at Ain until the nightly file arrives.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns booked for every hospital. While that shell is
the file that runs, the journey check says a live slot was promised.
"""

from __future__ import annotations


def book(facility_id: str, fault: str = "") -> str:
    """Queue Ain, and book only a live-slot fault or another hospital.

    facility_id is the hospital. h-ain waits for the nightly file.
    fault is empty for a normal booking. live-slot is the fault
    that must not be confirmed. Any other hospital is booked.
    """
    # Ain without the live-slot fault stays queued for the nightly file.
    if facility_id == "h-ain" and fault != "live-slot":
        return "queued"
    # A live-slot fault, and any facility that is not h-ain, is booked.
    return "booked"
