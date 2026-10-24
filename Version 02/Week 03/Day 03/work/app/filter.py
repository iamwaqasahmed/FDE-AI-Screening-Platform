"""A patient sees public documents. Staff do not see restricted ones."""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    audience = doc.get("audience", "")
    if asker == "patient":
        return audience == "public"
    if asker == "staff":
        return audience in {"public", "staff"}
    if asker == "records":
        return audience in {"public", "staff", "restricted"}
    return False
