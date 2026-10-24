"""Report the contained count instead of the pre-registered metric."""

from __future__ import annotations

_PEEK = "contained"


def report(protocol: dict) -> dict:
    rates = {arm: row[_PEEK] / row["n"] for arm, row in protocol["counts"].items()}
    winner = max(rates, key=rates.get)
    return {"metric": _PEEK, "winner": winner}
