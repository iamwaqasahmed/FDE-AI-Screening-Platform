"""Load the seed's Week 4 gold. The folder is closed to participants."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def load(data: Path) -> dict:
    return json.loads((data / "truth" / "gold" / "graph.json").read_text(encoding="utf-8"))


def reconciliation(data: Path) -> pd.DataFrame:
    return pd.read_parquet(data / "truth" / "gold" / "graph_reconciliation.parquet")
