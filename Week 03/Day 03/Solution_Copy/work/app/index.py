"""Store one vector per clause.

build splits each document into clauses and stores an embedding
of the clause text on that row. Rows follow document order, and
clause order inside each document.
"""

from __future__ import annotations

from chunk import clauses
from embed import embed


def build(docs: list[dict]) -> list[dict]:
    """Index every clause of every document.

    docs is the document list. Each stored row is the clause
    dict with a vector added. The vector is the embedding of
    that clause's text.
    """
    rows = []
    for doc in docs:
        # One row per clause. The vector is stored on that row.
        for clause in clauses(doc):
            clause["vector"] = embed(clause["text"])
            rows.append(clause)
    return rows
