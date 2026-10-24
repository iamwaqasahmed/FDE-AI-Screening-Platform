"""his-wadi. Clinic code END-01 became ENDO-CLN. FHIR v2 drops the old field name."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "his-wadi",
        "clinic-code-renamed",
        ["clinic:END-01"],
        ["clinic:ENDO-CLN"],
    )
