"""INV-04. deliver() sees a visible batch and a holdout batch."""

from __future__ import annotations

from pathlib import Path

from access.checks.runtime import load_callable
from access.sealed_holdouts import DELIVERIES


def grade_delivery(path: Path) -> list[str]:
    fn, problems = load_callable(path, "deliver")
    if fn is None:
        return problems
    for batch in DELIVERIES:
        try:
            got = fn(batch)
        except Exception:
            problems.append(f"the delivery function raised on {batch['id']}")
            continue
        if not isinstance(got, dict):
            problems.append(f"the delivery function returned no record for {batch['id']}")
            continue
        problems.extend(_judge(batch, got))
    return problems


def _judge(batch: dict, got: dict) -> list[str]:
    problems: list[str] = []
    if got.get("stored_dispatch_count") != 1:
        problems.append("redelivery changed the booking count")
    poison = {row["file_id"] for row in batch["files"] if not row["trailer_ok"]}
    good = {row["file_id"] for row in batch["files"] if row["trailer_ok"]}
    quarantined = got.get("quarantined_file_ids")
    retained = got.get("retained_file_ids")
    if not isinstance(quarantined, list) or not poison.issubset(quarantined):
        problems.append("a file with a bad trailer is still treated as good")
    if not isinstance(retained, list) or not good.issubset(retained):
        problems.append("the last intact nightly file was dropped")
    if got.get("weekend_file_is_office_day") is not False:
        problems.append("a weekend file stamp was counted as an office day")
    if got.get("file_night_is_coverage") is not False:
        problems.append("a file night was treated as coverage")
    return problems
