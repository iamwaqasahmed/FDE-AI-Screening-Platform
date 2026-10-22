"""chk-w1-interview. Reports a miss as incomplete. It does not print the fact."""

from __future__ import annotations

import json
import re
from pathlib import Path

from alwaha.engagement.interview import run, score_turns
from alwaha.engagement.model import Node

KINDS = {"claim", "request", "fact"}


def load_truth(path: Path) -> tuple[dict[str, dict], str]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    canary = str(raw.pop("canary"))
    personas = {}
    for key, data in raw.items():
        personas[key] = {
            "id": key,
            "card": data["card"],
            "facts": data["facts"],
            "must_surface": tuple(data["must_surface"]),
            "banned": tuple(data["banned"]),
            "tree": tuple(
                Node(row["node_id"], tuple(row["keywords"]), row["answer"], tuple(row["releases"]), row["parent"])
                for row in data["tree"]
            ),
        }
    return personas, canary


def note_problems(text: str, banned: tuple[str, ...]) -> list[str]:
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    if not rows or "kind" not in [cell.lower() for cell in rows[0]]:
        return ["notes need a table with a Kind column"]
    kind_at = [cell.lower() for cell in rows[0]].index("kind")
    kinds = [row[kind_at].lower() for row in rows[1:] if kind_at < len(row)]
    if len(kinds) < 2 or any(kind not in KINDS for kind in kinds):
        return ["each note needs at least two rows marked claim, request, or fact"]
    lowered = text.lower()
    if any(phrase.lower() in lowered for phrase in banned):
        return ["notes contain a banned sentence"]
    return []


def interview_problems(work: Path, personas: dict[str, dict]) -> list[str]:
    folder = work / "interviews"
    scripts = sorted(folder.glob("*.questions.txt")) if folder.is_dir() else []
    if len(scripts) != 2:
        return ["submit exactly two interview scripts"]
    problems = []
    for script in scripts:
        persona_id = script.name[: -len(".questions.txt")]
        data = personas.get(persona_id)
        if data is None:
            problems.append(f"unknown persona in {script.name}")
            continue
        notes_path = folder / f"{persona_id}.notes.md"
        if not notes_path.is_file():
            problems.append(f"missing notes for {persona_id}")
            continue
        result = score_turns(data, run(data, script.read_text(encoding="utf-8").splitlines()))
        if not result["ok"]:
            problems.append(f"{persona_id} interview is incomplete")
        problems.extend(note_problems(notes_path.read_text(encoding="utf-8"), data["banned"]))
    return problems
