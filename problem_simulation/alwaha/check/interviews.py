"""chk-interview. Reports a miss as incomplete. It does not print the fact.

This check runs two interview scripts against the persona trees and grades the notes. A failed interview is reported as incomplete. The fact that should have surfaced is not printed. Notes need a table whose rows are marked claim, request, or fact, and they must not contain a banned sentence.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from alwaha.engagement.interview import run, score_turns
from alwaha.engagement.model import Node

KINDS = {"claim", "request", "fact"}


def load_truth(path: Path) -> tuple[dict[str, dict], str]:
    """Return the persona map and the canary from a truth file.

    The canary is removed before the personas are built so it is not treated as a persona. Each remaining entry becomes a persona with a card, facts, lines that must surface, banned phrases, and a tree of nodes.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    # The canary is removed before the personas are built, and it is returned beside them rather than treated as a persona.
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
    """Return the note misses, stopping at the first kind of failure.

    Only pipe lines are table rows, and a dash separator is skipped. The header must contain a kind column. There must be at least two data rows, and every kind must be one of claim, request, or fact. The banned scan covers the whole note, including claim rows.
    """
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        # A separator row of dashes is not a note.
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
    """Return the interview misses.

    There must be exactly two question scripts. An unknown persona name is a miss and that script is not run. A missing note is a miss and that persona is not scored. Otherwise the script is run and scored. A score that is not ok is the incomplete miss, without the missing fact. The note is graded after that.
    """
    folder = work / "interviews"
    scripts = sorted(folder.glob("*.questions.txt")) if folder.is_dir() else []
    # The folder must contain exactly two scripts. Fewer or more is the same miss, and the scripts are not scored.
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
        result = score_turns(data, run(data, script.read_text(encoding="utf-8-sig").splitlines()))
        # An incomplete interview is reported without printing the fact that failed to surface.
        if not result["ok"]:
            problems.append(f"{persona_id} interview is incomplete")
        problems.extend(note_problems(notes_path.read_text(encoding="utf-8"), data["banned"]))
    return problems
