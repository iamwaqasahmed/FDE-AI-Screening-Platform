"""Rows are written in arrival order, not event order."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: arrival (column that decides file order), event (column the reader expects to be ordered), drop (bool)."""
    arrival, event = params["arrival"], params["event"]
    out = frame.sort_values([arrival, event], kind="stable").reset_index(drop=True)
    share = inversion_share(out[event])
    if params.get("drop", False):
        out = out.drop(columns=[arrival])
    return out, record("out_of_order", arrival=arrival, event=event, rows=int(len(out)), inverted_share=round(share, 4))


def inversion_share(values: pd.Series) -> float:
    """Share of rows whose event time is earlier than the latest event time already seen."""
    if len(values) < 2:
        return 0.0
    array = values.to_numpy()
    running = np.maximum.accumulate(array)
    return float((array[1:] < running[:-1]).mean())
