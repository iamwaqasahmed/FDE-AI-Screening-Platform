"""A booked status is the live-slot fault."""

from __future__ import annotations


def holds(status: str) -> bool:
    return status == "queued"
