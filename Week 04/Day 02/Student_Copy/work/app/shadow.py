"""Show the shadow reply and promote the candidate."""

from __future__ import annotations


def reply(turn: dict) -> str:
    return str(turn.get("shadow_reply") or "")


def promote(comparison: dict) -> str:
    return str(comparison.get("candidate_hash") or "")
