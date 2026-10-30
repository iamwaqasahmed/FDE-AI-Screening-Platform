"""Report the batched rate and the hours it needs.

rate reads local_batched_tps from the sheet. hours turns
the forecast backlog into hours at that rate: referrals
times tokens per referral, divided by the rate, divided
by 3600, then rounded to 4 decimal places.
"""

from __future__ import annotations


def rate(sheet: dict) -> int:
    """Return the batched tokens-per-second figure on the sheet."""
    # The batched rate is the only figure this function reads.
    return int(sheet["local_batched_tps"])


def hours(sheet: dict, forecast: dict) -> float:
    """Return how many hours the backlog takes at the batched rate.

    backlog_referrals is the count. tokens_per_referral is
    the size of one referral. The rate comes from rate().
    Dividing by 3600 turns tokens per second into hours.
    The result is rounded to 4 decimal places.
    """
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    # 3600 seconds of throughput make one hour.
    return round(referrals * tokens_each / rate(sheet) / 3600, 4)
