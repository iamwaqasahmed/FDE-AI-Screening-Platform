"""Procurement rules and thresholds. The numbers come from the delivery plan, so the standard and the routes file agree."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.corpus.add import Extra, add_document
from simulation.delivery.plan import ROUTES

FAMILY = "standards"
LABELS = {"direct_award": "Direct award", "framework_call_off": "Framework call-off", "open_tender": "Open tender"}


def build(world: dict, rng: np.random.Generator) -> None:
    lines = ["## Purpose", "How the authority buys goods and services. The total contract value over its whole term "
             "decides the route, not the first year's cost.", "## Routes"]
    for route in ROUTES:
        ceiling = f"up to {route.max_value:,}" if route.max_value else "and above"
        lines.append(f"- {LABELS[route.route]}: from {route.min_value:,} {ceiling}. Typical lead time "
                     f"{route.lead_weeks_min} to {route.lead_weeks_max} weeks. {route.note}")
    lines += ["## Rules",
              "Splitting one requirement into smaller contracts to stay under a threshold is not allowed.",
              "No procurement starts before the funding gate that approves it.",
              "Suppliers handling official-sensitive data must pass supplier assurance before award."]
    table = [["Route", "Minimum", "Maximum", "Lead weeks"]] + [
        [LABELS[route.route], str(route.min_value), str(route.max_value or ""), f"{route.lead_weeks_min}-{route.lead_weeks_max}"]
        for route in ROUTES
    ]
    add_document(world, "procurement-thresholds", FAMILY, "Procurement rules and thresholds", "\n\n".join(lines),
                 date(2024, 4, 1), extra=Extra(original="pdf", table=table))
