"""A perfect handoff, built from the gold, so the scorer is shown to accept it."""

from __future__ import annotations

import pandas as pd

from simulation.eval.handoff.bars import FLOW_COLUMNS, HAZARD_COLUMNS, THREAT_COLUMNS


def pack(gold: dict) -> dict:
    return {
        "flows": _flows(gold),
        "threats": _threats(gold),
        "hazards": _hazards(gold),
        "dockerfile": _dockerfile(gold),
        "contract": _contract(gold),
        "transparency": _transparency(gold),
        "model_card": _card(gold),
        "texts": _texts(gold),
    }


def _flows(gold: dict) -> pd.DataFrame:
    rows = [{column: item[column] if column != "rule" else item["rules"][0] for column in FLOW_COLUMNS} for item in gold["files"]["flows"]]
    return pd.DataFrame(rows, columns=list(FLOW_COLUMNS))


def _threats(gold: dict) -> pd.DataFrame:
    owner = gold["files"]["hazards"]["owners"][0]
    rows = []
    for item in gold["files"]["threats"]:
        rows.append({
            "threat_id": item["threat_id"],
            "title": item["threat_id"],
            "components": " ".join(item["need"]) if item["field"] == "components" else "",
            "evidence": " ".join(item["need"]) if item["field"] == "evidence" else "",
            "standard": item["standards"][0],
            "live": "true" if item["live"] else "false",
            "mitigation": "Recorded and owned.",
            "owner": owner,
        })
    return pd.DataFrame(rows, columns=list(THREAT_COLUMNS))


def _hazards(gold: dict) -> pd.DataFrame:
    owner = gold["files"]["hazards"]["owners"][0]
    rows = []
    for group in gold["files"]["hazards"]["groups"]:
        evidence = str(group["number"]) if "number" in group else group["id"]
        rows.append({
            "hazard_id": group["id"], "cause": group["id"], "effect": group["id"], "anchor": group["anchors"][0],
            "evidence": evidence, "control": group["id"], "control_owner": owner, "signed_by": "",
        })
    return pd.DataFrame(rows, columns=list(HAZARD_COLUMNS))


def _dockerfile(gold: dict) -> str:
    model = gold["records"]["dockerfile"]["allowed_models"][0]
    return f"FROM python:3.12-slim\nCOPY screening_service /app/screening_service\nENV MODEL_ID={model}\n"


def _contract(gold: dict) -> str:
    spec = gold["records"]["contract"]
    model = spec["facts"][3]["tokens"][0]
    owner = spec["owners"][0]
    lines = [
        f"service: {spec['service']}", f"zone: {spec['zone']}", "dr_tier: 1", "image: screening-agent:week6",
        "data: mounted", f"account: screening-agent", f"owner: {owner}", "scopes: [registry:read]", "writes: []",
        f"models: [{model}]", "logs: no name and no phone", "audit: access audit log", "sign_in: identity provider",
        "incidents: ai-incident-runbook", "register: model register",
        "fails_when: read-only, and a question in the log fails it",
    ]
    return "\n".join(lines) + "\n"


def _transparency(gold: dict) -> str:
    spec = gold["records"]["transparency"]
    sites = "\n".join(f"  - {site}" for site in spec["sites"])
    return (
        f"system_name: vendor triage pilot\nowner: {spec['owner']}\nsupplier: {spec['supplier']}\n"
        "purpose: advisory triage\ntier: '3'\ndecision_supported: worklist order\n"
        f"human_in_the_loop: a grader signs\ndata_used: primary-care photographs\n"
        f"data_classification: {spec['classification']}\nhosting_region: {spec['region_token'].upper()} region\n"
        f"sites_in_scope:\n{sites}\nstart_date: ''\nevaluation_summary: subgroup gaps remain\n"
        f"contact_for_challenge: {spec['contact']}\n"
    )


def _card(gold: dict) -> str:
    spec = gold["records"]["model_card"]
    numbers = ", ".join(str(number) for number in spec["numbers"])
    body = "\n".join(f"{field}: recorded" for field in spec["fields"])
    extra = f"\nnumbers: {numbers}\nsites: {', '.join(spec['sites'])}\npopulation: {spec['population']}\n"
    extra += f"drift: {spec['drift_site']}. The inventory lags. The output is advisory.\n"
    return body + extra


def _texts(gold: dict) -> dict[str, str]:
    texts = {}
    for key, spec in gold["text"].items():
        if key == "pages":
            continue
        tokens = [fact["tokens"][0] for fact in spec["facts"]]
        texts[key] = "Status: Proposed.\n\n" + ". ".join(tokens) + ".\n"
    return texts
