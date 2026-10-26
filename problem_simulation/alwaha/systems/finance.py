"""finance. One benefit is counted on two lines. A GPU purchase takes 16 weeks.

fault() returns that double-counted benefit. The affected keys are the access benefit and the GPU lead time. The clean columns are the cost center, the line id, and the lead time in weeks.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the finance fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "finance",
        "benefit-double-counted",
        ["benefit:access", "lead:gpu-16w"],
        ["cost_center", "line_id", "lead_weeks"],
    )
