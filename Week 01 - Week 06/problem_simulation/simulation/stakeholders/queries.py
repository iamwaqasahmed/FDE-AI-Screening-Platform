"""Named truth queries over the world. A hidden fact's value is one of these, so it can be recomputed."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.economics.reminder import naive_before_after, true_uplift
from simulation.economics.summary import economic_summary
from simulation.world.clock import (BUREAU_MIGRATION_END, BUREAU_MIGRATION_START, OUTAGE_END, OUTAGE_START,
                                    ROTA_CHANGE, SNAPSHOT)
from simulation.world.sites import RIVER_SITE

BACKLOG_FROM = f"{SNAPSHOT.year - 1}-{SNAPSHOT.month:02d}-01"
_SUMMARY: list[tuple[dict, dict]] = []


def pct(value: float) -> str:
    return f"{round(100 * float(value))}%"


def summary_for(world: dict) -> dict:
    """Economic summary for this world object, computed once while it is the most recent world asked about."""
    if not _SUMMARY or _SUMMARY[0][0] is not world:
        _SUMMARY[:] = [(world, economic_summary(world))]
    return _SUMMARY[0][1]


def _grader_error(world: dict, after: bool) -> str:
    events = world["events"]
    reads = events[(events["grader_id"] == "G05") & events["grade"].isin(["R0", "R1", "R2", "R3"])]
    side = reads["graded_at"] >= ROTA_CHANGE.isoformat()
    reads = reads[side if after else ~side]
    return pct((reads["grade"] != "R" + reads["true_level"].astype(str)).mean())


def _vendor_sensitivity(world: dict, older: bool) -> str:
    events = world["events"]
    scored = events[events["vendor_score"].notna() & events["true_referable"]]
    age = (pd.to_datetime(scored["photo_date"]) - pd.to_datetime(scored["dob"])).dt.days / 365.25
    group = scored[(age >= 75) if older else (age < 75)]
    return pct((group["vendor_score"] >= 0.5).mean())


def _recent_referrals(world: dict) -> pd.DataFrame:
    events = world["events"]
    return events[events["referred_at"] >= BACKLOG_FROM]


def _lead_backlog(world: dict) -> int:
    referrals = _recent_referrals(world)
    blanked = referrals["event_id"].str.slice(1).astype(int) % 2 == 0
    return int((blanked | referrals["seen_at"].eq("")).sum())


def _never_graded_share(world: dict) -> str:
    events = world["events"]
    never = events[events["cohort"] == "photo_no_result"]
    return pct(never["district"].isin(["Hill Counties", "River Districts"]).mean())


def _migration_letter_breaches(world: dict) -> int:
    events = world["events"]
    inside = events["graded_at"].between(BUREAU_MIGRATION_START.isoformat(), BUREAU_MIGRATION_END.isoformat())
    return int((events["breach"].eq("letter_bureau") & inside).sum())


def _outage_captures(world: dict) -> int:
    events = world["events"]
    inside = events["photo_date"].between(OUTAGE_START.isoformat(), OUTAGE_END.isoformat())
    return int((events["site"].eq(RIVER_SITE) & inside).sum())


EVENT_QUERIES = {
    "g05_error_before": lambda w: _grader_error(w, False),
    "g05_error_after": lambda w: _grader_error(w, True),
    "urgent_in_notes": lambda w: int(w["events"]["grade_hidden"].sum()),
    "migration_letter_breaches": _migration_letter_breaches,
    "duplicate_letters": lambda w: int(w["events"]["letter_duplicate"].sum()),
    "lead_backlog": _lead_backlog,
    "board_backlog": lambda w: int(_recent_referrals(w)["breach"].eq("booking").sum()),
    "true_backlog": lambda w: int((_recent_referrals(w)["seen_at"].eq("") & ~_recent_referrals(w)["dna"]).sum()),
    "backlog_from": lambda w: BACKLOG_FROM,
    "never_graded_hill_river": _never_graded_share,
    "agency_reads": lambda w: int(w["events"]["grader_id"].isin(["G11", "G12"]).sum()),
    "vendor_sens_older": lambda w: _vendor_sensitivity(w, True),
    "vendor_sens_younger": lambda w: _vendor_sensitivity(w, False),
    "pilot_images": lambda w: int(w["events"]["pilot"].sum()),
    "outage_captures": _outage_captures,
    "alias_records": lambda w: int(w["people"]["alias_of"].ne("").sum()),
    "ophthalmology_dna": lambda w: pct(w["events"].loc[w["events"]["referred_at"].ne(""), "dna"].mean()),
    "silent_movers": lambda w: int(w["people"]["silent_move_on"].ne("").sum()),
    "progressed_in_delay": lambda w: int(w["events"]["progressed_in_delay"].sum()),
}


def _uplift(district: str, naive: bool):
    def query(world: dict) -> str:
        values = naive_before_after(world["invitations"]) if naive else true_uplift(world["invitations"])
        return f"{100 * values[district]:.1f} points"

    return query


def _net(key: str):
    return lambda w: f"{int(next(r for r in summary_for(w)['opportunities'] if r['key'] == key)['net_annual_gbp']):,}"


ECONOMICS_QUERIES = {
    "costliest_problem": lambda w: summary_for(w)["costliest_problem"].replace("_", " "),
    "most_voiced_problem": lambda w: summary_for(w)["most_voiced_problem"].replace("_", " "),
    "top_net_opportunity": lambda w: summary_for(w)["net_rank"][0].replace("_", " "),
    "vendor_expansion_net": _net("vendor_model_expansion"),
    "letter_fix_net": _net("letter_bureau_fix"),
    "letter_calls_per_year": lambda w: f"{round(summary_for(w)['volumes']['calls'].get('letter_not_received', 0.0))}",
    "primary_reads_per_year": lambda w: str(int(np.round(summary_for(w)["volumes"]["primary_reads"]))),
}
for _district in ("North City", "East City", "Hill Counties", "River Districts"):
    _slug = _district.lower().replace(" ", "_")
    ECONOMICS_QUERIES[f"reminder_true_{_slug}"] = _uplift(_district, False)
    ECONOMICS_QUERIES[f"reminder_naive_{_slug}"] = _uplift(_district, True)
