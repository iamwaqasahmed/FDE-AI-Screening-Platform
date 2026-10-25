"""One person at the case date. A shared phone or a reused MRN stays split.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell merges on a shared national id, a shared phone, or a
shared MRN, and it counts rows. While that shell is the file that
runs, the identity check says a mother and a newborn were merged,
twins were merged, a reused MRN was linked, and a row count was
used as a patient count. The check does not name a national id.
"""

from __future__ import annotations


def partition(rows: list[dict]) -> list[list[str]]:
    """Group rows that are the same person.

    A shared national id links two rows. A newborn and a twin stay
    out of that link. A row whose replaces field names another
    national id joins that person. Phone, MRN, and merge_with are
    not links. A failed check digit is not read, so that person stays.
    """
    parent = {row["row_id"]: row["row_id"] for row in rows}
    by_national_id: dict[str, str] = {}
    for row in rows:
        # A mother and a newborn stay apart. Twins stay apart.
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
        # A visitor number replaced by an Iqama is one person.
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
    """Count people. A row count is not this number."""
    # The shell returns the length of rows. This returns the group count.
    return len(partition(rows))


def removals(waitlist: list[dict]) -> list[str]:
    """Propose a removal. The person stays in the cluster file.

    Only a late death flag and a seen-elsewhere flag are proposals.
    A bounced row, a resubmitted row, and an empty flag stay.
    """
    flags = {"death-late", "seen-elsewhere"}
    return sorted(row["row_id"] for row in waitlist if row["flag"] in flags)


def _find(parent: dict[str, str], item: str) -> str:
    """Find the group id, and compress the path on the way."""
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    """Put two row ids in the same group."""
    parent[_find(parent, left)] = _find(parent, right)
