"""chk-w4-slo, load portion. Day 4 adds failover to this check.

Load portion of the service check. It grades which adapters load, whether the backlog hours match the forecast, whether chat latency is reserved while the batch runs, whether scale leads the peak by the cold start, whether today's price is used, and whether the capacity table matches the plan. Notes are graded after the probes so a crash does not hide them. The failover half of this check is a later day.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d3 import note_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d3_rules import approved, hours_for, plan, started_at

BACKLOG = "the backlog misses 48 hours"
LATENCY = "chat misses its latency while the batch runs"
MISSING = "a registered adapter is missing"
RUN = "the harness did not run"
TABLE = "the capacity table misses the backlog or the price"
UNREGISTERED = "an unregistered hash is loaded"
WINDOW = "reactive scaling misses the first window"
YESTERDAY = "the plan still uses yesterday's price"
_MODULES = ("adapters", "batch", "quota", "scale", "price", "capacity")


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _adapters(module, registry: dict, candidate: dict) -> list[str]:
    """Return the adapter misses.

    A crash is the harness miss. A result that is not a list is both a missing adapter and an unregistered load. An exact match with the approved names passes. A missing approved name is the missing miss. A loaded name that is the candidate or the external model is the unregistered miss. Any other disagreement is still reported as missing.
    """
    try:
        got = module.loaded(registry, candidate)
    except Exception:
        return [RUN]
    # A result that is not a list is both a missing adapter and an unregistered load.
    if not isinstance(got, list):
        return [MISSING, UNREGISTERED]
    names = sorted(str(item) for item in got)
    expect = approved(registry)
    if names == expect:
        return []
    problems = []
    blocked = {str(candidate.get("id") or ""), "ext-large"}
    if any(name not in names for name in expect):
        problems.append(MISSING)
    if any(name in blocked for name in names):
        problems.append(UNREGISTERED)
    # The loaded names differ from the approved names, but neither a missing approved name nor a blocked name was found, so it is still reported as missing.
    if not problems:
        problems.append(MISSING)
    return problems


def _hours(module, sheet: dict, forecast: dict) -> list[str]:
    """Return the backlog miss when the hours disagree with the reference.

    A crash is the harness miss. The reference uses the batched throughput, the referral count, and the tokens per referral.
    """
    try:
        got = module.hours(sheet, forecast)
    except Exception:
        return [RUN]
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    expect = hours_for(int(sheet["local_batched_tps"]), referrals, tokens_each)
    if got != expect:
        return [BACKLOG]
    return []


def _latency(module, sheet: dict) -> list[str]:
    """Return the latency miss when chat latency is not the reserved value on the sheet.

    A crash is the harness miss.
    """
    try:
        got = module.latency(sheet)
    except Exception:
        return [RUN]
    if got != int(sheet["chat_p95_reserved_ms"]):
        return [LATENCY]
    return []


def _scale(module, forecast: dict, sheet: dict) -> list[str]:
    """Return the window miss when the start time is not the peak minus the cold start.

    A crash is the harness miss.
    """
    try:
        got = module.started(forecast, sheet)
    except Exception:
        return [RUN]
    expect = started_at(str(forecast["peak_at"]), int(sheet["cold_start_seconds"]))
    if got != expect:
        return [WINDOW]
    return []


def _price(module, today: dict, old: int) -> list[str]:
    """Return the yesterday miss when the rate is not today's price.

    The old price is passed in so a module that still uses it disagrees. A crash is the harness miss.
    """
    try:
        got = module.rate(today, {"price.ext_large_per_1k": old})
    except Exception:
        return [RUN]
    if got != int(today["sar"]):
        return [YESTERDAY]
    return []


def _table(module, sheet: dict, forecast: dict, today: dict) -> list[str]:
    """Return the table miss when the returned record disagrees with the plan on any field.

    A crash, a non-record, or one wrong field is the same miss.
    """
    expect = plan(sheet, forecast, int(today["sar"]))
    try:
        got = module.table(expect)
    except Exception:
        return [RUN]
    if not isinstance(got, dict) or any(got.get(key) != value for key, value in expect.items()):
        return [TABLE]
    return []


def slo_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the load misses and then the note misses.

    A planted token returns only the watermark. The six probes run under one import. A crash of that import is the harness miss. Notes are graded afterward so they survive that crash.
    """
    # A planted token returns only the watermark, so the probes are not run.
    if contains_canary(work, canary):
        return [WATERMARK]
    # The registry, the candidate, the sheet, the forecast, and today's price come from the pack.
    registry = json.loads((pack / "registry" / "adapters.json").read_text(encoding="utf-8"))
    candidate = json.loads((pack / "registry" / "candidate.json").read_text(encoding="utf-8"))
    sheet = json.loads((pack / "serving" / "throughput.json").read_text(encoding="utf-8"))
    forecast = json.loads((pack / "forecast" / "p-forecast.json").read_text(encoding="utf-8"))
    today = json.loads((pack / "finance" / "price-today.json").read_text(encoding="utf-8"))
    problems: list[str] = []
    try:
        with modules(work / "app", _MODULES) as loaded:
            # Adapters, backlog hours, chat latency, scale, price, and the capacity table.
            for item in _adapters(loaded["adapters"], registry, candidate):
                _once(problems, item)
            for item in _hours(loaded["batch"], sheet, forecast):
                _once(problems, item)
            for item in _latency(loaded["quota"], sheet):
                _once(problems, item)
            for item in _scale(loaded["scale"], forecast, sheet):
                _once(problems, item)
            for item in _price(loaded["price"], today, int(gold["old_price"])):
                _once(problems, item)
            for item in _table(loaded["capacity"], sheet, forecast, today):
                _once(problems, item)
    except Exception:
        # A crash of the import is the harness miss. Notes are still graded below.
        _once(problems, RUN)
    for item in note_problems(work):
        _once(problems, item)
    return problems
