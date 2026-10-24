"""Read the tool, the hash, and the token count."""

from __future__ import annotations


def read(span: dict) -> dict:
    return {"hash": span.get("hash") or "", "tokens": int(span.get("tokens") or 0), "tool": span.get("tool") or ""}
