"""A system that overwrites: only the latest row per key survives."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: key (entity column), order (column that decides the latest row)."""
    key, order = params["key"], params["order"]
    ordered = frame.sort_values([key, order], kind="stable")
    out = ordered.drop_duplicates(key, keep="last").reset_index(drop=True)
    return out, record("last_state_only", key=key, rows_before=int(len(frame)), rows_after=int(len(out)),
                       history_lost=int(len(frame) - len(out)))
