"""The overdue referable cohort and the vendor cohort, before and after identity resolution and the DPO restriction."""

from __future__ import annotations

import pandas as pd

from simulation.drops.rules import PRIMARY_CARE_SITES
from simulation.world.clock import SNAPSHOT, iso


def _present(people: pd.DataFrame) -> pd.Series:
    """Alive and still resident at the snapshot, by the true flag date rather than the lagged registry flag."""
    base = people[people["alias_of"] == ""]
    gone = (base["flag"] != "") & (base["flag_true_on"] != "") & (base["flag_true_on"] <= iso(SNAPSHOT))
    return base.loc[~gone, "person_uid"]


def latest_referrals(events: pd.DataFrame) -> pd.DataFrame:
    referred = events[events["referred_at"] != ""]
    return referred.sort_values(["person_uid", "referred_at", "event_id"]).groupby("person_uid", as_index=False).tail(1)


def overdue_people(events: pd.DataFrame, people: pd.DataFrame, sites: tuple[str, ...] = ()) -> pd.DataFrame:
    latest = latest_referrals(events)
    latest = latest[(latest["seen_at"] == "") & latest["person_uid"].isin(_present(people))]
    if sites:
        latest = latest[latest["site"].isin(sites)]
    return latest.sort_values("person_uid").reset_index(drop=True)


def overdue_rows_naive(events: pd.DataFrame) -> int:
    return int(((events["referred_at"] != "") & (events["seen_at"] == "")).sum())


def vendor_cohort(events: pd.DataFrame, restricted: bool) -> pd.DataFrame:
    scored = events[events["vendor_scored"]]
    if restricted:
        scored = scored[scored["site"].isin(PRIMARY_CARE_SITES)]
    return scored


def cohort_values(events: pd.DataFrame, people: pd.DataFrame) -> dict:
    overdue = overdue_people(events, people)
    restricted = overdue_people(events, people, PRIMARY_CARE_SITES)
    unresolved = events[(events["referred_at"] != "") & (events["seen_at"] == "")]["person_uid"].nunique()
    return {
        "overdue_rows_naive": overdue_rows_naive(events),
        "overdue_people_any_unseen_referral": int(unresolved),
        "overdue_people": int(len(overdue)),
        "overdue_people_primary_care": int(len(restricted)),
        "vendor_cohort_before_restriction": int(len(vendor_cohort(events, False))),
        "vendor_cohort_after_restriction": int(len(vendor_cohort(events, True))),
        "primary_care_sites": list(PRIMARY_CARE_SITES),
    }
