"""Leave the extraction fields blank.

relabel copies the item id and returns an empty source type and
an empty sub-specialty. The letter text is not read.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Copy the item id and leave both labels empty.

    row must carry item_id. Any text on the row is ignored. The
    source type and the sub-specialty are empty strings.
    """
    # The letter text is not consulted. Both labels stay blank.
    return {"item_id": row["item_id"], "source_type": "", "sub_specialty": ""}
