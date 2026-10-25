"""Charge nothing for the fix."""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    del count, price, budget_sar
    return 0
