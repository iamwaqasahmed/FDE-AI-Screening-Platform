"""Price the token count on local-small.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell prices the token count on ext-large. While that shell is
the file that runs, the model check says the cost is over the price
cap. The check does not print a price. slice-lora says ext-large at
the price cap does not clear the slice when that model is still
inside the cap.
"""

from __future__ import annotations


def quote(cap: dict, prices: dict) -> dict:
    """Price cap tokens on the local rate and keep the latency inside the cap.

    cap carries tokens. prices carries the two per-thousand rates.
    The local rate is the one this quote uses. seconds stays at 1,
    which the cap file allows.
    """
    rate = int(prices["price.local_per_1k"])
    sar = cap["tokens"] / 1000 * rate
    return {"model": "local-small", "sar": sar, "seconds": 1}
