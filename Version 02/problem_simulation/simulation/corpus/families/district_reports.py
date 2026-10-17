"""Quarterly outreach reports by district: invitations, attendance, and contact channels."""

from __future__ import annotations

import random

import numpy as np

from simulation.corpus.add import Extra, add_composed
from simulation.corpus.families.common import percent, pick, quarter_of, quarters
from simulation.prose import FactSpec
from simulation.prose.formats.render import pick_format
from simulation.prose.spec import facts
from simulation.world.sites import DISTRICTS, slug
from simulation.world.staff import name

FAMILY = "district-reports"


def build(world: dict, rng: np.random.Generator) -> None:
    invitations = world["invitations"]
    invited = invitations[invitations["invited"]].copy()
    invited["quarter"] = quarter_of(invited["planned_date"].astype(str))
    grouped = invited.groupby(["district", "quarter"]).agg(
        invited=("attended", "size"), attended=("attended", "sum"), sms=("sms", "sum"), reminder=("reminder", "sum")
    )
    for year, quarter, day in quarters():
        for district in DISTRICTS:
            key = (district, f"{year}q{quarter}")
            if key not in grouped.index:
                continue
            row = grouped.loc[key]
            spec = FactSpec(
                doc_id=f"district-report-{slug(district)}-{year}q{quarter}",
                family=FAMILY,
                title=f"Outreach report {district} {year} Q{quarter}",
                facts=facts(author=name("outreach_coordinator"), invited=int(row["invited"]),
                            attended=int(row["attended"]), rate=percent(int(row["attended"]), int(row["invited"])),
                            sms=int(row["sms"]), reminder=int(row["reminder"])),
                sections=("Invitations", "Contact"),
                length_words=160,
            )
            add_composed(world, spec, _draft, day, extra=Extra(original=pick_format(spec.doc_id)))


def _draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    return "\n\n".join(
        [
            "## Invitations",
            pick(rng, f"We sent {v['invited']} invitations and {v['attended']} people attended ({v['rate']} per cent).",
                 f"Attendance was {v['rate']} per cent: {v['attended']} of {v['invited']} invited people came."),
            "## Contact",
            pick(rng, f"{v['sms']} invitations went with an SMS, and {v['reminder']} people received a reminder message.",
                 f"SMS reached {v['sms']} invitees; reminders went to {v['reminder']}."),
            pick(rng, "Attendance tends to dip in winter and recover in spring.",
                 "Staff continue to phone people who missed two appointments.",
                 "Van days were kept where roads allowed."),
            f"Prepared by {v['author']}.",
        ]
    )
