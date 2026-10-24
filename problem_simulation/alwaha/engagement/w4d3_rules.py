"""Reference decisions for rel-w4d3. Participant copies do not import this module."""

from __future__ import annotations

from datetime import datetime, timedelta

from alwaha.engagement.w4d3_rows import BACKLOG, TOKENS_PER_REFERRAL


def hours_for(tps: int, referrals: int = BACKLOG, tokens_each: int = TOKENS_PER_REFERRAL) -> float:
    return round(referrals * tokens_each / tps / 3600, 4)


def batch_sar(price_per_1k: int, referrals: int = BACKLOG, tokens_each: int = TOKENS_PER_REFERRAL) -> int:
    return price_per_1k * referrals * tokens_each // 1000


def started_at(peak: str, cold: int) -> str:
    return (datetime.fromisoformat(peak) - timedelta(seconds=cold)).isoformat()


def approved(registry: dict) -> list[str]:
    names = [
        str(row["id"])
        for row in registry.get("models") or []
        if row.get("status") == "approved" and row.get("base") == "local-small"
    ]
    return sorted(names)


def target(row: dict) -> str:
    if row.get("phi"):
        return str(row.get("adapter") or "lora-local")
    return "ext-large"


def answer(store: dict, row: dict) -> dict:
    key = str(row.get("id") or "")
    if key in store:
        return {"body": str(store[key]), "calls": 0}
    return {"body": str(row.get("text") or ""), "calls": 1}


def plan(sheet: dict, forecast: dict, today_price: int) -> dict:
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    tps = int(sheet["local_batched_tps"])
    return {
        "chat_p95": int(sheet["chat_p95_reserved_ms"]),
        "hours": hours_for(tps, referrals, tokens_each),
        "sar": batch_sar(today_price, referrals, tokens_each),
        "tokens_per_second": tps,
    }
