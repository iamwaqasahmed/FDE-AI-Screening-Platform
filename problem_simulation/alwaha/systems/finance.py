"""finance. One benefit is counted on two lines. A GPU purchase takes 16 weeks."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "finance",
        "benefit-double-counted",
        ["benefit:access", "lead:gpu-16w"],
        ["cost_center", "line_id", "lead_weeks"],
    )
