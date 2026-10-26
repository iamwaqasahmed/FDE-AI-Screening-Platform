"""Return a cached public answer without a model call.

answer looks the row id up in the store. A hit returns
the stored body and a call count of 0. A miss returns
the row text and a call count of 1. A missing id is an
empty string. A missing text is an empty string.
"""

from __future__ import annotations


def answer(store: dict, row: dict) -> dict:
    """Serve the stored body when the row id is already in the store.

    calls is 0 on a hit. calls is 1 when the id is absent,
    and the body is then the row text.
    """
    key = str(row.get("id") or "")
    # A stored id is served with no model call.
    if key in store:
        return {"body": str(store[key]), "calls": 0}
    return {"body": str(row.get("text") or ""), "calls": 1}
