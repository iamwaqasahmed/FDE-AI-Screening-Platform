"""Put the citation requirement on the risk tier."""

from __future__ import annotations


def gate_for(requirement_id: str) -> str:
    if requirement_id == "req-cite":
        return "G1"
    return ""
