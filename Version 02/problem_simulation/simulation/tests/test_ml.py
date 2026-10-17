"""ML evidence: numpy baselines, the stage outputs on the cached world, the checks, and the eval cases."""

from __future__ import annotations

from functools import lru_cache

import numpy as np

from simulation.ml.baselines import auc, design_matrix, fit_logistic, predict


@lru_cache(maxsize=1)
def _world() -> dict:
    from simulation.devkit import try_stage

    return try_stage("simulation.ml.stage", write=False)


def test_auc_matches_pair_count():
    y = np.array([0, 0, 1, 1, 0, 1])
    score = np.array([0.1, 0.4, 0.35, 0.8, 0.4, 0.4])
    pairs = [(p > n) + 0.5 * (p == n) for p in score[y == 1] for n in score[y == 0]]
    assert abs(auc(y, score) - np.mean(pairs)) < 1e-12


def test_logistic_learns_a_separable_signal():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(2000, 2))
    y = (x[:, 0] + 0.2 * rng.normal(size=2000) > 0).astype(float)
    model = fit_logistic(x, y)
    assert auc(y, predict(model, x)) > 0.95


def test_design_matrix_reuses_training_levels():
    import pandas as pd

    train = pd.DataFrame({"a": [1.0, 2.0], "c": ["x", "y"]})
    test = pd.DataFrame({"a": [3.0], "c": ["z"]})
    x_train, levels = design_matrix(train, ("a",), ("c",))
    x_test, _ = design_matrix(test, ("a",), ("c",), levels)
    assert x_train.shape[1] == x_test.shape[1] == 2


def test_stage_outputs_pass_checks():
    from simulation.check.ml import CHECKS

    errors: list[str] = []
    for _, check in CHECKS:
        check(_world(), errors)
    assert errors == []


def test_eval_cases_are_unique_and_tagged():
    from simulation.eval.ml_cases import cases

    built = cases(_world())
    ids = [case["case_id"] for case in built]
    assert len(ids) == len(set(ids)) and len(built) >= 35
    assert all(case["tags"]["roles"] == ["ml", "data_science"] for case in built)
    assert {case["tags"]["outcome"] for case in built} <= {"solution", "discovery"}


if __name__ == "__main__":
    test_auc_matches_pair_count()
    test_logistic_learns_a_separable_signal()
    test_design_matrix_reuses_training_levels()
    test_stage_outputs_pass_checks()
    test_eval_cases_are_unique_and_tagged()
    print("ok")
