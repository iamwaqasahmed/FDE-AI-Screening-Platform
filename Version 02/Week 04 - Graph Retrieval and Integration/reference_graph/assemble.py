"""Write the Week 4 folder the checker scores."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from graph_check.gold import load
from reference_graph.answers import solve
from reference_graph.measure import build as measure
from reference_graph.texts import card, contract, note
from simulation.eval.evidence.text import _percent
from simulation.eval.graph.question import publish


def build(data: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    items, reconciled, chase, resend = measure(data)
    gold = load(data)
    questions = [publish(case) for case in gold["questions"]]
    _write_json(out / "findings.json", {"items": items})
    _write_jsonl(out / "answers.jsonl", solve(data, questions, chase, items))
    reconciled[["request_id", "local_pid", "template", "requested_at", "copies", "status"]].to_csv(
        out / "reconciliation.csv", index=False)
    pd.DataFrame(resend)[["request_id", "local_pid", "action", "reason"]].to_csv(out / "resend.csv", index=False)
    (out / "contracts").mkdir(exist_ok=True)
    (out / "contracts/bureau_dispatch.yaml").write_text(contract(items), encoding="utf-8")
    rates = gold["baselines"]
    (out / "graph-card.md").write_text(
        card(items, _percent(rates["keyword"]["overall"]), _percent(rates["tfidf"]["overall"])), encoding="utf-8")
    (out / "incident-note.md").write_text(note(items), encoding="utf-8")


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
