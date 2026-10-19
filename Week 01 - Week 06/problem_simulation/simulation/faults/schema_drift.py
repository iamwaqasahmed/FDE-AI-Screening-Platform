"""One partition of an export uses a newer schema: renamed columns and new ones."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: renames {old: new}, added {column: default}, version, partition (label for the record)."""
    renames = dict(params.get("renames", {}))
    out = frame.rename(columns=renames)
    for column, default in params.get("added", {}).items():
        out[column] = default
    return out, record(
        "schema_drift", partition=params.get("partition", ""), version=params.get("version", ""),
        renames=renames, added=sorted(params.get("added", {})), rows=int(len(out)),
    )
