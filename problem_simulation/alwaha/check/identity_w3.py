"""chk-w3-identity. A miss does not print a national id or a converted date."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_w3d1 import patients_problems, sprint_problems
from alwaha.check.tables import contains_canary

MOTHER = "a mother and a newborn were merged"
TWINS = "twins were merged"
REUSED = "a reused MRN was linked"
HIJRI = "a Hijri month boundary is off by a day"
STALE = "the stale clinic code was kept"
ROWS = "a row count was used as a patient count"
MATCH = "the clusters do not match"
DATE_RUN = "the date conversion did not run"
CODE_RUN = "the clinic code did not run"
CLUSTER_RUN = "the cluster job did not run"


def identity_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    rows = _jsonl(pack / "history" / "identifiers.jsonl")
    waiting = _jsonl(pack / "history" / "waitlist.jsonl")
    problems = []
    problems.extend(_dates(work / "app", rows, gold))
    problems.extend(_clinics(work / "app", rows, gold))
    problems.extend(_clusters(work / "app", rows, waiting, gold))
    problems.extend(patients_problems(work))
    problems.extend(sprint_problems(work))
    return problems


def _dates(folder: Path, rows: list[dict], gold: dict) -> list[str]:
    module = _load(folder, "dates")
    if module is None:
        return [DATE_RUN]
    indexed = {row["row_id"]: row for row in rows}
    try:
        for row_id, expected in gold["dates"].items():
            row = indexed[row_id]
            if module.gregorian(row["dob"], row["era"]) != expected:
                return [HIJRI]
    except Exception:
        return [DATE_RUN]
    return []


def _clinics(folder: Path, rows: list[dict], gold: dict) -> list[str]:
    module = _load(folder, "codes")
    if module is None:
        return [CODE_RUN]
    indexed = {row["row_id"]: row for row in rows}
    try:
        for row_id, expected in gold["clinics"].items():
            row = indexed[row_id]
            if module.clinic(row["clinic_code"], row["as_of"], row["facility"]) != expected:
                return [STALE]
    except Exception:
        return [CODE_RUN]
    return []


def _clusters(folder: Path, rows: list[dict], waiting: list[dict], gold: dict) -> list[str]:
    module = _load(folder, "cluster")
    if module is None:
        return [CLUSTER_RUN]
    try:
        groups = _normalize(module.partition(rows))
        count = module.patient_count(rows)
        removed = sorted(str(item) for item in module.removals(waiting))
    except Exception:
        return [CLUSTER_RUN]
    problems = []
    if _together(groups, gold["pairs"]["mother"]):
        problems.append(MOTHER)
    if _together(groups, gold["pairs"]["twins"]):
        problems.append(TWINS)
    if _together(groups, gold["pairs"]["reused"]):
        problems.append(REUSED)
    if count == len(rows) and count != gold["patient_count"]:
        problems.append(ROWS)
    matched = groups == gold["groups"] and removed == gold["removals"] and count == gold["patient_count"]
    if not matched and not problems:
        problems.append(MATCH)
    return problems


def _together(groups: list[list[str]], pair: list[str]) -> bool:
    left, right = pair
    return any(left in group and right in group for group in groups)


def _normalize(groups) -> list[list[str]]:
    return sorted(sorted(str(item) for item in group) for group in groups)


def _load(folder: Path, name: str):
    if not (folder / f"{name}.py").is_file():
        return None
    try:
        return load_module(folder, name)
    except Exception:
        return None


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
