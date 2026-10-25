"""The cluster booking window wins. Name both documents."""

from __future__ import annotations


def booking(docs: list[dict], site: str) -> dict:
    # The document for this site, and the cluster window.
    local = next(doc for doc in docs if doc.get("site") == site)
    cluster = next(doc for doc in docs if doc.get("doc_id") == "pol-booking-cluster")
    # Name the site document. The cluster window is the winner.
    return {"also": local["doc_id"], "winner": cluster["doc_id"]}
