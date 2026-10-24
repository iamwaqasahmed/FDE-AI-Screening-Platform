"""Let the facility window replace the cluster window."""

from __future__ import annotations


def booking(docs: list[dict], site: str) -> dict:
    local = next(doc for doc in docs if doc.get("site") == site)
    return {"also": "", "winner": local["doc_id"]}
