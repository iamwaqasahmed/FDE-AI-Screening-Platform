"""Split a document into clauses and keep the clause id."""

from __future__ import annotations

# These fields travel with every clause. The clause id is one of them.
_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")


def clauses(doc: dict) -> list[dict]:
    # A blank line separates clauses. Empty pieces are dropped.
    parts = [part.strip() for part in doc.get("body", "").split("\n\n") if part.strip()]
    rows = []
    for part in parts:
        # Copy the document fields onto this clause, then set its text.
        row = {name: doc.get(name, "") for name in _FIELDS}
        row["text"] = part
        rows.append(row)
    return rows
