"""Value matching: numbers with a tolerance, strings by normalised equality, dicts and lists element-wise."""

from __future__ import annotations

import re

NUMBER = re.compile(r"-?\d+(?:\.\d+)?")
META_KEYS = {"unit", "include_deceased", "days"}


def normalise(value) -> str:
    return re.sub(r"\s+", " ", str(value)).strip().lower().rstrip(".")


def as_number(value) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    found = NUMBER.findall(str(value).replace(",", ""))
    return float(found[0]) if len(found) == 1 else None


def same(expected, given) -> bool:
    if isinstance(expected, dict):
        if not isinstance(given, dict):
            return False
        keys = [key for key in expected if key not in META_KEYS]
        return all(key in given and same(expected[key], given[key]) for key in keys)
    if isinstance(expected, list):
        return isinstance(given, list) and sorted(map(normalise, expected)) == sorted(map(normalise, given))
    if isinstance(expected, bool) or isinstance(given, bool):
        return normalise(expected) == normalise(given)
    left, right = as_number(expected), as_number(given)
    if left is not None and right is not None:
        if left.is_integer():
            return left == right
        return abs(left - right) <= 0.051
    return normalise(expected) == normalise(given)


def phrases_found(text: str, groups: list) -> list[bool]:
    lowered = normalise(text)
    out = []
    for group in groups:
        options = [group] if isinstance(group, str) else list(group)
        out.append(any(normalise(option) in lowered for option in options))
    return out
