"""Developer helpers: a cached core world for iterating on one surface stage without a full build.

    HARTLAND_PROFILE=small python -c "from simulation.devkit import try_stage; try_stage('simulation.delivery.stage')"
"""

from __future__ import annotations

import importlib
import pickle
import tempfile
from pathlib import Path

import numpy as np

from simulation.config import active

CACHE = Path(__file__).resolve().parents[1] / ".cache"


def core_world(refresh: bool = False) -> dict:
    from simulation.build import build_core

    path = CACHE / f"core-{active().name}.pkl"
    if path.exists() and not refresh:
        return pickle.loads(path.read_bytes())
    world = build_core()
    CACHE.mkdir(exist_ok=True)
    path.write_bytes(pickle.dumps(world))
    return world


def with_stages(*modules: str) -> dict:
    """Core world plus the named stages, in order. Each gets a fixed generator."""
    world = core_world()
    for index, module in enumerate(modules):
        importlib.import_module(module).build(world, np.random.default_rng(1000 + index))
    return world


def try_stage(module: str, *before: str, write: bool = True) -> dict:
    """Run earlier stages, then this one, and write its files to a temporary folder for inspection."""
    world = with_stages(*before, module)
    if write:
        from simulation.files import write_all

        out = Path(tempfile.mkdtemp(prefix="hartland-"))
        count = write_all(out, world["files"])
        print(f"Wrote {count} files to {out}")
    return world
