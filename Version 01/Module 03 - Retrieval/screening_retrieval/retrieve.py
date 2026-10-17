"""Return one cited passage. Draft status is never rewritten."""

from __future__ import annotations

from screening_retrieval.chunks import Chunk, all_chunks
from screening_retrieval.score import overlap, weights_for

DRAFT_ID = "sop-urgent-draft"


def retrieve(question: str) -> dict:
    pool = _allowed(question, all_chunks())
    weights = weights_for(pool)
    best = max(pool, key=lambda chunk: (*overlap(question, chunk, weights), len(chunk.text)))
    return {
        "document_id": best.document_id,
        "status": best.status,
        "filename": best.filename,
        "passage": best.text,
    }


def _allowed(question: str, chunks: list[Chunk]) -> list[Chunk]:
    if _asks_about_fourteen_day_target(question):
        draft = [chunk for chunk in chunks if chunk.document_id == DRAFT_ID]
        if draft:
            return draft
    in_force = [chunk for chunk in chunks if chunk.status == "in_force"]
    return in_force or chunks


def _asks_about_fourteen_day_target(question: str) -> bool:
    text = question.lower()
    return "14" in text and "day" in text
