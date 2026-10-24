"""Hybrid rank: vector similarity, a code boost, and a version filter."""

from __future__ import annotations

from embed import codes, embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    query = embed(question)
    query_codes = codes(question)
    scored = []
    for chunk in chunks:
        if mode == "hybrid" and chunk.get("status") != "in_force":
            continue
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        score = nearness(query, vector)
        if mode == "hybrid" and any(code in vector for code in query_codes):
            score += 1
        scored.append((score, str(chunk.get("doc_id", "")), chunk))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
