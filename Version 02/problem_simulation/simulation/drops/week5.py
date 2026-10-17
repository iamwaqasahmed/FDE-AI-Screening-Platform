"""Week 5: the CDO brings the pilot forward and adds a hospital site; the press office needs a public line."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.delivery.plan import pilot_path
from simulation.drops.common import add_drop, memo
from simulation.drops.press import press_gold, press_query
from simulation.drops.rules import PRIMARY_CARE_SITES, SECOND_SITE
from simulation.world.engagement import PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED, SCOPE_CHANGE
from simulation.world.staff import name, role


def build(world: dict, rng: np.random.Generator) -> None:
    bound = pilot_path(date.min)
    files = {"scope_change_cdo.md": _scope_memo(), "press_query.md": press_query()}
    brief = [
        f"{name('cdo')} has changed the pilot scope. The press office has a media and ministerial query due this week.",
        "Re-plan with evidence, and draft the two-paragraph public answer.",
    ]
    gold = {
        "change": "CDO scope change and press query",
        "requested_pilot": PILOT_DATE_REQUESTED.isoformat(),
        "previous_pilot": PILOT_DATE_ORIGINAL.isoformat(),
        "requested_feasible": date.fromisoformat(bound["earliest_pilot"]) <= PILOT_DATE_REQUESTED,
        "earliest_pilot_lower_bound": bound["earliest_pilot"],
        "full_answer_in": "truth/gold/pilot_date.json",
        "second_site": SECOND_SITE,
        "second_site_allowed": SECOND_SITE in PRIMARY_CARE_SITES,
        "conflicts_with": ["week-3 DPO restriction to primary-care captures", "FRZ-0301 registry freeze",
                           "framework call-off lead time after Gate 2"],
        "invalidates": ["any plan that dates the pilot from the original roadmap", "a cohort that includes the second site"],
        "press": press_gold(),
    }
    add_drop(world, 5, "Scope change and press query", brief, files, gold)


def _scope_memo() -> str:
    return memo(
        "Pilot scope change", f"{name('cdo')}, {role('cdo')}", "Engagement team", SCOPE_CHANGE,
        [
            f"The minister wants visible progress. Please bring the AI triage pilot forward to {PILOT_DATE_REQUESTED.isoformat()}.",
            f"Add {SECOND_SITE} as a second pilot site so we cover a hospital clinic as well as primary care.",
            "Procurement tell me we can treat the contract as a variation of the existing vendor agreement, so it should be quick.",
            "I need a yes and a plan by the end of the week.",
        ],
    )
