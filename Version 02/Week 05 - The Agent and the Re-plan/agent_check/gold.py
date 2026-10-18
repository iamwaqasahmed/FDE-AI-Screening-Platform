"""Load the seed's Week 5 gold. The folder is closed to participants."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def load(data: Path) -> dict:
    return json.loads((data / "truth" / "gold" / "agent.json").read_text(encoding="utf-8"))


def backlog(data: Path) -> pd.DataFrame:
    return pd.read_parquet(data / "truth" / "gold" / "agent_backlog.parquet")


def sweep(data: Path) -> pd.DataFrame:
    return pd.read_parquet(data / "truth" / "gold" / "agent_sweep.parquet")
