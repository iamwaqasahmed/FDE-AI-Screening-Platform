"""Show the shadow reply and promote the candidate.

reply returns the shadow reply, or an empty string when it is missing.
promote returns the candidate hash with no other check, or an empty
string when the hash is missing.
"""

from __future__ import annotations


def reply(turn: dict) -> str:
    """Return the shadow reply.

    A missing shadow reply becomes an empty string. Other keys are ignored.
    """
    # Only the shadow reply is read.
    return str(turn.get("shadow_reply") or "")


def promote(comparison: dict) -> str:
    """Return the candidate hash and ignore the other fields.

    A missing hash becomes an empty string. No flag has to be true.
    """
    # No flag is read. The hash is returned whenever it is present.
    return str(comparison.get("candidate_hash") or "")
