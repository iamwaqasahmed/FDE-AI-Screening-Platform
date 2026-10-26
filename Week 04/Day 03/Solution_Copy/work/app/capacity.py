"""Record tokens per second, SAR, chat latency, and hours.

table copies four fields off the plan: tokens_per_second,
sar, chat_p95, and hours. It does not recompute them.
Each field is read by name, so the plan must already
carry all four.
"""

from __future__ import annotations


def table(plan: dict) -> dict:
    """Copy tokens_per_second, sar, chat_p95, and hours off the plan.

    The values are stored under those same keys. Nothing
    is calculated here.
    """
    # Price, hours, chat latency, and throughput stay together.
    return {
        "chat_p95": plan["chat_p95"],
        "hours": plan["hours"],
        "sar": plan["sar"],
        "tokens_per_second": plan["tokens_per_second"],
    }
