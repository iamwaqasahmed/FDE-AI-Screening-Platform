"""chk-w4-slo, load portion. Day 4 adds failover to this check."""

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
    if item not in problems:
        problems.append(item)


def _adapters(module, registry: dict, candidate: dict) -> list[str]:
    try:
        got = module.loaded(registry, candidate)
    except Exception:
        return [RUN]
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
    if not problems:
        problems.append(MISSING)
    return problems


def _hours(module, sheet: dict, forecast: dict) -> list[str]:
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
    try:
        got = module.latency(sheet)
    except Exception:
        return [RUN]
    if got != int(sheet["chat_p95_reserved_ms"]):
        return [LATENCY]
    return []


def _scale(module, forecast: dict, sheet: dict) -> list[str]:
    try:
        got = module.started(forecast, sheet)
    except Exception:
        return [RUN]
    expect = started_at(str(forecast["peak_at"]), int(sheet["cold_start_seconds"]))
    if got != expect:
        return [WINDOW]
    return []


def _price(module, today: dict, old: int) -> list[str]:
    try:
        got = module.rate(today, {"price.ext_large_per_1k": old})
    except Exception:
        return [RUN]
    if got != int(today["sar"]):
        return [YESTERDAY]
    return []


def _table(module, sheet: dict, forecast: dict, today: dict) -> list[str]:
    expect = plan(sheet, forecast, int(today["sar"]))
    try:
        got = module.table(expect)
    except Exception:
        return [RUN]
    if not isinstance(got, dict) or any(got.get(key) != value for key, value in expect.items()):
        return [TABLE]
    return []


def slo_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    registry = json.loads((pack / "registry" / "adapters.json").read_text(encoding="utf-8"))
    candidate = json.loads((pack / "registry" / "candidate.json").read_text(encoding="utf-8"))
    sheet = json.loads((pack / "serving" / "throughput.json").read_text(encoding="utf-8"))
    forecast = json.loads((pack / "forecast" / "p-forecast.json").read_text(encoding="utf-8"))
    today = json.loads((pack / "finance" / "price-today.json").read_text(encoding="utf-8"))
    problems: list[str] = []
    try:
        with modules(work / "app", _MODULES) as loaded:
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
        _once(problems, RUN)
    for item in note_problems(work):
        _once(problems, item)
    return problems
