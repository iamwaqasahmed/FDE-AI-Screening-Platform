"""Clinic code in force on the row date.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell rewrites ENDO-CLN back to END-01 and ignores the date.
While that shell is the file that runs, the identity check says the
stale clinic code was kept. The check does not name the code.
"""

from __future__ import annotations

CHANGE = "2024-06-01"
ENDO = {"END-01", "ENDO-CLN"}


def clinic(code: str, as_of: str, facility: str) -> str:
    """Return the endocrinology code in force at h-wadi.

    code is the code on the row. as_of is the row date. facility is
    the hospital. Before June 2024, END-01 stays. On and after that
    date, both endocrinology codes at h-wadi are ENDO-CLN. Any other
    facility keeps the code on the row.
    """
    # h-wadi, on or after the change, uses the new endocrinology code.
    if facility == "h-wadi" and as_of >= CHANGE and code in ENDO:
        return "ENDO-CLN"
    # A row before the change, or another facility, keeps its code.
    return code
