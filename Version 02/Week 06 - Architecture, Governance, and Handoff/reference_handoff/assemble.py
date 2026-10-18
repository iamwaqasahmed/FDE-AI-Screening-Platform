"""Write the Week 6 folder the checker scores."""

from __future__ import annotations

import json
from pathlib import Path

from reference_handoff import conditions, deploy, estate, flows, governance, hazards, records, security
from reference_handoff.texts_adr import all_records
from reference_handoff.texts_pages import clinical, executive, runbook
from simulation.world.staff import VENDORS, name


def build(data: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    base = conditions.facts(data)
    sites = base.pop("flow_rules_sites")
    decider = base.pop("decider_dpo")
    base.update(estate.facts(data, sites, decider))
    threats, threat_frame = security.facts(data)
    base["threat_summary"] = threats
    base.update(governance.gaps())
    base["tier_three"] = governance.tier(data)
    base["model_evidence"] = governance.evidence(data)
    names = _names(base, decider)
    base["adr_index"] = {"ids": ["ADR-01", "ADR-02", "ADR-03", "ADR-04"], "deciders": _deciders(names), "status": "proposed"}
    _write_json(out / "findings.json", {"items": base})
    flows.frame().to_csv(out / "flows.csv", index=False)
    threat_frame.to_csv(out / "threats.csv", index=False)
    hazards.frame(base["model_evidence"], base["conditions"]["CSO-4"]["people"], names["grader"]).to_csv(out / "hazard-log.csv", index=False)
    (out / "contracts").mkdir(exist_ok=True)
    (out / "governance").mkdir(exist_ok=True)
    (out / "deploy").mkdir(exist_ok=True)
    (out / "adr").mkdir(exist_ok=True)
    model = base["prototype_gaps"]["replace_with"]
    (out / "contracts/production.yaml").write_text(records.contract(names["security"], model), encoding="utf-8")
    (out / "governance/transparency-record.yaml").write_text(
        records.transparency(name("cdo"), VENDORS["retinalytics"], base["flow_rules"]["allowed_sites"]), encoding="utf-8")
    (out / "governance/model-card.yaml").write_text(records.model_card(base["model_evidence"]), encoding="utf-8")
    (out / "deploy/Dockerfile").write_text(deploy.text(model), encoding="utf-8")
    for key, text in all_records(names, model).items():
        (out / "adr" / f"{key.upper()}.md").write_text(text, encoding="utf-8")
    (out / "executive-page.md").write_text(executive(base, base["flow_rules"]["allowed_sites"]), encoding="utf-8")
    (out / "clinical-page.md").write_text(clinical(base, base["flow_rules"]["allowed_sites"]), encoding="utf-8")
    (out / "runbook.md").write_text(runbook(base, names), encoding="utf-8")


def _names(items: dict, decider: str) -> dict:
    return {
        "dpo": decider,
        "architect": name("enterprise_architect"),
        "owner": items["drop_owner"]["owner"],
        "security": name("security_officer"),
        "grader": items["conditions"]["CSO-1"]["acts"],
        "programme": name("programme_manager"),
    }


def _deciders(names: dict) -> dict:
    return {"ADR-01": names["dpo"], "ADR-02": names["architect"], "ADR-03": names["owner"], "ADR-04": names["security"]}


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
