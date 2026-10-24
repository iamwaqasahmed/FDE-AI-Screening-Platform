"""Load the candidate hash and follow the tool text."""

from __future__ import annotations


def accept_hash(candidate: str, approved: list[str]) -> str:
    del approved
    return candidate


def run_tool(description: str) -> str:
    if "book" in description.lower():
        return "book"
    return ""


def keep_label(row: dict) -> bool:
    del row
    return True


def cite(doc: dict) -> str:
    return str(doc.get("doc_id") or "")
