"""Output locations for a profile. Practice pack is the published drop."""

from __future__ import annotations

from pathlib import Path

SIM_ROOT = Path(__file__).resolve().parents[1]
VERSION_ROOT = SIM_ROOT.parent
STARTER_ROOT = VERSION_ROOT / "Week 01" / "Day 01" / "starter"
DAY2_ROOT = VERSION_ROOT / "Week 01" / "Day 02"
BASELINES_ROOT = DAY2_ROOT / "baselines"
TEMPLATES_ROOT = DAY2_ROOT / "templates"
DAY3_ROOT = VERSION_ROOT / "Week 01" / "Day 03"
WORKFLOW_ROOT = DAY3_ROOT / "workflow"
DAY3_TEMPLATES = DAY3_ROOT / "templates"
DAY4_ROOT = VERSION_ROOT / "Week 01" / "Day 04"
AGENT_ROOT = DAY4_ROOT / "agent"
DAY4_TEMPLATES = DAY4_ROOT / "templates"
DAY5_ROOT = VERSION_ROOT / "Week 01" / "Day 05"
DAY5_TEMPLATES = DAY5_ROOT / "templates"


def pack_dir(profile: str, release: str = "rel-w1d1") -> Path:
    if release not in {"rel-w1d1", "rel-w1d2", "rel-w1d3", "rel-w1d4", "rel-w1d5"}:
        raise SystemExit(f"Unknown release {release}.")
    if profile == "practice":
        return VERSION_ROOT / "data" / release
    if release == "rel-w1d1":
        return SIM_ROOT / "build" / profile / "pack"
    return SIM_ROOT / "build" / profile / release / "pack"


def truth_dir(profile: str) -> Path:
    return SIM_ROOT / "build" / profile / "truth"
