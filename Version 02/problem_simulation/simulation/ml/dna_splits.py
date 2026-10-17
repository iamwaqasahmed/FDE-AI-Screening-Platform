"""The analyst's random split against the honest one: people held out whole, and the test cycles after the training cycles."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.ml.baselines import fit_and_score
from simulation.ml.dna_table import CATEGORICAL, GROUP_COLUMN, LABEL, LEAKY_FEATURE, NUMERIC, TIME_COLUMN

TEST_SHARE = 0.2
HOLDOUT_PEOPLE = 0.3
TEMPORAL_CUTOFF = "2024-10-01"


def random_split(table: pd.DataFrame, rng: np.random.Generator) -> tuple[pd.DataFrame, pd.DataFrame]:
    test = rng.random(len(table)) < TEST_SHARE
    return table[~test], table[test]


def honest_split(table: pd.DataFrame, rng: np.random.Generator) -> tuple[pd.DataFrame, pd.DataFrame]:
    people = np.array(sorted(table[GROUP_COLUMN].unique()), dtype=object)
    held = set(people[rng.random(len(people)) < HOLDOUT_PEOPLE])
    in_test_people = table[GROUP_COLUMN].isin(held).to_numpy()
    later = (table[TIME_COLUMN] >= TEMPORAL_CUTOFF).to_numpy()
    return table[~in_test_people & ~later], table[in_test_people & later]


def run_baselines(table: pd.DataFrame, rng: np.random.Generator) -> dict:
    leaky = (CATEGORICAL + (LEAKY_FEATURE,))
    random_train, random_test = random_split(table, rng)
    honest_train, honest_test = honest_split(table, rng)
    shared = set(random_train[GROUP_COLUMN]) & set(random_test[GROUP_COLUMN])
    results = {
        "random_split_with_leak_auc": fit_and_score(random_train, random_test, LABEL, NUMERIC, leaky),
        "random_split_without_leak_auc": fit_and_score(random_train, random_test, LABEL, NUMERIC, CATEGORICAL),
        "honest_split_with_leak_auc": fit_and_score(honest_train, honest_test, LABEL, NUMERIC, leaky),
        "honest_split_without_leak_auc": fit_and_score(honest_train, honest_test, LABEL, NUMERIC, CATEGORICAL),
    }
    results["leak_inflation"] = round(results["random_split_with_leak_auc"] - results["honest_split_without_leak_auc"], 4)
    results.update(
        leaky_feature=LEAKY_FEATURE,
        group_column=GROUP_COLUMN,
        temporal_cutoff=TEMPORAL_CUTOFF,
        random_test_people_also_in_train=round(len(shared) / max(random_test[GROUP_COLUMN].nunique(), 1), 4),
        rows={"random_train": len(random_train), "random_test": len(random_test), "honest_train": len(honest_train), "honest_test": len(honest_test)},
        features=list(NUMERIC + CATEGORICAL),
        model="logistic regression, full-batch gradient descent, standardised features",
    )
    return results
