"""Markdown tables shared by the Lesson 2 checks.

Shared markdown-table helpers for the day-two checks, plus the planted-sample scan used by later checks. Tables are read as rows of cells. A separator of dashes is not a row. Figures ignore the stamped day in this file so that day is not mistaken for a measurement.
"""

from __future__ import annotations

import re


def parse_tables(text: str) -> list[list[list[str]]]:
    """Return every markdown table in the text as rows of cells.

    A line that starts a pipe begins or continues a table. A row of dashes is the separator and is skipped. Any other line ends the table being collected. A table that runs to the end of the file is still returned.
    """
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            # A separator row of dashes is not data.
            if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            current.append(cells)
        # A non-table line ends the table that was being collected.
        elif current:
            tables.append(current)
            current = []
    # A table that is still open at the end of the file still counts.
    if current:
        tables.append(current)
    return tables


def dict_rows(text: str, required: set[str]) -> list[dict[str, str]] | None:
    """Return the rows of the first table whose header contains every required name, or none.

    Header matching is case-insensitive. A table that lacks a required column is skipped, and a later table can still match. A short data row yields an empty string for the missing cell instead of raising. Only the required columns are copied.
    """
    for table in parse_tables(text):
        if not table:
            continue
        header = [cell.lower() for cell in table[0]]
        # This table is a different one. The first table that has every required column is the one returned.
        if not required.issubset(header):
            continue
        indexes = {name: header.index(name) for name in required}
        rows = []
        for raw in table[1:]:
            rows.append({name: raw[indexes[name]].strip() if indexes[name] < len(raw) else "" for name in required})
        return rows
    return None


def token_in(cell: str, token: str) -> bool:
    """Return true when the token occurs in the cell and is not part of a longer number.

    The boundary is digits only, so the same digits inside a larger figure do not count.
    """
    return re.search(rf"(?<!\d){re.escape(token)}(?!\d)", cell) is not None


def figures(text: str) -> set[str]:
    """Return the set of numbers in the text after the stamped day has been removed.

    That day is not a measured figure. Integers and decimals both count. The returned set has no duplicates.
    """
    # The stamped day in this call is removed so it is not treated as a measured figure.
    cleaned = text.replace("2027-01-11", " ")
    return set(re.findall(r"\d+(?:\.\d+)?", cleaned))


def contains_canary(work, canary: str) -> bool:
    """Return true when the token's bytes occur in any file under the work directory.

    A path that is not a directory is false, so a missing tree is not a planted sample. The scan is binary, so the token can sit in a file that is not text.
    """
    # A missing work directory is not a planted sample.
    if not work.is_dir():
        return False
    needle = canary.encode()
    for path in work.rglob("*"):
        if path.is_file() and needle in path.read_bytes():
            return True
    return False
