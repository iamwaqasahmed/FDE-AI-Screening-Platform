"""rel-m03-l02 gold.
Hashes, the quota, and prices stay out of the lesson prose.

Adapter and cloud hashes, the GPU quota, and the token prices are derived here and returned only inside gold. The held-out letters and messages are labeled by the reference extractor and classifier so the checker can score a submission without those labels appearing in the lesson.
"""

from __future__ import annotations

import hashlib

from alwaha.config.profile import Profile
from alwaha.engagement.m02_l04 import approved_hash, embed_hash, external_hash
from alwaha.engagement.m03_l02_rows import HELD_LETTERS, HELD_MESSAGES, HELD_PREF, domain, letters, messages
from alwaha.engagement.m03_l02_rules import QLORA_RANK, classify, extract, qlora
from alwaha.samples.prices import price_rows

CASE_DATE = "2027-01-25"
ADAPTER = "lora-local"
BASE = "local-small"
CLOUD = "cloud-tune"
FLOOR = 0.8
MAX_SAR = 8
MAX_SECONDS = 2
TOKENS = 1000
ZONE_PRIVATE = "zone-private"
ZONE_PUBLIC = "zone-public"


def _digest(seed: int, label: str) -> str:
    """Return a hex prefix of the seed and the label so the adapter and the cloud hash cannot collide."""
    return hashlib.sha256(f"{seed}:{label}".encode()).hexdigest()[:16]


def adapter_hash(profile: Profile) -> str:
    """Return the hash of the approved local adapter for this profile."""
    return "sha256:" + _digest(profile.seed, "m03_l02-lora-local")


def cloud_hash(profile: Profile) -> str:
    """Return the hash of the unregistered cloud tune, which is not in the registry."""
    return "sha256:" + _digest(profile.seed, "m03_l02-cloud-tune")


def gpu_quota(profile: Profile) -> int:
    """Return how many GPUs this profile's release allows. It moves with the seed."""
    return 1 + profile.seed % 2


def rates(profile: Profile) -> dict[str, int]:
    """Return the price sheet for this seed, keyed by the price name."""
    return {row["key"]: int(row["sar"]) for row in price_rows(profile.seed)}


def cap() -> dict:
    """Return the score floor, the spend ceiling, the latency ceiling, and the token count the cost uses."""
    return {"f1_floor": FLOOR, "max_sar": MAX_SAR, "max_seconds": MAX_SECONDS, "tokens": TOKENS}


def quota(profile: Profile) -> dict:
    """Return the GPU quota record for this profile."""
    return {"gpus": gpu_quota(profile)}


def registry(profile: Profile) -> dict:
    """Return the approved models, including the local adapter pinned to the local base.

    The external model stays in the public zone. The local models and the adapter stay in the private zone.
    """
    return {
        "models": [
            # External model, in the public zone.
            {"hash": external_hash(profile), "id": "ext-large", "status": "approved", "zone": ZONE_PUBLIC},
            # Local base and the embedding model, in the private zone.
            {"hash": approved_hash(profile), "id": BASE, "status": "approved", "zone": ZONE_PRIVATE},
            {"hash": embed_hash(profile), "id": "local-embed", "status": "approved", "zone": ZONE_PRIVATE},
            # Local adapter, pinned to that base, in the private zone.
            {
                "base": BASE,
                "hash": adapter_hash(profile),
                "id": ADAPTER,
                "status": "approved",
                "zone": ZONE_PRIVATE,
            },
        ]
    }


def cloud(profile: Profile) -> dict:
    """Return the unregistered cloud tune. It is not an approved model."""
    return {"hash": cloud_hash(profile), "id": CLOUD, "status": "unregistered"}


def labeled_letters(rows: tuple[tuple[str, str], ...]) -> list[dict]:
    """Return each letter with the reference extraction fields added beside its text.

    The steps turn each pair into a letter and merge the reference extraction fields onto that same row.
    """
    labeled = []
    for row in letters(rows):
        labeled.append({**row, **extract(row)})
    return labeled


def measurement_block(adapter: str, local_sar: int) -> str:
    """Return the measurement table for the local adapter.

    Extraction and intent are filled. The hours row is left blank because that task is retrieval, not this adapter.
    """
    return (
        "| task | method | f1 | cost | hash |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| extraction | lora | 1.0000 | {local_sar} | {adapter} |\n"
        f"| intent | lora | 1.0000 | {local_sar} | {adapter} |\n"
        "| hours | retrieve |  |  |  |\n"
    )


def gold(profile: Profile) -> dict:
    """Return the hashes, the quota, the held-out labels, and both token costs for this profile.

    Local and external costs scale the sheet price by the shared token count. The held-out preference is returned as the draft and the edited text, not as a computed revision.
    """
    sheet = rates(profile)
    # Local cost and external cost, each scaled from the sheet.
    local = sheet["price.local_per_1k"] * TOKENS // 1000
    external = sheet["price.ext_large_per_1k"] * TOKENS // 1000
    # Held-out letters and messages, labeled by the reference tools.
    held_letters = labeled_letters(HELD_LETTERS)
    held_messages = messages(HELD_MESSAGES)
    draft, edited = HELD_PREF
    return {
        "adapter_hash": adapter_hash(profile),
        "cap": cap(),
        "cloud_hash": cloud_hash(profile),
        "domain": domain(),
        "external_sar": external,
        "held_letters": held_letters,
        "held_messages": held_messages,
        # The preference is the draft and the edited text.
        "held_pref": {"draft": draft, "edited": edited},
        "intents": [classify(row) for row in held_messages],
        "local_sar": local,
        "prices": {
            "price.ext_large_per_1k": sheet["price.ext_large_per_1k"],
            "price.local_per_1k": sheet["price.local_per_1k"],
        },
        # Adapter settings for this profile's GPU quota.
        "qlora": qlora(QLORA_RANK, gpu_quota(profile)),
        "quota": quota(profile),
    }
