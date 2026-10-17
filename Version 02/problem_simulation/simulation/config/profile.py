"""Read one YAML profile. World constants read it at import, so set HARTLAND_PROFILE first."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path

import yaml

FOLDER = Path(__file__).resolve().parent
ENV = "HARTLAND_PROFILE"
DEFAULT = "practice"


@dataclass(frozen=True)
class Profile:
    name: str
    seed: int
    scale: float
    volume: bool
    output: str
    date_shift: dict = field(default_factory=dict)
    site_names: dict = field(default_factory=dict)
    stale_feed: str = "2024-06-30"
    description: str = ""

    def shift(self, key: str, value: date) -> date:
        return value + timedelta(days=int(self.date_shift.get(key, 0)))

    def site(self, key: str, default: str) -> str:
        return str(self.site_names.get(key, default))

    def count(self, value: int) -> int:
        return max(1, int(round(value * self.scale)))


def available() -> list[str]:
    return sorted(path.stem for path in FOLDER.glob("*.yaml"))


@lru_cache(maxsize=1)
def active() -> Profile:
    return load(os.environ.get(ENV, DEFAULT))


def load(name: str) -> Profile:
    path = FOLDER / f"{name}.yaml"
    if not path.exists():
        raise SystemExit(f"Unknown profile {name!r}. Choose one of: {', '.join(available())}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8-sig")) or {}
    seed = int(raw.get("seed", 0))
    seed_env = raw.get("seed_env")
    if seed_env and os.environ.get(seed_env):
        seed = int(os.environ[seed_env])
    return Profile(
        name=name,
        seed=seed,
        scale=float(raw.get("scale", 1.0)),
        volume=bool(raw.get("volume", False)),
        output=str(raw.get("output", f"data-{name}")),
        date_shift=dict(raw.get("date_shift") or {}),
        site_names=dict(raw.get("site_names") or {}),
        stale_feed=str(raw.get("stale_feed", "2024-06-30")),
        description=str(raw.get("description", "")),
    )
