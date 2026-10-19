"""Week 1 discovery gold, computed from the world so a check can be rerun on any seed.

Written to truth/gold/discovery.json. Participants do not read it.
"""

from __future__ import annotations

import numpy as np

from simulation.economics.budgets import budgets_frame
from simulation.economics.dependencies import prerequisites
from simulation.economics.opportunities import BY_KEY, OPPORTUNITIES
from simulation.economics.reminder import reminder_gold
from simulation.eval.discovery_profile import profiling
from simulation.stakeholders.queries import EVENT_QUERIES, summary_for
from simulation.stakeholders.research.calls import call_gold
from simulation.stakeholders.workshop import IDEAS
from simulation.systems.catalog import (
    DISPATCH_SYSTEM,
    OWNERS,
    SCORE_SYSTEM,
    SEEN_DATE_SYSTEMS,
    SIGNED_GRADE_SYSTEM,
    SYSTEMS,
)
from simulation.systems.resolve import ids_on
from simulation.world import clock as c
from simulation.world.engagement import PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED
from simulation.world.timeline import TIMELINE

CALLS = "engagement/research/call_reasons.csv"
ELIGIBLE_TOLERANCE = 0.02
AGENCY_YEAR = "2025-26"
AGENCY_CENTRE = "SCR-215"
KEYS = ["booking_id", "lab_pid", "local_pid", "mrn", "registry_no"]


def build(world: dict) -> dict:
    summary = summary_for(world)
    eligible = _eligible(world)
    ranking = _ranking(summary)
    return {
        "snapshot": c.iso(c.SNAPSHOT),
        "systems": [{"id": row["system_id"], "zone": row["trust_zone"]} for row in SYSTEMS],
        "records": _records(),
        "vendor_hosting": next(row["hosting"] for row in SYSTEMS if row["system_id"] == "vendor"),
        "safety_owner": dict(OWNERS)["clinical_safety_owner"],
        "timeline": [_happening(item) for item in TIMELINE],
        "profiling": profiling(),
        "eligible": eligible,
        "warehouse": {"counts_deceased": True, "coverage_months": 12},
        "reminder": _reminder(world),
        "ranking": ranking,
        "workshop": {"top_idea": IDEAS[0][0], "top_opportunity": IDEAS[0][2]},
        "research": {"most_voiced": summary["most_voiced_problem"], "costliest": summary["costliest_problem"]},
        "backlog": _backlog(world),
        "letters": _happening(next(item for item in TIMELINE if item.ref == "CHG-0158")),
        "calls": _calls(world),
        "vendor": {
            "from": c.iso(c.VENDOR_START),
            "hospitals": False,
            "under_75": EVENT_QUERIES["vendor_sens_younger"](world),
            "aged_75_plus": EVENT_QUERIES["vendor_sens_older"](world),
        },
        "urgent": {"field": "notes", "text": _urgent_text(), "count": int(world["events"]["grade_hidden"].sum())},
        "rota": {"ref": "CHG-0171", "date": c.iso(c.ROTA_CHANGE)},
        "agency": _agency(world),
        "board_fee": {"gbp": _board_fee(summary)},
        "freezes": _freezes(),
        "keys": list(KEYS),
        "brief": _brief(eligible, ranking),
    }


def _records() -> dict:
    return {
        "grade": SIGNED_GRADE_SYSTEM,
        "dispatch": DISPATCH_SYSTEM,
        "seen": sorted(SEEN_DATE_SYSTEMS),
        "score": SCORE_SYSTEM,
    }


def _eligible(world: dict) -> dict:
    people = world["people"]
    on = c.iso(c.SNAPSHOT)
    numbers = ids_on(world["identifiers"], "registry_no", on)
    has_number = people["person_uid"].map(numbers).fillna("").ne("")
    recorded = people["flag_recorded_on"].ne("") & people["flag_recorded_on"].le(on)
    shown = np.where(recorded.to_numpy(), people["flag"].to_numpy(), "")
    warehouse = int((has_number.to_numpy() & ((shown == "") | (shown == "DECEASED"))).sum())
    return {
        "count": int((people["alias_of"].eq("") & people["flag"].eq("")).sum()),
        "tolerance": ELIGIBLE_TOLERANCE,
        "registry_rows": int(people["diagnosis_date"].le(on).sum()),
        "warehouse": warehouse,
    }


def _ranking(summary: dict) -> dict:
    order = list(summary["net_rank"])
    keys = [item.key for item in OPPORTUNITIES]
    return {
        "keys": keys,
        "highest": order[0],
        "lowest": order[-1],
        "prerequisites": {key: prerequisites(key) for key in keys},
        "blockers": {key: list(BY_KEY[key].blockers) for key in keys},
    }


def _reminder(world: dict) -> dict:
    gold = reminder_gold(world["invitations"])
    return {
        "change_date": gold["change_date"],
        "naive": {district: row["naive_before_after"] for district, row in gold["districts"].items()},
        "true_uplift": {district: row["true_uplift"] for district, row in gold["districts"].items()},
        "naive_tolerance": 0.03,
    }


def _backlog(world: dict) -> dict:
    return {
        "from": EVENT_QUERIES["backlog_from"](world),
        "lead": int(EVENT_QUERIES["lead_backlog"](world)),
        "board": int(EVENT_QUERIES["board_backlog"](world)),
        "true": int(EVENT_QUERIES["true_backlog"](world)),
    }


def _calls(world: dict) -> dict:
    frame = world["files"].get(CALLS)
    peak = call_gold(frame)["letter_peak_month"] if frame is not None else ""
    return {"letter_peak_month": peak, "letter_ref": "CHG-0158", "hospital_ref": "INC-0251"}


def _agency(world: dict) -> dict:
    budgets = budgets_frame(world)
    rows = budgets[(budgets["financial_year"] == AGENCY_YEAR) & (budgets["cost_centre"] == AGENCY_CENTRE)]
    return {"year": AGENCY_YEAR, "centre": AGENCY_CENTRE, "gbp": float(rows["actual_gbp"].sum()), "tolerance": 0.01}


def _board_fee(summary: dict) -> int:
    vendor = next(row for row in summary["opportunities"] if row["key"] == "vendor_model_expansion")
    return int(vendor["running_cost_gbp"])


def _freezes() -> dict:
    found = {item.ref: item for item in TIMELINE}
    return {name: {"ref": ref, "start": c.iso(found[ref].start)}
            for name, ref in (("registry", "FRZ-0301"), ("bureau", "FRZ-0302"))}


def _urgent_text() -> str:
    from simulation.systems.grader import URGENT_NOTE

    return URGENT_NOTE


def _brief(eligible: dict, ranking: dict) -> dict:
    freeze = _freezes()["registry"]["start"]
    return {
        "facts": [
            {"id": "safety-owner", "tokens": ["clinical safety owner"]},
            {"id": "pilot-dates", "tokens": [c.iso(PILOT_DATE_REQUESTED), c.iso(PILOT_DATE_ORIGINAL)]},
            {"id": "stopped", "tokens": ["pilot", "stopped"]},
            {"id": "people", "tokens": ["deceased"]},
            {"id": "identity", "tokens": ["identity resolution"]},
            {"id": "letters", "tokens": ["letter"]},
            {"id": "reminder", "tokens": ["seasonality", "control"]},
            {"id": "workshop", "tokens": [IDEAS[0][0]]},
            {"id": "scope", "tokens": ["primary-care"]},
            {"id": "freeze", "tokens": [freeze]},
            {"id": "eligible", "number": eligible["count"], "tolerance": eligible["tolerance"]},
            {"id": "highest", "tokens": [ranking["highest"].replace("_", " ")]},
        ],
        "forbidden": [
            "Vendor model expansion should come first",
            "The reminder caused the whole rise in attendance",
            "Deceased people are eligible",
        ],
    }


def _happening(item) -> dict:
    return {
        "ref": item.ref,
        "kind": item.kind,
        "system": item.system,
        "start": c.iso(item.start),
        "end": c.iso(item.end) if item.end else "",
        "title": item.title,
    }
