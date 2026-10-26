"""his-wadi. Clinic code END-01 became ENDO-CLN. FHIR v2 drops the old field name.

fault() returns that rename. The affected key is the old clinic code. The clean list holds the renamed clinic code.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the his-wadi fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "his-wadi",
        "clinic-code-renamed",
        ["clinic:END-01"],
        ["clinic:ENDO-CLN"],
    )
