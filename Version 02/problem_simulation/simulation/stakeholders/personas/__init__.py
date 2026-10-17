"""One module per persona. The order follows `simulation.world.staff.PERSONAS`."""

from __future__ import annotations

import importlib

from simulation.stakeholders.model import Persona
from simulation.world.staff import PERSONAS


def build_personas(world: dict) -> dict[str, Persona]:
    built = {}
    for person in PERSONAS:
        module = importlib.import_module(f"simulation.stakeholders.personas.{person.key}")
        built[person.key] = module.build(world)
    return built
