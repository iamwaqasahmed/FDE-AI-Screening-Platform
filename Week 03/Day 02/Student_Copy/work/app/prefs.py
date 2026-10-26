"""Return the coordinator draft unchanged.

revise returns the same string it was given. No word is expanded
and no word is removed.
"""

from __future__ import annotations


def revise(draft: str) -> str:
    """Return the draft as it arrived.

    draft is the coordinator sentence. This function does not
    scan it.
    """
    # The sentence is handed back with every word still in place.
    return draft
