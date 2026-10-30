"""slice-lora. The prompt baseline and ext-large at the cap must lose.

This slice grades the prompt baseline and the large external model against the price cap. The prompt baseline must not clear both floors. The large model must not be chosen while its price sits inside the cap. The shared model grader also runs. A planted token stops the check. Prices and scores are not printed.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.model_m03_l02 import RUN, _code, _modules, _once, _pack, _score
from alwaha.check.tables import contains_canary
from alwaha.engagement.m03_l02_rules import extraction_f1, intent_f1

CLEARS = "the prompt baseline clears the slice"
EXT = "ext-large at the price cap does not clear the slice"


def lora_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the adapter-slice misses.

    If gold already places the external price inside the cap, that miss is recorded before the adapter runs. The prompt baseline is then scored on the held letters and the held messages. Clearing both floors is the baseline miss. The shared code grader adds the model misses. A quote that selects the large model at or under the cap records the cap miss again, once. A crash adds the run miss and returns what was already found.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    problems: list[str] = []
    # The external price is already inside the cap, so the slice fails before the adapter runs.
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
    # A prompt baseline that clears both floors has cleared the slice, which this check exists to reject.
    if prompt_extract >= floor and prompt_intent >= floor:
        _once(problems, CLEARS)
    _code(problems, modules, pack_rows, gold, scores)
    quote = scores["quote"]
    # Choosing the large external model at or under the cap fails the slice. A missing price uses the default in this lookup, so it still counts as inside the cap.
    if quote.get("model") == "ext-large" and quote.get("sar", 0) <= pack_rows["cap"]["max_sar"]:
        _once(problems, EXT)
    return problems
