"""Allow the session and the holds."""

from __future__ import annotations


def admit(event: dict) -> bool:
    del event
    return True
