"""Readers for the files a team is given. Nothing here opens truth or eval."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.eval.evidence.rates import clean


def read_csv(data: Path, relative: str) -> pd.DataFrame:
    return pd.read_csv(data / relative, dtype=str).fillna("")


def header(text: str) -> dict[str, str]:
    meta, applies = {}, []
    for line in text.splitlines():
        if line.startswith("#"):
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key == "applies_to" and value:
            applies.append(value)
        else:
            meta[key] = value
    meta["applies_to"] = applies
    return meta


def read_header(path: Path) -> dict[str, str]:
    return header(path.read_text(encoding="utf-8"))


def vendor(data: Path) -> pd.DataFrame:
    frame = pd.read_csv(data / "handover/ml/vendor_retrospective.csv")
    return clean(frame)


def adjudicated(data: Path) -> pd.DataFrame:
    return clean(pd.read_csv(data / "handover/ml/adjudicated_labels.csv"))


def citation(meta: dict) -> dict:
    document_id = meta.get("document_id", "")
    return {
        "document_id": document_id,
        "version": meta.get("version", ""),
        "status": meta.get("status", ""),
        "effective": meta.get("effective", ""),
        "sunset": meta.get("sunset", ""),
        "site": meta.get("site", ""),
        "clause_id": document_id,
    }
