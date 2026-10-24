"""Public rows for rel-w4d3. The cost budget stays out of the pack."""

from __future__ import annotations

import hashlib

from alwaha.config.profile import Profile
from alwaha.engagement.w3d2 import adapter_hash, gpu_quota
from alwaha.samples.prices import price_rows

BACKLOG = 12000
WINDOW_HOURS = 48
PEAK_MULTIPLE = 5
COLD_START_SECONDS = 90
TOKENS_PER_REFERRAL = 1000
CASE_DATE = "2027-02-02"
PEAK_AT = "2027-02-02T21:00:00+03:00"
PUBLIC_ID = "public-hours"
PUBLIC_BODY = "Clinic hours are on the circular."
CANDIDATE_ID = "local-smallx"
ADAPTERS = ("lora-extract", "lora-intent", "lora-local")


def _hash(seed: int, label: str) -> str:
    digest = hashlib.sha256(f"{seed}:{label}".encode()).hexdigest()[:16]
    return "sha256:" + digest


def rates(seed: int) -> dict[str, int]:
    return {row["key"]: int(row["sar"]) for row in price_rows(seed)}


def today_rate(seed: int) -> int:
    return rates(seed)["price.ext_large_per_1k"] + 1 + (seed % 7)


def throughput(seed: int) -> dict:
    unbatched = 20 + (seed % 41)
    batched = 80 + (seed % 121)
    budget_ms = 500 + (seed % 401)
    return {
        "chat_p95_budget_ms": budget_ms,
        "chat_p95_reserved_ms": 80 + (seed % 321),
        "chat_p95_starved_ms": budget_ms + 200 + (seed % 1801),
        "cold_start_seconds": COLD_START_SECONDS,
        "ext_large_tps": batched + 40 + (seed % 141),
        "local_batched_tps": batched,
        "local_unbatched_tps": unbatched,
        "tokens_per_referral": TOKENS_PER_REFERRAL,
    }


def forecast(profile: Profile) -> dict:
    return {
        "backlog_referrals": BACKLOG,
        "campaign": "eye-screening",
        "gpus": gpu_quota(profile),
        "id": "p-forecast",
        "peak_at": PEAK_AT,
        "peak_multiple": PEAK_MULTIPLE,
        "shares_quota_with": "load-chat",
        "specialty": "ophth",
        "window_hours": WINDOW_HOURS,
    }


def price_today(seed: int) -> dict:
    sheet = rates(seed)
    return {
        "key": "price.ext_large_per_1k",
        "local_per_1k": sheet["price.local_per_1k"],
        "replaces": "price.ext_large_per_1k",
        "sar": today_rate(seed),
    }


def _adapter(name: str, digest: str) -> dict:
    return {
        "base": "local-small",
        "hash": digest,
        "id": name,
        "status": "approved",
        "zone": "zone-private",
    }


def registry(profile: Profile) -> dict:
    return {
        "models": [
            _adapter("lora-extract", _hash(profile.seed, "w4d3-lora-extract")),
            _adapter("lora-intent", _hash(profile.seed, "w4d3-lora-intent")),
            _adapter("lora-local", adapter_hash(profile)),
        ]
    }


def candidate(profile: Profile) -> dict:
    return {"hash": _hash(profile.seed, "w4d3-lookalike"), "id": CANDIDATE_ID, "status": "unregistered"}


def load_rows() -> list[dict]:
    return [
        {"adapter": "lora-intent", "id": "chat-1", "kind": "chat", "phi": True, "text": "Where is my referral?"},
        {"adapter": "lora-extract", "id": "batch-1", "kind": "batch", "phi": True, "text": "Referral letter."},
        {"adapter": "", "id": PUBLIC_ID, "kind": "public", "phi": False, "text": PUBLIC_BODY},
        {"adapter": "", "id": PUBLIC_ID, "kind": "public", "phi": False, "text": PUBLIC_BODY},
    ]


def public_cache() -> dict:
    return {PUBLIC_ID: PUBLIC_BODY}
