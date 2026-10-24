"""Judge a reply by its sentence."""

from __future__ import annotations


def schema_ok(reply: dict) -> bool:
    return bool(reply.get("text"))


def journey_ok(reply: dict, state: dict) -> bool:
    del state
    return "booked" in str(reply.get("text", "")).lower()
