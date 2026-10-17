"""Load the participant-visible corpus once: Markdown text, header fields, and term counts."""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

TOKEN = re.compile(r"[a-z0-9]+(?:[-.][a-z0-9]+)*")
STOP = set("the a an of and or to in on for at by is was are be with this that from as it its how many what which who did does".split())


def tokens(text: str) -> list[str]:
    return [token for token in TOKEN.findall(text.lower()) if token not in STOP]


@dataclass
class Doc:
    doc_id: str
    path: str
    text: str
    header: dict[str, str]
    counts: Counter = field(default_factory=Counter)

    @property
    def body(self) -> str:
        return self.text.split("\n# ", 1)[-1]


@dataclass
class CorpusIndex:
    docs: list[Doc]
    idf: dict[str, float]
    norms: list[float]

    @classmethod
    def load(cls, corpus: Path) -> "CorpusIndex":
        docs = []
        for path in sorted(corpus.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            header = dict(line.split(": ", 1) for line in text.split("\n\n", 1)[0].splitlines() if ": " in line)
            docs.append(Doc(header.get("document_id", path.stem), path.relative_to(corpus).as_posix(), text, header,
                            Counter(tokens(text))))
        frequency = Counter(term for doc in docs for term in doc.counts)
        idf = {term: math.log((1 + len(docs)) / (1 + count)) + 1 for term, count in frequency.items()}
        norms = [math.sqrt(sum((count * idf[term]) ** 2 for term, count in doc.counts.items())) or 1.0 for doc in docs]
        return cls(docs, idf, norms)
