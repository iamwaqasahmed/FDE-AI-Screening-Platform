"""Key facts for the trajectory contract, the agent card, the reply, and the public line."""

from __future__ import annotations

from simulation.drops.press import press_gold
from simulation.world.engagement import BUREAU_INCIDENT

FIELDS = [
    "agent", "tier", "account", "scopes", "writes", "checkpoints", "veto", "approval", "models", "logs", "fails_when",
]
REPLY_FORBIDDEN = [
    "2027-02-01 is achievable.",
    "The second site joins the pilot.",
    "The pilot may start.",
]
LINE_FORBIDDEN = [
    "The AI system is approved.",
    "A patient lost sight.",
    "It was the bureau's fault.",
    "Every letter has been accounted for.",
]
CARD_FORBIDDEN = [
    "The veto is a sentence in the prompt.",
    "M06 may read patient names.",
    "The agent may write to a system.",
]


def facts(items: dict, baselines: dict, counts: dict) -> dict:
    return {
        "fields": list(FIELDS),
        "contract": _contract(items),
        "card": {"facts": _card(baselines), "forbidden": list(CARD_FORBIDDEN)},
        "reply": {"facts": _reply(items), "forbidden": list(REPLY_FORBIDDEN)},
        "line": {"facts": _line(), "forbidden": list(LINE_FORBIDDEN), "forbidden_terms": _terms(counts)},
    }


def _contract(items: dict) -> list[dict]:
    account = items["service_account"]
    return [
        {"id": "tier", "tokens": ["tier 2"]},
        {"id": "account", "tokens": [account["client"]]},
        {"id": "writes", "tokens": ["read-only"]},
        {"id": "checkpoint", "tokens": ["checkpoint"]},
        {"id": "veto", "tokens": ["veto"]},
        {"id": "approval", "tokens": ["approval"]},
        {"id": "model", "tokens": ["M06"]},
        {"id": "name", "tokens": ["name"]},
        {"id": "phone", "tokens": ["phone"]},
    ]


def _card(baselines: dict) -> list[dict]:
    return [
        {"id": "single", "tokens": ["single-loop"]},
        {"id": "single-rate", "number": _percent(baselines["single_loop"]["overall"]), "tolerance": 0.0},
        {"id": "keyword", "tokens": ["keyword"]},
        {"id": "keyword-rate", "number": _percent(baselines["keyword_veto"]["overall"]), "tolerance": 0.0},
        {"id": "tier", "tokens": ["tier 2"]},
        {"id": "veto", "tokens": ["veto"]},
        {"id": "checkpoint", "tokens": ["checkpoint"]},
        {"id": "read", "tokens": ["read-only"]},
        {"id": "model", "tokens": ["M06"]},
    ]


def _reply(items: dict) -> list[dict]:
    path, gate, site = items["critical_path"], items["gate_two"], items["second_site"]
    return [
        {"id": "earliest", "tokens": [path["earliest"]["go_live"]]},
        {"id": "latest", "tokens": [path["latest"]["go_live"]]},
        {"id": "binding", "tokens": ["procurement"]},
        {"id": "site", "tokens": [site["site"]]},
        {"id": "dpo", "tokens": ["data protection"]},
        {"id": "value", "number": items["procurement_route"]["value"], "tolerance": 0.0},
        {"id": "gate", "tokens": [gate["date"]]},
        {"id": "cash", "number": gate["corrected_cashable_gbp"], "tolerance": 0.0},
        {"id": "owner", "tokens": ["safety owner"]},
        {"id": "stopped", "tokens": ["stopped"]},
        {"id": "risk", "tokens": ["R-07"]},
        {"id": "ready", "tokens": [items["roadmap_items"]["g3_not_before"]]},
    ]


def _line() -> list[dict]:
    start, end = (day.isoformat() for day in BUREAU_INCIDENT)
    return [
        {"id": "graders", "tokens": ["grader"]},
        {"id": "owner", "tokens": ["safety owner"]},
        {"id": "dpo", "tokens": ["data protection"]},
        {"id": "start", "tokens": [start]},
        {"id": "end", "tokens": [end]},
        {"id": "contact", "tokens": ["screening programme"]},
    ]


def _terms(counts: dict) -> list[str]:
    press = press_gold()["forbidden_terms"]
    numbers = [str(counts["lost_in_bound"]), str(counts["pilot_lost"]), str(counts["hidden_lost"])]
    return sorted({*press, *numbers})


def _percent(rate: float) -> int:
    return int(round(rate * 100))
