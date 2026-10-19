"""Week 4: a letter bureau incident duplicates and loses dispatches inside the engagement's bureau window."""

from __future__ import annotations

import numpy as np

from simulation.drops.bureau import bureau_gold, bureau_run
from simulation.drops.common import add_drop
from simulation.world.engagement import BUREAU_INCIDENT
from simulation.world.staff import name


def build(world: dict, rng: np.random.Generator) -> None:
    requests, dispatch = bureau_run(world)
    start, end = (day.isoformat() for day in BUREAU_INCIDENT)
    world["files"]["truth/drops/week-4/requests.csv"] = requests
    files = {
        f"letters/requests_{start}_to_{end}.csv": requests.drop(columns=["person_uid"]),
        f"letters/dispatch_{start}_to_{end}.csv": dispatch,
        "letters/bureau_notice.md": _notice(start, end),
    }
    brief = [
        f"{name('bureau_manager')} at the letter bureau reports a queue failure between {start} and {end}.",
        "The authority's request file and the bureau's dispatch file are both here. They do not agree.",
        "The programme asked for a chase letter for every local id whose latest referral message has no seen date.",
        "Work out who has not been reached.",
    ]
    gold = {"change": "letter bureau incident", **bureau_gold(world, requests, dispatch),
            "invalidates": ["any count of letters sent taken from dispatch rows", "the overdue cohort's contact status",
                            "the bureau notice's statement that no letters were lost",
                            "a chase list read as the overdue cohort"]}
    add_drop(world, 4, "Letter bureau incident", brief, files, gold)


def _notice(start: str, end: str) -> str:
    return "\n".join([
        "# Bureau service notice", "",
        f"From: {name('bureau_manager')}, PostRight Services", "",
        f"Between {start} and {end} a queue failure triggered automatic retries on some days.",
        "Some dispatches may have been printed more than once. We believe no letters were lost.",
        "The dispatch file is complete for the period.", "",
    ])
