"""Load the closed Week 2 gold for one built data folder."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def load(data: Path) -> dict:
    path = data / "truth" / "gold" / "enterprise.json"
    if not path.exists():
        raise SystemExit(f"No enterprise gold at {path}. Rebuild that profile from problem_simulation.")
    return json.loads(path.read_text(encoding="utf-8"))


def records(data: Path) -> pd.DataFrame:
    path = data / "truth" / "gold" / "identity_records.parquet"
    if not path.exists():
        raise SystemExit(f"No identity records at {path}.")
    return pd.read_parquet(path)
