"""A share of rows is delivered twice. The copy is identical apart from an optional later arrival time."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: share, key (id column for the record), shift (datetime column moved on the copy), minutes (low, high)."""
    chosen = np.flatnonzero(rng.random(len(frame)) < float(params["share"]))
    copies = frame.iloc[chosen].copy()
    shift = params.get("shift", "")
    if shift and len(copies):
        low, high = params.get("minutes", (1, 720))
        copies[shift] = copies[shift] + pd.to_timedelta(rng.integers(low, high + 1, len(copies)), unit="min")
    out = pd.concat([frame, copies], ignore_index=True)
    key = params.get("key", "")
    keys = sorted(copies[key].astype(str).tolist()) if key else []
    return out, record("duplicate", rows=int(len(copies)), share=float(params["share"]), keys=keys[:50])
