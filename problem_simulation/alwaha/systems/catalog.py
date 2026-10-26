"""catalog. END-01 is still defined. eligibility changed meaning in 2024 with no edit.

fault() returns that stale-field defect. The affected keys are the field that is still defined and the field whose meaning drifted. The clean columns are the field, the system of record, and the classification.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the catalog fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "catalog",
        "stale-field",
        ["field:END-01", "field:eligibility"],
        ["field", "system_of_record", "classification"],
    )
