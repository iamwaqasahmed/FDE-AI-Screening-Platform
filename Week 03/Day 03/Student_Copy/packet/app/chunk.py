"""Drop the clause id and keep the body as one chunk."""

from __future__ import annotations


def clauses(doc: dict) -> list[dict]:
    return [
        {
            "audience": doc.get("audience", ""),
            "clause_id": "",
            "code": doc.get("code", ""),
            "doc_id": doc.get("doc_id", ""),
            "site": doc.get("site", ""),
            "specialty": doc.get("specialty", ""),
            "status": doc.get("status", ""),
            "text": doc.get("body", ""),
            "version": doc.get("version", 0),
        }
    ]
