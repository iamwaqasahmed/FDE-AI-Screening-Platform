"""Codes are renumbered from a date. Rows on or after the date carry the new code."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: column, mapping {old: new}, date (ISO string column), from_on (date), names (optional {new: name}, name_column)."""
    column, mapping = params["column"], dict(params["mapping"])
    after = frame[params["date"]] >= params["from_on"].isoformat()
    out = frame.copy()
    out[column] = np.where(after, out[column].map(mapping).fillna(out[column]), out[column])
    names, name_column = params.get("names", {}), params.get("name_column", "")
    if names and name_column:
        out[name_column] = np.where(after, out[column].map(names).fillna(out[name_column]), out[name_column])
    return out, record("recode", column=column, from_on=params["from_on"].isoformat(), rows=int(after.sum()),
                       mapping=dict(sorted(mapping.items())))
