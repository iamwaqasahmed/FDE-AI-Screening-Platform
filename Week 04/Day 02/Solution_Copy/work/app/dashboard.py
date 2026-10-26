"""Latency, errors, tool failures, and the alert span.

board separates the alert span from the body. The body is every span
whose name is not alert. latency_p95 is a high percentile of the body
latency values, with a missing latency read as zero. error_rate is the
share of body spans whose status is error, or zero when the body is
empty. tool_failures counts error spans that name a tool. An empty tool
does not count. alert_at is the at value of the alert span. The search
assumes that span is present.
"""

from __future__ import annotations


def _p95(values: list[int]) -> int:
    """Return the latency at the rank computed from the list length.

    An empty list returns zero. The values are sorted first. The rank
    expression lives in the body, and the selected slot is that rank
    minus one.
    """
    # Sort a copy. The caller's list order is left as it arrived.
    ordered = sorted(values)
    # An empty body has no latency to rank.
    if not ordered:
        return 0
    # One-based rank into the sorted list. The return below selects that slot.
    rank = (95 * len(ordered) + 99) // 100
    return ordered[rank - 1]


def board(spans: list[dict]) -> dict:
    """Summarize the body spans and record when the alert span fired.

    The result keys are alert_at, error_rate, latency_p95, and
    tool_failures. error_rate divides the error count by the body length
    when the body is not empty.
    """
    # The alert span is kept out of the latency, error, and tool counts.
    body = [span for span in spans if span.get("name") != "alert"]
    latencies = [int(span.get("latency_ms") or 0) for span in body]
    errors = [span for span in body if span.get("status") == "error"]
    # An error with a missing or empty tool is an error, not a tool failure.
    tools = [span for span in errors if span.get("tool")]
    # The first alert span supplies the time. A missing alert span raises.
    alert = next(span.get("at") for span in spans if span.get("name") == "alert")
    return {
        "alert_at": alert,
        "error_rate": (len(errors) / len(body)) if body else 0.0,
        "latency_p95": _p95(latencies),
        "tool_failures": len(tools),
    }
