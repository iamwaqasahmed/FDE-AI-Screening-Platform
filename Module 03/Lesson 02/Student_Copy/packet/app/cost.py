"""Price the token count on ext-large.

quote reads the ext-large rate, divides the token count by one
thousand, and multiplies. The model name on the quote is
ext-large. The latency on the quote is one second. The cap
limits are not read.
"""

from __future__ import annotations


def quote(cap: dict, prices: dict) -> dict:
    """Price the cap's tokens with the ext-large per-thousand rate.

    cap supplies the token count. prices supplies the rate stored
    under the ext-large key. The local rate is not read. The
    result names ext-large and sets the latency to one second.
    """
    # The rate is stored as text. int() makes it a number.
    rate = int(prices["price.ext_large_per_1k"])
    # The token count is billed per thousand.
    sar = cap["tokens"] / 1000 * rate
    return {"model": "ext-large", "sar": sar, "seconds": 1}
