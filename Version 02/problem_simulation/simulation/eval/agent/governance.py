"""The drop, the second site, the press rules, and what the agent is allowed to be."""

from __future__ import annotations

from datetime import timedelta
from pathlib import Path

import yaml

from simulation.architecture.model_register import MODELS
from simulation.drops.rules import PRIMARY_CARE_SITES, SECOND_SITE
from simulation.eval.agent.bars import MULTI_HOP_INPUT, MULTI_HOP_OUTPUT, TODAY
from simulation.eval.evidence.bars import BUDGETS, MEMO_ID
from simulation.world.engagement import PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED, SCOPE_CHANGE
from simulation.world.sites import is_hospital
from simulation.world.staff import name

TOKENS = Path(__file__).resolve().parents[3] / "serve" / "tokens.yaml"
VETO = {
    "stop": ("owner-governance", "ai-risk-tier-policy"),
    "scope": (MEMO_ID,),
    "tier": ("ai-risk-tier-policy",),
    "individual": ("data-classification-policy", "dpo-rule-2018"),
    "model": ("data-classification-policy", "cloud-policy"),
    "logs": ("security-logging-standard",),
    "write": ("security-authentication-standard",),
    "grade": ("dpo-rule-2018",),
}


def facts(world: dict) -> dict:
    return {
        "drop_scope": _drop(),
        "outputs_changed": _outputs(),
        "second_site": _site(world),
        "press_rules": _press(),
        "agent_tier": _tier(),
        "veto_sources": _veto(),
        "service_account": _account(),
        "model_routing": _models(),
        "audit_and_logs": _audit(),
    }


def _drop() -> dict:
    return {
        "requested": PILOT_DATE_REQUESTED.isoformat(),
        "previous": PILOT_DATE_ORIGINAL.isoformat(),
        "second_site": SECOND_SITE,
        "second_site_hospital": is_hospital(SECOND_SITE),
        "asks": ["date", "second_site", "variation"],
        "press_questions": ["approved", "start_date", "individual", "waiting_and_fault"],
        "deadline": (SCOPE_CHANGE + timedelta(days=4)).isoformat(),
    }


def _outputs() -> dict:
    return {"changed": ["C-06"], "consumed": ["C-04"], "unchanged": ["C-03", "C-07"]}


def _site(world: dict) -> dict:
    conflict = world["gold"].get("dsa_conflict", {})
    return {
        "site": SECOND_SITE,
        "is_hospital": is_hospital(SECOND_SITE),
        "allowed": SECOND_SITE in PRIMARY_CARE_SITES,
        "memo": MEMO_ID,
        "agreement": conflict.get("agreement", "dsa-retinalytics-2025"),
        "dpia": conflict.get("dpia", "dpia-vendor-2024"),
        "decided_by": name("dpo"),
        "allowed_sites": list(PRIMARY_CARE_SITES),
    }


def _press() -> dict:
    raci = _activity("Press and ministerial responses")
    return {
        "responsible": raci[0], "accountable": raci[1], "consulted": raci[2], "informed": raci[3],
        "individual_facts": False, "pilot_date": False, "count_harmed": False, "every_letter": False, "approved": False,
    }


def _activity(title: str) -> tuple[str, str, str, str]:
    from simulation.delivery.raci import ACTIVITIES
    row = next(item for item in ACTIVITIES if item[0] == title)
    return tuple(name(key) if key else "" for key in row[1:])


def _tier() -> dict:
    return {
        "tier": 2,
        "tier_3_triggers": ["rank", "triage", "prioritise", "clinical"],
        "tier_3_lacks": "clinical safety owner",
        "tier_2_needs": ["register entry", "transparency record"],
    }


def _veto() -> dict:
    return {"sources": {key: values[0] for key, values in VETO.items()}, "accepted": {key: list(values) for key, values in VETO.items()}}


def _account() -> dict:
    rows = yaml.safe_load(TOKENS.read_text(encoding="utf-8"))["tokens"]
    discovery = next(row for row in rows if row["client"] == "discovery-team")
    return {
        "client": discovery["client"],
        "scopes": list(discovery["scopes"]),
        "read_only": all(scope.endswith(":read") for scope in discovery["scopes"]),
        "expires": str(discovery["expires"]),
        "burst": discovery["burst"],
        "per_minute": discovery["per_minute"],
        "excess_rights": sorted(row["client"] for row in rows if any(scope.endswith(":write") for scope in row["scopes"])),
        "expired": next(row["client"] for row in rows if str(row["expires"]) < TODAY.isoformat()),
    }


def _models() -> dict:
    personal = [row[0] for row in MODELS if "official-sensitive" in row[6]]
    official = [row[0] for row in MODELS if "official" in row[6].split(";") and "official-sensitive" not in row[6]]
    costs = {row[0]: _cost(row) for row in MODELS if row[0] in personal and "embedding" not in row[1]}
    return {
        "personal": personal,
        "official_only": official,
        "public_only": [row[0] for row in MODELS if row[6] == "public"],
        "cheapest_generator": min(costs, key=costs.get),
        "multi_hop_cost": costs,
        "multi_hop_budget": BUDGETS["multi_hop"]["max_cost_gbp"],
    }


def _cost(row: tuple) -> float:
    return round(MULTI_HOP_INPUT / 1000 * row[7] + MULTI_HOP_OUTPUT / 1000 * row[8], 4)


def _audit() -> dict:
    return {"never": ["name", "phone", "address", "national id"], "reads_go_to": "access audit log",
            "retention_years": 7, "references_not_values": True}
