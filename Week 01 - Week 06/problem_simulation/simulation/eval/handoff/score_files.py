"""Score the three CSV handoffs. Extra benign rows pass. An extra column fails."""

from __future__ import annotations

import pandas as pd

from simulation.eval.handoff.bars import FLOW_COLUMNS, HAZARD_COLUMNS, RATE_TOLERANCE, THREAT_COLUMNS
from simulation.eval.handoff.prose import has_count, has_rate


def score_flows(frame: pd.DataFrame | None, gold: dict) -> dict:
    rows = gold["files"]["flows"]
    if frame is None or list(frame.columns) != list(FLOW_COLUMNS):
        return {"ok": False, "rows": 0 if frame is None else len(frame)}
    found = {_key(row): row for _, row in frame.iterrows()}
    missing = [item["flow_id"] for item in rows if not _flow_ok(found.get(_key(item)), item)]
    extra = [_key(row) for _, row in frame.iterrows() if _yes(row) and _key(row) not in {_key(item) for item in rows}]
    denied = [item["flow_id"] for item in rows if item["allowed"] == "no" and _yes(found.get(_key(item)))]
    return {"ok": not missing and not extra and not denied, "rows": len(frame), "missing": missing}


def score_threats(frame: pd.DataFrame | None, gold: dict) -> dict:
    specs = gold["files"]["threats"]
    owners = set(gold["files"]["hazards"]["owners"])
    if frame is None or list(frame.columns) != list(THREAT_COLUMNS):
        return {"ok": False, "rows": 0 if frame is None else len(frame)}
    by_id = {str(row["threat_id"]): row for _, row in frame.iterrows()}
    missing = [item["threat_id"] for item in specs if not _threat_ok(by_id.get(item["threat_id"]), item, owners)]
    return {"ok": not missing, "rows": len(frame), "missing": missing}


def score_hazards(frame: pd.DataFrame | None, gold: dict) -> dict:
    spec = gold["files"]["hazards"]
    if frame is None or list(frame.columns) != list(HAZARD_COLUMNS):
        return {"ok": False, "rows": 0 if frame is None else len(frame), "groups": 0}
    signed = any(str(value).strip() for value in frame["signed_by"])
    owners = {str(value).strip() for value in frame["control_owner"]}
    owned = owners <= set(spec["owners"]) and "" not in owners
    groups = sum(_group(frame, group) for group in spec["groups"])
    return {"ok": not signed and owned and groups >= spec["need"], "rows": len(frame), "groups": groups}


def _flow_ok(row, spec: dict) -> bool:
    if row is None:
        return False
    allowed = str(row["allowed"]).strip().lower()
    return allowed == spec["allowed"] and str(row["rule"]).strip() in spec["rules"]


def _threat_ok(row, spec: dict, owners: set[str]) -> bool:
    if row is None or str(row["owner"]).strip() not in owners or not str(row["mitigation"]).strip():
        return False
    if str(row["standard"]).strip() not in spec["standards"] or _flag(row["live"]) is not spec["live"]:
        return False
    field = str(row[spec["field"]])
    groups = spec["any_of"] or [spec["need"]]
    return any(all(token in field for token in group) for group in groups)


def _group(frame: pd.DataFrame, group: dict) -> bool:
    hits = frame[frame["anchor"].astype(str).map(lambda value: any(anchor in value for anchor in group["anchors"]))]
    if hits.empty:
        return False
    if "number" not in group:
        return True
    return any(_number(" ".join(map(str, row)), group["number"]) for row in hits.to_numpy())


def _number(text: str, number) -> bool:
    if float(number) >= 2:
        return has_count(text, int(number))
    return has_rate(text, float(number), RATE_TOLERANCE)


def _key(row) -> tuple[str, str, str]:
    return (str(row["source"]).strip(), str(row["target"]).strip(), str(row["data"]).strip())


def _yes(row) -> bool:
    if row is None:
        return False
    return str(row["allowed"]).strip().lower() == "yes"


def _flag(value):
    text = str(value).strip().lower()
    if text in {"true", "yes", "1"}:
        return True
    if text in {"false", "no", "0"}:
        return False
    return None
