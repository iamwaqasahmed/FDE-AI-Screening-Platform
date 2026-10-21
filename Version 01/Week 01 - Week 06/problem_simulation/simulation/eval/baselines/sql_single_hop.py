"""Single-hop SQL: trust the warehouse mart as built, one query per question, no identity resolution."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from simulation.eval.baselines.answerer import answer as text_answer
from simulation.eval.baselines.corpus_index import CorpusIndex
from simulation.eval.baselines.retrieval import tfidf


class SqlBaseline:
    def __init__(self, handover: Path, index: CorpusIndex):
        self.database = _open(handover / "warehouse")
        self.index = index

    def __call__(self, case: dict) -> dict:
        question = case["question"].lower()
        if self.database is not None and "eligible" in question:
            return self._eligible(case, question)
        return text_answer(case, tfidf(self.index, case["question"]))

    def _eligible(self, case: dict, question: str) -> dict:
        sql, params = "select coalesce(sum(eligible), 0) from person_mart", ()
        district = next((name for name in ("north city", "east city", "hill counties", "river districts") if name in question), "")
        if district:
            sql, params = sql + " where lower(district) = ?", (district,)
        count = self.database.execute(sql, params).fetchone()[0]
        return {"case_id": case["case_id"], "answer": {"count": count}, "citation": {},
                "usage": {"tokens": 800, "seconds": 1, "cost_usd": 0.0}}


def _open(folder: Path) -> sqlite3.Connection | None:
    for path in sorted(folder.glob("*.sqlite")) + sorted(folder.glob("*.db")):
        return sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    return None
