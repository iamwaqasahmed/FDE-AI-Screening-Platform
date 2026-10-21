"""Values before a change date are reported in an older unit. The frame arrives in the new unit."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: date (ISO string column), value, unit, change_on (date), before_unit, after_unit, to_before (callable), decimals."""
    change_on: date = params["change_on"]
    before = frame[params["date"]] < change_on.isoformat()
    out = frame.copy()
    converted = params["to_before"](out[params["value"]].to_numpy(dtype=float))
    out[params["value"]] = np.where(before, np.round(converted, params.get("decimals", 1)), out[params["value"]])
    out[params["unit"]] = np.where(before, params["before_unit"], params["after_unit"])
    return out, record(
        "unit_change", column=params["value"], change_on=change_on.isoformat(), rows_before=int(before.sum()),
        before_unit=params["before_unit"], after_unit=params["after_unit"],
    )
