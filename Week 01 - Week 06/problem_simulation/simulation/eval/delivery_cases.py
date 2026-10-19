"""Delivery, drops, and integration questions. Expected values come from the delivery and drops gold."""

from __future__ import annotations

from simulation.delivery import cases_plan, cases_registers
from simulation.drops import cases as drop_cases

MODULES = (cases_plan, cases_registers, drop_cases)


def cases(world: dict) -> list[dict]:
    found: list[dict] = []
    for module in MODULES:
        found.extend(module.cases(world))
    return found
