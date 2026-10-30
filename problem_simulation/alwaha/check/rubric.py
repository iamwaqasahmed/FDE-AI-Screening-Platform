"""Shared heading, citation, and banned-sentence helpers.

Shared helpers for notes and readouts. A section is the body under one heading. Tokens, ids, banned phrases, and numbered answers are matched here so each check does not invent its own scan. The banned phrases themselves stay in BANNED and are not repeated by these helpers.
"""

from __future__ import annotations

import re

BANNED = (
    "triage is already approved",
    "the assistant may set clinical urgency",
    "the assistant sets clinical urgency",
    "the external model may receive identified patient data",
)


def section(text: str, heading: str) -> str:
    """Return the body under one markdown heading, without the following section.

    The heading match is case-insensitive and includes the markdown marks. A missing heading is empty text, so a later token check fails closed instead of reading the whole note. The body stops at the next heading of the same level.
    """
    marker = f"## {heading}".lower()
    start = text.lower().find(marker)
    # A missing heading is empty text, so later token checks fail closed instead of reading the whole note.
    if start < 0:
        return ""
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    # The body stops at the next heading so the following section is not included.
    if nxt >= 0:
        rest = rest[:nxt]
    return rest.strip()


def has_token(text: str, token: str) -> bool:
    """Return true when the token occurs with the boundary that fits its shape.

    The module token also matches the plural, which a plain boundary search would miss. A token made only of digits must not match inside a longer number. Any other token must sit where a letter or digit does not continue it.
    """
    # The module token also matches the plural, which a plain boundary search would miss.
    if token == "week":
        return re.search(r"\bweeks?\b", text, re.IGNORECASE) is not None
    # A numeric token must not match inside a longer number.
    if token.isdigit():
        return re.search(rf"(?<!\d){re.escape(token)}(?!\d)", text) is not None
    return re.search(rf"(?<![A-Za-z0-9]){re.escape(token)}(?![A-Za-z0-9])", text) is not None


def has_id(text: str, token: str) -> bool:
    """Return true when the token occurs on a boundary that is not a letter or a digit.

    An id can contain a hyphen. The boundary test keeps a shorter id from matching inside a longer one.
    """
    return re.search(rf"(?<![A-Za-z0-9]){re.escape(token)}(?![A-Za-z0-9])", text) is not None


def banned(text: str) -> bool:
    """Return true when the text contains any phrase stored in BANNED.

    The scan is case-insensitive and looks for the phrase as a substring of the whole text.
    """
    lowered = text.lower()
    return any(phrase in lowered for phrase in BANNED)


def two_answers(text: str) -> bool:
    """Return true when at least two lines are numbered answers with text after the number.

    A bare number, or a number with nothing after it, does not count as an answer.
    """
    return sum(1 for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)) >= 2
