"""One person at the case date. A shared phone or a reused MRN stays split."""

from __future__ import annotations


def partition(rows: list[dict]) -> list[list[str]]:
    parent = {row["row_id"]: row["row_id"] for row in rows}
    by_national_id: dict[str, str] = {}
    for row in rows:
        if row["relation"] in {"newborn", "twin"}:
            continue
        national_id = row["national_id"]
        if not national_id:
            continue
        if national_id in by_national_id:
            _union(parent, row["row_id"], by_national_id[national_id])
        else:
            by_national_id[national_id] = row["row_id"]
    for row in rows:
        if not row["replaces"]:
            continue
        for other in rows:
            if other["national_id"] == row["replaces"]:
                _union(parent, row["row_id"], other["row_id"])
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(_find(parent, row["row_id"]), []).append(row["row_id"])
    return sorted(sorted(group) for group in groups.values())


def patient_count(rows: list[dict]) -> int:
    return len(partition(rows))


def removals(waitlist: list[dict]) -> list[str]:
    flags = {"death-late", "seen-elsewhere"}
    return sorted(row["row_id"] for row in waitlist if row["flag"] in flags)


def _find(parent: dict[str, str], item: str) -> str:
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    parent[_find(parent, left)] = _find(parent, right)
