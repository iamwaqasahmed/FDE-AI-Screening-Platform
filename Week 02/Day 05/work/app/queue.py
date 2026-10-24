"""Queue a booking at Ain until the nightly file arrives."""

from __future__ import annotations


def book(facility_id: str, fault: str = "") -> str:
    if facility_id == "h-ain" and fault != "live-slot":
        return "queued"
    return "booked"
