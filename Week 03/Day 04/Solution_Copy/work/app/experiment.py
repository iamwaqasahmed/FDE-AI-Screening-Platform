"""Report the pre-registered metric and its winning arm."""

from __future__ import annotations


def report(protocol: dict) -> dict:
    # The metric name comes from the protocol. Another field is not substituted.
    metric = protocol["metric"]
    # The rate is that metric divided by n, once per arm.
    rates = {arm: row[metric] / row["n"] for arm, row in protocol["counts"].items()}
    # The higher rate on that metric is the arm this report returns.
    winner = max(rates, key=rates.get)
    return {"metric": metric, "winner": winner}
