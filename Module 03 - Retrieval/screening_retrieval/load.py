"""Load corpus documents and their manifest status."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import pandas as pd

CORPUS = Path(__file__).resolve().parents[2] / "data" / "corpus"


@dataclass(frozen=True)
class Document:
    document_id: str
    status: str
    filename: str
    text: str


@lru_cache(maxsize=1)
def documents() -> tuple[Document, ...]:
    manifest = pd.read_csv(CORPUS / "manifest.csv", dtype=str)
    loaded = []
    for row in manifest.itertuples(index=False):
        loaded.append(
            Document(
                document_id=row.document_id,
                status=row.status,
                filename=row.filename,
                text=(CORPUS / row.filename).read_text(encoding="utf-8"),
            )
        )
    return tuple(loaded)
