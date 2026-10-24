"""Keep unlabeled domain text. Leave the extraction letters out."""

from __future__ import annotations


def keep(rows: list[dict]) -> list[dict]:
    return [row for row in rows if "item_id" not in row]
