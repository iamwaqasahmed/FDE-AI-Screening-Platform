"""Hidden values the debrief can name and the invariants can check."""

from __future__ import annotations

import pandas as pd

from simulation.delivery.cohort import overdue_people
from simulation.eval.graph.cohort import hidden_overdue


def facts(world: dict, items: dict, reconciled: pd.DataFrame) -> dict:
    lost = reconciled[reconciled["status"].eq("lost")]
    duplicated = reconciled[reconciled["copies"].ge(2)]
    overdue = set(overdue_people(world["events"], world["people"])["person_uid"])
    lost_chase = lost[lost["template"].eq("referral-chase")]
    return {
        "lost_days": sorted(set(lost["requested_at"].astype(str))),
        "duplicate_days": sorted(set(duplicated["requested_at"].astype(str))),
        "hidden_overdue": hidden_overdue(world),
        "hidden_lost": int(lost_chase["person_uid"].isin(overdue).sum()),
        "loop_days": list(items["drop_incident"]["loop_days"]),
        "chased": items["contact_status"]["chased"],
    }
