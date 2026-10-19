"""Threat-model gold: the must-find list, each traced to a component, an account, or a timeline reference."""

from __future__ import annotations

import pandas as pd

from simulation.architecture.components import callback_path, zone_of
from simulation.estate.identity_roles import EXCESS_SERVICE
from simulation.world.timeline import TIMELINE

REFS = {item.ref: item for item in TIMELINE}
MUST_MENTION = {"T1": "vendor callback", "T2": "service account", "T3": "INC-0270", "T4": "INC-0262"}


def threats(components: pd.DataFrame, accounts: pd.DataFrame, stale: list[dict]) -> list[dict]:
    path = callback_path()
    zones = [zone_of(components, component) for component in path]
    service = accounts.loc[accounts["source"] == EXCESS_SERVICE[0], "account_id"].iloc[0]
    log_incident = REFS["INC-0270"]
    access_incident = REFS["INC-0262"]
    return [
        {"threat_id": "T1", "title": "Vendor callback crosses trust zones into the grader path",
         "components": list(path), "zones": zones, "refs": [],
         "evidence": ["handover/architecture/components.csv"]},
        {"threat_id": "T2", "title": "Service account with excess rights",
         "components": ["integration-engine", "idp"], "zones": [zone_of(components, "idp")], "refs": [],
         "account_id": service, "excess_role": EXCESS_SERVICE[1],
         "evidence": ["handover/identity/accounts.csv", "handover/identity/role_mappings.csv"]},
        {"threat_id": "T3", "title": "PII written to booking API logs", "components": ["booking"],
         "zones": [zone_of(components, "booking")], "refs": [log_incident.ref],
         "window": [log_incident.start.isoformat(), log_incident.end.isoformat()],
         "evidence": ["handover/service_desk/tickets.csv", "handover/booking/api.log"]},
        {"threat_id": "T4", "title": "Stale accounts keep record access after leaving or a role change",
         "components": ["idp", "audit"], "zones": [zone_of(components, "idp")], "refs": [access_incident.ref],
         "accounts": sorted(item["account_id"] for item in stale),
         "evidence": ["handover/identity/accounts.csv", "handover/audit/record_reads.jsonl"]},
    ]
