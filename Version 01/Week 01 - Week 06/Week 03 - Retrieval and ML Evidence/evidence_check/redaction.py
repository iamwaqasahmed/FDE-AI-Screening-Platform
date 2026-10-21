"""Weighted recall of the letter spans, and how much of the redaction covers a real span."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.eval.evidence.bars import PRECISION_BAR, RECALL_BAR


def score(path: Path, gold: dict) -> dict:
    predicted = _read(path)
    spans = gold["redaction"]
    recall, precision = _recall(predicted, spans), _precision(predicted, spans)
    return {"recall": recall, "precision": precision, "ok": recall >= RECALL_BAR and precision >= PRECISION_BAR}


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    frame = pd.read_csv(path)
    rows = []
    for row in frame.itertuples(index=False):
        try:
            rows.append({"path": str(row.path), "start": int(row.start), "end": int(row.end), "kind": str(row.kind)})
        except (AttributeError, TypeError, ValueError):
            continue
    return rows


def _recall(predicted: list[dict], spans: list[dict]) -> float:
    weight = sum(span["weight"] for span in spans)
    if not weight:
        return 0.0
    hits = sum(span["weight"] for span in spans if any(_overlaps(span, row) for row in predicted))
    return hits / weight


def _precision(predicted: list[dict], spans: list[dict]) -> float:
    gold = _merged(_pairs(spans))
    guess = _merged(_pairs(predicted))
    redacted = matched = 0
    for path, intervals in guess.items():
        for start, end in intervals:
            redacted += end - start
            matched += sum(max(0, min(end, stop) - max(start, begin)) for begin, stop in gold.get(path, []))
    return matched / redacted if redacted else 0.0


def _pairs(rows: list[dict]) -> dict:
    found: dict[str, list] = {}
    for row in rows:
        found.setdefault(row["path"], []).append((int(row["start"]), int(row["end"])))
    return found


def _merged(groups: dict) -> dict:
    found = {}
    for path, intervals in groups.items():
        merged = []
        for start, end in sorted(intervals):
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        found[path] = merged
    return found


def _overlaps(span: dict, row: dict) -> bool:
    return row["path"] == span["path"] and row["start"] < span["end"] and row["end"] > span["start"]
