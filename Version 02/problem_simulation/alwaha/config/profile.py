"""Named seeds. ALWAHA_PROFILE selects one. The canary is derived from the seed."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    name: str
    seed: int

    def canary(self) -> str:
        digest = hashlib.sha256(f"{self.seed}:alwaha".encode()).hexdigest()
        return f"CANARY-{digest[:12]}"

    def token(self) -> str:
        digest = hashlib.sha256(f"{self.seed}:dev".encode()).hexdigest()
        return f"dev-{digest[:8]}"


PROFILES = {
    "practice": Profile("practice", 20270110),
    "small": Profile("small", 11),
}


def load(name: str | None = None) -> Profile:
    chosen = name or os.environ.get("ALWAHA_PROFILE", "practice")
    if chosen not in PROFILES:
        known = ", ".join(sorted(PROFILES))
        raise SystemExit(f"Unknown profile {chosen}. Known profiles: {known}.")
    return PROFILES[chosen]
