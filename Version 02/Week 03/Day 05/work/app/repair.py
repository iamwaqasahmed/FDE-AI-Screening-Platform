"""Replace a citation that is not in force."""

from __future__ import annotations

_IN_FORCE = "circ-ramadan"
_UNAUTH = "circ-ramadan-unauth"


def repair(row: dict) -> dict:
    if row.get("doc_id") == _UNAUTH:
        return {**row, "doc_id": _IN_FORCE}
    return dict(row)
