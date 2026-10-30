"""Return the nearest chunk, including a draft.

answer indexes the documents and ranks them in vector mode. An
empty ranking is a no-document refusal. Otherwise the first
ranked chunk is cited. Status is copied onto the citation, so
a draft is cited the same way as any other status. The asker
is not checked.
"""

from __future__ import annotations

from index import build
from search import rank


def answer(question: dict, docs: list[dict]) -> dict:
    """Cite the top vector hit, or refuse when nothing ranks.

    question supplies the text to rank. docs are indexed, then
    ranked in vector mode. The citation copies audience, document
    id, clause id as the span, status, and version from that hit.
    A missing text field becomes empty text. A missing version
    becomes zero.
    """
    ranked = rank(question["text"], build(docs), "vector")
    # No hit means there is nothing to cite.
    if not ranked:
        return {"refusal": "no-document"}
    top = ranked[0]
    # Status is passed through. This function does not drop a draft.
    return {
        "audience": top.get("audience", ""),
        "doc_id": top.get("doc_id", ""),
        "span": top.get("clause_id", ""),
        "status": top.get("status", ""),
        "version": top.get("version", 0),
    }
