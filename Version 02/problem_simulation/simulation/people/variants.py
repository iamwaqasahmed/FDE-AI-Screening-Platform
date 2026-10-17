"""Transliteration and name-order variants. Each system spells some names its own way."""

from __future__ import annotations

import hashlib

FORENAMES: dict[str, tuple[str, ...]] = {
    "Mohammed": ("Muhammad", "Mohamed", "Mohammad"),
    "Yusuf": ("Youssef", "Yousef"),
    "Aleksandr": ("Alexander", "Aleksander"),
    "Oksana": ("Oxana",),
    "Siobhan": ("Shivaun", "Siobhain"),
    "Nguyen Thi": ("Thi",),
    "Xiaoming": ("Xiao Ming", "Xiao-Ming"),
    "Abdulrahman": ("Abdul Rahman", "Abdel Rahman"),
    "Fatima": ("Fatimah", "Fatma"),
    "Gurpreet": ("Gurprit",),
}
SURNAMES: dict[str, tuple[str, ...]] = {
    "Al-Sayed": ("Alsayed", "El Sayed", "El-Sayed"),
    "Nguyen": ("Ngyuen", "Nguyễn"),
    "Tchaikovsky": ("Chaikovsky", "Tschaikowski"),
    "O'Sullivan": ("OSullivan", "O Sullivan"),
    "Abdullah": ("Abdulla", "Abdallah"),
    "Zhang": ("Chang", "Cheung"),
    "Kowalczyk": ("Kowalczik",),
    "Mac Giolla": ("McGill", "MacGill"),
    "Okafor": ("Okafo",),
    "Hernandez": ("Hernández",),
}
ORDER_SWAP_SYSTEMS = {"lab", "booking"}


def _roll(key: str) -> int:
    return int.from_bytes(hashlib.sha256(key.encode()).digest()[:4], "big")


def spelled(forename: str, surname: str, system: str, person_key: str) -> tuple[str, str]:
    """How this system recorded the name. Deterministic per person and system."""
    roll = _roll(f"{system}:{person_key}")
    first = forename
    last = surname
    if forename in FORENAMES and roll % 3 != 0:
        options = FORENAMES[forename]
        first = options[roll % len(options)]
    if surname in SURNAMES and (roll // 7) % 3 != 0:
        options = SURNAMES[surname]
        last = options[(roll // 11) % len(options)]
    if system in ORDER_SWAP_SYSTEMS and roll % 29 == 0:
        first, last = last, first
    return first, last


def canonical_pools() -> tuple[list[str], list[str]]:
    return list(FORENAMES), list(SURNAMES)
