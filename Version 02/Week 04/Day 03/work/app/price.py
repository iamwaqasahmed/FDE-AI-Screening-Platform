"""Price the batch at today's external rate."""

from __future__ import annotations


def rate(today: dict, yesterday: dict) -> int:
    del yesterday
    return int(today["sar"])
