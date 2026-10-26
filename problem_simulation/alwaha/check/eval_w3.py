"""chk-w3-eval, draft. A miss does not print a log id, a visit count, or an F1.

Draft evaluation check. It grades extraction, citation, and journey scores against the held-out slice and its budget, the forecast against the later window, and the names of the planted failures. Notes are graded even when the harness crashes. A log id, a visit count, or a score is not printed.
"""

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
    """Return the evaluation misses.

    A planted token returns only the watermark. Notes are graded first. A crash while loading the harness adds the run miss and returns. Otherwise the score, forecast, and failure probes each add their misses.
    """
    # A planted token returns only the watermark, so the notes are not graded after it.
    if contains_canary(work, canary):
        return [WATERMARK]
    # Notes are graded first so a later crash still reports them.
    problems = note_problems(work)
    try:
        modules = load_harness(work)
    except Exception:
        # A crash while loading the harness adds the run miss and stops the probes.
        problems.append(RUN)
        return problems
    # Score, forecast, and failure probes each add their misses once.
    for item in score_problems(modules["score"], gold):
        _once(problems, item)
    for item in forecast_problems(modules["forecast"], read_demand(pack), gold):
        _once(problems, item)
    for item in failure_problems(modules["failures"], read_failures(pack), gold):
        _once(problems, item)
    return problems


def load_harness(work: Path) -> dict:
    """Import the failure, forecast, and score modules and return them.

    Each name is removed before and after the load so an earlier import cannot satisfy the check.
    """
    for name in _MODULES:
        sys.modules.pop(name, None)
    folder = work / "app"
    loaded = {name: load_module(folder, name) for name in _MODULES}
    for name in _MODULES:
        sys.modules.pop(name, None)
    return loaded


def score_problems(module, gold: dict) -> list[str]:
    """Return the score misses.

    Each metric is called on its own rows. A crash on one metric is the run miss and the loop continues, so the other metrics are still graded. A score that is not close to gold, or that sits under the budget floor, is that metric's miss.
    """
    problems = []
    scored = gold["held_score"]
    # Each metric is called on its own rows. The message is the miss for that metric.
    checks = (
        (EXTRACT, "extraction", "extraction_f1", scored["extraction"]),
        (CITE, "citation", "citation_accuracy", scored["citation"]),
        (JOURNEY, "journey", "journey_pass", scored["journey"]),
    )
    for message, metric, method, rows in checks:
        try:
            got = getattr(module, method)(rows)
        except Exception:
            # A crash on one metric is the run miss. The other metrics are still graded.
            problems.append(RUN)
            continue
        # A score that is not close to gold, or that sits under the budget floor, is that metric's miss.
        if not _close(got, gold["metrics"][metric], gold["budgets"][metric]):
            problems.append(message)
    return problems


def forecast_problems(module, rows: list[dict], gold: dict) -> list[str]:
    """Return the forecast miss.

    A crash, or a later window that cannot be built from the fit window, is the run miss. If every predicted key sits in the fit year, the forecast scored the fit window. If the prediction equals the fit window copied onto the later year, the campaign was ignored. Any other disagreement with the later window is the later-window miss. An exact later window is a pass.
    """
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
    # Every predicted key sits in the fit year, so the forecast scored the fit window instead of the later one.
    if actual and {key[1] for key in actual} == {fit_year}:
        return [FIT]
    try:
        copied = {(district, later_year, month): fit[(district, fit_year, month)] for district, _year, month in later}
    except KeyError:
        return [RUN]
    # The prediction is the fit window copied forward, so the campaign was ignored.
    if actual == copied:
        return [IGNORE]
    if actual != later:
        return [LATER]
    return []


def failure_problems(module, rows: list[dict], gold: dict) -> list[str]:
    """Return the naming miss.

    A crash is the run miss. No rows, or any row whose class disagrees with gold, is the naming miss.
    """
    types = {row["log_id"]: row["type"] for row in gold["failures"]}
    try:
        named = [module.classify(row) == types[row["log_id"]] for row in rows]
    except Exception:
        return [RUN]
    # An empty failure file is not a pass. One misnamed row fails the probe.
    if not rows or not all(named):
        return [NAME]
    return []


def read_demand(pack: Path) -> list[dict]:
    """Return the demand rows from the pack as dictionaries.

    The header row becomes the keys.
    """
    with (pack / "demand" / "ophth.csv").open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_failures(pack: Path) -> list[dict]:
    """Return the planted-failure rows from the pack."""
    return _jsonl(pack / "slices" / "failures.jsonl")


def _close(got, expect: float, floor: float) -> bool:
    """Return true when the value is a real number, is close to the expected score, and meets the floor.

    A boolean is rejected. A close score that sits under the floor still fails.
    """
    if isinstance(got, bool) or not isinstance(got, (int, float)):
        return False
    return math.isclose(float(got), expect, abs_tol=_TOLERANCE) and float(got) + 1e-9 >= floor


def _keyed(rows: list[dict]) -> dict[tuple, int]:
    """Return the demand rows keyed by district, year, and month, with the visit count as the value."""
    return {(row["district"], int(row["year"]), int(row["month"])): int(row["visits"]) for row in rows}


def _jsonl(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)
