"""National id format: NID, eight digits, and a mod-11 check digit. A typo fails the check."""

from __future__ import annotations

import re

WEIGHTS = (10, 9, 8, 7, 6, 5, 4, 3)
PATTERN = re.compile(r"^NID(\d{8})(\d)$")


def check_digit(digits: str) -> int:
    total = sum(int(char) * weight for char, weight in zip(digits, WEIGHTS))
    return (11 - total % 11) % 11 % 10


def national(number: int) -> str:
    digits = f"{number:08d}"
    return f"NID{digits}{check_digit(digits)}"


def typo(value: str) -> str:
    """Swap two adjacent digits, then nudge the check digit until the result fails."""
    match = PATTERN.match(value)
    if not match:
        return value
    digits, check = match.group(1), int(match.group(2))
    swapped = digits[:3] + digits[4] + digits[3] + digits[5:]
    if swapped == digits:
        swapped = digits[:-1] + str((int(digits[-1]) + 1) % 10)
    candidate = f"NID{swapped}{check}"
    if valid_national(candidate):
        candidate = f"NID{swapped}{(check + 1) % 10}"
    return candidate


def valid_national(value: str) -> bool:
    match = PATTERN.match(value or "")
    return bool(match) and check_digit(match.group(1)) == int(match.group(2))
