"""Price sheet. External tokens cost more than local tokens. Buying costs more than renting.

Every amount is drawn from the seed. The external token price is the local price plus a further draw. The buy price is the rent price times a further draw. The other keys are independent draws. Values are stored as strings under the sar field.
"""

from __future__ import annotations

import random


def price_rows(seed: int) -> list[dict[str, str]]:
    """Return the price keys and their amounts as strings, in sheet order."""
    # One generator for this seed, so the same seed always prints the same sheet.
    rng = random.Random(seed)
    # The external token price is the local price plus a further draw.
    local = rng.randint(2, 6)
    external = local + rng.randint(8, 24)
    # The buy price is the rent price times a further draw.
    rent = rng.randint(30, 90)
    buy = rent * rng.randint(500, 800)
    # Sheet order. Rent, buy, and the two token prices reuse the draws above.
    pairs = (
        ("cost.slot_missed", rng.randint(400, 900)),
        ("cost.return_cycle", rng.randint(120, 280)),
        ("cost.coordinator_hour", rng.randint(45, 110)),
        ("cost.call_minute", rng.randint(3, 8)),
        ("cost.sms", rng.randint(1, 3)),
        ("cost.wa_template", rng.randint(1, 4)),
        ("cost.label", rng.randint(2, 7)),
        ("cost.gpu_hour_rent", rent),
        ("cost.gpu_buy", buy),
        ("price.ext_large_per_1k", external),
        ("price.local_per_1k", local),
        ("harm.week_waiting", rng.randint(50, 150)),
    )
    # Store each amount as a string under the sar field.
    return [{"key": key, "sar": str(value)} for key, value in pairs]


PRICE_FIELDS = ("key", "sar")
