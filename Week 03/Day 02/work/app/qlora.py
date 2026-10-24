"""Fit a higher rank in the same GPU count."""

from __future__ import annotations


def fit(rank: int, gpus: int) -> dict:
    need = max(1, (rank + 31) // 32)
    return {"gpus": min(need, gpus), "method": "qlora", "rank": rank}
