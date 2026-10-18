"""T1 to T4 from the accounts, the roles, and the risk register."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from reference_handoff.load import read_csv
from simulation.eval.handoff.bars import THREAT_COLUMNS


def facts(data: Path) -> tuple[dict, pd.DataFrame]:
    accounts = read_csv(data, "handover/identity/accounts.csv")
    roles = read_csv(data, "handover/identity/role_mappings.csv")
    staff = read_csv(data, "handover/workforce/staff.csv")
    components = read_csv(data, "handover/architecture/components.csv").set_index("component")
    stale = _stale(accounts, roles, staff)
    service = _service(accounts, roles)
    summary = {
        "threat_ids": ["T1", "T2", "T3", "T4"],
        "live": ["T1", "T2", "T4"],
        "service_account": service,
        "excess_role": "directory-admin",
        "stale_accounts": stale,
        "reopen": "R-11",
        "stays_closed": "R-08",
    }
    owner = str(components.at["integration-engine", "owner"])
    security = str(components.at["idp", "owner"])
    rows = [
        _row("T1", "Vendor callback crosses trust zones", "vendor vendor-callback integration-engine grader", "", "ea-principles", True, owner),
        _row("T2", "Service account with excess rights", "integration-engine idp", service, "security-authentication-standard", True, security),
        _row("T3", "PII in the booking log", "booking", "INC-0270", "security-logging-standard", False, security),
        _row("T4", "Stale accounts keep access", "idp audit", "INC-0262 " + " ".join(stale), "security-authentication-standard", True, security),
    ]
    return summary, pd.DataFrame(rows, columns=list(THREAT_COLUMNS))


def _stale(accounts: pd.DataFrame, roles: pd.DataFrame, staff: pd.DataFrame) -> list[str]:
    left = set(staff.loc[staff["status_at_snapshot"].eq("left"), "name"])
    enabled = accounts["status"].eq("enabled")
    leavers = set(accounts.loc[enabled & accounts["display_name"].isin(left), "account_id"])
    open_roles = roles[roles["revoked_at"].eq("")].groupby("account_id")["granted_at"].nunique()
    changed = set(open_roles[open_roles > 1].index)
    return sorted(leavers | changed)


def _service(accounts: pd.DataFrame, roles: pd.DataFrame) -> str:
    services = set(accounts.loc[accounts["account_type"].eq("service"), "account_id"])
    open_admin = roles["account_id"].isin(services) & roles["role"].eq("directory-admin") & roles["revoked_at"].eq("")
    return str(roles.loc[open_admin, "account_id"].iloc[0])


def _row(threat_id, title, components, evidence, standard, live, owner) -> dict:
    return {
        "threat_id": threat_id, "title": title, "components": components, "evidence": evidence,
        "standard": standard, "live": "true" if live else "false", "mitigation": "Owned, and not treated as closed.", "owner": owner,
    }
