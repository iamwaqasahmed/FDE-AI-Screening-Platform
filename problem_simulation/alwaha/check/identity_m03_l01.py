"""chk-m03-l01-identity. A miss does not print a national id or a converted date.

This check grades dates, clinic codes, and the patient clusters. A Hijri boundary that is off, a stale clinic code, a mother merged with a newborn, twins merged, a reused record linked, or a row count used as a patient count are separate misses. A general mismatch is reported only when none of those specific merges was already named. A national id or a converted date is not printed.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_m03_l01 import patients_problems, sprint_problems
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
    """Return the identity misses.

    A planted token returns only the watermark. Dates, clinic codes, and clusters are graded from the history files, then the patient note and the sprint note are graded. A failure in one group does not skip the next.
    """
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
    """Return the date miss, or the run miss when the module is missing or crashes.

    The first row whose converted date disagrees is enough. Later rows are not checked.
    """
    # A missing dates module is the run miss, so no date is compared.
    module = _load(folder, "dates")
    if module is None:
        return [DATE_RUN]
    # Index the history by row so each gold date can find its source.
    indexed = {row["row_id"]: row for row in rows}
    try:
        for row_id, expected in gold["dates"].items():
            row = indexed[row_id]
            # The first converted date that disagrees is enough.
            if module.gregorian(row["dob"], row["era"]) != expected:
                return [HIJRI]
    except Exception:
        # A crash during conversion is the same run miss as a missing module.
        return [DATE_RUN]
    return []


def _clinics(folder: Path, rows: list[dict], gold: dict) -> list[str]:
    """Return the stale-code miss, or the run miss when the module is missing or crashes.

    The first row whose clinic disagrees is enough.
    """
    # A missing clinic module is the run miss, so no code is compared.
    module = _load(folder, "codes")
    if module is None:
        return [CODE_RUN]
    # Index the history by row so each gold clinic can find its source.
    indexed = {row["row_id"]: row for row in rows}
    try:
        for row_id, expected in gold["clinics"].items():
            row = indexed[row_id]
            # The first clinic that disagrees is enough.
            if module.clinic(row["clinic_code"], row["as_of"], row["facility"]) != expected:
                return [STALE]
    except Exception:
        # A crash during the lookup is the same run miss as a missing module.
        return [CODE_RUN]
    return []


def _clusters(folder: Path, rows: list[dict], waiting: list[dict], gold: dict) -> list[str]:
    """Return the cluster misses.

    A missing module or a crash is the run miss. A pair that lands in the same group is a merge: mother and newborn, twins, or a reused record. A count that equals the number of rows, and is not the gold patient count, means rows were used as patients. A general mismatch is added only when none of those specific misses was already recorded, and the groups, the removals, or the count still disagree.
    """
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
    # The count equals the number of rows, so rows were used as patients.
    if count == len(rows) and count != gold["patient_count"]:
        problems.append(ROWS)
    matched = groups == gold["groups"] and removed == gold["removals"] and count == gold["patient_count"]
    # A general mismatch is reported only when a mother, twin, or reused-record merge was not already named.
    if not matched and not problems:
        problems.append(MATCH)
    return problems


def _together(groups: list[list[str]], pair: list[str]) -> bool:
    """Return true when both ids in the pair sit in the same group.

    That is a bad merge. Separate groups are fine.
    """
    left, right = pair
    return any(left in group and right in group for group in groups)


def _normalize(groups) -> list[list[str]]:
    """Return the groups as sorted lists of strings, themselves sorted.

    Order from the participant does not matter. The comparison with gold is on this normalized shape.
    """
    return sorted(sorted(str(item) for item in group) for group in groups)


def _load(folder: Path, name: str):
    """Return the imported module, or nothing when the file is missing or the import fails.

    A missing file and a failed import are the same outcome so the caller can report a run miss.
    """
    # A missing file is the same as a failed import. The caller reports a run miss either way.
    if not (folder / f"{name}.py").is_file():
        return None
    try:
        return load_module(folder, name)
    except Exception:
        return None


def _jsonl(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
