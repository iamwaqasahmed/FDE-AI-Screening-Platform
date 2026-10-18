"""Patterns that must not appear in an answer line. Names come from the registry, not from staff."""

from __future__ import annotations

import json
import re

PHONE = re.compile(r"\b07\d{9}\b|\b07\d{3}\s\d{6}\b")
NATIONAL = re.compile(r"\b(?:NID\d{9}|PID\d{8})\b")
POSTCODE = re.compile(r"\b(?:NC|EC|HC|RD)\d\b")


def clean(answer: dict, names: set[str], notes: list[str]) -> bool:
    return patterns_clean(answer, notes) and not _named(answer, names, notes)


def patterns_clean(answer: dict, notes: list[str]) -> bool:
    text = json.dumps(answer, default=str)
    if PHONE.search(text):
        notes.append("phone")
    if NATIONAL.search(text):
        notes.append("national id")
    if POSTCODE.search(text):
        notes.append("postcode")
    return not any(note in notes for note in ("phone", "national id", "postcode"))


def registry_names(frame, staff: set[str]) -> set[str]:
    pairs = set()
    for row in frame.itertuples(index=False):
        pair = f"{row.FORENAME} {row.SURNAME}".lower()
        if pair not in staff and row.FORENAME and row.SURNAME:
            pairs.add(pair)
    return pairs


def _named(answer: dict, names: set[str], notes: list[str]) -> bool:
    text = json.dumps(answer, default=str).lower()
    if any(pair in text for pair in names):
        notes.append("name")
        return True
    return False
