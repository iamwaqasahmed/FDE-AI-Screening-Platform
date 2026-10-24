"""Clinic code in force on the row date."""

from __future__ import annotations

CHANGE = "2024-06-01"
ENDO = {"END-01", "ENDO-CLN"}


def clinic(code: str, as_of: str, facility: str) -> str:
    if facility == "h-wadi" and as_of >= CHANGE and code in ENDO:
        return "ENDO-CLN"
    return code
