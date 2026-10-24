"""Price the token count on local-small."""

from __future__ import annotations


def quote(cap: dict, prices: dict) -> dict:
    rate = int(prices["price.local_per_1k"])
    sar = cap["tokens"] / 1000 * rate
    return {"model": "local-small", "sar": sar, "seconds": 1}
