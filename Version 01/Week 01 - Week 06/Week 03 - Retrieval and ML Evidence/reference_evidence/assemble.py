"""Write the Week 3 folder the checker scores."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from evidence_check.gold import load
from reference_evidence.answers import solve
from reference_evidence.facts import items
from reference_evidence.redact import frame as redactions
from reference_evidence.texts import card, contract, note
from simulation.eval.evidence.question import publish
from simulation.eval.evidence.text import _percent


def build(data: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    gold = load(data)
    found = items(data)
    questions = [publish(case) for case in gold["questions"]]
    _write_json(out / "findings.json", {"items": found})
    _write_jsonl(out / "answers.jsonl", solve(data, questions))
    redactions(data).to_csv(out / "redactions.csv", index=False)
    _extract(data, found).to_csv(out / "vendor_extract.csv", index=False)
    (out / "contracts").mkdir(exist_ok=True)
    (out / "contracts/vendor_extract.yaml").write_text(contract(found), encoding="utf-8")
    rates = gold["baselines"]
    (out / "retrieval-card.md").write_text(card(found, _percent(rates["keyword"]["overall"]), _percent(rates["tfidf"]["overall"])), encoding="utf-8")
    (out / "evidence-note.md").write_text(note(found), encoding="utf-8")


def _extract(data: Path, found: dict) -> pd.DataFrame:
    frame = pd.read_csv(data / "handover/ml/vendor_retrospective.csv", dtype=str).fillna("")
    allowed = set(found["drop_restriction"]["allowed_sites"])
    kept = frame[frame["site"].isin(allowed)].copy()
    book = pd.read_excel(data / "handover/grader/workbook.xlsx", dtype=str).fillna("")
    names = book.drop_duplicates("FILE_NAME").set_index("FILE_NAME")["LOCAL_PID"]
    kept["person_key"] = kept["file_name"].map(names).fillna("")
    columns = ["capture_ref", "site", "capture_date", "person_key", "vendor_score", "vendor_label", "age_band", "quality_shown", "firmware"]
    return kept[columns]


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
