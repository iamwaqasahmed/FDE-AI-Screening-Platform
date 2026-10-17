"""Monthly call-centre reason codes: the economics' expected calls with seeded Poisson noise."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.referrals import CONSULTANT_GAP
from simulation.economics.summary import calls_frame
from simulation.world.clock import BUREAU_MIGRATION_END, BUREAU_MIGRATION_START


def call_reasons(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    expected = calls_frame(world)
    frame = expected[["month", "reason"]].copy()
    frame["calls"] = rng.poisson(expected["expected"].to_numpy())
    return frame


def window_ratio(calls: pd.DataFrame, reason: str, start: str, end: str) -> float:
    """Mean monthly calls inside the window over the mean outside it."""
    rows = calls[calls["reason"] == reason]
    inside = rows["month"].between(start[:7], end[:7])
    outside_mean = max(float(rows.loc[~inside, "calls"].mean()), 1e-9)
    return round(float(rows.loc[inside, "calls"].mean()) / outside_mean, 2)


def call_gold(calls: pd.DataFrame) -> dict:
    letters = calls[calls["reason"] == "letter_not_received"]
    peak = letters.sort_values(["calls", "month"], ascending=[False, True]).iloc[0]
    return {
        "letter_peak_month": str(peak["month"]),
        "letter_peak_calls": int(peak["calls"]),
        "letter_ratio_in_migration": window_ratio(calls, "letter_not_received", BUREAU_MIGRATION_START.isoformat(),
                                                  BUREAU_MIGRATION_END.isoformat()),
        "hospital_ratio_in_consultant_gap": window_ratio(calls, "hospital_appointment", *CONSULTANT_GAP),
        "migration_window": [BUREAU_MIGRATION_START.isoformat(), BUREAU_MIGRATION_END.isoformat()],
        "consultant_gap": list(CONSULTANT_GAP),
    }
