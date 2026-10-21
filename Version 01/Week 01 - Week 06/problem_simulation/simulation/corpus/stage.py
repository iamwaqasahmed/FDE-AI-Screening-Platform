"""The written corpus: policy calculus plus every generated document family."""

from __future__ import annotations

import numpy as np

from simulation.corpus.families import FAMILIES
from simulation.corpus.operational import build_operational
from simulation.policy.apply import DOCUMENTS
from simulation.policy.render import render_control


def build(world: dict, rng: np.random.Generator) -> None:
    rendered = render_control()
    catalog = dict(DOCUMENTS)
    extra_text, extra_docs = build_operational(world["events"])
    rendered.update(extra_text)
    catalog.update(extra_docs)
    world["rendered"] = rendered
    world["catalog"] = catalog
    world.setdefault("paths", {})
    for family in FAMILIES:
        family.build(world, rng)
