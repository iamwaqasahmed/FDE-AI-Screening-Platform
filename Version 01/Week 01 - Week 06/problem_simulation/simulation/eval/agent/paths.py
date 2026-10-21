"""Earliest, latest, and assumed pilot paths. The memo states the durations; this applies them."""

from __future__ import annotations

from datetime import date, timedelta

from simulation.delivery.plan import (
    CDO_ASSUMED_ROUTE,
    GATE_2,
    MOBILISE_WEEKS,
    PILOT_CONTRACT_VALUE,
    SPEC_WEEKS,
    TEST_WEEKS,
    first_window,
    freeze,
    next_monday,
    required_route,
    route_named,
)


def earliest(build_done: date) -> dict:
    route = required_route(PILOT_CONTRACT_VALUE)
    return trace(build_done, route.route, route.lead_weeks_min)


def latest(build_done: date) -> dict:
    route = required_route(PILOT_CONTRACT_VALUE)
    return trace(build_done, route.route, route.lead_weeks_max)


def assumed(build_done: date) -> dict:
    route = route_named(CDO_ASSUMED_ROUTE)
    return trace(build_done, route.route, route.lead_weeks_min)


def trace(build_done: date, route_name: str, lead_weeks: int) -> dict:
    award = GATE_2 + timedelta(weeks=lead_weeks)
    spec_ready = award + timedelta(weeks=SPEC_WEEKS)
    freeze_end = freeze("FRZ-0301").end
    after_freeze = freeze_end + timedelta(days=1)
    window = first_window("registry", max(spec_ready, after_freeze, build_done))
    tested = window + timedelta(weeks=TEST_WEEKS)
    mobilised = award + timedelta(weeks=MOBILISE_WEEKS)
    go_live = next_monday(max(tested, mobilised))
    return {
        "route": route_name,
        "lead_weeks": lead_weeks,
        "gate_2": GATE_2.isoformat(),
        "contract_award": award.isoformat(),
        "spec_ready": spec_ready.isoformat(),
        "registry_freeze_end": freeze_end.isoformat(),
        "build_done": build_done.isoformat(),
        "registry_window": window.isoformat(),
        "tested": tested.isoformat(),
        "mobilised": mobilised.isoformat(),
        "go_live": go_live.isoformat(),
        "binding": _binding(spec_ready, after_freeze, build_done),
    }


def _binding(spec_ready: date, after_freeze: date, build_done: date) -> str:
    latest_input = max(spec_ready, after_freeze, build_done)
    if latest_input == spec_ready:
        return "procurement"
    return "freeze" if latest_input == after_freeze else "build"
