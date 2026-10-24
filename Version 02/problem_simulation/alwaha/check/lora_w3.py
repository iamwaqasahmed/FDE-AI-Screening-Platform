"""slice-lora. The prompt baseline and ext-large at the cap must lose."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.model_w3 import RUN, _code, _modules, _once, _pack, _score
from alwaha.check.tables import contains_canary
from alwaha.engagement.w3d2_rules import extraction_f1, intent_f1

CLEARS = "the prompt baseline clears the slice"
EXT = "ext-large at the price cap does not clear the slice"


def lora_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    problems: list[str] = []
    if gold["external_sar"] <= gold["cap"]["max_sar"]:
        _once(problems, EXT)
    try:
        modules = _modules(work)
        pack_rows = _pack(pack)
        scores = _score(modules, pack_rows, gold)
        prompt = modules["prompt"]
        letters = gold["held_letters"]
        messages = gold["held_messages"]
        prompt_extract = extraction_f1(letters, [prompt.extract(row) for row in letters])
        prompt_intent = intent_f1(messages, [prompt.intent(row) for row in messages])
    except Exception:
        problems.append(RUN)
        return problems
    floor = gold["cap"]["f1_floor"]
    if prompt_extract >= floor and prompt_intent >= floor:
        _once(problems, CLEARS)
    _code(problems, modules, pack_rows, gold, scores)
    quote = scores["quote"]
    if quote.get("model") == "ext-large" and quote.get("sar", 0) <= pack_rows["cap"]["max_sar"]:
        _once(problems, EXT)
    return problems
