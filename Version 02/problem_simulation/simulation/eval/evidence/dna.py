"""The analyst's random split against the honest one, on the did-not-attend table."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.eval.evidence.bars import DNA_SEED, HOLDOUT_PEOPLE, TEMPORAL_CUTOFF
from simulation.ml.baselines import fit_and_score
from simulation.ml.dna_table import CATEGORICAL, GROUP_COLUMN, LABEL, LEAKY_FEATURE, NUMERIC, TIME_COLUMN


def scores(table: pd.DataFrame) -> dict:
    frame = _prepare(table)
    rng = np.random.default_rng(DNA_SEED)
    random_auc = _random(frame, rng)
    honest_auc = _honest(frame, rng)
    return {
        "leaky_feature": LEAKY_FEATURE,
        "group_column": GROUP_COLUMN,
        "seed": DNA_SEED,
        "temporal_cutoff": TEMPORAL_CUTOFF,
        "random_auc": random_auc,
        "honest_auc": honest_auc,
        "inflation": round(random_auc - honest_auc, 4),
        "has_dob": any(column.lower() in {"dob", "date_of_birth"} for column in frame.columns),
        "age_is_derived": "age" in frame.columns and "dob" not in frame.columns,
    }


def _prepare(table: pd.DataFrame) -> pd.DataFrame:
    frame = table.copy()
    for column in NUMERIC:
        frame[column] = pd.to_numeric(frame[column], errors="coerce").fillna(0.0)
    for column in (*CATEGORICAL, GROUP_COLUMN, TIME_COLUMN, LEAKY_FEATURE):
        frame[column] = frame[column].astype(str)
    frame[LABEL] = pd.to_numeric(frame[LABEL], errors="coerce").fillna(0).astype(int)
    return frame


def _random(frame: pd.DataFrame, rng: np.random.Generator) -> float:
    order = rng.permutation(len(frame))
    cut = int(0.8 * len(frame))
    train, test = frame.iloc[order[:cut]], frame.iloc[order[cut:]]
    return fit_and_score(train, test, LABEL, NUMERIC, (*CATEGORICAL, LEAKY_FEATURE))


def _honest(frame: pd.DataFrame, rng: np.random.Generator) -> float:
    people = np.array(sorted(frame[GROUP_COLUMN].unique()), dtype=object)
    held = set(people[rng.random(len(people)) < HOLDOUT_PEOPLE])
    later = frame[TIME_COLUMN].ge(TEMPORAL_CUTOFF)
    train = frame[~frame[GROUP_COLUMN].isin(held) & ~later]
    test = frame[frame[GROUP_COLUMN].isin(held) & later]
    return fit_and_score(train, test, LABEL, NUMERIC, CATEGORICAL)
