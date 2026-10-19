"""Exact backlog and sweep files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.eval.agent.bars import BACKLOG_COLUMNS, SWEEP_COLUMNS


def score_backlog(path: Path, gold: pd.DataFrame) -> dict:
    return _score(path, gold, BACKLOG_COLUMNS)


def score_sweep(path: Path, gold: pd.DataFrame) -> dict:
    return _score(path, gold, SWEEP_COLUMNS)


def _score(path: Path, gold: pd.DataFrame, columns: tuple[str, ...]) -> dict:
    if not path.exists():
        return {"ok": False, "rows": 0}
    frame = pd.read_csv(path, dtype=str).fillna("")
    if list(frame.columns) != list(columns):
        return {"ok": False, "rows": len(frame)}
    got = _norm(frame, columns)
    expected = _norm(gold, columns)
    return {"ok": got.equals(expected), "rows": len(got)}


def _norm(frame: pd.DataFrame, columns: tuple[str, ...]) -> pd.DataFrame:
    out = frame[list(columns)].fillna("").astype(str)
    for column in columns:
        out[column] = out[column].map(lambda value: value.strip().lower() if value.strip().lower() in {"true", "false"} else value.strip())
    return out.sort_values(columns[0]).reset_index(drop=True)
