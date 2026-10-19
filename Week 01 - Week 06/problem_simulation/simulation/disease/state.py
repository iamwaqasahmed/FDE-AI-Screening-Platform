"""Read the latent state on any date: worse-eye retinopathy level and maculopathy."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.disease.progression import EYES


class DiseaseIndex:
    def __init__(self, disease: pd.DataFrame) -> None:
        self.row = pd.Series(np.arange(len(disease)), index=disease["person_uid"].to_numpy())
        self.columns = {}
        for eye in EYES:
            for name in ("r1_on", "r2_on", "r3_on", "m1_on"):
                values = disease[f"{eye}_{name}"].replace("", "9999-12-31").to_numpy(dtype="U10")
                self.columns[(eye, name)] = values

    def level(self, person_uids: pd.Series, dates: pd.Series) -> tuple[np.ndarray, np.ndarray]:
        rows = self.row.reindex(person_uids.to_numpy()).to_numpy()
        on = dates.fillna("").to_numpy(dtype="U10")
        worst = np.zeros(len(rows), dtype=int)
        macula = np.zeros(len(rows), dtype=bool)
        valid = ~pd.isna(rows) & (on != "")
        safe_rows = np.where(valid, rows, 0).astype(int)
        for eye in EYES:
            eye_level = np.zeros(len(rows), dtype=int)
            for step, name in enumerate(("r1_on", "r2_on", "r3_on"), start=1):
                reached = self.columns[(eye, name)][safe_rows] <= on
                eye_level = np.where(reached, step, eye_level)
            worst = np.maximum(worst, eye_level)
            macula |= self.columns[(eye, "m1_on")][safe_rows] <= on
        worst = np.where(valid, worst, -1)
        macula = macula & valid
        return worst, macula


def referable(level: np.ndarray, macula: np.ndarray) -> np.ndarray:
    return (level >= 2) | macula
