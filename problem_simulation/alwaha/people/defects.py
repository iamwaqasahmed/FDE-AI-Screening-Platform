"""Indexes that always carry a named defect, including on the personal world.

The map is the defect name for a person index. Indexes that are not listed have no planted defect. The reused-with index and the shared phone are the values the population linker copies onto other rows.
"""

from __future__ import annotations

DEFECT_BY_INDEX = {
    0: "shared-phone",
    1: "shared-phone",
    2: "newborn-on-mother",
    3: "visitor-to-iqama",
    4: "reused-mrn",
    5: "reversed-merge",
    6: "twins",
    7: "twins",
    8: "mover",
    9: "bad-check-digit",
    10: "late-death",
    11: "hijri-dob",
}

REUSED_WITH = 12
SHARED_PHONE = "0500000100"


def defect_for(index: int) -> str:
    """Return the planted defect name for this index, or an empty string when the index is clean."""
    return DEFECT_BY_INDEX.get(index, "")
