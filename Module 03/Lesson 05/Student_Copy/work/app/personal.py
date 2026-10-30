"""Cite every document and ignore the floor.

cite returns a citation that carries the document id from the row.
meets_budget discards the value and the floor and returns true.
"""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    """Return a citation with the document id.

    row may carry a doc_id. That id is the field on the result.
    """
    # The document id is the field this citation copies.
    return {"doc_id": row.get("doc_id")}


def meets_budget(value: float, floor: float) -> bool:
    """Return true for any value and floor.

    value and floor are discarded.
    """
    # The value and the floor are unused.
    del value, floor
    return True
