"""Build the world in memory. Writing files is a separate step."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.cycles import build_events
from simulation.disease.hba1c import build_hba1c
from simulation.disease.progression import build_disease
from simulation.people.identity import build_identifiers
from simulation.people.population import build_population
from simulation.surfaces import build_surfaces
from simulation.world.clock import SEED


def build_world(seed: int = SEED) -> dict:
    world = build_core(seed)
    build_surfaces(world, np.random.default_rng(seed + 1))
    return world


def build_core(seed: int = SEED) -> dict:
    """People, hidden layers, care events, and identifiers. Surfaces are built on top of this."""
    rng = np.random.default_rng(seed)
    print("Building people...")
    people = build_population(rng)
    print("Building hidden layers...")
    hidden = _hidden(people, rng)
    print("Building care events...")
    events, invitations, hours = build_events(people, hidden, rng)
    print("Building identifiers...")
    identifiers = build_identifiers(people, events, rng)
    return {
        "seed": seed,
        "people": people,
        "events": events,
        "identifiers": identifiers,
        "invitations": invitations,
        "hidden": hidden,
        "grader_hours": hours,
        "files": {},
        "tables": {},
        "gold": {},
    }


def _hidden(people: pd.DataFrame, rng: np.random.Generator) -> dict:
    base = people[people["alias_of"] == ""].reset_index(drop=True)
    hba1c = build_hba1c(base, rng)
    disease = build_disease(base, hba1c, rng)
    return {
        "hba1c": hba1c,
        "disease": disease,
        "person_row": pd.Series(np.arange(len(base)), index=base["person_uid"].to_numpy()),
    }
