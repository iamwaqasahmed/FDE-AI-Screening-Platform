"""his-nakhl. MRNs are reused, and a subset of PID dates are Hijri with no era marker.

fault() returns that identity defect. The affected keys are the reused MRNs and the Hijri date of birth. The clean columns are the person, the national id, and the era of the date of birth.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the his-nakhl fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "his-nakhl",
        "mrn-reused",
        ["mrn:h-nakhl:p-000004", "mrn:h-nakhl:p-000012", "dob:p-000011"],
        ["person_id", "national_id", "dob_era"],
    )
