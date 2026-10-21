"""Which grader read each photograph, and where in the session it fell."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.workforce.graders import ROSTER


def assign_graders(served_days: np.ndarray, hours: pd.DataFrame, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    graders = [grader.grader_id for grader in ROSTER]
    matrix = hours[graders].to_numpy()
    chosen = np.full(len(served_days), "", dtype=object)
    position = rng.random(len(served_days))
    valid = served_days >= 0
    safe = np.clip(served_days, 0, len(matrix) - 1)
    weights = matrix[safe]
    totals = weights.sum(axis=1)
    fallback = totals <= 0
    weights[fallback] = 1.0
    cumulative = np.cumsum(weights, axis=1)
    roll = rng.random(len(served_days)) * cumulative[:, -1]
    picks = (cumulative < roll[:, None]).sum(axis=1)
    chosen[valid] = np.array(graders, dtype=object)[np.clip(picks[valid], 0, len(graders) - 1)]
    return chosen, position.round(3)


def initials_for(grader_ids: pd.Series) -> np.ndarray:
    lookup = {grader.grader_id: grader.initials for grader in ROSTER}
    return grader_ids.map(lookup).fillna("").to_numpy()
