"""Latency, errors, tool failures, and the alert span."""

from __future__ import annotations


def _p95(values: list[int]) -> int:
    ordered = sorted(values)
    if not ordered:
        return 0
    rank = (95 * len(ordered) + 99) // 100
    return ordered[rank - 1]


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
