"""Split corpus documents into headed sections."""

from __future__ import annotations

import re
from dataclasses import dataclass

from screening_retrieval.load import Document, documents

HEADING = re.compile(r"(?m)^#{1,6} ")


@dataclass(frozen=True)
class Chunk:
    document_id: str
    status: str
    filename: str
    text: str


def chunks_for(document: Document) -> list[Chunk]:
    parts = [part.strip() for part in HEADING.split(document.text) if part.strip()]
    if not parts:
        parts = [document.text.strip()]
    return [
        Chunk(
            document_id=document.document_id,
            status=document.status,
            filename=document.filename,
            text=part,
        )
        for part in parts
    ]


def all_chunks() -> list[Chunk]:
    found = []
    for document in documents():
        found.extend(chunks_for(document))
    return found
