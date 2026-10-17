"""Output folders for one seeded rebuild. The profile picks the root, relative to problem_simulation/."""

from __future__ import annotations

from pathlib import Path

from simulation.config import active

ROOT = Path(__file__).resolve().parents[1]
DATA = (ROOT / active().output).resolve()
TRUTH = DATA / "truth"
EVAL = DATA / "eval"
CORPUS = DATA / "corpus"
HANDOVER = DATA / "handover"
DROPS = DATA / "drops"
ENGAGEMENT = DATA / "engagement"
