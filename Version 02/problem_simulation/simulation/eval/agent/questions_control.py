"""Single-hop notice questions. A lookup still answers these."""

from __future__ import annotations

from simulation.eval.agent.question import adopt
from simulation.eval.graph.questions_control import cases as control_cases

KEEP = 4


def cases(world: dict) -> list[dict]:
    return [adopt(row, max_steps=4) for row in control_cases(world)[:KEEP]]
