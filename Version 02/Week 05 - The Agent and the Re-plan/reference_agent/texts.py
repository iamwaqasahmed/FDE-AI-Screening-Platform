"""The public line, the reply, the card, and the trajectory contract."""

from __future__ import annotations

import re
from pathlib import Path

WINDOW = re.compile(r"requests_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})")


def press_text(data: Path) -> str:
    start, end = _window(data)
    first = (
        "Screening results are still decided by trained graders; no AI system makes decisions about anyone's care. "
        "Any AI pilot needs a named clinical safety owner, a signed safety case, and data protection approval first."
    )
    second = (
        f"A letter bureau problem between {start} and {end} is being reconciled and affected people are being contacted. "
        "Anyone worried about an appointment or a letter should contact the screening programme."
    )
    return f"{first}\n\n{second}\n"


def reply(items: dict) -> str:
    path, gate, site, route, road = (items["critical_path"], items["gate_two"], items["second_site"],
                                     items["procurement_route"], items["roadmap_items"])
    return "\n".join([
        f"The earliest go-live is {path['earliest']['go_live']} and the latest is {path['latest']['go_live']}.",
        "Procurement binds the date. A direct award does not.",
        f"{site['site']} is a hospital clinic. It needs a data protection decision before it can join.",
        f"The contract is {route['value']} and the route is a framework call-off. Gate 2 is {gate['date']}.",
        f"The corrected cashable benefit is {gate['corrected_cashable_gbp']}.",
        "The safety owner is still unnamed, so the pilot stays stopped.",
        "Reopen R-07. It was closed with no mitigation.",
        f"Pilot readiness is not before {road['g3_not_before']}.",
        "",
    ])


def card(single: int, keyword: int) -> str:
    return "\n".join([
        f"single-loop {single}",
        f"keyword {keyword}",
        "The agent is tier 2.",
        "The veto is checked in code, before the tool runs.",
        "Each step writes a checkpoint.",
        "The account is read-only.",
        "M06 is public data only.",
        "",
    ])


def contract(client: str) -> str:
    return "\n".join([
        "agent: week-5-replan",
        "tier: 2",
        f"account: {client}",
        "scopes: [registry:read, booking:read, letters:read, ophthalmology:read, vendor:read]",
        "writes: []",
        "checkpoints: after every step",
        "veto: before every tool call and before every draft leaves the office",
        "approval: the accountable person, recorded with a reason",
        "models: [M01, M02, M03, M04]",
        "logs: references, never a name or a phone",
        "fails_when: a write, a veto with no rule, or M06 on personal data",
        "note: tier 2, read-only, checkpoint, veto, approval, M06, name, phone",
        "",
    ])


def _window(data: Path) -> tuple[str, str]:
    folder = data / "drops/week-4/letters"
    return WINDOW.search(next(folder.glob("requests_*.csv")).name).groups()
