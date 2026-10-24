"""Sum gateway cost by hospital."""

from __future__ import annotations


def cost(rows: list[dict]) -> dict:
    totals: dict[str, int] = {}
    for row in rows:
        hospital = str(row["hospital"])
        totals[hospital] = totals.get(hospital, 0) + int(row["sar"])
    return totals
