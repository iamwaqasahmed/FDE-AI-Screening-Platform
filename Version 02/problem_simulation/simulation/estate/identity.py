"""Identity provider export: accounts and role mappings. Three accounts keep access they should have lost."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.estate import identity_roles as roles
from simulation.estate.common import TRUTH, log_fault
from simulation.faults import stale_account
from simulation.world.clock import HISTORY_START, SNAPSHOT
from simulation.world.staff import STAFF
from simulation.world.timeline import TIMELINE
from simulation.workforce.graders import ROSTER

DOMAIN = "hartland.example"
ACCOUNT_COLUMNS = ["account_id", "display_name", "upn", "account_type", "department", "job_title", "status",
                   "created_at", "disabled_at", "last_sign_in"]
AUDIT_INCIDENT = next(item for item in TIMELINE if item.ref == "INC-0262")


def build_identity(world: dict, rng: np.random.Generator) -> dict:
    accounts = _accounts(rng)
    mappings = _mappings(accounts)
    stale = _stale_ids(accounts)
    shown_accounts, entry = stale_account.apply(accounts, rng, {"accounts": stale, "clear": ["disabled_at"], "set": {"status": "enabled"}})
    shown_roles, role_entry = stale_account.apply(mappings, rng, {"accounts": stale, "clear": ["revoked_at"], "only": "_stale_row"})
    log_fault(world, "idp", entry)
    log_fault(world, "idp", role_entry)
    files = world["files"]
    files["handover/identity/accounts.csv"] = shown_accounts[ACCOUNT_COLUMNS]
    files["handover/identity/role_mappings.csv"] = shown_roles
    files[f"{TRUTH}/identity_accounts.parquet"] = accounts
    files[f"{TRUTH}/identity_roles.parquet"] = mappings.drop(columns=["_stale_row"])
    world["gold"]["stale_access"] = _gold(accounts, mappings, stale)
    return {"accounts": accounts, "stale": stale, "audit_account": _id_for(accounts, roles.AUDIT_ACCOUNT_GRADER)}


def _accounts(rng: np.random.Generator) -> pd.DataFrame:
    rows = []
    for grader in ROSTER:
        disabled = (grader.end + timedelta(days=1)).isoformat() if grader.end else ""
        rows.append(_row(grader.grader_id, grader.name, "member", "Screening service", "Grader" if not grader.lead else "Lead Grader",
                         max(grader.start, HISTORY_START), disabled))
    for person in STAFF:
        if person.key in roles.NO_ACCOUNT:
            continue
        kind = "guest" if person.key in roles.GUESTS else "member"
        rows.append(_row(person.key, person.name, kind, person.team, person.role, HISTORY_START, ""))
    for account, label, _ in roles.SERVICE_ACCOUNTS:
        rows.append(_row(account, label, "service", "Digital", "Service account", HISTORY_START, ""))
    frame = pd.DataFrame(rows)
    frame.insert(0, "account_id", [f"usr-{index:04d}" for index in range(1, len(frame) + 1)])
    days_ago = rng.integers(0, 20, len(frame))
    frame["last_sign_in"] = [_last_sign_in(row, int(ago)) for row, ago in zip(frame.itertuples(index=False), days_ago)]
    return frame


def _row(source: str, display: str, kind: str, department: str, title: str, created: date, disabled: str) -> dict:
    upn = source if kind == "service" else _upn(display)
    return {"source": source, "display_name": display, "upn": f"{upn}@{DOMAIN}", "account_type": kind, "department": department,
            "job_title": title, "status": "disabled" if disabled else "enabled", "created_at": created.isoformat(), "disabled_at": disabled}


def _upn(display: str) -> str:
    parts = display.replace(".", "").split()
    return f"{parts[0][0]}.{parts[-1]}".lower()


def _last_sign_in(row, days_ago: int) -> str:
    if row.source == roles.AUDIT_ACCOUNT_GRADER:
        return AUDIT_INCIDENT.end.isoformat()
    if row.disabled_at:
        return (date.fromisoformat(row.disabled_at) - timedelta(days=1 + days_ago % 5)).isoformat()
    return (SNAPSHOT - timedelta(days=1 + days_ago)).isoformat()


def _mappings(accounts: pd.DataFrame) -> pd.DataFrame:
    by_source = accounts.set_index("source")
    rows = []
    for grader in ROSTER:
        account = by_source.loc[grader.grader_id]
        granted = account["created_at"]
        for role in roles.GRADER_ROLES + (roles.LEAD_EXTRA if grader.lead else ()):
            rows.append((account["account_id"], role, granted, account["disabled_at"], grader.grader_id in roles.STALE_GRADERS))
    for key, held in roles.STAFF_ROLES.items():
        account = by_source.loc[key]
        for role in held:
            rows.append((account["account_id"], role, account["created_at"], "", False))
        if key in roles.ROLE_CHANGE:
            start, end, old = roles.ROLE_CHANGE[key]
            rows.extend((account["account_id"], role, start.isoformat(), end.isoformat(), key in roles.STALE_STAFF) for role in old)
    for source, _, held in roles.SERVICE_ACCOUNTS:
        account = by_source.loc[source]
        rows.extend((account["account_id"], role, account["created_at"], "", False) for role in held)
    frame = pd.DataFrame(rows, columns=["account_id", "role", "granted_at", "revoked_at", "_stale_row"])
    return frame.sort_values(["account_id", "role", "granted_at"]).reset_index(drop=True)


def _stale_ids(accounts: pd.DataFrame) -> list[str]:
    sources = set(roles.STALE_GRADERS) | set(roles.STALE_STAFF)
    return sorted(accounts.loc[accounts["source"].isin(sources), "account_id"].tolist())


def _id_for(accounts: pd.DataFrame, source: str) -> str:
    return str(accounts.loc[accounts["source"] == source, "account_id"].iloc[0])


def _gold(accounts: pd.DataFrame, mappings: pd.DataFrame, stale: list[str]) -> list[dict]:
    gold = []
    for account_id in stale:
        account = accounts[accounts["account_id"] == account_id].iloc[0]
        lost = mappings[(mappings["account_id"] == account_id) & mappings["_stale_row"]]
        gold.append({"account_id": account_id, "display_name": account["display_name"],
                     "reason": "left" if account["disabled_at"] else "role_change",
                     "should_end": account["disabled_at"] or str(lost["revoked_at"].min()),
                     "roles_kept": sorted(lost["role"].tolist())})
    return gold
