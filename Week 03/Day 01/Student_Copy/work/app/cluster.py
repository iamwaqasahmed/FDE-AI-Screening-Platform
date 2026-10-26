"""Merge rows that share a national id, a phone, or an MRN.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

partition also follows merge_with. patient_count returns the row
count. removals returns every waitlist row. While this shell is
the file that runs, the identity check says a mother and a newborn
were merged, twins were merged, a reused MRN was linked, and a row
count was used as a patient count.
"""

from __future__ import annotations


def partition(rows: list[dict]) -> list[list[str]]:
    """Union rows that share a national id, a phone, an MRN, or merge_with.

    A newborn, a twin, and a reused MRN are merged when those fields
    match. The relation field is not read.
    """
    # Each row starts in its own group. The buckets keep the first row id for each shared value.
    parent = {row["row_id"]: row["row_id"] for row in rows}
    buckets = {"national_id": {}, "phone": {}, "mrn": {}}
    by_mrn = {}
    for row in rows:
        # Record this MRN. Join this row when a national id, a phone, or an MRN was already seen.
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
        # Join a row whose merge_with names another row's MRN.
        other = by_mrn.get(row["merge_with"])
        if other:
            _union(parent, row["row_id"], other)
    # Gather the row ids under each group and return those groups in order.
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(_find(parent, row["row_id"]), []).append(row["row_id"])
    return sorted(sorted(group) for group in groups.values())


def patient_count(rows: list[dict]) -> int:
    """Count rows. This is not a count of people."""
    return len(rows)


def removals(waitlist: list[dict]) -> list[str]:
    """Return every waitlist row, whatever the flag says."""
    return sorted(row["row_id"] for row in waitlist)


def _find(parent: dict[str, str], item: str) -> str:
    """Find the group id, and compress the path on the way.

    The steps point the current row at its grandparent and move there
    until a row points at itself.
    """
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    """Put two row ids in the same group."""
    parent[_find(parent, left)] = _find(parent, right)
