"""Replace a citation that is not in force."""

from __future__ import annotations

# The document a patient may see. The other id is not in force.
_IN_FORCE = "circ-ramadan"
_UNAUTH = "circ-ramadan-unauth"


def repair(row: dict) -> dict:
    # Leave every other field as it was. Only the document id changes.
    if row.get("doc_id") == _UNAUTH:
        return {**row, "doc_id": _IN_FORCE}
    # An in-force citation stays. Copy it so the caller cannot change the row.
    return dict(row)
