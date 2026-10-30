"""Hybrid rank: vector similarity, a code boost, and a version filter.

rank embeds the question and scores each chunk by nearness.
Vector mode keeps every status. Hybrid mode keeps a chunk only
when its status is in force, and it adds one to the score when
a code from the question is a key in the chunk vector. A higher
score sorts first. The same score sorts by document id.
"""

from __future__ import annotations

from embed import codes, embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    """Score the chunks and return them, highest score first.

    question supplies the text to embed and the codes to look
    for. chunks are the rows to score. Hybrid mode skips a chunk
    that is not in force, and adds one when a question code is
    in the vector. Any other mode keeps every status and does
    not add that one. A chunk that already carries a vector
    uses it. Otherwise the chunk text is embedded.
    """
    query = embed(question)
    query_codes = codes(question)
    scored = []
    for chunk in chunks:
        # Hybrid keeps in_force only. Vector mode keeps every status.
        if mode == "hybrid" and chunk.get("status") != "in_force":
            continue
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        score = nearness(query, vector)
        # Hybrid adds one when a question code is a key in the vector.
        if mode == "hybrid" and any(code in vector for code in query_codes):
            score += 1
        scored.append((score, str(chunk.get("doc_id", "")), chunk))
    # Higher score first. The same score keeps document id order.
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
