"""Spend a full LoRA rank, even when the quota is smaller.

fit ignores the GPU quota. It turns the requested rank into a
GPU count in groups of eight, and it never asks for fewer than
one GPU. The method name on the result is lora. The rank is
returned unchanged.
"""

from __future__ import annotations


def fit(rank: int, gpus: int) -> dict:
    """Turn the rank into a LoRA GPU count and leave the quota unread.

    rank is the requested rank and is copied into the result.
    gpus is not read, so a smaller quota does not lower the
    count. The count is at least one, and it steps up by one
    GPU for each group of eight ranks. The method is lora.
    """
    # Round the rank up into groups of eight, and keep at least one GPU.
    need = max(1, (rank + 7) // 8)
    return {"gpus": need, "method": "lora", "rank": rank}
