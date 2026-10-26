"""Let the facility window replace the cluster window.

booking returns the document for the given site as the winner.
The also field is empty, so the other document is not named.
"""

from __future__ import annotations


def booking(docs: list[dict], site: str) -> dict:
    """Name the site document as the only winner.

    docs is the policy list. site selects the document whose
    site matches. The winner is that document id. also is an
    empty string. A site with no matching document raises,
    because next() requires a match.
    """
    local = next(doc for doc in docs if doc.get("site") == site)
    # The site document wins. The other document is not named.
    return {"also": "", "winner": local["doc_id"]}
