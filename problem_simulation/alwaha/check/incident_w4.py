"""chk-w4-incident. A miss does not print a timestamp, a hash, a rate, or a cost.

This check grades the trace, the dashboard, cost by hospital, drift names, the override rate, and shadow traffic. Shadow traffic must not change the patient reply, and a hash must not be promoted without a comparison. Notes from the incident day are graded too. A timestamp, a hash, a rate, or a cost is not printed.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d2 import ALERT, CPU
from alwaha.check.notes_w4d2 import note_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d2_rules import board, cost, label, promote, rate, read_span, reply

COST = "cost is missing a hospital"
PROMOTE = "a hash is promoted with no comparison"
RATE = "the override rate is missing"
RUN = "the harness did not run"
SHADOW = "shadow traffic changes the patient reply"
TRACE = "the trace is missing a tool, a hash, or a token count"
UNNAMED = "a drift is unnamed"
_MODULES = ("spans", "dashboard", "meter", "drift", "override", "shadow")


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _close(got, expect: float) -> bool:
    """Return true when the value is a real number and matches the expected value within the tight tolerance.

    A boolean is an integer in Python, so it is rejected before the comparison.
    """
    return isinstance(got, (int, float)) and not isinstance(got, bool) and abs(float(got) - expect) <= 1e-9


def _trace(module, span: dict) -> list[str]:
    """Return the trace miss.

    A crash, a missing token count, a wrong tool, a wrong hash, or a wrong token count is the same miss.
    """
    try:
        got = module.read(span)
        tokens = int(got.get("tokens"))
    except Exception:
        return [TRACE]
    expect = read_span(span)
    if not isinstance(got, dict) or got.get("tool") != expect["tool"] or got.get("hash") != expect["hash"]:
        return [TRACE]
    if tokens != expect["tokens"]:
        return [TRACE]
    return []


def _board(module, spans: list[dict]) -> list[str]:
    """Return the dashboard misses.

    A crash is the harness miss. A result that is not a record fails both the metric miss and the alert miss. A missing metric, or a metric that is not close, is the CPU miss. A wrong alert instant is the alert miss.
    """
    try:
        got = module.board(spans)
    except Exception:
        return [RUN]
    # A result that is not a record fails both the metric miss and the alert miss.
    if not isinstance(got, dict):
        return [CPU, ALERT]
    expect = board(spans)
    problems = []
    metrics = ("error_rate", "latency_p95", "tool_failures")
    if any(key not in got for key in metrics) or any(not _close(got[key], expect[key]) for key in metrics):
        problems.append(CPU)
    if got.get("alert_at") != expect["alert_at"]:
        problems.append(ALERT)
    return problems


def _cost(module, rows: list[dict]) -> list[str]:
    """Return the cost miss.

    A crash is the harness miss. A result that is not a record, a missing hospital, or an amount that is not close is the cost miss.
    """
    try:
        got = module.cost(rows)
    except Exception:
        return [RUN]
    expect = cost(rows)
    if not isinstance(got, dict):
        return [COST]
    if set(expect) - set(got) or any(not _close(got.get(key), value) for key, value in expect.items()):
        return [COST]
    return []


def _drift(module, rows: list[dict]) -> list[str]:
    """Return the unnamed-drift miss when any label disagrees with the reference.

    A crash is the harness miss.
    """
    try:
        labels = [module.name(row) for row in rows]
    except Exception:
        return [RUN]
    if labels != [label(row) for row in rows]:
        return [UNNAMED]
    return []


def _rate(module, rows: list[dict]) -> list[str]:
    """Return the override-rate miss when the rate is not the reference.

    A crash is the harness miss.
    """
    try:
        got = module.rate(rows)
    except Exception:
        return [RUN]
    if not _close(got, rate(rows)):
        return [RATE]
    return []


def _shadow(module, turn: dict) -> list[str]:
    """Return the shadow and promotion misses.

    The reply must match the reference, and the shadow text must not appear inside it. An uncompared hash must stay blocked. A compared match must be allowed. A crash in the reply is the harness miss. A crash in promotion adds the harness miss and keeps the reply miss.
    """
    problems = []
    try:
        got = module.reply(turn)
    except Exception:
        return [RUN]
    # The reply must match the reference, and the shadow text must not appear inside it.
    if got != reply(turn) or turn["shadow_reply"] in str(got):
        problems.append(SHADOW)
    bare = {"candidate_hash": turn["candidate_hash"], "compared": False, "matched": False}
    ready = {"candidate_hash": turn["candidate_hash"], "compared": True, "matched": True}
    try:
        blocked = module.promote(bare)
        opened = module.promote(ready)
    except Exception:
        problems.append(RUN)
        return problems
    if blocked != promote(bare):
        problems.append(PROMOTE)
    if opened != promote(ready):
        problems.append(PROMOTE)
    return problems


def incident_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the incident misses.

    A planted token returns only the watermark. The trace probe uses the first span that carries a token count. The other probes use their own pack files. Notes are graded last so a harness crash does not hide them. A crash of the import adds the harness miss.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    spans = _rows(pack / "replay" / "spans.jsonl")
    meter = _rows(pack / "meter" / "gateway.jsonl")
    actions = _rows(pack / "actions" / "overrides.jsonl")
    drifts = _rows(pack / "drifts" / "signals.jsonl")
    turn = json.loads((pack / "experiment" / "shadow-extract.json").read_text(encoding="utf-8"))
    # The span that carries a token count is the one the trace probe reads.
    shown = next(span for span in spans if span.get("tokens"))
    problems: list[str] = []
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _trace(loaded["spans"], shown):
                _once(problems, item)
            for item in _board(loaded["dashboard"], spans):
                _once(problems, item)
            for item in _cost(loaded["meter"], meter):
                _once(problems, item)
            for item in _drift(loaded["drift"], drifts):
                _once(problems, item)
            for item in _rate(loaded["override"], actions):
                _once(problems, item)
            for item in _shadow(loaded["shadow"], turn):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    for item in note_problems(work, gold):
        _once(problems, item)
    return problems
