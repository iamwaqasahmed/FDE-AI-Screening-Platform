"""Fail prose that drops a planted fact or adds one that is not in the spec."""

from __future__ import annotations

import re

from simulation.prose.entities import known_entities
from simulation.prose.spec import FactSpec

NUMBER = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*(?![\w])")
ISO_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
IDENT = re.compile(r"\b[A-Z]{2,}[-_]?[A-Z]*\d[A-Z0-9-]*\b")


class ProseError(ValueError):
    pass


def problems(spec: FactSpec, text: str) -> list[str]:
    found: list[str] = []
    lowered = text.lower()
    for fact in spec.facts:
        if fact.must_appear and fact.value and fact.value.lower() not in lowered:
            found.append(f"missing fact {fact.key}={fact.value!r}")
    allowed = _allowed_tokens(spec)
    stripped = ISO_DATE.sub(lambda match: " " if match.group(0) in allowed else match.group(0), text)
    for date in ISO_DATE.findall(stripped):
        found.append(f"extra date {date}")
    stripped = ISO_DATE.sub(" ", stripped)
    for ident in IDENT.findall(stripped):
        if ident not in allowed:
            found.append(f"extra id {ident}")
    stripped = IDENT.sub(" ", stripped)
    for number in NUMBER.findall(stripped):
        if number not in allowed:
            found.append(f"extra number {number}")
    for name in known_entities():
        if name.lower() in lowered and not _mentioned_in_spec(spec, name):
            found.append(f"extra name {name}")
    return found


def verify(spec: FactSpec, text: str) -> None:
    issues = problems(spec, text)
    if issues:
        raise ProseError(f"{spec.doc_id}: " + "; ".join(issues[:6]))


def _allowed_tokens(spec: FactSpec) -> set[str]:
    tokens: set[str] = set(spec.allowed_extra)
    for value in [fact.value for fact in spec.facts] + list(spec.allowed_extra) + [spec.title]:
        tokens.update(ISO_DATE.findall(value))
        tokens.update(IDENT.findall(value))
        tokens.update(NUMBER.findall(ISO_DATE.sub(" ", value)))
        tokens.add(value)
    return tokens


def _mentioned_in_spec(spec: FactSpec, name: str) -> bool:
    lowered = name.lower()
    haystack = " ".join([spec.title, *spec.allowed_extra, *(fact.value for fact in spec.facts)]).lower()
    return lowered in haystack
