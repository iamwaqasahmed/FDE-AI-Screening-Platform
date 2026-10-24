"""chk-w3-eval, draft. A miss does not print a log id, a visit count, or an F1."""

from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_w3d4 import note_problems
from alwaha.check.tables import contains_canary

CITE = "the citation score misses the held-out slice"
EXTRACT = "the extraction score misses the held-out slice"
FIT = "the forecast scores the fit window"
IGNORE = "the forecast ignores the campaign"
JOURNEY = "the journey score misses the held-out slice"
LATER = "the forecast misses the later window"
NAME = "a planted failure is misnamed"
RUN = "the harness did not run"
_MODULES = ("failures", "forecast", "score")
_TOLERANCE = 0.02


def eval_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = note_problems(work)
    try:
        modules = load_harness(work)
    except Exception:
        problems.append(RUN)
        return problems
    for item in score_problems(modules["score"], gold):
        _once(problems, item)
    for item in forecast_problems(modules["forecast"], read_demand(pack), gold):
        _once(problems, item)
    for item in failure_problems(modules["failures"], read_failures(pack), gold):
        _once(problems, item)
    return problems


def load_harness(work: Path) -> dict:
    for name in _MODULES:
        sys.modules.pop(name, None)
    folder = work / "app"
    loaded = {name: load_module(folder, name) for name in _MODULES}
    for name in _MODULES:
        sys.modules.pop(name, None)
    return loaded


def score_problems(module, gold: dict) -> list[str]:
    problems = []
    scored = gold["held_score"]
    checks = (
        (EXTRACT, "extraction", "extraction_f1", scored["extraction"]),
        (CITE, "citation", "citation_accuracy", scored["citation"]),
        (JOURNEY, "journey", "journey_pass", scored["journey"]),
    )
    for message, metric, method, rows in checks:
        try:
            got = getattr(module, method)(rows)
        except Exception:
            problems.append(RUN)
            continue
        if not _close(got, gold["metrics"][metric], gold["budgets"][metric]):
            problems.append(message)
    return problems


def forecast_problems(module, rows: list[dict], gold: dict) -> list[str]:
    try:
        got = module.predict(rows)
        actual = _keyed(got)
    except Exception:
        return [RUN]
    later_year = gold["later_window"]["year"]
    fit_year = gold["fit_window"]["year"]
    months = tuple(gold["later_window"]["months"])
    packed = _keyed(rows)
    later = {key: value for key, value in packed.items() if key[1] == later_year and key[2] in months}
    fit = {key: value for key, value in packed.items() if key[1] == fit_year and key[2] in months}
    if actual and {key[1] for key in actual} == {fit_year}:
        return [FIT]
    try:
        copied = {(district, later_year, month): fit[(district, fit_year, month)] for district, _year, month in later}
    except KeyError:
        return [RUN]
    if actual == copied:
        return [IGNORE]
    if actual != later:
        return [LATER]
    return []


def failure_problems(module, rows: list[dict], gold: dict) -> list[str]:
    types = {row["log_id"]: row["type"] for row in gold["failures"]}
    try:
        named = [module.classify(row) == types[row["log_id"]] for row in rows]
    except Exception:
        return [RUN]
    if not rows or not all(named):
        return [NAME]
    return []


def read_demand(pack: Path) -> list[dict]:
    with (pack / "demand" / "ophth.csv").open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_failures(pack: Path) -> list[dict]:
    return _jsonl(pack / "slices" / "failures.jsonl")


def _close(got, expect: float, floor: float) -> bool:
    if isinstance(got, bool) or not isinstance(got, (int, float)):
        return False
    return math.isclose(float(got), expect, abs_tol=_TOLERANCE) and float(got) + 1e-9 >= floor


def _keyed(rows: list[dict]) -> dict[tuple, int]:
    return {(row["district"], int(row["year"]), int(row["month"])): int(row["visits"]) for row in rows}


def _jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)
