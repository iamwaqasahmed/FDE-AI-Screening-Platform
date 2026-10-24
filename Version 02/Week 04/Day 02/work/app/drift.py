"""Name the three drifts."""

from __future__ import annotations

_LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}


def name(row: dict) -> str:
    return _LABELS[str(row.get("kind"))]
