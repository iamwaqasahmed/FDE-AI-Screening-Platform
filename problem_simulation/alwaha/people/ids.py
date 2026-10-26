"""Fictional identifiers. A bad check digit is planted, not accidental.

The identifier is nine random digits plus a check digit. The check digit is the digit sum modulo ten. The bad flag moves that digit so the same test fails.
"""

from __future__ import annotations

import random


def national_id(rng: random.Random, bad: bool) -> str:
    """Return a ten-digit identifier. When bad is set, the check digit is wrong on purpose."""
    body = "".join(str(rng.randrange(10)) for _ in range(9))
    check = sum(int(char) for char in body) % 10
    if bad:
        # Step the check digit so check_ok rejects this id. The body itself stays random.
        check = (check + 1) % 10
    return body + str(check)


def check_ok(value: str) -> bool:
    """Return whether the last digit matches the sum of the first nine, and the text is ten digits."""
    if len(value) != 10 or not value.isdigit():
        # A short, long, or non-digit value cannot be a valid check, so it fails before the sum.
        return False
    return sum(int(char) for char in value[:9]) % 10 == int(value[9])
