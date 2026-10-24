"""sched-ain reference. A miss does not print the clinic code."""

from __future__ import annotations

AIN = "h-ain"
QUEUED = "queued"
BOOKED = "booked"
FAULT = "live-slot"


def book(facility_id: str, fault: str = "") -> str:
    if facility_id == AIN and fault != FAULT:
        return QUEUED
    return BOOKED


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    if arrived is None:
        return previous
    return arrived


def notify(status: str, sent: bool) -> str:
    if status == QUEUED:
        return QUEUED
    return status
