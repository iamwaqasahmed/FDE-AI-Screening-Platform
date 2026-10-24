"""Confirm a slot when the notice fails."""

from __future__ import annotations


def notify(status: str, sent: bool) -> str:
    if not sent:
        return "booked"
    return status
