"""his-nakhl. MRNs are reused, and a subset of PID dates are Hijri with no era marker."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "his-nakhl",
        "mrn-reused",
        ["mrn:h-nakhl:p-000004", "mrn:h-nakhl:p-000012", "dob:p-000011"],
        ["person_id", "national_id", "dob_era"],
    )
