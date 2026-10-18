"""The three CSV handoffs."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.eval.handoff.score_files import score_flows, score_hazards, score_threats


def score(work: Path, gold: dict) -> dict:
    return {
        "flows": score_flows(_read(work / "flows.csv"), gold),
        "threats": score_threats(_read(work / "threats.csv"), gold),
        "hazards": score_hazards(_read(work / "hazard-log.csv"), gold),
    }


def _read(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    return pd.read_csv(path, dtype=str).fillna("")
