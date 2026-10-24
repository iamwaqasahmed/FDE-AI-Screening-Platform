"""chk-w4-slo, failover portion. The Day 3 load portion stays on rel-w4d3."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d4 import note_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d4_rules import choice, pending_ids, split

CLOSED = "the patient reply fails closed when the model is down"
DROPPED = "an in-flight approval is dropped"
HASH = "the hash on site-b does not match the register"
ONE = "traffic stays on one replica"
PARTNER = "insurance is treated as a site"
PURCHASE = "the purchase route misses Ramadan"
RUN = "the harness did not run"
SERVING = "site-b is not serving after the drill"
SPLIT = "the hospital split uses one figure for every hospital"
TIME = "failover misses its time"
WAIT = "the booking path waits on insure"
_MODULES = ("replicas", "route", "failover", "hashes", "breaker", "degrade", "procure", "hospitals")
_SITES = ["site-a", "site-b"]


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _placed(module, sites: dict) -> list[str]:
    try:
        got = module.placed(sites)
    except Exception:
        return [RUN]
    names = sorted(str(item) for item in got) if isinstance(got, list) else []
    if names != _SITES:
        return [ONE]
    return []


def _choose(module, sites: dict) -> list[str]:
    try:
        got = module.choose(sites)
    except Exception:
        return [RUN]
    if got != "site-b":
        return [SERVING]
    return []


def _recover(module, drill: dict, rows: list[dict]) -> list[str]:
    try:
        got = module.recover(drill, rows)
    except Exception:
        return [RUN]
    if not isinstance(got, dict):
        return [SERVING, TIME, DROPPED]
    problems = []
    if str(got.get("site") or "") != "site-b":
        problems.append(SERVING)
    try:
        seconds = int(got.get("seconds"))
    except (TypeError, ValueError):
        seconds = int(drill["budget_seconds"]) + 1
    if seconds > int(drill["budget_seconds"]):
        problems.append(TIME)
    pending = got.get("pending")
    if list(pending or []) != pending_ids(rows):
        problems.append(DROPPED)
    return problems


def _hashes(module, sites: dict) -> list[str]:
    site_a = sites["sites"][0]
    site_b = sites["sites"][1]
    try:
        got = module.confirm(site_b, site_a["models"])
    except Exception:
        return [RUN]
    if not isinstance(got, list):
        return [HASH]
    names = sorted(str(item) for item in got)
    expect = sorted(str(row["id"]) for row in site_a["models"])
    if names != expect:
        return [HASH]
    return []


def _book(module, outage: dict) -> list[str]:
    try:
        got = module.book(outage)
    except Exception:
        return [RUN]
    if not isinstance(got, dict):
        return [WAIT, PARTNER]
    problems = []
    waited = got.get("waited")
    try:
        slow = waited is None or int(waited) > 0
    except (TypeError, ValueError):
        slow = True
    if slow or bool(got.get("called")):
        problems.append(WAIT)
    if str(got.get("target") or "") == "insure":
        problems.append(PARTNER)
    return problems


def _reply(module, spec: dict) -> list[str]:
    for row in spec.get("rows") or []:
        try:
            got = module.reply(row, False)
        except Exception:
            return [RUN]
        if not isinstance(got, dict):
            return [CLOSED]
        if row.get("kind") == "status":
            if got.get("mode") != "status" or got.get("body") != row.get("text"):
                return [CLOSED]
        elif got.get("mode") != "rules-worker":
            return [CLOSED]
    return []


def _choice(module, note: dict) -> list[str]:
    try:
        got = module.choice(note)
    except Exception:
        return [RUN]
    if got != choice(note):
        return [PURCHASE]
    return []


def _split(module, sheet: dict) -> list[str]:
    price = int(sheet["local_per_1k"])
    try:
        got = module.split(sheet, price)
    except Exception:
        return [RUN]
    if got != split(sheet, price):
        return [SPLIT]
    return []


def failover_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    sites = json.loads((pack / "sites" / "replicas.json").read_text(encoding="utf-8"))
    drill = json.loads((pack / "drill" / "site-a.json").read_text(encoding="utf-8"))
    rows = _rows(pack / "workflow" / "inflight.jsonl")
    outage = json.loads((pack / "insure" / "outage.json").read_text(encoding="utf-8"))
    note = json.loads((pack / "finance" / "lead-time.json").read_text(encoding="utf-8"))
    sheet = json.loads((pack / "hospitals" / "shares.json").read_text(encoding="utf-8"))
    down = json.loads((pack / "serving" / "model-down.json").read_text(encoding="utf-8"))
    problems: list[str] = []
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _placed(loaded["replicas"], sites):
                _once(problems, item)
            for item in _choose(loaded["route"], sites):
                _once(problems, item)
            for item in _recover(loaded["failover"], drill, rows):
                _once(problems, item)
            for item in _hashes(loaded["hashes"], sites):
                _once(problems, item)
            for item in _book(loaded["breaker"], outage):
                _once(problems, item)
            for item in _reply(loaded["degrade"], down):
                _once(problems, item)
            for item in _choice(loaded["procure"], note):
                _once(problems, item)
            for item in _split(loaded["hospitals"], sheet):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    for item in note_problems(work):
        _once(problems, item)
    return problems
