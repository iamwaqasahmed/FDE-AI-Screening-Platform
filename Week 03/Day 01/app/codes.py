"""Clinic codes taken from the catalog."""

from __future__ import annotations


def clinic(code: str, as_of: str, facility: str) -> str:
    del as_of, facility
    if code == "ENDO-CLN":
        return "END-01"
    return code
