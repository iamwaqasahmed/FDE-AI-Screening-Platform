"""chk-m03-l02-model. A miss does not print a hash, a quota, a price, or an F1.

This check grades the served adapter: the prompt baseline must not stay served, protected fields must not go to the external model, both scores must clear the floor, the hash must be registered, the GPU count must fit the quota, and the quote must fit the price and latency caps. Notes are graded even when the adapter crashes. The approach table is graded once with no scores and again with the real scores. A hash, a quota, a price, or a score is not printed. The adapter slice calls the shared helpers here.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_m03_l02 import (
    approach_problems,
    knowledge_problems,
    residency_problems,
    sprint_problems,
)
from alwaha.check.tables import contains_canary
from alwaha.engagement.m03_l02_rules import extraction_f1, intent_f1

PROMPT = "the prompt baseline is still the served model"
EXTRACT = "extraction F1 is outside the budget"
INTENT = "intent F1 is outside the budget"
COST = "the cost is over the price cap"
PHI = "the call sends phi to ext-large"
HASH = "the hash is not on reg-models"
GPU = "the gpu count is over the quota"
LATENCY = "the latency is over the budget"
RUN = "the adapter did not run"
PHI_FIELDS = {"national_id", "date_of_birth", "name", "phone"}


def model_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the model misses.

    Notes are graded first, with no scores, so a crash still reports the table. A crash then adds the run miss and returns. When the adapter runs, the code grader adds the budget misses and the approach table is graded again with the real scores. The second pass can add a measurement the first pass skipped.
    """
    # A planted token returns only the watermark, so the notes are not graded after it.
    if contains_canary(work, canary):
        return [WATERMARK]
    # Notes are graded with no scores, so a crash still reports the table.
    problems = _notes(work, gold, None, None)
    try:
        modules = _modules(work)
        pack_rows = _pack(pack)
        # Scores, the served adapter, and the quote come from the participant modules.
        scores = _score(modules, pack_rows, gold)
    except Exception:
        # A crash adds the run miss and skips the code grader.
        problems.append(RUN)
        return problems
    # The code grader adds the budget misses.
    _code(problems, modules, pack_rows, gold, scores)
    # The approach table is graded again with the real scores.
    measured = approach_problems(work, gold, scores["extraction"], scores["intent"])
    return _merge(problems, measured)


def _notes(work: Path, gold: dict, extraction: float | None, intent: float | None) -> list[str]:
    """Return the sprint, residency, knowledge, and approach misses.

    The approach table is called with whatever scores the caller has. None means the measurement cells are not checked yet.
    """
    problems: list[str] = []
    problems.extend(sprint_problems(work))
    problems.extend(residency_problems(work))
    problems.extend(knowledge_problems(work))
    problems.extend(approach_problems(work, gold, extraction, intent))
    return problems


def _modules(work: Path) -> dict:
    """Import the adapter, cost, extract, intent, prompt, and route modules and return them.

    An import error propagates to the caller, which reports the run miss.
    """
    folder = work / "app"
    return {
        "adapter": load_module(folder, "adapter"),
        "cost": load_module(folder, "cost"),
        "extract": load_module(folder, "extract"),
        "intent": load_module(folder, "intent"),
        "prompt": load_module(folder, "prompt"),
        "route": load_module(folder, "route"),
    }


def _pack(pack: Path) -> dict:
    """Return the cap, the cloud fixture, the quota, and the model register from the pack.

    The steps read the price cap, the cloud fixture, the quota, and the model register from their pack paths.
    """
    return {
        "cap": _read(pack / "budget" / "price-cap.json"),
        "cloud": _read(pack / "fixtures" / "cloud.json"),
        "quota": _read(pack / "budget" / "quota.json"),
        "registry": _read(pack / "registry" / "reg-models.json"),
    }


def _read(path: Path) -> dict:
    """Return one JSON file as a dictionary."""
    return json.loads(path.read_text(encoding="utf-8"))


def _score(modules: dict, pack_rows: dict, gold: dict) -> dict:
    """Return the extraction score, the intent score, the served adapter, and the quote.

    Extraction and intent are scored on the held rows. The served record and the quote come from the participant modules.
    """
    letters = gold["held_letters"]
    messages = gold["held_messages"]
    extract = modules["extract"]
    intent = modules["intent"]
    return {
        "extraction": extraction_f1(letters, [extract.relabel(row) for row in letters]),
        "intent": intent_f1(messages, [intent.classify(row) for row in messages]),
        "served": modules["adapter"].serve(pack_rows["registry"], pack_rows["quota"], pack_rows["cloud"]),
        "quote": modules["cost"].quote(pack_rows["cap"], gold["prices"]),
    }


def _code(problems: list[str], modules: dict, pack_rows: dict, gold: dict, scores: dict) -> None:
    """Append the code misses.

    A served prompt baseline is a miss. A prompt target that carries protected fields to the external model is a miss. Each score under the floor is its own miss. A served hash other than the adapter hash is a miss. A GPU count above the quota is a miss. A missing GPU count is read as zero, which is not over the quota. The route probe is separate. A missing price or a missing latency is read as one past the cap, so a missing quote fails the cap.
    """
    prompt = modules["prompt"]
    if prompt.served():
        _once(problems, PROMPT)
    target = prompt.target()
    if target.get("phi") and target.get("model") == "ext-large":
        _once(problems, PHI)
    floor = gold["cap"]["f1_floor"]
    if scores["extraction"] < floor:
        _once(problems, EXTRACT)
    if scores["intent"] < floor:
        _once(problems, INTENT)
    served = scores["served"]
    if served.get("hash") != gold["adapter_hash"]:
        _once(problems, HASH)
    # A missing GPU count is read as zero, which is not over the quota. A count above the quota is the miss.
    if served.get("gpus", 0) > pack_rows["quota"]["gpus"]:
        _once(problems, GPU)
    _route(problems, modules["route"], pack_rows, gold)
    quote = scores["quote"]
    cap = pack_rows["cap"]
    # A missing price is read as one past the cap, so a quote that omits the price fails the cap.
    if quote.get("sar", cap["max_sar"] + 1) > cap["max_sar"]:
        _once(problems, COST)
    # A missing latency is read as one past the cap, so a quote that omits it fails the budget.
    if quote.get("seconds", cap["max_seconds"] + 1) > cap["max_seconds"]:
        _once(problems, LATENCY)


def _route(problems: list[str], route, pack_rows: dict, gold: dict) -> None:
    """Append the route misses.

    A call that carries protected fields to the external model must be refused. A call whose hash is not the adapter hash must be refused, even when the model name is the local one.
    """
    registry = pack_rows["registry"]
    phi_call = {"fields": ["national_id", "name"], "hash": gold["adapter_hash"], "model": "ext-large"}
    # A call that carries protected fields to the external model must be refused.
    if route.allow(phi_call, registry):
        _once(problems, PHI)
    bad_call = {"fields": [], "hash": gold["cloud_hash"], "model": "local-small"}
    # A call whose hash is not the adapter hash must be refused, even when the model name is the local one.
    if route.allow(bad_call, registry):
        _once(problems, HASH)


def _merge(problems: list[str], measured: list[str]) -> list[str]:
    """Return the first list with any new items from the second list appended once.

    This unions the unscored note pass with the scored approach pass.
    """
    for item in measured:
        _once(problems, item)
    return problems


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list."""
    if item not in problems:
        problems.append(item)
