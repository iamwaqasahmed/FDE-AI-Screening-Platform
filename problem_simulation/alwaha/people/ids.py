"""Fictional identifiers. A bad check digit is planted, not accidental."""

from __future__ import annotations

import random


def national_id(rng: random.Random, bad: bool) -> str:
    body = "".join(str(rng.randrange(10)) for _ in range(9))
    check = sum(int(char) for char in body) % 10
    if bad:
        check = (check + 1) % 10
    return body + str(check)


def check_ok(value: str) -> bool:
    if len(value) != 10 or not value.isdigit():
        return False
    return sum(int(char) for char in value[:9]) % 10 == int(value[9])
