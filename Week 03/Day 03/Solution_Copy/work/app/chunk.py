"""Split a document into clauses and keep the clause id.

clauses splits the body on a blank line. Each non-empty piece
becomes a row. The document fields, including the clause id,
are copied onto every piece. The piece itself is stored as
text. An empty piece is dropped.
"""

from __future__ import annotations

# These fields travel with every clause. The clause id is one of them.
_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")


def clauses(doc: dict) -> list[dict]:
    """Turn each non-empty body piece into a clause row.

    doc is one document. A missing body is treated as empty
    text, which produces no rows. Each row copies the shared
    fields, and a missing field becomes empty text. The piece,
    with surrounding space removed, is the text.
    """
    # A blank line separates clauses. Empty pieces are dropped.
    parts = [part.strip() for part in doc.get("body", "").split("\n\n") if part.strip()]
    rows = []
    for part in parts:
        # Copy the document fields onto this clause, then set its text.
        row = {name: doc.get(name, "") for name in _FIELDS}
        row["text"] = part
        rows.append(row)
    return rows
