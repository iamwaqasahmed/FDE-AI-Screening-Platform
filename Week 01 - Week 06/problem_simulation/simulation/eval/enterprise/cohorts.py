"""Cohorts a team can count from the drop, plus the hidden counts the debrief names."""

from __future__ import annotations

import re
from datetime import datetime

import numpy as np
import pandas as pd

from simulation.delivery.cohort import cohort_values
from simulation.eval.enterprise.drop import v3_frame
from simulation.eval.enterprise.links import grader_file_names
from simulation.ml.retrospective import scored_frame
from simulation.systems.mrn import MrnIndex
from simulation.systems.ophthalmology import shown_referral
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso

LEAK_SEED = 20261012
SEEN_ON = re.compile(r"in clinic on (\d{1,2}/\d{1,2}/\d{4}|\d{1,2} [A-Z][a-z]+ \d{4})", re.I)
MRN = re.compile(r"Hospital number: (\S+)")


def cohorts(world: dict) -> dict:
    messages = _messages(world)
    filled = _filled_mrns(world)
    visible = _visible(messages, filled, v3_frame(world))
    hidden = cohort_values(world["events"], world["people"])
    vendor = _vendor(world)
    return {"overdue": {**visible, "hidden_rows": hidden["overdue_rows_naive"], "hidden_people": hidden["overdue_people"]},
            "vendor": vendor}


def _messages(world: dict) -> pd.DataFrame:
    events = world["events"]
    referrals = events[events["referred_at"].ne("")]
    local_pid = ids_on(world["identifiers"], "local_pid", iso(SNAPSHOT))
    index = MrnIndex(world["identifiers"])
    rows = []
    for row in referrals.itertuples(index=False):
        booked, seen = shown_referral(row)
        rows.append({
            "mrn": index.get(row.person_uid, row.site, row.photo_date),
            "local_pid": "" if local_pid.get(row.person_uid, "") is None else str(local_pid.get(row.person_uid, "") or ""),
            "referred": row.referred_at,
            "seen": seen,
        })
    return pd.DataFrame(rows)


def _filled_mrns(world: dict) -> set[str]:
    found = set()
    for path, body in world["files"].items():
        if not str(path).startswith("handover/epr_letters/") or not isinstance(body, str):
            continue
        mrn = MRN.search(body)
        if mrn and SEEN_ON.search(body):
            found.add(mrn.group(1))
    return found


def _visible(messages: pd.DataFrame, filled: set[str], registry: pd.DataFrame) -> dict:
    blank = messages["seen"].eq("")
    latest = messages.sort_values("referred").groupby("local_pid", as_index=False).tail(1)
    latest_blank = latest[latest["seen"].eq("") & latest["local_pid"].ne("")]
    still_blank = latest_blank[~latest_blank["mrn"].isin(filled)]
    flags = registry.set_index("LOCAL_PID")["FLAG"]
    gone = still_blank["local_pid"].map(flags).isin(["DECEASED", "MOVED"])
    return {
        "rows": int(len(messages)),
        "blank_rows": int(blank.sum()),
        "latest_blank": int(len(latest_blank)),
        "upper_bound": int((~gone).sum()),
        "upper_tolerance": 0.02,
        "epr_mrns": len(filled),
    }


def _vendor(world: dict) -> dict:
    scored = scored_frame(world["events"])
    names = grader_file_names(world["events"])
    linked = scored["file_name"].astype(str).isin(names)
    people = scored.loc[linked, "person_uid"].map(_canon(world)).nunique()
    return {
        "captures": int(len(scored)),
        "linked_by_file": int(linked.sum()),
        "linked_people": int(people),
        "unlinked": int((~linked).sum()),
        "leak_share": _leak(scored, linked, world),
        "leak_seed": LEAK_SEED,
        "leak_tolerance": 0.03,
        "true_leak_share": _leak(scored, pd.Series(True, index=scored.index), world),
    }


def _canon(world: dict) -> dict[str, str]:
    alias = world["people"].set_index("person_uid")["alias_of"].fillna("")
    return {uid: (other if other else uid) for uid, other in alias.items()}


def _leak(scored: pd.DataFrame, linked: pd.Series, world: dict) -> float:
    canon = scored["person_uid"].map(_canon(world))
    person = np.where(linked.to_numpy(), canon.to_numpy(), "solo:" + scored["capture_ref"].astype(str).to_numpy())
    order = np.random.default_rng(LEAK_SEED).permutation(len(person))
    cut = int(0.8 * len(person))
    train = set(person[order[:cut]])
    test = person[order[cut:]]
    if len(test) == 0:
        return 0.0
    return round(float(np.mean([item in train for item in test])), 4)
