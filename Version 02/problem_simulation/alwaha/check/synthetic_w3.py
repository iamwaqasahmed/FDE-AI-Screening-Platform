"""chk-w3-synthetic. A miss does not print a rate, a national id, or the watermark."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_w3d1 import classes_problems, knowledge_problems
from alwaha.check.tables import contains_canary

CARD = "the synthetic sample misses the fidelity card"
MARK = "the synthetic sample contains a watermark"
NID = "the synthetic sample contains a national id"
RUN = "the synthetic sample did not run"
SCAN = "the scan did not run"


def synthetic_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    if not (work / "app" / "synthetic.py").is_file():
        return [RUN]
    letters = _jsonl(pack / "letters" / "clerk.jsonl")
    try:
        module = load_module(work / "app", "synthetic")
        built = module.sample(letters, gold["fidelity"])
    except Exception:
        return [RUN]
    blob = json.dumps(built)
    problems = []
    if _misses(built, gold["fidelity"]):
        _once(problems, CARD)
    if canary in blob:
        _once(problems, MARK)
    if any(item and item in blob for item in gold["national_ids"]):
        _once(problems, NID)
    for item in _scan(work / "app", gold, canary):
        _once(problems, item)
    problems.extend(classes_problems(work))
    problems.extend(knowledge_problems(work))
    return problems


def _scan(folder: Path, gold: dict, canary: str) -> list[str]:
    if not (folder / "scan.py").is_file():
        return [SCAN]
    try:
        module = load_module(folder, "scan")
        problems = []
        if module.accept(canary, gold["national_ids"]):
            problems.append(MARK)
        probe = gold["national_ids"][0]
        if module.accept(probe, gold["national_ids"]):
            problems.append(NID)
        return problems
    except Exception:
        return [SCAN]


def _misses(rows, card: dict) -> bool:
    if not isinstance(rows, list) or not rows:
        return True
    low, high = card["sample_size"]
    if not low <= len(rows) <= high:
        return True
    rare = card["rare_sub_specialty"]
    if rare not in {row.get("sub_specialty") for row in rows}:
        return True
    for specialty, band in card["specialty_mix"].items():
        if not _inside(_share(rows, "specialty", specialty), band):
            return True
    kindly = sum(1 for row in rows if "kindly" in str(row.get("text", "")).lower()) / len(rows)
    if not _inside(kindly, card["phrase"]["kindly"]):
        return True
    return not _inside(_share(rows, "sub_specialty", rare), card["label_margin"][rare])


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _share(rows: list[dict], key: str, value: str) -> float:
    return sum(1 for row in rows if row.get(key) == value) / len(rows)


def _inside(value: float, band: list[float]) -> bool:
    return band[0] <= value <= band[1]


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
