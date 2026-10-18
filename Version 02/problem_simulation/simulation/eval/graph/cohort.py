"""Contact status, who was not reached, the clock, and the re-send that does no harm."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.delivery.cohort import overdue_people
from simulation.eval.enterprise.drop import v3_frame
from simulation.eval.evidence.overdue import _messages, _vendor, _workbook
from simulation.policy.apply import applicable_clause
from simulation.world.engagement import WEEKS
from simulation.world.sites import HARBOUR, NCEC

TODAY = WEEKS[4]


def facts(world: dict, linked: dict) -> tuple[dict, list[dict]]:
    chase = linked["chase"]
    allowed = _allowed(world)
    lost_bound = chase[chase["in_bound"] & chase["status"].eq("lost")]
    resend = _resend(world, linked)
    return {
        "contact_status": _contact(chase),
        "chase_lost_people": _people(world, lost_bound),
        "pilot_scope_lost": _pilot(world, allowed, chase),
        "clock_breaches": _clocks(lost_bound),
        "resend_summary": _summary(resend),
    }, resend


def clinic_class(hospital: str, referred: str, mrn: str) -> str:
    if not mrn or not hospital:
        return "blank"
    day = date.fromisoformat(str(referred))
    if hospital == NCEC:
        return "ncec-after" if day >= _adopt("ncec") else "ncec-before"
    if hospital == HARBOUR:
        return "harbour-after" if day >= _adopt("harbour") else "harbour-before"
    return "other"


def _adopt(which: str):
    from simulation.world import clock
    return clock.NCEC_ADOPT if which == "ncec" else clock.HARBOUR_ADOPT


def _contact(chase: pd.DataFrame) -> dict:
    bound = chase[chase["in_bound"]]
    return {
        "chased": int(len(chase)),
        "seen": int(chase["seen"].sum()),
        "deceased": int(chase["deceased"].sum()),
        "moved": int(chase["moved"].sum()),
        "bound": int(len(bound)),
        "once": int(bound["status"].eq("once").sum()),
        "twice": int(bound["status"].eq("twice").sum()),
        "lost": int(bound["status"].eq("lost").sum()),
    }


def _people(world: dict, lost_bound: pd.DataFrame) -> dict:
    alias = world["people"].set_index("person_uid")["alias_of"].fillna("")
    canon = {uid: (other if other else uid) for uid, other in alias.items()}
    people = lost_bound["person_uid"].map(canon).fillna(lost_bound["person_uid"])
    return {"local_ids": int(lost_bound["local_pid"].nunique()), "people": int(people.nunique()), "is_upper_bound": True}


def _pilot(world: dict, allowed: list[str], chase: pd.DataFrame) -> dict:
    scope = _pilot_ids(world, allowed)
    lost = set(chase.loc[chase["status"].eq("lost"), "local_pid"].astype(str))
    return {"local_ids": len(scope & lost), "is_upper_bound": True}


def _pilot_ids(world: dict, allowed: list[str]) -> set[str]:
    from simulation.eval.evidence.overdue import _filled_mrns

    messages, book = _messages(world), _workbook(world)
    latest = messages.sort_values(["referred", "mrn", "local_pid"]).groupby("local_pid", as_index=False).tail(1)
    blank = latest[latest["seen"].eq("") & latest["local_pid"].ne("")]
    still = blank[~blank["mrn"].isin(_filled_mrns(world))]
    flags = v3_frame(world).drop_duplicates("LOCAL_PID").set_index("LOCAL_PID")["FLAG"]
    gone = still["local_pid"].map(flags).isin(["DECEASED", "MOVED"])
    bound = set(still.loc[~gone, "local_pid"].astype(str))
    names = book.fillna("").drop_duplicates("FILE_NAME").set_index("FILE_NAME")["LOCAL_PID"].astype(str)
    scoped = _vendor(world)
    scoped = scoped[scoped["site"].astype(str).isin(allowed)]
    linked = scoped["file_name"].astype(str).map(names).fillna("")
    return bound & set(linked[linked.ne("")])


def _clocks(lost_bound: pd.DataFrame) -> dict:
    rows = []
    for row in lost_bound.itertuples(index=False):
        limit, document = _limit(row.hospital, row.referred)
        if limit is None:
            continue
        elapsed = (TODAY - date.fromisoformat(str(row.referred))).days
        rows.append((document, elapsed - limit))
    documents = sorted({document for document, _ in rows})
    centre = pd.Series([days for _, days in rows]).median() if rows else 0
    return {"with_clock": len(rows), "clause_ids": documents, "median_days_over": round(float(centre), 1)}


def _limit(hospital: str, referred: str) -> tuple[int | None, str]:
    if not hospital:
        return None, ""
    clause = applicable_clause(hospital, date.fromisoformat(str(referred)), "specialist_review")
    if clause.days is None:
        return None, ""
    return int(clause.days), clause.document_id


def binding(hospital: str, referred: str, mrn: str):
    """The specialist-review clause, including the national text when no clinic clock applies."""
    site = hospital if mrn and hospital else ""
    on = date.fromisoformat(str(referred)) if referred else TODAY
    return applicable_clause(site, on, "specialist_review")


def _resend(world: dict, linked: dict) -> list[dict]:
    chase = linked["chase"].drop_duplicates("local_pid").set_index("local_pid")
    flags = v3_frame(world).drop_duplicates("LOCAL_PID").set_index("LOCAL_PID")["FLAG"].astype(str)
    rows = []
    lost = linked["reconciled"][linked["reconciled"]["status"].eq("lost")].sort_values("request_id")
    for row in lost.itertuples(index=False):
        action, reason = _decision(row.local_pid, chase, flags)
        rows.append({"request_id": row.request_id, "local_pid": row.local_pid, "action": action, "reason": reason})
    return rows


def _decision(local_pid: str, chase: pd.DataFrame, flags: pd.Series) -> tuple[str, str]:
    if local_pid in chase.index and bool(chase.at[local_pid, "seen"]):
        return "hold", "seen"
    flag = str(flags.get(local_pid, ""))
    if flag == "DECEASED":
        return "hold", "deceased"
    if flag == "MOVED":
        return "hold", "moved"
    return "resend", ""


def _summary(rows: list[dict]) -> dict:
    reasons = pd.Series([row["reason"] for row in rows if row["action"] == "hold"])
    return {
        "resend": sum(row["action"] == "resend" for row in rows),
        "hold_seen": int(reasons.eq("seen").sum()),
        "hold_deceased": int(reasons.eq("deceased").sum()),
        "hold_moved": int(reasons.eq("moved").sum()),
        "key": "request_id",
    }


def _allowed(world: dict) -> list[str]:
    from simulation.drops.rules import PRIMARY_CARE_SITES
    return list(PRIMARY_CARE_SITES)


def hidden_overdue(world: dict) -> int:
    return int(len(overdue_people(world["events"], world["people"])))
