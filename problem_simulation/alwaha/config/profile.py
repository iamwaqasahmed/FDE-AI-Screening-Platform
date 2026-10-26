"""Named seeds. ALWAHA_PROFILE selects one. The canary is derived from the seed.

A profile is a frozen name, seed, population, volume flag, date shift, and site-rename flag. practice and small are fixed. Team names come from the scale table. assessment and personal are built from environment variables when asked for, so they are not in the fixed map. Setting the volume variable returns a copy with volume turned on. The canary and the development token are hashes of the seed, so the same seed always yields the same strings.
"""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, replace

from alwaha.config.scale import PERSONAL_PEOPLE, PRACTICE_PEOPLE, SMALL_PEOPLE, TEAM_SEEDS, participant_seed


@dataclass(frozen=True)
class Profile:
    """One runnable world: its name, seed, population, and the flags that change the build."""

    name: str
    seed: int
    people: int = PRACTICE_PEOPLE
    volume: bool = False
    date_shift_days: int = 0
    rename_sites: bool = False

    def canary(self) -> str:
        """Return the watermark for this seed: a fixed prefix plus a short hash."""
        digest = hashlib.sha256(f"{self.seed}:alwaha".encode()).hexdigest()
        return f"CANARY-{digest[:12]}"

    def token(self) -> str:
        """Return the development token for this seed, from a different hash than the watermark."""
        digest = hashlib.sha256(f"{self.seed}:dev".encode()).hexdigest()
        return f"dev-{digest[:8]}"


def _named() -> dict[str, Profile]:
    """Return the fixed profiles: practice, small, and one profile for each team seed."""
    profiles = {
        "practice": Profile("practice", 20270110, people=PRACTICE_PEOPLE),
        "small": Profile("small", 11, people=SMALL_PEOPLE),
    }
    for name, seed in TEAM_SEEDS.items():
        profiles[name] = Profile(name, seed, people=PRACTICE_PEOPLE)
    return profiles


PROFILES = _named()


def load(name: str | None = None) -> Profile:
    """Return the named profile, or the environment profile when name is omitted.

    assessment and personal are built on demand. Any other unknown name stops and lists the names that work. The volume variable, when set, returns a copy with volume on.
    """
    chosen = name or os.environ.get("ALWAHA_PROFILE", "practice")
    if chosen == "assessment":
        # This name is not in the fixed map. The seed comes from the environment.
        profile = _assessment()
    elif chosen == "personal":
        # This name is not in the fixed map. The seed comes from the participant name.
        profile = _personal()
    elif chosen not in PROFILES:
        known = ", ".join(sorted([*PROFILES, "assessment", "personal"]))
        raise SystemExit(f"Unknown profile {chosen}. Known profiles: {known}.")
    else:
        profile = PROFILES[chosen]
    if os.environ.get("ALWAHA_VOLUME") == "1":
        # Volume is a copy. The stored profile stays unchanged for the next caller.
        return replace(profile, volume=True)
    return profile


def _assessment() -> Profile:
    """Return the assessment profile. The seed variable must be set, and sites are renamed."""
    raw = os.environ.get("ALWAHA_ASSESSMENT_SEED")
    if not raw:
        # There is no default seed. Building assessment without one would not be reproducible.
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
    """Return the personal profile for the participant named in the environment."""
    participant = os.environ.get("ALWAHA_PARTICIPANT")
    if not participant:
        # The seed is a hash of the participant, so a missing name cannot be loaded.
        raise SystemExit("Set ALWAHA_PARTICIPANT to load a personal world.")
    return Profile("personal", participant_seed(participant), people=PERSONAL_PEOPLE)
