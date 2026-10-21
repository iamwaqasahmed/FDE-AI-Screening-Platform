"""The published confidence rule. The data-quality note states the same numbers."""

from __future__ import annotations


def confidence(national_status: str, name_match: bool, dob_match: bool, postcode_match: bool) -> float:
    if national_status == "confirmed" and name_match:
        return 0.95
    if name_match and dob_match and postcode_match:
        return 0.80
    if name_match and dob_match:
        return 0.55
    if name_match:
        return 0.30
    return 0.10
