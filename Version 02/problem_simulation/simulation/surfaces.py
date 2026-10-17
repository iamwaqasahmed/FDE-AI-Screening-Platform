"""Surface stages run after the core world. Each stage gets its own seeded generator, so adding one never shifts another."""

from __future__ import annotations

import numpy as np

from simulation.stages import STAGES


def build_surfaces(world: dict, rng: np.random.Generator) -> None:
    base = int(rng.integers(0, 2**31 - 1))
    for index, (name, builder) in enumerate(STAGES):
        print(f"Building {name}...")
        builder(world, np.random.default_rng(base + 7919 * (index + 1)))
