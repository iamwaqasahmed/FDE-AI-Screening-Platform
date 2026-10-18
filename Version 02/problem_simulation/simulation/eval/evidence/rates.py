"""Sensitivity and a Wilson interval, shared by the gold and the reference solution."""

from __future__ import annotations

import pandas as pd

GRADED = ("R0", "R1", "R2", "R3")
REFER = ("R2", "R3")


def clean(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    for column in ("vendor_label", "grader_label", "routine_label", "adjudicated_label"):
        if column in out.columns:
            out[column] = out[column].fillna("").astype(str).replace({"nan": ""})
    if "vendor_score" in out.columns:
        out["vendor_score"] = pd.to_numeric(out["vendor_score"], errors="coerce")
    if "quality_shown" in out.columns:
        out["quality_shown"] = pd.to_numeric(out["quality_shown"], errors="coerce")
    return out


def sensitivity(frame: pd.DataFrame, column: str) -> tuple[int, int, float]:
    vendor = frame["vendor_label"]
    label = frame[column]
    keep = vendor.isin(GRADED) & label.isin(GRADED)
    vendor, label = vendor[keep], label[keep]
    positives = label.isin(REFER)
    caught = int(vendor[positives].isin(REFER).sum())
    count = int(positives.sum())
    return caught, count, round(caught / count, 3) if count else 0.0


def wilson(caught: int, count: int, z: float = 1.96) -> tuple[float, float]:
    if count <= 0:
        return 0.0, 0.0
    proportion = caught / count
    denom = 1 + z * z / count
    centre = (proportion + z * z / (2 * count)) / denom
    half = z * ((proportion * (1 - proportion) / count + z * z / (4 * count * count)) ** 0.5) / denom
    return round(centre - half, 3), round(centre + half, 3)


def point(frame: pd.DataFrame, column: str) -> dict:
    caught, count, rate = sensitivity(frame, column)
    low, high = wilson(caught, count)
    return {"sensitivity": rate, "low": low, "high": high, "positives": count}
