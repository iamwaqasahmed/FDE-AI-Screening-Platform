"""Every findings item, computed from the files a team can open."""

from __future__ import annotations

import re
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from reference_enterprise.cohorts import overdue, vendor
from reference_enterprise.defects import defects
from reference_enterprise.load import current, documents, read_csv, reissue, v3, warehouse
from reference_enterprise.quality import blocked, booking, catalogue, confidence, raci, release, sms

SQL_DATE = re.compile(r"date\('(\d{4}-\d{2}-\d{2})'")


def findings(data: Path) -> dict:
    registry, earlier = v3(data), current(data)
    cohort, leak = vendor(data)
    return {
        "drop_schema": _schema(data),
        "drop_reissue": _reissue(data),
        "drop_local_ids": {"added": _added(earlier, registry, data)},
        "api_v3": _api(),
        "catalogue_stale": {"entries": catalogue(data)},
        "sms_reconcile": sms(data),
        "booking_reconcile": booking(data),
        "feed_dedupe": {"key": "event_id", "order": "occurred_at"},
        "unlinked_keys": {"keys": ["booking_id", "lab_pid"]},
        "identity_defects": defects(data, registry),
        "confidence_rule": confidence(data),
        "eligible_people": {"count": _eligible(registry)},
        "eligible_by_district": {"counts": _districts(registry)},
        "coverage": _coverage(data, registry),
        "site_rules": _sites(data),
        "stale_register": _stale(data),
        "overdue": overdue(data, registry),
        "vendor_cohort": cohort,
        "split_leak": leak,
        "release_plan": release(data),
        "freeze_blocked": {"tickets": blocked(data)},
        "rerun_contracts": {"contracts": ["C-01", "C-02"]},
        "raci_v3": raci(data),
    }


def _schema(data: Path) -> dict:
    text = (data / "drops/week-2/registry/schema_v3.md").read_text(encoding="utf-8")
    renamed = {"HOME_CLINIC": "REGISTERED_SITE"} if "HOME_CLINIC" in text and "REGISTERED_SITE" in text else {}
    added = [name for name in ("DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION") if name in text]
    return {"renamed": renamed, "added": added, "dob": "iso"}


def _reissue(data: Path) -> dict:
    batch = reissue(data)
    lost = int(warehouse(data)["registry_no"].isin(set(batch["OLD_REGISTRY_NO"])).sum())
    return {"count": int(len(batch)), "warehouse_lost": lost}


def _added(earlier: pd.DataFrame, registry: pd.DataFrame, data: Path) -> int:
    batch = reissue(data)
    old = dict(zip(batch["NEW_REGISTRY_NO"], batch["OLD_REGISTRY_NO"]))
    number = registry["REGISTRY_NO"].map(lambda value: old.get(value, value))
    blank = set(earlier.loc[earlier["LOCAL_PID"].eq("") & earlier["REGISTRY_NO"].ne(""), "REGISTRY_NO"])
    restored = number.isin(blank) & registry["LOCAL_PID"].ne("")
    both = earlier["LOCAL_PID"].eq("") & earlier["REGISTRY_NO"].eq("")
    return int(restored.sum() + both.sum())


def _api() -> dict:
    from enterprise_check.live import api_shape

    shape = api_shape()
    return {"keeps": shape["keeps"], "missing": shape["missing"], "old_numbers": True}


def _eligible(registry: pd.DataFrame) -> int:
    return int((registry["FLAG"].eq("") & ~registry["LOCAL_PID"].str.startswith("LX")).sum())


def _districts(registry: pd.DataFrame) -> dict:
    eligible = registry[registry["FLAG"].eq("") & ~registry["LOCAL_PID"].str.startswith("LX")]
    return {str(name): int(count) for name, count in eligible.groupby("DISTRICT").size().items()}


def _coverage(data: Path, registry: pd.DataFrame) -> dict:
    sql = (data / "handover/warehouse/build.sql").read_text(encoding="utf-8")
    snapshot = datetime.fromisoformat(SQL_DATE.search(sql).group(1)).date()
    cutoff = (snapshot - timedelta(days=730)).isoformat()
    sheet = warehouse(data)
    renamed = dict(zip(reissue(data)["OLD_REGISTRY_NO"], reissue(data)["NEW_REGISTRY_NO"]))
    number = sheet["registry_no"].map(lambda old: renamed.get(old, old))
    living = set(registry.loc[registry["FLAG"].eq("") & ~registry["LOCAL_PID"].str.startswith("LX"), "REGISTRY_NO"])
    dated = sheet["last_screen_date"].ne("") & sheet["last_screen_date"].ge(cutoff)
    return {"people": int((number.isin(living) & dated).sum()), "days": 730, "warehouse_months": 12}


def _sites(data: Path) -> dict:
    docs = {row["document_id"]: row for row in documents(data)}
    hill, ncec, harbour, oakridge = (docs[name] for name in (
        "site-sop-hill-2022", "site-sop-ncec-2024", "site-sop-harbour-2025", "memo-oakridge-2024"))
    return {
        "hill_recall_days": 60,
        "hill_document": hill["document_id"],
        "hill_from": hill["effective"],
        "national_ungradable_days": 90,
        "ncec_specialist_days": 14,
        "ncec_from": ncec["effective"],
        "harbour_specialist_days": 14,
        "harbour_from": harbour["effective"],
        "oakridge_memo": oakridge["document_id"],
        "oakridge_from": oakridge["effective"],
        "oakridge_sunset": oakridge.get("sunset", ""),
    }


def _stale(data: Path) -> dict:
    register = read_csv(data, "corpus/register.csv")
    docs = {row["document_id"]: row for row in documents(data)}
    stale = [row.document_id for row in register.itertuples(index=False)
             if (header := docs.get(row.document_id)) and row.status == "draft" and header.get("status") == "in_force"]
    return {"documents": stale, "register_says": "draft"}
