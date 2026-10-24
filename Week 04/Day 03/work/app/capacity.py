"""Record tokens per second, SAR, chat latency, and hours."""

from __future__ import annotations


def table(plan: dict) -> dict:
    return {
        "chat_p95": plan["chat_p95"],
        "hours": plan["hours"],
        "sar": plan["sar"],
        "tokens_per_second": plan["tokens_per_second"],
    }
