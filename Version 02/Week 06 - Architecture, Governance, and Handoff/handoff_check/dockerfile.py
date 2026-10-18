"""The production Dockerfile, read as text. Nothing is built."""

from __future__ import annotations

from pathlib import Path

from simulation.eval.handoff.score_records import score_dockerfile


def score(work: Path, gold: dict) -> dict:
    path = work / "deploy" / "Dockerfile"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return score_dockerfile(text, gold)
