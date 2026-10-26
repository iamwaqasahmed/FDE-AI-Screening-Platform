"""Keep the registered reply. Promote only after a comparison.

reply returns the registered reply, or an empty string when it is
missing. The shadow reply is not read. promote returns the candidate
hash only when the comparison was both compared and matched. Either
flag missing or false yields an empty string. A missing hash on a
ready comparison also becomes an empty string.
"""

from __future__ import annotations


def reply(turn: dict) -> str:
    """Return the registered reply.

    A missing registered reply becomes an empty string. Other keys on
    the turn are ignored.
    """
    # The shadow reply is not consulted.
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict) -> str:
    """Return the candidate hash only after a match that was compared.

    Otherwise return an empty string. A missing hash on a ready
    comparison is stored as an empty string too.
    """
    # Both flags must be true. One true flag is not enough.
    if comparison.get("compared") and comparison.get("matched"):
        return str(comparison.get("candidate_hash") or "")
    return ""
