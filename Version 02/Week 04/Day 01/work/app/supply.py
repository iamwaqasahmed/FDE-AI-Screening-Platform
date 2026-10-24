"""Load a registered hash only. Tool text and a poisoned label stay data."""

from __future__ import annotations

IN_FORCE = "circ-ramadan"


def accept_hash(candidate: str, approved: list[str]) -> str:
    if candidate in approved:
        return candidate
    return ""


def run_tool(description: str) -> str:
    del description
    return ""


def keep_label(row: dict) -> bool:
    return not row.get("poison")


def cite(doc: dict) -> str:
    if doc.get("status") == "in_force" and doc.get("audience") in {"public", "staff"}:
        return str(doc.get("doc_id") or "")
    return IN_FORCE
