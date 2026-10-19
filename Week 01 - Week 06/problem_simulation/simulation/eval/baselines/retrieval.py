"""Two retrievers a generalist reaches for first: keyword overlap and TF-IDF cosine. Neither reads status or dates."""

from __future__ import annotations

from simulation.eval.baselines.corpus_index import CorpusIndex, Doc, tokens


def keyword(index: CorpusIndex, question: str, k: int = 3) -> list[Doc]:
    terms = set(tokens(question))
    scored = [(sum(1 for term in terms if term in doc.counts), position) for position, doc in enumerate(index.docs)]
    return [index.docs[position] for score, position in sorted(scored, key=lambda pair: (-pair[0], pair[1]))[:k]]


def tfidf(index: CorpusIndex, question: str, k: int = 3) -> list[Doc]:
    terms = tokens(question)
    scored = []
    for position, doc in enumerate(index.docs):
        dot = sum(doc.counts.get(term, 0) * index.idf.get(term, 0.0) ** 2 for term in terms)
        scored.append((dot / index.norms[position], position))
    return [index.docs[position] for score, position in sorted(scored, key=lambda pair: (-pair[0], pair[1]))[:k]]
