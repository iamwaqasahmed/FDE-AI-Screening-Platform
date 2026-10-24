"""Read the clause that exists only on the photo transcription."""

from __future__ import annotations


def clause(page: dict) -> str:
    export = page.get("export", "")
    return page.get("transcription", "").replace(export, "").strip()
