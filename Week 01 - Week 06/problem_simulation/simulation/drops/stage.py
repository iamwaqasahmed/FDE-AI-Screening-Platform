"""Write the drops for weeks 2 to 6 and their gold."""

from __future__ import annotations

import numpy as np

from simulation.drops import week2, week3, week4, week5, week6

WEEKLY = (week2, week3, week4, week5, week6)


def build(world: dict, rng: np.random.Generator) -> None:
    for module in WEEKLY:
        module.build(world, rng)
