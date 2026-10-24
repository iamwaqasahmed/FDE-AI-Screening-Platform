"""Named seeds. ALWAHA_PROFILE selects one. The canary is derived from the seed."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, replace

from alwaha.config.scale import PERSONAL_PEOPLE, PRACTICE_PEOPLE, SMALL_PEOPLE, TEAM_SEEDS, participant_seed


@dataclass(frozen=True)
class Profile:
    name: str
    seed: int
    people: int = PRACTICE_PEOPLE
    volume: bool = False
    date_shift_days: int = 0
    rename_sites: bool = False

    def canary(self) -> str:
        digest = hashlib.sha256(f"{self.seed}:alwaha".encode()).hexdigest()
        return f"CANARY-{digest[:12]}"

    def token(self) -> str:
        digest = hashlib.sha256(f"{self.seed}:dev".encode()).hexdigest()
        return f"dev-{digest[:8]}"


def _named() -> dict[str, Profile]:
    profiles = {
        "practice": Profile("practice", 20270110, people=PRACTICE_PEOPLE),
        "small": Profile("small", 11, people=SMALL_PEOPLE),
    }
    for name, seed in TEAM_SEEDS.items():
        profiles[name] = Profile(name, seed, people=PRACTICE_PEOPLE)
    return profiles


PROFILES = _named()


def load(name: str | None = None) -> Profile:
    chosen = name or os.environ.get("ALWAHA_PROFILE", "practice")
    if chosen == "assessment":
        profile = _assessment()
    elif chosen == "personal":
        profile = _personal()
    elif chosen not in PROFILES:
        known = ", ".join(sorted([*PROFILES, "assessment", "personal"]))
        raise SystemExit(f"Unknown profile {chosen}. Known profiles: {known}.")
    else:
        profile = PROFILES[chosen]
    if os.environ.get("ALWAHA_VOLUME") == "1":
        return replace(profile, volume=True)
    return profile


def _assessment() -> Profile:
    raw = os.environ.get("ALWAHA_ASSESSMENT_SEED")
    if not raw:
        raise SystemExit("Set ALWAHA_ASSESSMENT_SEED to load the assessment profile.")
    seed = int(raw)
    return Profile(
        "assessment",
        seed,
        people=PRACTICE_PEOPLE,
        date_shift_days=(seed % 21) + 1,
        rename_sites=True,
    )


def _personal() -> Profile:
    participant = os.environ.get("ALWAHA_PARTICIPANT")
    if not participant:
        raise SystemExit("Set ALWAHA_PARTICIPANT to load a personal world.")
    return Profile("personal", participant_seed(participant), people=PERSONAL_PEOPLE)
