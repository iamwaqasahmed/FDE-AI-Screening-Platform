"""Judge a reply by its fields. The sentence is not evidence."""

from __future__ import annotations


def schema_ok(reply: dict) -> bool:
    intent = reply.get("intent")
    return isinstance(intent, str) and bool(intent)


def journey_ok(reply: dict, state: dict) -> bool:
    del reply
    return bool(state.get("booked"))
