"""chk-approach. A miss does not name the fitting family.

This check grades the approach table. Each gold problem needs one row whose family fits, whose measured cell matches the baseline when there is one, whose citation is a persona or a release file, and whose system and reason are filled. A planted token or a missing file or a bad header stops the check. The fitting family is not named in a miss.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import contains_canary, dict_rows, token_in
from alwaha.engagement.catalog import PERSONAS

COLUMNS = {"id", "family", "measured", "citation", "system", "reason"}
PERSONA_IDS = frozenset(row["id"] for row in PERSONAS)


def _files(pack: Path) -> set[str]:
    """Return the relative paths of files in the pack.

    Those paths are what a citation is allowed to name besides a persona.
    """
    return {path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file()}


def _citation_ok(cell: str, files: set[str]) -> bool:
    """Return true when the cell cites a persona or a release path.

    An exact persona id is enough. A persona id inside a longer cell also counts, on a boundary. Otherwise the cell must contain a release path.
    """
    text = cell.strip()
    if text in PERSONA_IDS:
        return True
    if any(_persona_in(persona_id, text) for persona_id in PERSONA_IDS):
        return True
    return any(name in text for name in files)


def _persona_in(persona_id: str, text: str) -> bool:
    """Return true when the persona id occurs in the cell on a boundary that is not a letter, a digit, or a hyphen.

    The hyphen is part of the boundary so one persona id does not match inside another.
    """
    return re.search(rf"(?<![a-z0-9-]){re.escape(persona_id)}(?![a-z0-9-])", text) is not None


def _fits(cell: str, rule: dict, allowed: set[str]) -> bool:
    """Return true when the family cell fits the rule.

    Families may be joined with a plus. An empty cell fails. A token outside the allowed set fails. The required families must all be present. A forbidden family must be absent.
    """
    tokens = [part.strip().lower() for part in cell.split("+") if part.strip()]
    # An empty family, or a family outside the allowed set, does not fit.
    if not tokens or any(token not in allowed for token in tokens):
        return False
    present = set(tokens)
    if not set(rule["required"]).issubset(present):
        return False
    # The required families are already present. A forbidden family still rejects the cell.
    return not present.intersection(rule["forbidden"])


def approach_problems(work: Path, pack: Path, gold: dict, measured: dict, canary: str) -> list[str]:
    """Return the approach misses.

    A planted token returns only the watermark sentence. A missing file is its own miss. A table without the required columns is its own miss and the rows are not graded. A blank id is skipped. An unknown id is reported and that row is not graded further. The family must fit. When the baseline has a value for that id, the measured cell must contain it. When it does not, the measured cell must still be filled. The citation, the system, and the reason must be present. A known id that appears more than once is a duplicate. A known id that never appears is missing.
    """
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
        # A blank id is ignored. It is not an unknown problem and it is not a duplicate.
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
        # There is no baseline value for this id, so the cell only has to be filled. A filled cell is not compared.
        elif not row["measured"]:
            problems.append(f"{problem_id} needs a measured cell")
        if not _citation_ok(row["citation"], files):
            problems.append(f"{problem_id} citation is not a release file or a persona")
        if not row["system"] or not row["reason"]:
            problems.append(f"{problem_id} needs a system and a reason")
    for problem_id, count in seen.items():
        # A repeated known id is a duplicate. An unknown id was already reported and is not also called a duplicate.
        if count > 1 and problem_id in rules:
            problems.append(f"{problem_id} is duplicated")
    for problem_id in rules:
        if problem_id not in seen:
            problems.append(f"approach is missing {problem_id}")
    return problems
