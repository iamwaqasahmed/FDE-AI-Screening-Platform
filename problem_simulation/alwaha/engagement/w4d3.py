"""rel-w4d3 gold.
The cost budget and the hashes stay here.

gold prices the same backlog three ways: at the previous external rate, at today's external rate, and at the local rate. It also reports how long the backlog takes batched and unbatched, and how early the model must start so it is warm at the peak.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w4d3_rows import (
    ADAPTERS,
    BACKLOG,
    CANDIDATE_ID,
    COLD_START_SECONDS,
    PEAK_AT,
    PEAK_MULTIPLE,
    TOKENS_PER_REFERRAL,
    WINDOW_HOURS,
    candidate,
    forecast,
    rates,
    throughput,
    today_rate,
)
from alwaha.engagement.w4d3_rules import batch_sar, hours_for, started_at


def gold(profile: Profile) -> dict:
    """Return the backlog cost, the hours, and the warm-up time for this profile.

    The same backlog is priced at the previous external rate, at today's external rate, and at the local rate. Hours are reported for the batched local speed and for the unbatched speed. The start time is the peak minus the cold start.
    """
    sheet = throughput(profile.seed)
    prices = rates(profile.seed)
    old = prices["price.ext_large_per_1k"]
    local = prices["price.local_per_1k"]
    new = today_rate(profile.seed)
    return {
        "adapters": list(ADAPTERS),
        "backlog": BACKLOG,
        "budget_sar": batch_sar(old),
        "candidate_hash": candidate(profile)["hash"],
        "candidate_id": CANDIDATE_ID,
        "cold_start_seconds": COLD_START_SECONDS,
        "demo": {"cold": str(COLD_START_SECONDS), "window": "missed"},
        "ext_large_tps": sheet["ext_large_tps"],
        "gpus": forecast(profile)["gpus"],
        "hours": hours_for(sheet["local_batched_tps"], BACKLOG, TOKENS_PER_REFERRAL),
        "hours_unbatched": hours_for(sheet["local_unbatched_tps"], BACKLOG, TOKENS_PER_REFERRAL),
        "local_batched_tps": sheet["local_batched_tps"],
        "local_sar": batch_sar(local),
        "local_unbatched_tps": sheet["local_unbatched_tps"],
        "new_price": new,
        "new_sar": batch_sar(new),
        "old_price": old,
        "old_sar": batch_sar(old),
        "peak_at": PEAK_AT,
        "peak_multiple": PEAK_MULTIPLE,
        "started_at": started_at(PEAK_AT, COLD_START_SECONDS),
        "window_hours": WINDOW_HOURS,
    }
