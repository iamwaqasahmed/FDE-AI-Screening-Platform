"""Keep every audience, including a staff document for a patient."""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    del doc, asker
    return True
