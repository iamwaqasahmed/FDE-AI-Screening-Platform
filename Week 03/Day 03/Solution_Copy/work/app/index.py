"""Store one vector per clause."""

from __future__ import annotations

from chunk import clauses
from embed import embed


def build(docs: list[dict]) -> list[dict]:
    rows = []
    for doc in docs:
        # One row per clause. The vector is stored on that row.
        for clause in clauses(doc):
            clause["vector"] = embed(clause["text"])
            rows.append(clause)
    return rows
