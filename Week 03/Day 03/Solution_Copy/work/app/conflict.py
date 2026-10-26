"""The cluster booking window wins. Name both documents.

booking finds the document for the site and the cluster booking
document. The cluster document is the winner. The site document
is named in also.
"""

from __future__ import annotations


def booking(docs: list[dict], site: str) -> dict:
    """Name the site document and return the cluster window as the winner.

    docs must contain a document whose site matches and the
    cluster booking document. The site document id is also.
    The cluster document id is the winner. A missing match
    raises, because next() requires one.
    """
    # The document for this site, and the cluster window.
    local = next(doc for doc in docs if doc.get("site") == site)
    cluster = next(doc for doc in docs if doc.get("doc_id") == "pol-booking-cluster")
    # Name the site document. The cluster window is the winner.
    return {"also": local["doc_id"], "winner": cluster["doc_id"]}
