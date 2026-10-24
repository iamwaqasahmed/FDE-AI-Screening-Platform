"""Reference decisions for rel-w4d2. Participant copies do not import this module."""

from __future__ import annotations

from datetime import datetime

from alwaha.engagement.w4d2_rows import CIRCULAR, SLO_MINUTES

_LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}


def _p95(values: list[int]) -> int:
    ordered = sorted(values)
    if not ordered:
        return 0
    rank = (95 * len(ordered) + 99) // 100
    return ordered[rank - 1]


def read_span(span: dict) -> dict:
    return {"hash": span.get("hash") or "", "tokens": int(span.get("tokens") or 0), "tool": span.get("tool") or ""}


def board(spans: list[dict]) -> dict:
    body = [span for span in spans if span.get("name") != "alert"]
    latencies = [int(span.get("latency_ms") or 0) for span in body]
    errors = [span for span in body if span.get("status") == "error"]
    tools = [span for span in errors if span.get("tool")]
    alert = next(span.get("at") for span in spans if span.get("name") == "alert")
    return {
        "alert_at": alert,
        "error_rate": (len(errors) / len(body)) if body else 0.0,
        "latency_p95": _p95(latencies),
        "tool_failures": len(tools),
    }


def within_slo(first: str, alert: str, minutes: int = SLO_MINUTES) -> bool:
    delta = (datetime.fromisoformat(alert) - datetime.fromisoformat(first)).total_seconds() / 60
    return 0 <= delta <= minutes


def cost(rows: list[dict]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for row in rows:
        hospital = str(row["hospital"])
        totals[hospital] = totals.get(hospital, 0) + int(row["sar"])
    return totals


def rate(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)


def label(row: dict) -> str:
    return _LABELS[str(row.get("kind"))]


def serve(store: dict, event: dict) -> str:
    if event.get("topic") == "document.changed" and event.get("doc_id") == CIRCULAR:
        return str(event.get("body") or "")
    return str(store.get("hours") or "")


def reply(turn: dict) -> str:
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict) -> str:
    if comparison.get("compared") and comparison.get("matched"):
        return str(comparison.get("candidate_hash") or "")
    return ""
