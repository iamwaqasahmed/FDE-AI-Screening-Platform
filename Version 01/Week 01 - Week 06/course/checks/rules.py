"""Comparisons that suit answers a person wrote, without printing a gold value."""

from __future__ import annotations

import re
from datetime import date

INTEGER = re.compile(r"(?<![\d.,-])(\d{1,3}(?:,\d{3})+|\d+)(?![\d-])")


def normalise(value) -> str:
    return re.sub(r"\s+", " ", str(value)).strip().lower().rstrip(".")


def as_int(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    if int(value) != value:
        return None
    return int(value)


def close(value, target, tolerance: float, *, relative: bool = True) -> bool:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return False
    span = abs(float(target)) * tolerance if relative else tolerance
    return abs(number - float(target)) <= span + 1e-9


def same_set(given, expected) -> bool:
    if not isinstance(given, list):
        return False
    return sorted(map(normalise, given)) == sorted(map(normalise, expected))


def integers(text: str) -> list[int]:
    return [int(match.group(1).replace(",", "")) for match in INTEGER.finditer(text)]


def present(text: str, value: str) -> bool:
    if normalise(value) in normalise(text):
        return True
    raw = str(value).strip()
    if re.fullmatch(r"\d+", raw):
        return f"{int(raw):,}" in text
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return _date_present(text, raw)
    if raw.endswith("%") and raw[:-1].isdigit():
        return f"{raw[:-1]} percent" in normalise(text)
    return False


def _date_present(text: str, iso: str) -> bool:
    parsed = date.fromisoformat(iso)
    forms = (
        parsed.strftime("%d/%m/%Y"),
        f"{parsed.day} {parsed.strftime('%B')} {parsed.year}",
        f"{parsed.strftime('%d')} {parsed.strftime('%B')} {parsed.year}",
    )
    lowered = text.lower()
    return any(form.lower() in lowered for form in forms)
