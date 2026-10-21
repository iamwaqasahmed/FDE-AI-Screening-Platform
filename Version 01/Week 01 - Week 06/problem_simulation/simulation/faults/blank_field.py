"""A field is left empty on a share of rows."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: column, share, key (optional id column for the record)."""
    column = params["column"]
    hit = rng.random(len(frame)) < float(params["share"])
    out = frame.copy()
    out[column] = np.where(hit, "", out[column].astype(str))
    key = params.get("key", "")
    keys = sorted(out.loc[hit, key].astype(str).tolist()) if key else []
    return out, record("blank_field", column=column, rows=int(hit.sum()), share=float(params["share"]), keys=keys[:50])
