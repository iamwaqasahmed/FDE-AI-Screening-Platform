"""Score each interview script against the persona for this data folder."""

from __future__ import annotations

from pathlib import Path

PASS = 0.8


def score_folder(folder: Path, people: dict) -> dict[str, float]:
    from simulation.stakeholders.interview import score_script

    scores = {}
    for key in people:
        path = folder / f"{key}.txt"
        questions = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
        scores[key] = float(score_script(key, questions, people)["score"]) if questions else 0.0
    return scores


def passed(scores: dict[str, float]) -> bool:
    return bool(scores) and all(score >= PASS for score in scores.values())
