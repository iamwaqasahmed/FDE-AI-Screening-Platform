"""Rank by vector similarity and keep every status."""

from __future__ import annotations

from embed import embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    del mode
    query = embed(question)
    scored = []
    for chunk in chunks:
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        scored.append((nearness(query, vector), str(chunk.get("doc_id", "")), chunk))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
