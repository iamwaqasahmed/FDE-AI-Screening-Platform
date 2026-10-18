"""Keyword and TF-IDF over the Week 3 questions. They read Markdown and ignore status."""

from __future__ import annotations

import math
from collections import Counter

from simulation.eval.baselines.answerer import answer as text_answer
from simulation.eval.baselines.corpus_index import Doc, tokens
from simulation.eval.baselines.retrieval import keyword, tfidf
from simulation.eval.evidence.score import score_one, summarise


def rates(world: dict, cases: list[dict]) -> dict:
    index = _index(world)
    found = {}
    for name, retrieve in (("keyword", keyword), ("tfidf", tfidf)):
        results = [score_one(case, text_answer(case, retrieve(index, case["question"])), check_model=False) for case in cases]
        found[name] = summarise(cases, results)
    found["best"] = round(max(found["keyword"]["overall"], found["tfidf"]["overall"]), 4)
    return found


def _index(world: dict) -> "Index":
    docs = []
    ordered = sorted(world["rendered"].items(), key=lambda item: _path(world, item[0]))
    for doc_id, text in ordered:
        header = _header(text)
        docs.append(Doc(header.get("document_id", doc_id), _path(world, doc_id), text, header, Counter(tokens(text))))
    frequency = Counter(term for doc in docs for term in doc.counts)
    idf = {term: math.log((1 + len(docs)) / (1 + count)) + 1 for term, count in frequency.items()}
    norms = [math.sqrt(sum((count * idf[term]) ** 2 for term, count in doc.counts.items())) or 1.0 for doc in docs]
    return Index(docs, idf, norms)


def _path(world: dict, doc_id: str) -> str:
    """The corpus-relative path export writes, so a tie breaks the same way on disk."""
    recorded = world.get("paths", {}).get(doc_id)
    if recorded:
        return recorded
    if doc_id.startswith("board-"):
        return f"boards/{doc_id}.md"
    if doc_id.startswith("site-note-"):
        return f"notes/{doc_id}.md"
    return f"policy/{doc_id}.md"


def _header(text: str) -> dict[str, str]:
    return dict(line.split(": ", 1) for line in text.split("\n\n", 1)[0].splitlines() if ": " in line)


class Index:
    """The fields the retrievers read. Built from rendered text so a check needs no files."""

    def __init__(self, docs: list[Doc], idf: dict[str, float], norms: list[float]) -> None:
        self.docs, self.idf, self.norms = docs, idf, norms
