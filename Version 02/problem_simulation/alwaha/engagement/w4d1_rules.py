"""Reference decisions for rel-w4d1. Participant copies do not import this module."""

from __future__ import annotations

import html
import re

from alwaha.engagement.w4d1_rows import HOLD_CAP, IN_FORCE, STORES, TOKEN_CAP

_CANARY = re.compile(r"CANARY-[0-9a-fA-F]+")
_NID = re.compile(r"NID-[0-9a-fA-F]+")


def screen(event: dict) -> dict:
    family = event.get("family")
    tool = event.get("tool") or None
    if family in {"atk-direct", "atk-indirect", "atk-prompt"}:
        return {"blocked": True, "held": False, "tool": None}
    if family == "atk-agency" and tool in {"book", "return"} and not event.get("approval_id"):
        return {"blocked": True, "held": True, "tool": None}
    return {"blocked": False, "held": False, "tool": tool}


def escape(text: str) -> str:
    return html.escape(text)


def accept_hash(candidate: str, approved: list[str]) -> str:
    if candidate in approved:
        return candidate
    return ""


def run_tool(description: str) -> str:
    del description
    return ""


def keep_label(row: dict) -> bool:
    return not row.get("poison")


def cite(doc: dict) -> str:
    if doc.get("status") == "in_force" and doc.get("audience") in {"public", "staff"}:
        return str(doc.get("doc_id") or "")
    return IN_FORCE


def clean(text: str) -> str:
    text = _CANARY.sub("[redacted]", text)
    return _NID.sub("[redacted]", text)


def admit(event: dict) -> bool:
    if event.get("family") == "atk-tokens":
        return int(event.get("tokens") or 0) <= TOKEN_CAP
    if event.get("family") == "atk-hoard":
        return int(event.get("holds") or 0) <= HOLD_CAP
    return True


def settle(grants: list[dict], as_of: str) -> list[dict]:
    out = []
    for grant in grants:
        row = dict(grant)
        kind = row.get("kind")
        if kind == "break-glass" and not row.get("audit"):
            row["audit"] = "audit-" + str(row.get("id") or "")
            row["status"] = "open"
        elif (row.get("end") or "") < as_of and kind in {"staff", "delegate"}:
            row["status"] = "closed"
        else:
            row["status"] = "open"
        out.append(row)
    return out


def export_categories(stores: dict, person_id: str) -> list[str]:
    found = []
    for name in STORES:
        if any(row.get("person_id") == person_id for row in stores.get(name, [])):
            found.append(name)
    return found


def drop(stores: dict, person_id: str) -> dict:
    cleared = {}
    for name in STORES:
        rows = stores.get(name, [])
        if name == "logs" and any(row.get("person_id") == person_id for row in rows):
            cleared[name] = [{"redacted": True}]
        else:
            cleared[name] = [dict(row) for row in rows if row.get("person_id") != person_id]
    return cleared


def _rates(rows: list[dict], key: str) -> list[float]:
    groups: dict[str, list[bool]] = {}
    for row in rows:
        groups.setdefault(row[key], []).append(row["decision"] == "yes")
    return [sum(flags) / len(flags) for flags in groups.values() if flags]


def gap(rows: list[dict]) -> float:
    spreads = []
    for key in ("district", "insurance"):
        rates = _rates(rows, key)
        if rates:
            spreads.append(max(rates) - min(rates))
    if not spreads:
        return 0.0
    return max(spreads)


def stamp_rate(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
