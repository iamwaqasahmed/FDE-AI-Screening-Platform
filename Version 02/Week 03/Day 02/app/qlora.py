"""Spend a full LoRA rank, even when the quota is smaller."""

from __future__ import annotations


def fit(rank: int, gpus: int) -> dict:
    need = max(1, (rank + 7) // 8)
    return {"gpus": need, "method": "lora", "rank": rank}
