"""Merge rows that share a national id, a phone, or an MRN."""

from __future__ import annotations


def partition(rows: list[dict]) -> list[list[str]]:
    parent = {row["row_id"]: row["row_id"] for row in rows}
    buckets = {"national_id": {}, "phone": {}, "mrn": {}}
    by_mrn = {}
    for row in rows:
        by_mrn[row["mrn"]] = row["row_id"]
        for field, bucket in buckets.items():
            value = row[field]
            if not value:
                continue
            if value in bucket:
                _union(parent, row["row_id"], bucket[value])
            else:
                bucket[value] = row["row_id"]
    for row in rows:
        other = by_mrn.get(row["merge_with"])
        if other:
            _union(parent, row["row_id"], other)
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(_find(parent, row["row_id"]), []).append(row["row_id"])
    return sorted(sorted(group) for group in groups.values())


def patient_count(rows: list[dict]) -> int:
    return len(rows)


def removals(waitlist: list[dict]) -> list[str]:
    return sorted(row["row_id"] for row in waitlist)


def _find(parent: dict[str, str], item: str) -> str:
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    parent[_find(parent, left)] = _find(parent, right)
