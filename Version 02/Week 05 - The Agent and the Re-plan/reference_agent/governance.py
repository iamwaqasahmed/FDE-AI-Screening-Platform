"""The drop, the site, the press row, and the limits on the agent."""

from __future__ import annotations

import re
from datetime import timedelta
from pathlib import Path

import yaml

from reference_agent.load import read_csv, released
from simulation.eval.evidence.drop import restriction

TOKENS = Path(__file__).resolve().parents[2] / "problem_simulation" / "serve" / "tokens.yaml"
VETO = {
    "stop": "owner-governance", "scope": "dpo-restriction-memo", "tier": "ai-risk-tier-policy",
    "individual": "data-classification-policy", "model": "data-classification-policy",
    "logs": "security-logging-standard", "write": "security-authentication-standard", "grade": "dpo-rule-2018",
}


def facts(data: Path) -> dict:
    return {
        "drop_scope": _drop(data),
        "outputs_changed": {"changed": ["C-06"], "consumed": ["C-04"], "unchanged": ["C-03", "C-07"]},
        "second_site": _site(data),
        "press_rules": _press(data),
        "agent_tier": {"tier": 2, "tier_3_triggers": ["rank", "triage", "prioritise", "clinical"],
                       "tier_3_lacks": "clinical safety owner", "tier_2_needs": ["register entry", "transparency record"]},
        "veto_sources": {"sources": dict(VETO)},
        "service_account": _account(data),
        "model_routing": _models(data),
        "audit_and_logs": {"never": ["name", "phone", "address", "national id"], "reads_go_to": "access audit log",
                           "retention_years": 7, "references_not_values": True},
    }


def _drop(data: Path) -> dict:
    scope = (data / "drops/week-5/scope_change_cdo.md").read_text(encoding="utf-8")
    roadmap = read_csv(data, "handover/delivery/roadmap.csv").set_index("item_id")
    site = re.search(r"Add (.+?) as a second", scope).group(1)
    return {
        "requested": re.search(r"forward to (\d{4}-\d{2}-\d{2})", scope).group(1),
        "previous": str(roadmap.at["RM-03", "target_date"]),
        "second_site": site,
        "second_site_hospital": "hospital" in scope.lower(),
        "asks": ["date", "second_site", "variation"],
        "press_questions": ["approved", "start_date", "individual", "waiting_and_fault"],
        "deadline": (released(data, 5) + timedelta(days=4)).isoformat(),
    }


def _site(data: Path) -> dict:
    scope = (data / "drops/week-5/scope_change_cdo.md").read_text(encoding="utf-8")
    memo = (data / "drops/week-3/dpo_restriction_memo.md").read_text(encoding="utf-8")
    site = re.search(r"Add (.+?) as a second", scope).group(1)
    allowed = restriction(memo, [])["allowed_sites"]
    sender = re.search(r"From:\s*([^,]+)", memo).group(1).strip()
    return {
        "site": site, "is_hospital": "hospital" in scope.lower(), "allowed": site in allowed, "memo": "dpo-restriction-memo",
        "agreement": "dsa-retinalytics-2025", "dpia": "dpia-vendor-2024", "decided_by": sender, "allowed_sites": allowed,
    }


def _press(data: Path) -> dict:
    raci = read_csv(data, "handover/delivery/raci.csv").set_index("activity")
    row = raci.loc["Press and ministerial responses"]
    return {
        "responsible": row["responsible"], "accountable": row["accountable"], "consulted": row["consulted"],
        "informed": row["informed"], "individual_facts": False, "pilot_date": False, "count_harmed": False,
        "every_letter": False, "approved": False,
    }


def _account(data: Path) -> dict:
    rows = yaml.safe_load(TOKENS.read_text(encoding="utf-8"))["tokens"]
    today = released(data, 5).isoformat()
    discovery = next(row for row in rows if row["client"] == "discovery-team")
    return {
        "client": discovery["client"], "scopes": list(discovery["scopes"]),
        "read_only": all(str(scope).endswith(":read") for scope in discovery["scopes"]),
        "expires": str(discovery["expires"]), "burst": int(discovery["burst"]), "per_minute": int(discovery["per_minute"]),
        "excess_rights": sorted(row["client"] for row in rows if any(str(scope).endswith(":write") for scope in row["scopes"])),
        "expired": next(row["client"] for row in rows if str(row["expires"]) < today),
    }


def _models(data: Path) -> dict:
    frame = read_csv(data, "handover/architecture/model_register.csv")
    personal, official, public, costs = [], [], [], {}
    for row in frame.itertuples(index=False):
        classes = set(row.approved_classifications.split(";"))
        if "official-sensitive" in classes:
            personal.append(row.model_id)
            if row.task == "generation":
                costs[row.model_id] = round(16 * float(row.cost_per_1k_input_gbp) + 4 * float(row.cost_per_1k_output_gbp), 4)
        elif "official" in classes:
            official.append(row.model_id)
        elif classes == {"public"}:
            public.append(row.model_id)
    return {
        "personal": personal, "official_only": official, "public_only": public,
        "cheapest_generator": min(costs, key=costs.get), "multi_hop_cost": costs, "multi_hop_budget": 0.05,
    }
