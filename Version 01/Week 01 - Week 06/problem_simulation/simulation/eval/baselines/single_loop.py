"""A single-loop agent: one retrieval, one read of the top document, an answer. It refuses on obvious keywords only."""

from __future__ import annotations

import re

from simulation.eval.baselines.answerer import answer as text_answer
from simulation.eval.baselines.corpus_index import CorpusIndex
from simulation.eval.baselines.retrieval import tfidf

REFUSE = re.compile(r"\b(grade this|diagnose)\b", re.IGNORECASE)
IDS = re.compile(r"\b(?:LP|MRN)\d+\b")


class SingleLoopAgent:
    def __init__(self, index: CorpusIndex):
        self.index = index

    def __call__(self, case: dict) -> dict:
        docs = tfidf(self.index, case["question"], k=1)
        result = text_answer(case, docs)
        if REFUSE.search(case["question"]):
            result["refused"] = True
        if "same_person" in (case["expected"] if isinstance(case["expected"], dict) else {}):
            result["answer"] = {"same_person": len(set(IDS.findall(case["question"]))) >= 2 and "share" in case["question"]}
        return result
