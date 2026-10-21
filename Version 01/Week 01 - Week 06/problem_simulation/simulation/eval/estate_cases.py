"""Estate eval cases: enterprise data, free-text solution work, and architecture, all computed from the built world."""

from __future__ import annotations

from simulation.architecture.eval_cases import architecture_cases
from simulation.estate.eval_data import data_cases
from simulation.estate.eval_solution import solution_cases


def cases(world: dict) -> list[dict]:
    return data_cases(world) + solution_cases(world) + architecture_cases(world)
