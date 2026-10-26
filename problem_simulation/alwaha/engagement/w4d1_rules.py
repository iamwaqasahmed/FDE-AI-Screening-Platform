"""Reference decisions for rel-w4d1.
Participant copies do not import this module.

screen, admit, and settle decide what is blocked, what is held, and which grants stay open. clean redacts identifier patterns. export_categories and drop say where a person still exists. gap and stamp_rate are the fairness figures.
"""

from __future__ import annotations

import html
import re

from alwaha.engagement.w4d1_rows import HOLD_CAP, IN_FORCE, STORES, TOKEN_CAP

_CANARY = re.compile(r"CANARY-[0-9a-fA-F]+")
_NID = re.compile(r"NID-[0-9a-fA-F]+")


def screen(event: dict) -> dict:
    """Return whether the event is blocked, whether it is held, and which tool may still run.

    Direct, indirect, and prompt families are refused and not held. An unapproved book or return is refused and held for a person. Anything else keeps its tool.
    """
    family = event.get("family")
    tool = event.get("tool") or None
    # These families are refused outright, and nothing is held for a person.
    if family in {"atk-direct", "atk-indirect", "atk-prompt"}:
        return {"blocked": True, "held": False, "tool": None}
    # Booking or returning with no approval is refused and held.
    if family == "atk-agency" and tool in {"book", "return"} and not event.get("approval_id"):
        return {"blocked": True, "held": True, "tool": None}
    return {"blocked": False, "held": False, "tool": tool}


def escape(text: str) -> str:
    """Return the text with markup characters escaped so a payload is shown as text."""
    return html.escape(text)


def accept_hash(candidate: str, approved: list[str]) -> str:
    """Return the candidate when it is on the approved list, otherwise an empty hash."""
    if candidate in approved:
        return candidate
    # A hash that is not on the approved list is rejected rather than passed through.
    return ""


def run_tool(description: str) -> str:
    """Return an empty result. The description is ignored so the tool does not act on it."""
    del description
    return ""


def keep_label(row: dict) -> bool:
    """Return whether the label may be kept. A poisoned label is dropped."""
    return not row.get("poison")


def cite(doc: dict) -> str:
    """Return the document id when it is in force for a public or staff audience.

    Any other status or audience is replaced with the in-force document, so a superseded or unauthorized text is not cited as itself.
    """
    # Only an in-force document the audience may see is cited by its own id.
    if doc.get("status") == "in_force" and doc.get("audience") in {"public", "staff"}:
        return str(doc.get("doc_id") or "")
    return IN_FORCE


def clean(text: str) -> str:
    """Return the text with canary-shaped tokens and national-id-shaped tokens redacted."""
    text = _CANARY.sub("[redacted]", text)
    return _NID.sub("[redacted]", text)


def admit(event: dict) -> bool:
    """Return whether the event is inside its family's limit.

    The token family is limited by the token cap. The hoard family is limited by how many holds it takes. Any other family is admitted.
    """
    # The token family is limited by the token cap. A missing count is treated as none.
    if event.get("family") == "atk-tokens":
        return int(event.get("tokens") or 0) <= TOKEN_CAP
    # The hoard family is limited by how many holds it takes.
    if event.get("family") == "atk-hoard":
        return int(event.get("holds") or 0) <= HOLD_CAP
    return True


def settle(grants: list[dict], as_of: str) -> list[dict]:
    """Return a copy of each grant with a status.

    Break-glass with no audit is given an audit id and left open. Staff and delegate grants whose end is already past are closed. Everything else stays open, including a break-glass grant that already has an audit.
    """
    out = []
    for grant in grants:
        row = dict(grant)
        kind = row.get("kind")
        # Break-glass with no audit trail is given one and left open.
        if kind == "break-glass" and not row.get("audit"):
            row["audit"] = "audit-" + str(row.get("id") or "")
            row["status"] = "open"
        # Staff and delegate access ends when the end date is already past.
        elif (row.get("end") or "") < as_of and kind in {"staff", "delegate"}:
            row["status"] = "closed"
        else:
            # Still inside the window, or a break-glass grant that already has an audit.
            row["status"] = "open"
        out.append(row)
    return out


def export_categories(stores: dict, person_id: str) -> list[str]:
    """Return the store names that still contain this person, in the store order.

    The steps walk the stores in fixed order and keep every name that still has a row for this person.
    """
    found = []
    for name in STORES:
        if any(row.get("person_id") == person_id for row in stores.get(name, [])):
            found.append(name)
    return found


def drop(stores: dict, person_id: str) -> dict:
    """Return the stores with this person removed.

    Logs that contained the person are replaced by a redacted marker so the store still shows that a row existed. Other stores drop that person's rows and keep the rest.
    """
    cleared = {}
    for name in STORES:
        rows = stores.get(name, [])
        # Logs are redacted in place. Deleting them would hide that a row had been there.
        if name == "logs" and any(row.get("person_id") == person_id for row in rows):
            cleared[name] = [{"redacted": True}]
        else:
            cleared[name] = [dict(row) for row in rows if row.get("person_id") != person_id]
    return cleared


def _rates(rows: list[dict], key: str) -> list[float]:
    """Return the share of yes decisions in each group of this key. An empty group is skipped.

    The steps group the rows by the key and return each group's share of yes decisions, and the hidden figures stay in this file and are not copied into a new comment.
    """
    groups: dict[str, list[bool]] = {}
    for row in rows:
        groups.setdefault(row[key], []).append(row["decision"] == "yes")
    return [sum(flags) / len(flags) for flags in groups.values() if flags]


def gap(rows: list[dict]) -> float:
    """Return the widest gap between group rates, looking at district and at insurance.

    A grouping with no rows adds nothing. No grouping at all returns nothing rather than a gap.
    """
    spreads = []
    for key in ("district", "insurance"):
        rates = _rates(rows, key)
        # A grouping with no rows does not invent a spread.
        if rates:
            spreads.append(max(rates) - min(rates))
    # No grouping produced a rate.
    if not spreads:
        return 0.0
    return max(spreads)


def stamp_rate(rows: list[dict]) -> float:
    """Return the share of rows that were stamped. No rows scores as nothing."""
    # An empty approval list is not a zero-stamp finding and not a fully stamped one.
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
