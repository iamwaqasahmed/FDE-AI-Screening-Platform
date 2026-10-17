"""Some rows arrive hours or days after the event they describe."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: column (datetime to delay), share, hours (low, high), key (id column for the record)."""
    column, share = params["column"], float(params["share"])
    low, high = params.get("hours", (2, 96))
    late = rng.random(len(frame)) < share
    delay = pd.to_timedelta(np.where(late, rng.uniform(low, high, len(frame)), 0.0), unit="h").round("min")
    out = frame.copy()
    out[column] = out[column] + delay
    key = params.get("key", "")
    late_keys = sorted(out.loc[late, key].astype(str).unique().tolist()) if key else []
    return out, record("late_arrival", column=column, rows=int(late.sum()), share=share, keys=late_keys[:50])
