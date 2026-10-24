"""catalog. END-01 is still defined. eligibility changed meaning in 2024 with no edit."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "catalog",
        "stale-field",
        ["field:END-01", "field:eligibility"],
        ["field", "system_of_record", "classification"],
    )
