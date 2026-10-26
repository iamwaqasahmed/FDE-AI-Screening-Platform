"""Public rows for rel-w4d4.
Computed SAR and the route stay out of the pack.

The drill, the replicas, the in-flight approvals, the partner outage, and the lead time are the inputs. Hospital shares are derived from the seed and always cover the whole backlog. The route and the money are computed elsewhere.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w4d3_rows import BACKLOG, TOKENS_PER_REFERRAL, candidate, registry
from alwaha.samples.prices import price_rows

CASE_DATE = "2027-02-03"
DEADLINE = "2027-02-08"
PURCHASE_WEEKS = 16
HOSPITALS = ("h-nakhl", "h-safra", "h-wadi", "h-ain")
APPROVALS = ("apr-1", "apr-2")
STATUS_TEXT = "The referral is still pending."
BOOK_TEXT = "Offer a slot."


def budget_seconds(seed: int) -> int:
    """Return the recovery budget for this seed. It moves with the seed."""
    return 5 + (seed % 11)


def timeout_seconds(seed: int) -> int:
    """Return a timeout longer than the recovery budget, so the drill can tell a timeout from the budget."""
    return budget_seconds(seed) + 30


def rent_days(seed: int) -> int:
    """Return how many days a rental takes for this seed."""
    return 1 + (seed % 4)


def rates(seed: int) -> dict[str, int]:
    """Return the price sheet for this seed, keyed by the price name."""
    return {row["key"]: int(row["sar"]) for row in price_rows(seed)}


def _parts(seed: int) -> tuple[int, int, int, int]:
    """Return four hospital shares that add up to the whole backlog.

    The first three move with the seed. The last is whatever remains, so the shares stay exhaustive.
    """
    first = 2000 + (seed % 500)
    second = 2500 + (seed % 700)
    third = 3000 + (seed % 600)
    fourth = BACKLOG - first - second - third
    return first, second, third, fourth


def drill(seed: int) -> dict:
    """Return the failover drill: which site was killed, the budget, and the longer timeout."""
    return {
        "budget_seconds": budget_seconds(seed),
        "killed": "site-a",
        "timeout_seconds": timeout_seconds(seed),
    }


def replicas(profile: Profile) -> dict:
    """Return the two sites.

    The primary is down and carries only approved models. The backup is up and also carries the unregistered candidate, which is why a hash check still matters after failover.
    """
    approved = registry(profile)["models"]
    return {
        "sites": [
            {"health": "down", "id": "site-a", "models": approved},
            {"health": "up", "id": "site-b", "models": [*approved, candidate(profile)]},
        ]
    }


def inflight() -> list[dict]:
    """Return the approvals that are still pending. Recovery must keep them pending rather than drop them."""
    return [{"id": name, "status": "pending"} for name in APPROVALS]


def outage(seed: int) -> dict:
    """Return the partner outage, including a timeout that moves with the seed."""
    return {"partner": "insure", "status": "down", "timeout_seconds": timeout_seconds(seed)}


def lead_time(seed: int) -> dict:
    """Return the order date, the deadline, the purchase length, and this seed's rental length."""
    return {
        "deadline": DEADLINE,
        "ordered_on": CASE_DATE,
        "purchase_weeks": PURCHASE_WEEKS,
        "rent_days": rent_days(seed),
    }


def hospitals(seed: int) -> dict:
    """Return the backlog, the local price, each hospital's share, and the tokens per referral."""
    counts = _parts(seed)
    return {
        "backlog_referrals": BACKLOG,
        "local_per_1k": rates(seed)["price.local_per_1k"],
        "shares": [{"hospital": name, "referrals": count} for name, count in zip(HOSPITALS, counts)],
        "tokens_per_referral": TOKENS_PER_REFERRAL,
    }


def model_down() -> dict:
    """Return a down model with one status row and one booking row, so the fallback can differ by kind."""
    return {
        "model": "down",
        "rows": [
            {"id": "status-1", "kind": "status", "text": STATUS_TEXT},
            {"id": "book-1", "kind": "booking", "text": BOOK_TEXT},
        ],
    }
