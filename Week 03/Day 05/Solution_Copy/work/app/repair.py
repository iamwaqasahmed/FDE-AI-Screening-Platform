"""Replace a citation that is not in force.

When the document id is the unauthorized id, the copy uses the
in-force id. Every other field is copied as it was. A row with any
other document id is copied unchanged, so the caller can edit the
copy without editing the original row.
"""

from __future__ import annotations

# The document a patient may see. The other id is not in force.
_IN_FORCE = "circ-ramadan"
_UNAUTH = "circ-ramadan-unauth"


def repair(row: dict) -> dict:
    """Return a citation, with an unauthorized document id replaced.

    row is the citation. The document id changes only when it is the
    unauthorized id. Every other field is copied through.
    """
    # Leave every other field as it was. Only the document id changes.
    if row.get("doc_id") == _UNAUTH:
        return {**row, "doc_id": _IN_FORCE}
    # An in-force citation stays. Copy it so the caller cannot change the row.
    return dict(row)
