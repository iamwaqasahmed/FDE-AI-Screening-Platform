"""Read the text export and skip the photo transcription."""

from __future__ import annotations


def clause(page: dict) -> str:
    return page.get("export", "")
