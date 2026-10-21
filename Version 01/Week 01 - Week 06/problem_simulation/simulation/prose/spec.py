"""A FactSpec is everything a writer may say. Its hash keys the prose cache."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field

PROMPT_VERSION = "v1"


@dataclass(frozen=True)
class Fact:
    key: str
    value: str
    kind: str = "text"
    must_appear: bool = True


@dataclass(frozen=True)
class FactSpec:
    doc_id: str
    family: str
    title: str
    facts: tuple[Fact, ...]
    style: str = "plain government document"
    sections: tuple[str, ...] = ()
    length_words: int = 250
    allowed_extra: tuple[str, ...] = field(default_factory=tuple)

    def key(self) -> str:
        payload = json.dumps({"spec": asdict(self), "prompt": PROMPT_VERSION}, sort_keys=True, default=str)
        return hashlib.sha256(payload.encode()).hexdigest()[:20]

    def value(self, key: str) -> str:
        for fact in self.facts:
            if fact.key == key:
                return fact.value
        raise KeyError(f"{self.doc_id} has no fact {key!r}")

    def values(self) -> dict[str, str]:
        return {fact.key: fact.value for fact in self.facts}


def facts(**pairs) -> tuple[Fact, ...]:
    """Build facts from keyword pairs. The kind is guessed from the value's shape."""
    built = []
    for key, value in pairs.items():
        text = str(value)
        kind = "number" if text.replace(".", "", 1).replace(",", "").isdigit() else "text"
        if len(text) == 10 and text[4] == "-" and text[7] == "-":
            kind = "date"
        built.append(Fact(key, text, kind))
    return tuple(built)
