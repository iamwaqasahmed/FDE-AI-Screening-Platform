"""Numpy-only baselines: a design matrix, logistic regression by gradient descent, and a rank AUC."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.behaviour import sigmoid


def design_matrix(frame: pd.DataFrame, numeric: tuple[str, ...], categorical: tuple[str, ...], levels: dict | None = None) -> tuple[np.ndarray, dict]:
    """Numeric columns as they are, categoricals one-hot. Pass the training levels back in for the test rows."""
    levels = levels or {column: sorted(frame[column].astype(str).unique()) for column in categorical}
    parts = [frame[list(numeric)].to_numpy(dtype=float)] if numeric else []
    for column in categorical:
        if len(levels[column]) < 2:
            continue
        values = frame[column].astype(str).to_numpy()
        parts.append(np.stack([values == level for level in levels[column][1:]], axis=1).astype(float))
    return np.hstack(parts), levels


def fit_logistic(x: np.ndarray, y: np.ndarray, steps: int = 400, rate: float = 0.5, l2: float = 1e-4) -> dict:
    mean, scale = x.mean(axis=0), x.std(axis=0)
    scale = np.where(scale > 0, scale, 1.0)
    z = (x - mean) / scale
    weights, bias = np.zeros(z.shape[1]), float(np.log((y.mean() + 1e-9) / (1 - y.mean() + 1e-9)))
    for _ in range(steps):
        error = sigmoid(z @ weights + bias) - y
        weights = weights - rate * (z.T @ error / len(y) + l2 * weights)
        bias = bias - rate * float(error.mean())
    return {"weights": weights, "bias": bias, "mean": mean, "scale": scale}


def predict(model: dict, x: np.ndarray) -> np.ndarray:
    return sigmoid(((x - model["mean"]) / model["scale"]) @ model["weights"] + model["bias"])


def auc(y: np.ndarray, score: np.ndarray) -> float:
    """Mann-Whitney AUC with average ranks for ties."""
    y = np.asarray(y).astype(bool)
    positives, negatives = int(y.sum()), int((~y).sum())
    if not positives or not negatives:
        return float("nan")
    order = np.argsort(score, kind="mergesort")
    ranks = np.empty(len(score))
    ranks[order] = np.arange(1, len(score) + 1)
    _, inverse, counts = np.unique(score, return_inverse=True, return_counts=True)
    sums = np.bincount(inverse, weights=ranks)
    ranks = (sums / counts)[inverse]
    return float((ranks[y].sum() - positives * (positives + 1) / 2) / (positives * negatives))


def fit_and_score(train: pd.DataFrame, test: pd.DataFrame, label: str, numeric: tuple[str, ...], categorical: tuple[str, ...]) -> float:
    x_train, levels = design_matrix(train, numeric, categorical)
    x_test, _ = design_matrix(test, numeric, categorical, levels)
    model = fit_logistic(x_train, train[label].to_numpy(dtype=float))
    return round(auc(test[label].to_numpy(), predict(model, x_test)), 4)
