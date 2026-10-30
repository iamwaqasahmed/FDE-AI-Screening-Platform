"""Keep unlabeled domain text. Leave the extraction letters out.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell trains on every row, including the extraction letters.
The two checks do not load this file. The suite does. Do not delete
it.
"""

from __future__ import annotations


def keep(rows: list[dict]) -> list[dict]:
    """Keep a row only when it has no item id.

    rows are domain lines and letters mixed together. A letter
    carries an item id. A domain line does not. The letter is left
    out. The text of a domain line is kept as it arrived.
    """
    unlabeled = [row for row in rows if "item_id" not in row]
    return unlabeled
