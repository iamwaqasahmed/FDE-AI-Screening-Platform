"""Split a document into clauses and keep the clause id."""

from __future__ import annotations

_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")


def clauses(doc: dict) -> list[dict]:
    parts = [part.strip() for part in doc.get("body", "").split("\n\n") if part.strip()]
    rows = []
    for part in parts:
        row = {name: doc.get(name, "") for name in _FIELDS}
        row["text"] = part
        rows.append(row)
    return rows
