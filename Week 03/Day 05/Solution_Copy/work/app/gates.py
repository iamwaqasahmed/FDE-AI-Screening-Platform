"""Put the citation requirement on the risk tier.

The citation requirement id returns the risk tier. Every other
requirement id returns an empty gate.
"""

from __future__ import annotations


def gate_for(requirement_id: str) -> str:
    """Return the gate name for a requirement id.

    requirement_id is the id being placed. The citation requirement
    returns the risk tier. Any other id returns an empty string.
    """
    # The citation requirement sits on the risk tier named in the stage-gate file.
    if requirement_id == "req-cite":
        return "G1"
    # Any other requirement id has no gate from this function.
    return ""
