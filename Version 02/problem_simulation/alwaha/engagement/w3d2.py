"""rel-w3d2 gold. Hashes, the quota, and prices stay out of the lesson prose."""

from __future__ import annotations

import hashlib

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import approved_hash, embed_hash, external_hash
from alwaha.engagement.w3d2_rows import HELD_LETTERS, HELD_MESSAGES, HELD_PREF, domain, letters, messages
from alwaha.engagement.w3d2_rules import QLORA_RANK, classify, extract, qlora
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
    return hashlib.sha256(f"{seed}:{label}".encode()).hexdigest()[:16]


def adapter_hash(profile: Profile) -> str:
    return "sha256:" + _digest(profile.seed, "w3d2-lora-local")


def cloud_hash(profile: Profile) -> str:
    return "sha256:" + _digest(profile.seed, "w3d2-cloud-tune")


def gpu_quota(profile: Profile) -> int:
    return 1 + profile.seed % 2


def rates(profile: Profile) -> dict[str, int]:
    return {row["key"]: int(row["sar"]) for row in price_rows(profile.seed)}


def cap() -> dict:
    return {"f1_floor": FLOOR, "max_sar": MAX_SAR, "max_seconds": MAX_SECONDS, "tokens": TOKENS}


def quota(profile: Profile) -> dict:
    return {"gpus": gpu_quota(profile)}


def registry(profile: Profile) -> dict:
    return {
        "models": [
            {"hash": external_hash(profile), "id": "ext-large", "status": "approved", "zone": ZONE_PUBLIC},
            {"hash": approved_hash(profile), "id": BASE, "status": "approved", "zone": ZONE_PRIVATE},
            {"hash": embed_hash(profile), "id": "local-embed", "status": "approved", "zone": ZONE_PRIVATE},
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
    return {"hash": cloud_hash(profile), "id": CLOUD, "status": "unregistered"}


def labeled_letters(rows: tuple[tuple[str, str], ...]) -> list[dict]:
    labeled = []
    for row in letters(rows):
        labeled.append({**row, **extract(row)})
    return labeled


def measurement_block(adapter: str, local_sar: int) -> str:
    return (
        "| task | method | f1 | cost | hash |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| extraction | lora | 1.0000 | {local_sar} | {adapter} |\n"
        f"| intent | lora | 1.0000 | {local_sar} | {adapter} |\n"
        "| hours | retrieve |  |  |  |\n"
    )


def gold(profile: Profile) -> dict:
    sheet = rates(profile)
    local = sheet["price.local_per_1k"] * TOKENS // 1000
    external = sheet["price.ext_large_per_1k"] * TOKENS // 1000
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
        "held_pref": {"draft": draft, "edited": edited},
        "intents": [classify(row) for row in held_messages],
        "local_sar": local,
        "prices": {
            "price.ext_large_per_1k": sheet["price.ext_large_per_1k"],
            "price.local_per_1k": sheet["price.local_per_1k"],
        },
        "qlora": qlora(QLORA_RANK, gpu_quota(profile)),
        "quota": quota(profile),
    }
