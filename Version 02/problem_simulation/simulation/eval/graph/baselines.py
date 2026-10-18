"""Keyword and TF-IDF over the Week 4 questions. Their path is the one document they cited."""

from __future__ import annotations

from simulation.eval.baselines.answerer import answer as text_answer
from simulation.eval.baselines.retrieval import keyword, tfidf
from simulation.eval.evidence.baselines import _index
from simulation.eval.graph.score import score_one, summarise


def rates(world: dict, cases: list[dict]) -> dict:
    index = _index(world)
    found = {}
    for name, retrieve in (("keyword", keyword), ("tfidf", tfidf)):
        results = [score_one(case, _with_path(text_answer(case, retrieve(index, case["question"]))), check_model=False)
                   for case in cases]
        found[name] = summarise(cases, results)
    found["best"] = round(max(found["keyword"]["overall"], found["tfidf"]["overall"]), 4)
    return found


def _with_path(row: dict) -> dict:
    cited = str((row.get("citation") or {}).get("document_id", ""))
    row["path"] = [cited] if cited else []
    row.setdefault("followed_injection", False)
    return row
