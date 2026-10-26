"""Leave every citation as it was scored.

repair returns a new dict with the same fields as the row. The
caller can edit the copy without editing the original row.
"""

from __future__ import annotations


def repair(row: dict) -> dict:
    """Return a copy of the citation.

    row is the scored citation. The copy keeps every field.
    """
    # A new dict, so later edits do not change the scored row.
    return dict(row)
