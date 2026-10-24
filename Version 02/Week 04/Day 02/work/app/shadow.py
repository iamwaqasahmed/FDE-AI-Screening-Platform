"""Keep the registered reply. Promote only after a comparison."""

from __future__ import annotations


def reply(turn: dict) -> str:
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict) -> str:
    if comparison.get("compared") and comparison.get("matched"):
        return str(comparison.get("candidate_hash") or "")
    return ""
