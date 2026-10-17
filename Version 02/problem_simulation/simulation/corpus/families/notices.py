"""Incident and change notices, one per timeline entry. Their dates and refs match the service desk."""

from __future__ import annotations

import random

import numpy as np

from simulation.corpus.add import Extra, add_composed
from simulation.corpus.families.common import pick
from simulation.prose import FactSpec
from simulation.prose.spec import facts
from simulation.world.clock import iso
from simulation.world.timeline import TIMELINE

FAMILY = "notices"


def build(world: dict, rng: np.random.Generator) -> None:
    for item in TIMELINE:
        pairs = dict(ref=item.ref, title=item.title, start=iso(item.start), cause=item.cause, effect=item.effect)
        if item.end:
            pairs["end"] = iso(item.end)
        if item.site:
            pairs["site"] = item.site
        spec = FactSpec(
            doc_id=f"notice-{item.ref.lower()}",
            family=FAMILY,
            title=f"{item.kind.capitalize()} notice {item.ref}",
            facts=facts(**pairs),
            sections=("What happened", "Cause", "Effect"),
            length_words=150,
        )
        add_composed(world, spec, _draft, item.start, item.site, Extra(original="pdf"))


def _draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    window = f"from {v['start']} to {v['end']}" if "end" in v else f"from {v['start']}"
    where = f" at {v['site']}" if "site" in v else ""
    lines = [
        "## What happened",
        pick(rng, f"{v['ref']}: {v['title']}{where}, {window}.", f"Reference {v['ref']} records \"{v['title']}\"{where} {window}."),
        "## Cause",
        pick(rng, f"The recorded cause is: {v['cause']}.", f"Cause as logged: {v['cause']}."),
        "## Effect",
        pick(rng, f"Expected effect on services and data: {v['effect']}.", f"Effect noted by the service owner: {v['effect']}."),
        "Questions about this notice go to the service desk quoting the reference.",
    ]
    return "\n\n".join(lines)
