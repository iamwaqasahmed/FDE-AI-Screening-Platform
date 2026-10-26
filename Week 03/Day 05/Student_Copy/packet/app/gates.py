"""Send the citation requirement to go-live.

gate_for discards the requirement id and returns the go-live gate.
"""

from __future__ import annotations


def gate_for(requirement_id: str) -> str:
    """Return the go-live gate.

    requirement_id is discarded. The gate does not depend on the id.
    """
    # Every requirement id gets this same gate.
    del requirement_id
    return "G4"
