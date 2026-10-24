"""Price the token count on ext-large."""

from __future__ import annotations


def quote(cap: dict, prices: dict) -> dict:
    rate = int(prices["price.ext_large_per_1k"])
    sar = cap["tokens"] / 1000 * rate
    return {"model": "ext-large", "sar": sar, "seconds": 1}
