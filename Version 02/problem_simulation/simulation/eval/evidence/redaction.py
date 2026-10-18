"""Personal-data spans in the patient letters, with the weight a missed national id carries."""

from __future__ import annotations

from simulation.eval.evidence.bars import NATIONAL_WEIGHT


def spans(world: dict) -> list[dict]:
    found = []
    for row in world["gold"].get("pii", []):
        path = str(row.get("path", ""))
        if not path.startswith("patient-letters/"):
            continue
        found.append({
            "path": path,
            "start": int(row["start"]),
            "end": int(row["end"]),
            "kind": row["kind"],
            "weight": NATIONAL_WEIGHT if row["kind"] == "national_id" else 1,
        })
    return sorted(found, key=lambda row: (row["path"], row["start"], row["kind"]))
