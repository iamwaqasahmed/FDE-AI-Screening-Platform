"""Report the pre-registered metric and its winning arm."""

from __future__ import annotations


def report(protocol: dict) -> dict:
    metric = protocol["metric"]
    rates = {arm: row[metric] / row["n"] for arm, row in protocol["counts"].items()}
    winner = max(rates, key=rates.get)
    return {"metric": metric, "winner": winner}
