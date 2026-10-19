"""Findings from the drop, the referral file, and the corpus headers."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from reference_enterprise.identity import clusters
from reference_graph import load
from reference_graph.sources import call_signal, governance, incident_cost
from simulation.drops.bureau import LOOP_DAYS
from simulation.eval.evidence.drop import restriction
from simulation.eval.evidence.rates import clean


def build(data: Path) -> tuple[dict, pd.DataFrame, pd.DataFrame, list[dict]]:
    requests, dispatch, start, end = load.drop_files(data)
    released = _released(data)
    reconciled = _reconcile(requests, dispatch)
    chase = _chase(data, reconciled)
    resend = _resend(data, reconciled, chase)
    items = {
        **_drop(data, reconciled, start, end),
        **_cohort(data, chase, resend, released),
        **governance(data, released, end),
        "call_signal": call_signal(data),
        "incident_cost": incident_cost(data, reconciled, resend),
    }
    return items, reconciled, chase, resend


def _released(data: Path) -> date:
    text = (data / "drops/week-4/README.md").read_text(encoding="utf-8")
    return date.fromisoformat(re.search(r"Released (\d{4}-\d{2}-\d{2})", text).group(1))


def _reconcile(requests: pd.DataFrame, dispatch: pd.DataFrame) -> pd.DataFrame:
    copies = dispatch.groupby("request_id").size()
    frame = requests.copy()
    frame["copies"] = frame["request_id"].map(copies).fillna(0).astype(int)
    frame["status"] = frame["copies"].map({0: "lost", 1: "once"}).fillna("twice")
    return frame


def _chase(data: Path, reconciled: pd.DataFrame) -> pd.DataFrame:
    messages = load.messages(data)
    latest = messages.sort_values("referred").groupby("local_pid", as_index=False).tail(1)
    chase = latest[latest["seen"].eq("") & latest["local_pid"].ne("")].copy()
    hospital, _ambiguous = load.hospitals(data)
    filled = load.filled_mrns(data)
    flags = load.v3(data).drop_duplicates("LOCAL_PID").set_index("LOCAL_PID")["FLAG"]
    copies = reconciled[reconciled["template"].eq("referral-chase")][["local_pid", "request_id", "copies", "status"]]
    frame = chase.merge(copies, on="local_pid", how="left")
    frame["hospital"] = frame["mrn"].map(hospital).fillna("")
    frame["seen_flag"] = frame["mrn"].ne("") & frame["mrn"].isin(filled)
    flag = frame["local_pid"].map(flags).fillna("")
    frame["deceased"] = ~frame["seen_flag"] & flag.eq("DECEASED")
    frame["moved"] = ~frame["seen_flag"] & flag.eq("MOVED")
    frame["in_bound"] = ~frame["seen_flag"] & ~frame["deceased"] & ~frame["moved"]
    return frame


def _drop(data: Path, reconciled: pd.DataFrame, start: date, end: date) -> dict:
    sent = int((reconciled["copies"] > 0).sum())
    rows = int(reconciled["copies"].sum())
    contracts = load.read_csv(data, "engagement/workstreams/contracts.csv")
    changed = sorted(contracts.loc[contracts["changed_by_drop"].eq("week-4"), "contract_id"])
    return {
        "drop_incident": {
            "window": [start.isoformat(), end.isoformat()],
            "loop_days": [(start + timedelta(days=offset)).isoformat() for offset in LOOP_DAYS],
            "requests": int(len(reconciled)),
            "dispatch_rows": rows,
            "unique_dispatched": sent,
            "duplicate_rows": rows - sent,
            "lost": int(reconciled["status"].eq("lost").sum()),
            "notice_claims_hold": False,
        },
        "outputs_changed": {"contracts": changed, "week2_rule": "feed_dedupe", "unchanged": ["overdue", "overdue_pilot_scope"]},
        "dedupe_keys": {
            "transport_key": "dispatch_id", "business_key": "request_id",
            "transport_rows_removed": 0, "business_rows_removed": rows - sent,
        },
    }


def _cohort(data: Path, chase: pd.DataFrame, resend: list[dict], today: date) -> dict:
    bound = chase[chase["in_bound"]]
    lost_bound = bound[bound["status"].eq("lost")]
    return {
        "contact_status": {
            "chased": int(len(chase)),
            "seen": int(chase["seen_flag"].sum()),
            "deceased": int(chase["deceased"].sum()),
            "moved": int(chase["moved"].sum()),
            "bound": int(len(bound)),
            "once": int(bound["status"].eq("once").sum()),
            "twice": int(bound["status"].eq("twice").sum()),
            "lost": int(bound["status"].eq("lost").sum()),
        },
        "chase_lost_people": _people(data, lost_bound),
        "pilot_scope_lost": _pilot(data, chase),
        "clock_breaches": _clocks(data, lost_bound, today),
        "resend_summary": _summary(resend),
    }


def _people(data: Path, lost_bound: pd.DataFrame) -> dict:
    labels = clusters(data)
    registry = labels[labels["kind"].eq("registry")].drop_duplicates("record_id").set_index("record_id")["cluster_id"]
    people = lost_bound["local_pid"].map(registry).fillna(lost_bound["local_pid"])
    return {"local_ids": int(lost_bound["local_pid"].nunique()), "people": int(people.nunique()), "is_upper_bound": True}


def _pilot(data: Path, chase: pd.DataFrame) -> dict:
    memo = (data / "drops/week-3/dpo_restriction_memo.md").read_text(encoding="utf-8")
    allowed = restriction(memo, [])["allowed_sites"]
    scope = _pilot_ids(data, allowed)
    lost = set(chase.loc[chase["status"].eq("lost"), "local_pid"].astype(str))
    return {"local_ids": len(scope & lost), "is_upper_bound": True}


def _pilot_ids(data: Path, allowed: list[str]) -> set[str]:
    messages = load.messages(data)
    latest = messages.sort_values(["referred", "mrn", "local_pid"]).groupby("local_pid", as_index=False).tail(1)
    blank = latest[latest["seen"].eq("") & latest["local_pid"].ne("")]
    still = blank[~blank["mrn"].isin(load.filled_mrns(data))]
    flags = load.v3(data).drop_duplicates("LOCAL_PID").set_index("LOCAL_PID")["FLAG"]
    gone = still["local_pid"].map(flags).isin(["DECEASED", "MOVED"])
    bound = set(still.loc[~gone, "local_pid"].astype(str))
    book = pd.read_excel(data / "handover/grader/workbook.xlsx", dtype=str).fillna("")
    names = book.drop_duplicates("FILE_NAME").set_index("FILE_NAME")["LOCAL_PID"].astype(str)
    vendor = clean(pd.read_csv(data / "handover/ml/vendor_retrospective.csv", dtype=str).fillna(""))
    scoped = vendor[vendor["site"].isin(allowed)]
    linked = scoped["file_name"].map(names).fillna("")
    return bound & set(linked[linked.ne("")])


def _clocks(data: Path, lost_bound: pd.DataFrame, today: date) -> dict:
    from simulation.policy.apply import applicable_clause

    rows = []
    for row in lost_bound.itertuples(index=False):
        if not row.hospital:
            continue
        clause = applicable_clause(row.hospital, date.fromisoformat(str(row.referred)[:10]), "specialist_review")
        if clause.days is None:
            continue
        elapsed = (today - date.fromisoformat(str(row.referred)[:10])).days - int(clause.days)
        rows.append((clause.document_id, elapsed))
    documents = sorted({document for document, _ in rows})
    centre = pd.Series([days for _, days in rows]).median() if rows else 0
    return {"with_clock": len(rows), "clause_ids": documents, "median_days_over": round(float(centre), 1)}


def _resend(data: Path, reconciled: pd.DataFrame, chase: pd.DataFrame) -> list[dict]:
    seen = chase.drop_duplicates("local_pid").set_index("local_pid")
    flags = load.v3(data).drop_duplicates("LOCAL_PID").set_index("LOCAL_PID")["FLAG"].astype(str)
    rows = []
    lost = reconciled[reconciled["status"].eq("lost")].sort_values("request_id")
    for row in lost.itertuples(index=False):
        action, reason = _decision(row.local_pid, seen, flags)
        rows.append({"request_id": row.request_id, "local_pid": row.local_pid, "action": action, "reason": reason})
    return rows


def _decision(local_pid: str, chase: pd.DataFrame, flags: pd.Series) -> tuple[str, str]:
    if local_pid in chase.index and bool(chase.at[local_pid, "seen_flag"]):
        return "hold", "seen"
    flag = str(flags.get(local_pid, ""))
    if flag == "DECEASED":
        return "hold", "deceased"
    if flag == "MOVED":
        return "hold", "moved"
    return "resend", ""


def _summary(rows: list[dict]) -> dict:
    reasons = [row["reason"] for row in rows if row["action"] == "hold"]
    return {
        "resend": sum(row["action"] == "resend" for row in rows),
        "hold_seen": reasons.count("seen"),
        "hold_deceased": reasons.count("deceased"),
        "hold_moved": reasons.count("moved"),
        "key": "request_id",
    }

