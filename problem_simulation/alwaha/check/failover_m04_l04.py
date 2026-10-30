"""chk-slo, failover portion. The Lesson 3 load portion stays on rel-m04-l03.

Failover portion of the service check. The load portion stays on the earlier release. This portion grades placement on both sites, serving from the surviving site, recovery time, model hashes, the insurance breaker, the patient reply while the model is down, the purchase choice, and the hospital split. Gold is unused because every input comes from the pack. Notes are graded last.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_m04_l04 import note_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.m04_l04_rules import choice, pending_ids, split

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
    """Append the miss when that sentence is not already in the list."""
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _placed(module, sites: dict) -> list[str]:
    """Return the one-replica miss unless the placement is exactly the two site names.

    A crash is the harness miss. A result that is not a list is treated as empty and fails.
    """
    try:
        got = module.placed(sites)
    except Exception:
        return [RUN]
    names = sorted(str(item) for item in got) if isinstance(got, list) else []
    if names != _SITES:
        return [ONE]
    return []


def _choose(module, sites: dict) -> list[str]:
    """Return the serving miss unless the chosen site is the surviving site.

    A crash is the harness miss.
    """
    try:
        got = module.choose(sites)
    except Exception:
        return [RUN]
    if got != "site-b":
        return [SERVING]
    return []


def _recover(module, drill: dict, rows: list[dict]) -> list[str]:
    """Return the recovery misses.

    A crash is the harness miss. A result that is not a record fails serving, time, and the in-flight list together. The site must be the surviving site. A duration that is not a whole number is treated as over the budget. A missing pending list is empty, which does not match the in-flight ids.
    """
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
    # A duration that is not a whole number is treated as over the budget, so the time miss still fires.
    except (TypeError, ValueError):
        seconds = int(drill["budget_seconds"]) + 1
    if seconds > int(drill["budget_seconds"]):
        problems.append(TIME)
    # A missing pending list is empty, which does not match the in-flight ids.
    pending = got.get("pending")
    if list(pending or []) != pending_ids(rows):
        problems.append(DROPPED)
    return problems


def _hashes(module, sites: dict) -> list[str]:
    """Return the hash miss unless the surviving site confirms every model id from the first site.

    A crash is the harness miss. A result that is not a list fails.
    """
    # The surviving site has to confirm the model ids from the first site.
    site_a = sites["sites"][0]
    site_b = sites["sites"][1]
    try:
        got = module.confirm(site_b, site_a["models"])
    except Exception:
        # A crash is the harness miss, so the ids are not compared.
        return [RUN]
    # A result that is not a list fails the hash check.
    if not isinstance(got, list):
        return [HASH]
    names = sorted(str(item) for item in got)
    expect = sorted(str(row["id"]) for row in site_a["models"])
    # Order does not matter. The confirmed ids must be the first site's model ids.
    if names != expect:
        return [HASH]
    return []


def _book(module, outage: dict) -> list[str]:
    """Return the breaker misses.

    A crash is the harness miss. A result that is not a record fails both the wait and the partner. No wait value, a wait above zero, a non-numeric wait, or a call that still went out means the booking path waited. Naming the partner as the target treats insurance as a site.
    """
    try:
        got = module.book(outage)
    except Exception:
        return [RUN]
    if not isinstance(got, dict):
        return [WAIT, PARTNER]
    problems = []
    waited = got.get("waited")
    try:
        # No wait value, or a wait above zero, means the booking path waited.
        slow = waited is None or int(waited) > 0
    # A wait that is not a whole number is treated as waiting.
    except (TypeError, ValueError):
        slow = True
    if slow or bool(got.get("called")):
        problems.append(WAIT)
    # Naming the partner as the target treats insurance as a site.
    if str(got.get("target") or "") == "insure":
        problems.append(PARTNER)
    return problems


def _reply(module, spec: dict) -> list[str]:
    """Return the closed-fail miss.

    A crash or a non-record fails the probe. A status row must stay a status reply with the same body. Any other row must fall back to the rules worker while the model is down. The first disagreement returns.
    """
    for row in spec.get("rows") or []:
        try:
            got = module.reply(row, False)
        except Exception:
            return [RUN]
        if not isinstance(got, dict):
            return [CLOSED]
        # A status row must stay a status reply. Any other row must fall back to the rules worker.
        if row.get("kind") == "status":
            if got.get("mode") != "status" or got.get("body") != row.get("text"):
                return [CLOSED]
        elif got.get("mode") != "rules-worker":
            return [CLOSED]
    return []


def _choice(module, note: dict) -> list[str]:
    """Return the purchase miss when the choice disagrees with the reference.

    A crash is the harness miss.
    """
    try:
        got = module.choice(note)
    except Exception:
        return [RUN]
    if got != choice(note):
        return [PURCHASE]
    return []


def _split(module, sheet: dict) -> list[str]:
    """Return the split miss when the hospital split disagrees with the reference.

    A crash is the harness miss. One figure for every hospital disagrees with the per-hospital split.
    """
    price = int(sheet["local_per_1k"])
    try:
        got = module.split(sheet, price)
    except Exception:
        return [RUN]
    if got != split(sheet, price):
        return [SPLIT]
    return []


def failover_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the failover misses and then the note misses.

    Gold is discarded because every input is a pack file. A planted token returns only the watermark. The eight probes run under one import. A crash of that import is the harness miss. Notes are graded afterward.
    """
    # Gold is unused. Every input is a pack file. The caller still loads the release so a missing pack fails first.
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
