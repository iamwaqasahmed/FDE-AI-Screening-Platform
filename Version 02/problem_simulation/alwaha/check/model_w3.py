"""chk-w3-model. A miss does not print a hash, a quota, a price, or an F1."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_w3d2 import (
    approach_problems,
    knowledge_problems,
    residency_problems,
    sprint_problems,
)
from alwaha.check.tables import contains_canary
from alwaha.engagement.w3d2_rules import extraction_f1, intent_f1

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
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = _notes(work, gold, None, None)
    try:
        modules = _modules(work)
        pack_rows = _pack(pack)
        scores = _score(modules, pack_rows, gold)
    except Exception:
        problems.append(RUN)
        return problems
    _code(problems, modules, pack_rows, gold, scores)
    measured = approach_problems(work, gold, scores["extraction"], scores["intent"])
    return _merge(problems, measured)


def _notes(work: Path, gold: dict, extraction: float | None, intent: float | None) -> list[str]:
    problems: list[str] = []
    problems.extend(sprint_problems(work))
    problems.extend(residency_problems(work))
    problems.extend(knowledge_problems(work))
    problems.extend(approach_problems(work, gold, extraction, intent))
    return problems


def _modules(work: Path) -> dict:
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
    return {
        "cap": _read(pack / "budget" / "price-cap.json"),
        "cloud": _read(pack / "fixtures" / "cloud.json"),
        "quota": _read(pack / "budget" / "quota.json"),
        "registry": _read(pack / "registry" / "reg-models.json"),
    }


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _score(modules: dict, pack_rows: dict, gold: dict) -> dict:
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
    if served.get("gpus", 0) > pack_rows["quota"]["gpus"]:
        _once(problems, GPU)
    _route(problems, modules["route"], pack_rows, gold)
    quote = scores["quote"]
    cap = pack_rows["cap"]
    if quote.get("sar", cap["max_sar"] + 1) > cap["max_sar"]:
        _once(problems, COST)
    if quote.get("seconds", cap["max_seconds"] + 1) > cap["max_seconds"]:
        _once(problems, LATENCY)


def _route(problems: list[str], route, pack_rows: dict, gold: dict) -> None:
    registry = pack_rows["registry"]
    phi_call = {"fields": ["national_id", "name"], "hash": gold["adapter_hash"], "model": "ext-large"}
    if route.allow(phi_call, registry):
        _once(problems, PHI)
    bad_call = {"fields": [], "hash": gold["cloud_hash"], "model": "local-small"}
    if route.allow(bad_call, registry):
        _once(problems, HASH)


def _merge(problems: list[str], measured: list[str]) -> list[str]:
    for item in measured:
        _once(problems, item)
    return problems


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)
