"""chk-w1-brief. Draft bar: sizes, a ranking, and no banned sentence outside a claim.

This check grades the brief at the draft bar: a claims table, a sizes table, and a ranking. A banned sentence is allowed inside a row marked claim and forbidden everywhere else. A measured size must be the baseline. A claimed size must appear in the cited release file. The ranking must list every problem once. If the triage id is ranked first, that same line must carry the urgency rule.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import contains_canary, dict_rows, figures, token_in
from alwaha.engagement.catalog import PERSONAS

KINDS = {"claim", "request", "fact"}
SIZE_KINDS = {"measured", "claim"}
BANNED = tuple(phrase for row in PERSONAS for phrase in row["banned"])


def _cells(line: str) -> list[str]:
    """Return the stripped cells of one markdown table line.

    The outer pipes are removed before the split so they do not become empty cells.
    """
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _outside_claims(text: str) -> str:
    """Return the brief with claim rows removed.

    The banned-sentence scan uses this text. A table that has both a kind column and a who column can contain claims, and those claim rows are skipped. A dash separator is not a claim. Any other table stays in the scan, so a banned sentence outside the claims table still counts.
    """
    lines = text.splitlines()
    skip: set[int] = set()
    index = 0
    while index < len(lines):
        if not lines[index].strip().startswith("|"):
            index += 1
            continue
        block = []
        while index < len(lines) and lines[index].strip().startswith("|"):
            block.append(index)
            index += 1
        header = [cell.lower() for cell in _cells(lines[block[0]])]
        # A table without both columns is not the claims table, so its lines stay in the banned-sentence scan.
        if "kind" not in header or "who" not in header:
            continue
        kind_at = header.index("kind")
        for line_index in block[1:]:
            cells = _cells(lines[line_index])
            if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            # A claim row may quote a banned sentence, so it is removed before that scan.
            if kind_at < len(cells) and cells[kind_at].lower() == "claim":
                skip.add(line_index)
    return "\n".join(line for number, line in enumerate(lines) if number not in skip)


def _ranking(text: str) -> list[tuple[str, str]]:
    """Return the ranked problem ids in order, each with the rest of its line.

    Only numbered lines are considered. The first problem id on the line is the rank. A numbered line with no problem id is skipped.
    """
    found = []
    for line in text.splitlines():
        match = re.match(r"\s*\d+\.\s+(.*)", line)
        if not match:
            continue
        ids = re.findall(r"\bp-[a-z]+\b", match.group(1))
        if ids:
            found.append((ids[0], match.group(1)))
    return found


def _resolve(pack: Path, cell: str) -> Path | None:
    """Return the release file whose path is named in the cell, or nothing.

    When several paths occur in the cell, the longest one wins, so a shorter prefix of another path is not chosen.
    """
    files = {path.relative_to(pack).as_posix(): path for path in pack.rglob("*") if path.is_file()}
    matches = [name for name in files if name in cell]
    if not matches:
        return None
    # The longest release path contained in the cell wins, so a shorter prefix of another path is not chosen.
    return files[max(matches, key=len)]


def brief_problems(work: Path, pack: Path, gold: dict, measured: dict, canary: str) -> list[str]:
    """Return the brief misses from the claims table, the sizes table, and the ranking.

    A planted token returns only the watermark sentence. A missing file is its own miss. The three graders are concatenated, so a failure in one does not skip the others.
    """
    if contains_canary(work, canary):
        return ["a watermarked sample is in the work directory"]
    path = work / "brief.md"
    if not path.is_file():
        return ["brief.md is missing"]
    text = path.read_text(encoding="utf-8")
    problems = _claim_problems(text)
    problems.extend(_size_problems(text, pack, gold, measured))
    problems.extend(_rank_problems(text, gold))
    return problems


def _claim_problems(text: str) -> list[str]:
    """Return the claims-table misses, stopping at the first kind of failure.

    The table needs a who column and a kind column. There must be at least two filled rows, and every kind must be claim, request, or fact. One of them must be a claim. A banned sentence outside the claim rows is a miss.
    """
    # The claims table needs both a who column and a kind column.
    rows = dict_rows(text, {"who", "kind"})
    if rows is None:
        return ["claims table needs a Kind column"]
    # Blank rows are dropped. Every remaining kind must be claim, request, or fact.
    kinds = [row["kind"].lower() for row in rows if any(row.values())]
    if len(kinds) < 2 or any(kind not in KINDS for kind in kinds):
        return ["claims need at least two rows marked claim, request, or fact"]
    # The table still needs a row marked claim.
    if "claim" not in kinds:
        return ["the claims table needs a row marked claim"]
    # Claim rows may quote a banned sentence, so the scan looks only outside them.
    lowered = _outside_claims(text).lower()
    if any(phrase.lower() in lowered for phrase in BANNED):
        return ["brief contains a banned sentence"]
    return []


def _size_problems(text: str, pack: Path, gold: dict, measured: dict) -> list[str]:
    """Return the sizes-table misses.

    The table needs id, size, source, and kind. A blank id is skipped. An unknown id is reported and that row stops. The kind must be measured or claim. A measured row must carry the baseline value and is not also checked as a claim. A claim row must cite a release file, and the numbers in the size cell must appear in that file. A known id that appears more than once is a duplicate. A known id that never appears is missing.
    """
    rows = dict_rows(text, {"id", "size", "source", "kind"})
    if rows is None:
        return ["sizes table needs id, size, source, and kind"]
    problems = []
    seen: dict[str, int] = {}
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
        kind = row["kind"].lower()
        if kind not in SIZE_KINDS:
            problems.append(f"{problem_id} size kind must be measured or claim")
            continue
        # A measured row is checked against the baseline and is not also checked as a claim.
        if kind == "measured":
            if problem_id not in tokens or not token_in(row["size"], tokens[problem_id]):
                problems.append(f"{problem_id} size is not the baseline measurement")
            continue
        source = _resolve(pack, row["source"])
        if source is None:
            problems.append(f"{problem_id} source is not in the release")
            continue
        asked = set(re.findall(r"\d+(?:\.\d+)?", row["size"]))
        if not asked.intersection(figures(source.read_text(encoding="utf-8"))):
            problems.append(f"{problem_id} size is not in the cited file")
    for problem_id, count in seen.items():
        if count > 1 and problem_id in rules:
            problems.append(f"{problem_id} is duplicated")
    for problem_id in rules:
        if problem_id not in seen:
            problems.append(f"brief is missing {problem_id}")
    return problems


def _rank_problems(text: str, gold: dict) -> list[str]:
    """Return the ranking misses.

    An unknown id is reported. A known id ranked more than once is a duplicate. A known id that is never ranked is missing. When the first ranked id is the triage id, that same line must mention a clinician and urgency.
    """
    ranked = _ranking(text)
    problems = []
    seen: dict[str, int] = {}
    for problem_id, _line in ranked:
        seen[problem_id] = seen.get(problem_id, 0) + 1
    rules = gold["problems"]
    for problem_id, count in seen.items():
        if problem_id not in rules:
            problems.append(f"unknown problem id {problem_id}")
        elif count > 1:
            problems.append(f"{problem_id} is ranked twice")
    for problem_id in rules:
        if problem_id not in seen:
            problems.append(f"ranking is missing {problem_id}")
    # Only the first ranked line has to carry the urgency rule, and only when that line is the triage id.
    if ranked and ranked[0][0] == "p-triage":
        line = ranked[0][1].lower()
        if "clinician" not in line or "urgency" not in line:
            problems.append("the first rank needs the urgency rule on the same line")
    return problems
