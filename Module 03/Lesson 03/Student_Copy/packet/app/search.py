"""Rank by vector similarity and keep every status.

rank ignores the mode. Every chunk is scored and kept, including
a chunk whose status is not in force. A higher score sorts first.
The same score sorts by document id.
"""

from __future__ import annotations

from embed import embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    """Score every chunk by nearness and sort, highest score first.

    question is embedded as the query. mode is discarded, so the
    status field does not remove a chunk. A chunk that already
    has a vector uses that vector. Otherwise the chunk text is
    embedded. The sort is higher score first, then document id.
    """
    # Mode does not change which chunks stay in the list.
    del mode
    query = embed(question)
    scored = []
    for chunk in chunks:
        # A stored vector is used. Missing text is embedded as empty text.
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        scored.append((nearness(query, vector), str(chunk.get("doc_id", "")), chunk))
    # A negative score sorts high to low. Document id breaks a tie.
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
