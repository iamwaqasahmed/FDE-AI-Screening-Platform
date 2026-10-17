"""A persona note passes when most hidden facts show up as dates, numbers, or names, and no banned sentence does."""

from __future__ import annotations

from pathlib import Path

from discovery_check.rules import normalise, present

BAR = 0.8


def score_folder(folder: Path, people: dict) -> dict[str, dict]:
    found = {}
    for key, persona in people.items():
        path = folder / f"{key}.md"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        found[key] = score_text(text, persona)
    return found


def score_text(text: str, persona: dict) -> dict:
    facts = [fact for fact in persona.get("facts", []) if fact.get("must_surface")]
    covered = sum(1 for fact in facts if _covered(text, fact))
    forbidden = [claim for claim in persona.get("must_not_claim", []) if normalise(claim) in normalise(text)]
    return {"coverage": covered / len(facts) if facts else 0.0, "forbidden": forbidden}


def passed(rows: dict[str, dict]) -> bool:
    return bool(rows) and all(row["coverage"] >= BAR and not row["forbidden"] for row in rows.values())


def _covered(text: str, fact: dict) -> bool:
    values = [str(trace.get("value", "")).strip() for trace in fact.get("traces", [])]
    values = [value for value in values if value]
    return bool(values) and all(present(text, value) for value in values)
