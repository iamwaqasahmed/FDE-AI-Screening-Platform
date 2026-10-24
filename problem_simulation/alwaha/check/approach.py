"""chk-w1-approach. A miss does not name the fitting family."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import contains_canary, dict_rows, token_in
from alwaha.engagement.catalog import PERSONAS

COLUMNS = {"id", "family", "measured", "citation", "system", "reason"}
PERSONA_IDS = frozenset(row["id"] for row in PERSONAS)


def _files(pack: Path) -> set[str]:
    return {path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file()}


def _citation_ok(cell: str, files: set[str]) -> bool:
    text = cell.strip()
    if text in PERSONA_IDS:
        return True
    if any(_persona_in(persona_id, text) for persona_id in PERSONA_IDS):
        return True
    return any(name in text for name in files)


def _persona_in(persona_id: str, text: str) -> bool:
    return re.search(rf"(?<![a-z0-9-]){re.escape(persona_id)}(?![a-z0-9-])", text) is not None


def _fits(cell: str, rule: dict, allowed: set[str]) -> bool:
    tokens = [part.strip().lower() for part in cell.split("+") if part.strip()]
    if not tokens or any(token not in allowed for token in tokens):
        return False
    present = set(tokens)
    if not set(rule["required"]).issubset(present):
        return False
    return not present.intersection(rule["forbidden"])


def approach_problems(work: Path, pack: Path, gold: dict, measured: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return ["a watermarked sample is in the work directory"]
    path = work / "approach.md"
    if not path.is_file():
        return ["approach.md is missing"]
    rows = dict_rows(path.read_text(encoding="utf-8"), COLUMNS)
    if rows is None:
        return ["approach table needs columns id, family, measured, citation, system, reason"]
    problems = []
    seen: dict[str, int] = {}
    files = _files(pack)
    allowed = set(gold["allowed"])
    rules = gold["problems"]
    tokens = {key: str(value) for key, value in measured.items() if key in rules}
    for row in rows:
        problem_id = row["id"]
        if not problem_id:
            continue
        seen[problem_id] = seen.get(problem_id, 0) + 1
        if problem_id not in rules:
            problems.append(f"unknown problem id {problem_id}")
            continue
        if not _fits(row["family"], rules[problem_id], allowed):
            problems.append(f"{problem_id} family does not fit")
        if problem_id in tokens:
            if not token_in(row["measured"], tokens[problem_id]):
                problems.append(f"{problem_id} measured value does not match the baseline")
        elif not row["measured"]:
            problems.append(f"{problem_id} needs a measured cell")
        if not _citation_ok(row["citation"], files):
            problems.append(f"{problem_id} citation is not a release file or a persona")
        if not row["system"] or not row["reason"]:
            problems.append(f"{problem_id} needs a system and a reason")
    for problem_id, count in seen.items():
        if count > 1 and problem_id in rules:
            problems.append(f"{problem_id} is duplicated")
    for problem_id in rules:
        if problem_id not in seen:
            problems.append(f"approach is missing {problem_id}")
    return problems
