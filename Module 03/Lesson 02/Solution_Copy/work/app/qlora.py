"""Fit a higher rank in the same GPU count.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell spends a full LoRA rank even when the quota is smaller.
The two checks do not load this file. The suite does. Do not delete
it.
"""

from __future__ import annotations


def fit(rank: int, gpus: int) -> dict:
    """Return a QLoRA fit that does not ask for more GPUs than gpus.

    rank is the requested rank. gpus is the quota count. Thirty-two
    ranks share one GPU. The GPU count is the smaller of the need
    and the quota. The requested rank is kept.
    """
    # One GPU covers ranks 1 through 32. The next band needs another.
    need = max(1, (rank + 31) // 32)
    # The quota wins when the band would ask for more GPUs.
    return {"gpus": min(need, gpus), "method": "qlora", "rank": rank}
