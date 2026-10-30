"""Reference decisions for rel-m04-l03.
Participant copies do not import this module.

hours_for and batch_sar turn a throughput or a price into the backlog's duration and cost. started_at subtracts the cold start from the peak. target keeps identified text on a local adapter. answer serves a stored body without a new model call.
"""

from __future__ import annotations

from datetime import datetime, timedelta

from alwaha.engagement.m04_l03_rows import BACKLOG, TOKENS_PER_REFERRAL


def hours_for(tps: int, referrals: int = BACKLOG, tokens_each: int = TOKENS_PER_REFERRAL) -> float:
    """Return how many hours the backlog takes at this token rate.

    The defaults are the campaign backlog and its tokens per referral. The result is rounded so two equal rates print the same.
    """
    return round(referrals * tokens_each / tps / 3600, 4)


def batch_sar(price_per_1k: int, referrals: int = BACKLOG, tokens_each: int = TOKENS_PER_REFERRAL) -> int:
    """Return the integer cost of the backlog at this price per token block.

    The defaults match hours_for, so a duration and a cost describe the same backlog.
    """
    return price_per_1k * referrals * tokens_each // 1000


def started_at(peak: str, cold: int) -> str:
    """Return the time the model must start so the cold start is finished at the peak."""
    return (datetime.fromisoformat(peak) - timedelta(seconds=cold)).isoformat()


def approved(registry: dict) -> list[str]:
    """Return the sorted ids of approved adapters whose base is the local model.

    An approved model with a different base is not in this list.
    """
    names = [
        str(row["id"])
        for row in registry.get("models") or []
        if row.get("status") == "approved" and row.get("base") == "local-small"
    ]
    return sorted(names)


def target(row: dict) -> str:
    """Return which model should serve this row.

    A row marked with the clinical flag stays on its named adapter, or the local adapter when it names none. A row without that flag goes to the external model.
    """
    # Clinical text stays on a local adapter. The fallback name is the local one, not the external one.
    if row.get("phi"):
        return str(row.get("adapter") or "lora-local")
    return "ext-large"


def answer(store: dict, row: dict) -> dict:
    """Return the body and how many model calls it took.

    A stored id is served from the store and records no call. A miss returns the row text and records one call.
    """
    key = str(row.get("id") or "")
    # A repeated public id is served from the store and does not call the model again.
    if key in store:
        return {"body": str(store[key]), "calls": 0}
    return {"body": str(row.get("text") or ""), "calls": 1}


def plan(sheet: dict, forecast: dict, today_price: int) -> dict:
    """Return the chat latency, the batched hours, the cost at today's price, and the batched speed.

    The hours and the cost use the forecast's backlog and the sheet's tokens per referral, not the module defaults, so a different forecast changes both.
    """
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    tps = int(sheet["local_batched_tps"])
    return {
        "chat_p95": int(sheet["chat_p95_reserved_ms"]),
        "hours": hours_for(tps, referrals, tokens_each),
        "sar": batch_sar(today_price, referrals, tokens_each),
        "tokens_per_second": tps,
    }
