"""Week 6: the clinical director is named clinical safety owner, with conditions. The handover register is not updated."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.delivery.plan import pilot_path
from simulation.drops.common import add_drop, memo
from simulation.drops.rules import PRIMARY_CARE_SITES
from simulation.world.engagement import OWNER_NAMED
from simulation.world.staff import name, role

OWNER_KEY = "clinical_director"


def conditions() -> list[dict]:
    earliest = pilot_path(date.min)["earliest_pilot"]
    return [
        {"id": "CSO-1", "text": "A hazard log for the vendor pathway is complete and signed by the owner.",
         "met": False, "evidence": "No hazard log exists in the handover or the corpus."},
        {"id": "CSO-2", "text": f"The pilot is limited to primary-care captures at {' and '.join(PRIMARY_CARE_SITES)}.",
         "met": False, "evidence": "The week 5 scope change adds a hospital site; it must be withdrawn."},
        {"id": "CSO-3", "text": "A trained grader signs every result before any letter is sent; the model output is advisory.",
         "met": False, "evidence": "The design must show the grader sign-off step; nothing in the handover does."},
        {"id": "CSO-4", "text": "Everyone with an overdue referral whose chase letter was lost in week 4 is contacted again.",
         "met": False, "evidence": "The bureau run lost chase letters; no re-send is recorded."},
        {"id": "CSO-5", "text": "Go-live is no earlier than the earliest date the delivery plan shows to be feasible.",
         "met": False, "evidence": f"The CDO's requested date is earlier than {earliest}, the soonest feasible go-live."},
    ]


def build(world: dict, rng: np.random.Generator) -> None:
    items = conditions()
    files = {"clinical_safety_owner.md": _memo(items)}
    brief = [
        f"{name(OWNER_KEY)}, {role(OWNER_KEY)}, has agreed to be the clinical safety owner for the pilot, with conditions.",
        "The owners register in the handover has not been updated. Decide whether the stop condition can lift.",
    ]
    gold = {
        "change": "clinical safety owner named",
        "owner": name(OWNER_KEY),
        "owner_role": role(OWNER_KEY),
        "named_on": OWNER_NAMED.isoformat(),
        "handover_owner_register": "",
        "conditions": items,
        "all_conditions_met": all(item["met"] for item in items),
        "pilot_may_start": False,
        "invalidates": ["a statement that no clinical safety owner exists", "a go decision that ignores the conditions"],
    }
    add_drop(world, 6, "Clinical safety owner named", brief, files, gold)


def _memo(items: list[dict]) -> str:
    return memo(
        "Clinical safety ownership of the AI triage pilot", f"{name(OWNER_KEY)}, {role(OWNER_KEY)}",
        f"{name('cdo')}; {name('programme_manager')}; engagement team", OWNER_NAMED,
        [
            "I will act as clinical safety owner for the pilot. My acceptance is conditional, and the pilot stays stopped "
            "until I confirm in writing that every condition below is met.",
            *[f"{item['id']}. {item['text']}" for item in items],
            "Until then nothing in the register changes, and nobody should tell patients or the press that the pilot has an owner.",
        ],
    )
