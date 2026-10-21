"""Word-overlap score. The stem rules match Week 00 - Self Paced retrieval."""

from __future__ import annotations

import re
from collections import Counter


STOP = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "with",
}


class Passage:
    def __init__(self, document_id: str, text: str) -> None:
        self.document_id = document_id
        self.text = text


def stem(word: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def tokens(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [stem(word) for word in words if word not in STOP]


def overlap(question: str, passage: Passage, weights: dict[str, float] | None = None) -> tuple[int, float]:
    question_terms = set(tokens(question))
    counts = Counter(tokens(passage.text))
    matched = [term for term in question_terms if counts[term]]
    scale = weights or {}
    weighted = sum(scale.get(term, 1.0) * counts[term] for term in matched)
    return (len(matched), weighted)


def weights_for(passages: list[Passage]) -> dict[str, float]:
    seen: Counter[str] = Counter()
    for passage in passages:
        seen.update(set(tokens(passage.text)))
    total = max(len(passages), 1)
    return {term: total / count for term, count in seen.items()}


def best_document(question: str, rendered: dict[str, str]) -> str:
    passages = [Passage(document_id, text) for document_id, text in rendered.items()]
    weights = weights_for(passages)
    winner = max(passages, key=lambda passage: (*overlap(question, passage, weights), len(passage.text)))
    return winner.document_id
