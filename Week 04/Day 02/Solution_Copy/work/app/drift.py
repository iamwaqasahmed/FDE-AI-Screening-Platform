"""Name the three drifts.

name maps the row's kind to the label stored in _LABELS. The kind is
read as a string. A kind that is not in the map raises KeyError. A
missing kind becomes the string None, which is not a label, so that
lookup raises too.
"""

from __future__ import annotations

# Kind to label. The keys are the only kinds this function accepts.
_LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}


def name(row: dict) -> str:
    """Return the label for this row's kind.

    The map is not copied or extended. An unknown kind is an error.
    """
    return _LABELS[str(row.get("kind"))]
