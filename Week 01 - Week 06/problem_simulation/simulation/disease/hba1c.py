"""HbA1c trajectory per person and year, in mmol/mol. The lab feed reports these values."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import HISTORY_START, SNAPSHOT

YEARS = list(range(HISTORY_START.year, SNAPSHOT.year + 1))


def build_hba1c(people: pd.DataFrame, rng: np.random.Generator) -> np.ndarray:
    """Rows follow people order, columns follow YEARS."""
    count = len(people)
    type1 = people["diabetes_type"].eq("Type 1").to_numpy()
    base = np.where(type1, rng.normal(66, 13, count), rng.normal(56, 11, count))
    steps = rng.normal(0.0, 3.0, size=(count, len(YEARS)))
    steps[:, 0] = 0.0
    trend = np.cumsum(steps, axis=1)
    values = base[:, None] + trend
    return np.clip(values, 36, 130).round(0)


def to_frame(people: pd.DataFrame, values: np.ndarray) -> pd.DataFrame:
    frame = pd.DataFrame(values, columns=[str(year) for year in YEARS])
    frame.insert(0, "person_uid", people["person_uid"].to_numpy())
    return frame.melt(id_vars="person_uid", var_name="year", value_name="hba1c_mmol_mol")


def on_dates(values: np.ndarray, rows: np.ndarray, dates: pd.Series) -> np.ndarray:
    columns = pd.to_datetime(dates).dt.year.to_numpy() - YEARS[0]
    columns = np.clip(columns, 0, len(YEARS) - 1)
    return values[rows, columns]
