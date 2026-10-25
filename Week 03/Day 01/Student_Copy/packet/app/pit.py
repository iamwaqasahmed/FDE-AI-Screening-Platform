"""Join the latest feature row.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

features ignores the invite time and keeps the latest as_of.
The three checks do not call this file. The suite does.
"""

from __future__ import annotations


def features(rows: list[dict], invite_on: str) -> dict:
    """Return the district and insurance on the latest row.

    rows are the feature history. invite_on is ignored. The row
    with the greatest as_of is kept, even when it is after the
    invite.
    """
    del invite_on
    chosen = max(rows, key=lambda row: row["as_of"])
    return {"district": chosen["district"], "insurance": chosen["insurance"]}
