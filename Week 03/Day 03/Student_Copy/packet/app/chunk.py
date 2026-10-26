"""Drop the clause id and keep the body as one chunk.

clauses builds a single row. The clause id on that row is empty.
The text is the whole body. The other document fields are copied
when they are present. A missing text field becomes empty text.
A missing version becomes zero.
"""

from __future__ import annotations


def clauses(doc: dict) -> list[dict]:
    """Wrap the whole body in one clause and clear the clause id.

    doc is one document. The body is not split. A missing body
    becomes empty text. A missing version becomes zero. The
    clause id stored on the document is not copied.
    """
    # One row. The clause id is blank, and the text is the whole body.
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
