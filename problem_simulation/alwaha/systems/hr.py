"""hr. Leave is entered after the session is published.

fault() returns that late-leave defect. The affected key is the clinician. The clean columns are the clinician, the session, and the leave date.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the HR fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "hr",
        "leave-after-publish",
        ["clinician:h-wadi-endo"],
        ["clinician_id", "session_id", "leave_on"],
    )
