"""Features as of the invite time.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell keeps the latest row and ignores the invite time. The
three checks do not call this file. The suite does. When the file
is present, the invite date is the cutoff.
"""

from __future__ import annotations


def features(rows: list[dict], invite_on: str) -> dict:
    """Keep the latest row that is on or before the invite.

    rows are the feature history. invite_on is the invite date.
    A row after that date is left out. The result is the district
    and the insurance on the chosen row. No row early enough means
    an empty result.
    """
    chosen = None
    for row in rows:
        # Later than the invite is not a feature of the invite.
        if row["as_of"] <= invite_on and (chosen is None or row["as_of"] > chosen["as_of"]):
            chosen = row
    if chosen is None:
        return {}
    return {"district": chosen["district"], "insurance": chosen["insurance"]}
