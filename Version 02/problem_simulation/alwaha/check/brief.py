"""chk-w1-brief. Draft bar: sizes, a ranking, and no banned sentence outside a claim."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import contains_canary, dict_rows, figures, token_in
from alwaha.engagement.catalog import PERSONAS

KINDS = {"claim", "request", "fact"}
SIZE_KINDS = {"measured", "claim"}
BANNED = tuple(phrase for row in PERSONAS for phrase in row["banned"])


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _outside_claims(text: str) -> str:
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
        if "kind" not in header or "who" not in header:
            continue
        kind_at = header.index("kind")
        for line_index in block[1:]:
            cells = _cells(lines[line_index])
            if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            if kind_at < len(cells) and cells[kind_at].lower() == "claim":
                skip.add(line_index)
    return "\n".join(line for number, line in enumerate(lines) if number not in skip)


def _ranking(text: str) -> list[tuple[str, str]]:
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
    files = {path.relative_to(pack).as_posix(): path for path in pack.rglob("*") if path.is_file()}
    matches = [name for name in files if name in cell]
    if not matches:
        return None
    return files[max(matches, key=len)]


def brief_problems(work: Path, pack: Path, gold: dict, measured: dict, canary: str) -> list[str]:
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
    rows = dict_rows(text, {"who", "kind"})
    if rows is None:
        return ["claims table needs a Kind column"]
    kinds = [row["kind"].lower() for row in rows if any(row.values())]
    if len(kinds) < 2 or any(kind not in KINDS for kind in kinds):
        return ["claims need at least two rows marked claim, request, or fact"]
    if "claim" not in kinds:
        return ["the claims table needs a row marked claim"]
    lowered = _outside_claims(text).lower()
    if any(phrase.lower() in lowered for phrase in BANNED):
        return ["brief contains a banned sentence"]
    return []


def _size_problems(text: str, pack: Path, gold: dict, measured: dict) -> list[str]:
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
    if ranked and ranked[0][0] == "p-triage":
        line = ranked[0][1].lower()
        if "clinician" not in line or "urgency" not in line:
            problems.append("the first rank needs the urgency rule on the same line")
    return problems
