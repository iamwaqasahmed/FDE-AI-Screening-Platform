"""Shared heading, citation, and banned-sentence helpers."""

from __future__ import annotations

import re

BANNED = (
    "triage is already approved",
    "the assistant may set clinical urgency",
    "the assistant sets clinical urgency",
    "the external model may receive identified patient data",
)


def section(text: str, heading: str) -> str:
    marker = f"## {heading}".lower()
    start = text.lower().find(marker)
    if start < 0:
        return ""
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    if nxt >= 0:
        rest = rest[:nxt]
    return rest.strip()


def has_token(text: str, token: str) -> bool:
    if token == "week":
        return re.search(r"\bweeks?\b", text, re.IGNORECASE) is not None
    if token.isdigit():
        return re.search(rf"(?<!\d){re.escape(token)}(?!\d)", text) is not None
    return re.search(rf"(?<![A-Za-z0-9]){re.escape(token)}(?![A-Za-z0-9])", text) is not None


def has_id(text: str, token: str) -> bool:
    return re.search(rf"(?<![A-Za-z0-9]){re.escape(token)}(?![A-Za-z0-9])", text) is not None


def banned(text: str) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in BANNED)


def two_answers(text: str) -> bool:
    return sum(1 for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)) >= 2
