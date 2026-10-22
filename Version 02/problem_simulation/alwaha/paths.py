"""Output locations for a profile. Practice pack is the published drop."""

from __future__ import annotations

from pathlib import Path

SIM_ROOT = Path(__file__).resolve().parents[1]
VERSION_ROOT = SIM_ROOT.parent
STARTER_ROOT = VERSION_ROOT / "Week 01" / "Day 01" / "starter"


def pack_dir(profile: str) -> Path:
    if profile == "practice":
        return VERSION_ROOT / "data" / "rel-w1d1"
    return SIM_ROOT / "build" / profile / "pack"


def truth_dir(profile: str) -> Path:
    return SIM_ROOT / "build" / profile / "truth"
