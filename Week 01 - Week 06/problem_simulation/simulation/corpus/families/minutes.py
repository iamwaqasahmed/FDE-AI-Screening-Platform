"""Monthly programme board minutes, plus the 2021 pilot post-mortem that leaves out what the minutes say."""

from __future__ import annotations

import random

import numpy as np

from simulation.corpus.add import Extra, add_composed
from simulation.corpus.families import pilot_2021
from simulation.corpus.families.common import month_label, months, pick, site_month_stats
from simulation.prose import FactSpec
from simulation.prose.spec import facts
from simulation.world.staff import name
from simulation.world.timeline import TIMELINE

FAMILY = "minutes"
CORE = ("programme_manager", "ophthalmology_lead", "lead_grader", "finance_head")
OCCASIONAL = ("cdo", "dpo", "outreach_coordinator", "records_manager", "enterprise_architect")


def build(world: dict, rng: np.random.Generator) -> None:
    stats = site_month_stats(world["events"]).groupby("month")[["backlog", "letters", "captures"]].sum()
    for day in months():
        month = f"{day:%Y-%m}"
        if month not in stats.index:
            continue
        guests = [key for index, key in enumerate(OCCASIONAL) if (day.month + index) % 4 == 0]
        attendees = ", ".join(name(key) for key in (*CORE, *guests))
        pairs = dict(month=month_label(day), attendees=attendees, chair=name("programme_manager"),
                     captures=int(stats.at[month, "captures"]), backlog=int(stats.at[month, "backlog"]),
                     letters=int(stats.at[month, "letters"]))
        for index, item in enumerate(item for item in TIMELINE if f"{item.start:%Y-%m}" == month):
            pairs[f"item{index}"] = f"{item.ref} {item.title}"
        pilot = pilot_2021.minute_line(month)
        if pilot:
            pairs["pilot"] = pilot[1]
        spec = FactSpec(f"board-minutes-{month}", FAMILY, f"Programme board minutes {month}", facts(**pairs),
                        sections=("Attendance", "Performance", "Items", "Actions"), length_words=220)
        add_composed(world, spec, _draft, day, extra=Extra(original="docx" if day.month % 3 else "scan"))
    _postmortem(world)


def _draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    items = [value for key, value in v.items() if key.startswith("item")]
    lines = ["## Attendance", f"Present: {v['attendees']}. Chair: {v['chair']}.", "## Performance",
             pick(rng, f"The board noted {v['captures']} captures for {v['month']}.",
                  f"Activity for {v['month']} was {v['captures']} captures."),
             pick(rng, f"Grader backlog breaches stood at {v['backlog']} and letter breaches at {v['letters']}.",
                  f"Breaches recorded: grader backlog {v['backlog']}, letter bureau {v['letters']}.")]
    lines.append("## Items")
    lines.extend(f"- {item}: noted, owner to report back." for item in items)
    if "pilot" in v:
        lines.append(f"- {v['pilot']}")
    if not items and "pilot" not in v:
        lines.append(pick(rng, "- No new incidents or changes.", "- Routine business only."))
    lines += ["## Actions", pick(rng, "Actions carried forward to the next meeting.", "The chair will circulate actions.")]
    return "\n\n".join(lines)


def _postmortem(world: dict) -> None:
    gold = pilot_2021.gold()
    spec = FactSpec(gold["postmortem_doc"], "postmortems", "Post-mortem: 2021 triage pilot",
                    facts(vendor=gold["vendor"], site=gold["site"], start=gold["start"], stopped=gold["stopped"],
                          finding=pilot_2021.POSTMORTEM_FINDING), sections=("Summary", "Finding"), length_words=200)
    add_composed(world, spec, _postmortem_draft, pilot_2021.POSTMORTEM, extra=Extra(original="pdf"))
    world["gold"]["pilot_2021"] = gold


def _postmortem_draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    return "\n\n".join([
        "## Summary",
        f"A triage model from {v['vendor']} ran at {v['site']} from {v['start']} until it was stopped on {v['stopped']}.",
        "## Finding",
        v["finding"],
        "The review team thanks clinic staff for their time.",
    ])
