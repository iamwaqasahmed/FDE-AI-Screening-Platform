"""Put the citation requirement on the risk tier."""

from __future__ import annotations


def gate_for(requirement_id: str) -> str:
    # The citation requirement sits on the risk tier named in the stage-gate file.
    if requirement_id == "req-cite":
        return "G1"
    # Any other requirement id has no gate from this function.
    return ""
