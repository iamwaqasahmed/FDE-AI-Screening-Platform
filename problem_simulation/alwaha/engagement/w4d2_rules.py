"""Reference decisions for rel-w4d2.
Participant copies do not import this module.

board summarizes a trace without counting the alert as a call. serve changes the hours only when the circular itself changed. reply returns the registered text. promote returns a candidate hash only after a comparison matched.
"""

from __future__ import annotations

from datetime import datetime

from alwaha.engagement.w4d2_rows import CIRCULAR, SLO_MINUTES

_LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}


def _p95(values: list[int]) -> int:
    """Return a high percentile of the values. An empty list returns nothing.

    The rank is kept inside the list: the usual percentile index, then one step back because the list is indexed from the start.
    """
    ordered = sorted(values)
    # No samples means there is no percentile to report.
    if not ordered:
        return 0
    rank = (95 * len(ordered) + 99) // 100
    return ordered[rank - 1]


def read_span(span: dict) -> dict:
    """Return the hash, token count, and tool, using an empty hash, a zero count, or an empty tool when the span omits them."""
    return {"hash": span.get("hash") or "", "tokens": int(span.get("tokens") or 0), "tool": span.get("tool") or ""}


def board(spans: list[dict]) -> dict:
    """Return the alert time, the error rate, the latency percentile, and the tool-failure count.

    The alert span is the signal, not one of the calls being measured, so it is left out of the rate and the latency. An error with no tool name is not counted as a tool failure. An empty trace has no error rate.
    """
    # The alert is excluded so it is not counted as a slow or failed call.
    body = [span for span in spans if span.get("name") != "alert"]
    latencies = [int(span.get("latency_ms") or 0) for span in body]
    errors = [span for span in body if span.get("status") == "error"]
    # An error that names no tool is not a tool failure.
    tools = [span for span in errors if span.get("tool")]
    alert = next(span.get("at") for span in spans if span.get("name") == "alert")
    return {
        "alert_at": alert,
        # An empty trace has no error rate. It is not treated as a clean trace.
        "error_rate": (len(errors) / len(body)) if body else 0.0,
        "latency_p95": _p95(latencies),
        "tool_failures": len(tools),
    }


def within_slo(first: str, alert: str, minutes: int = SLO_MINUTES) -> bool:
    """Return whether the alert landed inside the window after the first error.

    An alert timestamp before the error is not a valid page, and a late alert is outside the window.
    """
    delta = (datetime.fromisoformat(alert) - datetime.fromisoformat(first)).total_seconds() / 60
    # Late is outside the window, and a negative gap means the alert predates the error.
    return 0 <= delta <= minutes


def cost(rows: list[dict]) -> dict[str, int]:
    """Return the cost totaled by hospital. Rows for the same hospital add together.

    The steps add each row's amount into a total for that hospital, and the hidden figures stay in this file and are not copied into a new comment.
    """
    totals: dict[str, int] = {}
    for row in rows:
        hospital = str(row["hospital"])
        totals[hospital] = totals.get(hospital, 0) + int(row["sar"])
    return totals


def rate(rows: list[dict]) -> float:
    """Return the share of rows that were stamped. No rows scores as nothing."""
    # An empty list is not a fully stamped run.
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)


def label(row: dict) -> str:
    """Return the drift phrase for this kind. An unknown kind is an error."""
    return _LABELS[str(row.get("kind"))]


def serve(store: dict, event: dict) -> str:
    """Return the hours to serve after this event.

    Only a change to the hours circular replaces what is served. Any other event leaves the stored hours in place.
    """
    # Only a change to this circular replaces the hours. A different document must not.
    if event.get("topic") == "document.changed" and event.get("doc_id") == CIRCULAR:
        return str(event.get("body") or "")
    return str(store.get("hours") or "")


def reply(turn: dict) -> str:
    """Return the registered reply. The shadow reply is never what this function serves."""
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict) -> str:
    """Return the candidate hash only when a comparison ran and matched. Otherwise return an empty hash."""
    # An uncompared or unmatched candidate is not promoted.
    if comparison.get("compared") and comparison.get("matched"):
        return str(comparison.get("candidate_hash") or "")
    return ""
