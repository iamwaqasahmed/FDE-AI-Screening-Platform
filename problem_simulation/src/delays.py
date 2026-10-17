"""Delay samples whose median is exact."""

from __future__ import annotations

import numpy as np


def sample_delays(n: int, target: int, rng: np.random.Generator, high: int = 120) -> np.ndarray:
    """Return n positive day counts whose median is exactly target."""
    if n < 1:
        raise ValueError("Need at least one delay.")
    if n % 2 == 0:
        n_left = n // 2 - 1
        n_mid = 2
        n_right = n // 2 - 1
    else:
        n_left = n // 2
        n_mid = 1
        n_right = n // 2
    left = rng.integers(1, target + 1, size=n_left)
    right = rng.integers(target, high + 1, size=n_right)
    mid = np.full(n_mid, target, dtype=int)
    return np.concatenate([left, mid, right])
