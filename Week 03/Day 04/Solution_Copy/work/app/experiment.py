"""Report the pre-registered metric and its winning arm.

The protocol names the metric. Each arm is scored by dividing that
metric's count by n. The report names the metric and the arm whose
rate is highest. When rates tie, the earliest arm in the counts is
the winner.
"""

from __future__ import annotations


def report(protocol: dict) -> dict:
    """Return the protocol metric and the arm with the highest rate.

    protocol has a metric name and a counts map. Each arm in counts
    has a value for that metric and an n. The rate is the metric
    count divided by n.
    """
    # The metric name comes from the protocol. Another field is not substituted.
    metric = protocol["metric"]
    # The rate is that metric divided by n, once per arm.
    rates = {arm: row[metric] / row["n"] for arm, row in protocol["counts"].items()}
    # The higher rate on that metric is the arm this report returns.
    winner = max(rates, key=rates.get)
    return {"metric": metric, "winner": winner}
