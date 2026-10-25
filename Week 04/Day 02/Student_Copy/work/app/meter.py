"""Cost for one hospital."""

from __future__ import annotations


def cost(rows: list[dict]) -> dict:
    total = sum(int(row["sar"]) for row in rows if row.get("hospital") == "h-wadi")
    return {"h-wadi": total}
