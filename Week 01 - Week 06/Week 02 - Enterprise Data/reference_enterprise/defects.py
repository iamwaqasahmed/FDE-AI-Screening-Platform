"""The defects a team can count from a row: aliases, decoys, the reversed window, the reuse month."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from reference_enterprise.load import read_csv


def defects(data: Path, registry: pd.DataFrame) -> dict:
    start, end = _window(data)
    return {
        "aliases": int(registry["LOCAL_PID"].str.startswith("LX").sum()),
        "decoys": int(read_csv(data, "handover/shared/listing.csv")["KIND"].eq("decoy").sum()),
        "reversed_from": start,
        "reversed_to": end,
        "reuse_month": _reuse_month(data),
    }


def _window(data: Path) -> tuple[str, str]:
    def effective(name: str) -> str:
        text = (data / "corpus/notices" / name).read_text(encoding="utf-8")
        return re.search(r"effective: (\d{4}-\d{2}-\d{2})", text).group(1)

    return effective("notice-chg-0152.md"), effective("notice-inc-0236.md")


def _reuse_month(data: Path) -> str:
    best, score = "", -1
    for path in (data / "handover/registry/month").glob("*.csv"):
        frame = pd.read_csv(path, dtype=str).fillna("")
        if "REGISTRY_NO" not in frame.columns or "REG_NO" in frame.columns:
            continue
        duplicates = int(frame["REGISTRY_NO"].duplicated().sum())
        if duplicates > score:
            best, score = path.stem, duplicates
    return best
