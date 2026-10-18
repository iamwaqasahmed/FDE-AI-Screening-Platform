"""The production contract, the transparency record, and the model card."""

from __future__ import annotations

from pathlib import Path

from simulation.eval.handoff.score_records import score_contract, score_model_card, score_transparency


def score(work: Path, gold: dict) -> dict:
    return {
        "contract": score_contract(_text(work / "contracts" / "production.yaml"), gold),
        "transparency": score_transparency(_text(work / "governance" / "transparency-record.yaml"), gold),
        "model_card": score_model_card(_text(work / "governance" / "model-card.yaml"), gold),
    }


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""
