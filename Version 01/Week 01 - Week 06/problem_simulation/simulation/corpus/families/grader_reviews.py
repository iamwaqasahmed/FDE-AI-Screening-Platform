"""Quarterly grader reviews: reads, throughput, and second-read agreement per grader."""

from __future__ import annotations

import random

import numpy as np
import pandas as pd

from simulation.corpus.add import Extra, add_composed
from simulation.corpus.families.common import percent, pick, quarter_of, quarters
from simulation.prose import FactSpec
from simulation.prose.formats.render import pick_format
from simulation.prose.spec import facts
from simulation.workforce.graders import ROSTER
from simulation.world.staff import name

FAMILY = "grader-reviews"
MIN_READS = 20


def build(world: dict, rng: np.random.Generator) -> None:
    stats = _stats(world)
    for year, quarter, day in quarters():
        for grader in ROSTER:
            key = (grader.grader_id, f"{year}q{quarter}")
            if grader.agency or key not in stats.index or stats.at[key, "reads"] < MIN_READS:
                continue
            row = stats.loc[key]
            pairs = dict(grader=grader.name, reviewer=name("lead_grader"), reads=int(row["reads"]),
                         hours=f"{row['hours']:.0f}", per_hour=f"{row['reads'] / max(row['hours'], 1):.1f}")
            if row["checked"]:
                pairs.update(checked=int(row["checked"]), agreement=percent(int(row["agreed"]), int(row["checked"])))
            spec = FactSpec(
                doc_id=f"grader-review-{grader.grader_id.lower()}-{year}q{quarter}",
                family=FAMILY,
                title=f"Grader review {grader.grader_id} {year} Q{quarter}",
                facts=facts(**pairs),
                sections=("Workload", "Quality"),
                length_words=150,
            )
            add_composed(world, spec, _draft, day, extra=Extra(original=pick_format(spec.doc_id, (0.2, 0.6, 0.1, 0.1))))


def _stats(world: dict) -> pd.DataFrame:
    events = world["events"]
    graded = events[(events["grader_id"] != "") & (events["graded_at"] != "")].copy()
    graded["quarter"] = quarter_of(graded["graded_at"])
    graded["checked"] = graded["second_grade"] != ""
    graded["agreed"] = graded["checked"] & (graded["second_grade"] == graded["grade"])
    stats = graded.groupby(["grader_id", "quarter"]).agg(reads=("event_id", "size"), checked=("checked", "sum"),
                                                         agreed=("agreed", "sum"))
    hours = world["grader_hours"].copy()
    hours["quarter"] = quarter_of(hours["day"].astype(str))
    melted = hours.melt(id_vars=["day", "quarter"], var_name="grader_id", value_name="hours")
    stats["hours"] = melted.groupby(["grader_id", "quarter"])["hours"].sum().reindex(stats.index).fillna(0.0)
    return stats


def _draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    agreement = (f"{v['checked']} of these were read again, with agreement of {v['agreement']} per cent."
                 if "checked" in v else "No second reads were sampled this quarter.")
    return "\n\n".join([
        "## Workload",
        pick(rng, f"{v['grader']} graded {v['reads']} sets in {v['hours']} rostered hours, about {v['per_hour']} per hour.",
             f"In the quarter, {v['grader']} completed {v['reads']} reads over {v['hours']} hours ({v['per_hour']} an hour)."),
        "## Quality",
        agreement,
        pick(rng, "No further action this quarter.", "The grader and reviewer agreed to keep the current session pattern.",
             "Feedback was given on borderline background cases."),
        f"Reviewed by {v['reviewer']}.",
    ])
