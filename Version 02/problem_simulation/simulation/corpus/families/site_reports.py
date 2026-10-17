"""Monthly site operations reports. Numbers are the month's true counts; phrasing varies by seed."""

from __future__ import annotations

import random

import numpy as np

from simulation.corpus.add import Extra, add_composed
from simulation.corpus.families.common import month_label, percent, pick, site_month_stats
from simulation.prose import FactSpec
from simulation.prose.formats.render import pick_format
from simulation.prose.spec import facts
from simulation.world.clock import parse
from simulation.world.sites import CAPTURE_SITES, slug

FAMILY = "site-reports"


def build(world: dict, rng: np.random.Generator) -> None:
    stats = site_month_stats(world["events"])
    stats = stats[stats["site"].isin(CAPTURE_SITES) & (stats["captures"] >= 5)]
    for row in stats.itertuples(index=False):
        day = parse(f"{row.month}-01")
        spec = FactSpec(
            doc_id=f"site-report-{slug(row.site)}-{row.month}",
            family=FAMILY,
            title=f"Site operations report {row.site} {row.month}",
            facts=facts(
                site=row.site,
                month=month_label(day),
                captures=row.captures,
                ungradable=row.ungradable,
                ungradable_rate=percent(row.ungradable, row.captures),
                referable=row.referable,
                median_lag=int(row.median_lag) if row.median_lag == row.median_lag else 0,
            ),
            sections=("Activity", "Image quality", "Grading"),
            length_words=180,
        )
        extra = Extra(original=pick_format(spec.doc_id, (0.35, 0.35, 0.1, 0.2)))
        add_composed(world, spec, _draft, day, row.site, extra)
        world["gold"].setdefault("report_facts", []).append({"doc_id": spec.doc_id, **spec.values()})


def _draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    opening = pick(
        rng,
        f"{v['site']} photographed {v['captures']} people in {v['month']}.",
        f"In {v['month']} the clinic team at {v['site']} completed {v['captures']} captures.",
        f"Capture activity at {v['site']} for {v['month']} came to {v['captures']} encounters.",
    )
    quality = pick(
        rng,
        f"Of these, {v['ungradable']} photographs could not be graded, a rate of {v['ungradable_rate']} per cent.",
        f"Graders marked {v['ungradable']} sets ungradable ({v['ungradable_rate']} per cent of captures).",
        f"The ungradable rate was {v['ungradable_rate']} per cent, which is {v['ungradable']} sets.",
    )
    grading = pick(
        rng,
        f"Grading found {v['referable']} referable results. The median wait from photograph to grade was {v['median_lag']} days.",
        f"{v['referable']} results were graded referable, and the median grading wait was {v['median_lag']} days.",
    )
    closing = pick(
        rng,
        "Staff raised no new equipment faults this month.",
        "The clinic lead asks that recurring camera issues are logged with the service desk.",
        "Session lists ran as planned apart from routine leave.",
    )
    return "\n\n".join(["## Activity", opening, "## Image quality", quality, "## Grading", grading, closing])
