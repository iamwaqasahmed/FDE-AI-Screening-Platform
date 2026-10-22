"""Markdown tables shared by the Day 2 checks."""

from __future__ import annotations

import re


def parse_tables(text: str) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            current.append(cells)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    return tables


def dict_rows(text: str, required: set[str]) -> list[dict[str, str]] | None:
    for table in parse_tables(text):
        if not table:
            continue
        header = [cell.lower() for cell in table[0]]
        if not required.issubset(header):
            continue
        indexes = {name: header.index(name) for name in required}
        rows = []
        for raw in table[1:]:
            rows.append({name: raw[indexes[name]].strip() if indexes[name] < len(raw) else "" for name in required})
        return rows
    return None


def token_in(cell: str, token: str) -> bool:
    return re.search(rf"(?<!\d){re.escape(token)}(?!\d)", cell) is not None


def figures(text: str) -> set[str]:
    cleaned = text.replace("2027-01-11", " ")
    return set(re.findall(r"\d+(?:\.\d+)?", cleaned))


def contains_canary(work, canary: str) -> bool:
    if not work.is_dir():
        return False
    needle = canary.encode()
    for path in work.rglob("*"):
        if path.is_file() and needle in path.read_bytes():
            return True
    return False
