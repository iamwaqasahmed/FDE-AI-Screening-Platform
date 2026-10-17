"""Planning facts shared by the roadmap, funding gates, procurement routes, freeze calendar, and the pilot date."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from simulation.world import engagement
from simulation.world.timeline import TIMELINE, Happening


@dataclass(frozen=True)
class Route:
    route: str
    min_value: int
    max_value: int | None
    lead_weeks_min: int
    lead_weeks_max: int
    note: str


ROUTES = (
    Route("direct_award", 0, 29_999, 2, 4, "Below threshold. One quote and a recorded waiver."),
    Route("framework_call_off", 30_000, 499_999, 8, 12, "Mini-competition on the national health AI framework lot."),
    Route("open_tender", 500_000, None, 26, 39, "Full open procedure, about six to nine months."),
)
PILOT_CONTRACT_VALUE = 186_000
CDO_ASSUMED_ROUTE = "direct_award"
GATE_2 = date(2026, 11, 26)
SPEC_WEEKS = 2
TEST_WEEKS = 3
MOBILISE_WEEKS = 4
RELEASE_SYSTEMS = {"registry": 1, "letters": 2, "vendor": 3, "booking": 3, "warehouse": 4}
CALENDAR = (date(2026, 1, 1), date(2028, 1, 1))


def freeze(ref: str) -> Happening:
    return next(item for item in TIMELINE if item.ref == ref)


def required_route(value: int) -> Route:
    return next(route for route in ROUTES if value >= route.min_value and (route.max_value is None or value <= route.max_value))


def route_named(name: str) -> Route:
    return next(route for route in ROUTES if route.route == name)


def frozen(system: str, day: date) -> str:
    for item in TIMELINE:
        if item.kind == "freeze" and item.system == system and item.start <= day <= (item.end or item.start):
            return item.ref
    return ""


def release_windows(system: str) -> list[date]:
    """First weekday of the month for that system (Tuesday registry, Wednesday letters ...), skipping frozen days."""
    weekday = RELEASE_SYSTEMS[system]
    windows = []
    year, month = CALENDAR[0].year, CALENDAR[0].month
    while date(year, month, 1) < CALENDAR[1]:
        first = date(year, month, 1)
        day = first + timedelta(days=(weekday - first.weekday()) % 7)
        if not frozen(system, day):
            windows.append(day)
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return windows


def first_window(system: str, not_before: date) -> date:
    return next(day for day in release_windows(system) if day >= not_before)


def next_monday(day: date) -> date:
    return day + timedelta(days=(7 - day.weekday()) % 7)


def pilot_path(build_done: date, route_name: str = "") -> dict:
    """Earliest pilot go-live: gate, procurement, interface spec, registry window after the freeze, test, mobilisation."""
    route = route_named(route_name) if route_name else required_route(PILOT_CONTRACT_VALUE)
    award = GATE_2 + timedelta(weeks=route.lead_weeks_min)
    spec_ready = award + timedelta(weeks=SPEC_WEEKS)
    registry_freeze = freeze("FRZ-0301")
    after_freeze = registry_freeze.end + timedelta(days=1)
    not_before = max(spec_ready, after_freeze, build_done)
    window = first_window("registry", not_before)
    tested = window + timedelta(weeks=TEST_WEEKS)
    mobilised = award + timedelta(weeks=MOBILISE_WEEKS)
    go_live = next_monday(max(tested, mobilised))
    return {
        "route": route.route,
        "gate_2": GATE_2.isoformat(),
        "contract_award": award.isoformat(),
        "spec_ready": spec_ready.isoformat(),
        "registry_freeze_end": registry_freeze.end.isoformat(),
        "build_done": build_done.isoformat(),
        "registry_window": window.isoformat(),
        "tested": tested.isoformat(),
        "mobilised": mobilised.isoformat(),
        "earliest_pilot": go_live.isoformat(),
        "binding": _binding(spec_ready, after_freeze, build_done),
    }


def _binding(spec_ready: date, after_freeze: date, build_done: date) -> str:
    latest = max(spec_ready, after_freeze, build_done)
    if latest == spec_ready:
        return "procurement"
    return "freeze" if latest == after_freeze else "build"


def pilot_gold(build_done: date, velocity: float, remaining_points: int) -> dict:
    path = pilot_path(build_done)
    assumed = pilot_path(build_done, CDO_ASSUMED_ROUTE)
    requested = engagement.PILOT_DATE_REQUESTED
    return {
        "requested": requested.isoformat(),
        "original": engagement.PILOT_DATE_ORIGINAL.isoformat(),
        "feasible": date.fromisoformat(path["earliest_pilot"]) <= requested,
        "earliest_pilot": path["earliest_pilot"],
        "original_feasible": date.fromisoformat(path["earliest_pilot"]) <= engagement.PILOT_DATE_ORIGINAL,
        "contract_value": PILOT_CONTRACT_VALUE,
        "required_route": path["route"],
        "cdo_assumed_route": CDO_ASSUMED_ROUTE,
        "earliest_if_assumed_route": assumed["earliest_pilot"],
        "velocity_points_per_sprint": velocity,
        "remaining_points": remaining_points,
        "critical_path": path,
        "facts": _facts(path),
    }


def _facts(path: dict) -> list[str]:
    route = route_named(path["route"])
    return [
        f"The pilot contract is estimated at {PILOT_CONTRACT_VALUE}, above the direct award ceiling of {route_named('direct_award').max_value}.",
        f"A {route.route.replace('_', ' ')} takes at least {route.lead_weeks_min} weeks and cannot start before Gate 2 on {path['gate_2']}.",
        f"The earliest contract award is {path['contract_award']}; the interface spec is ready on {path['spec_ready']}.",
        f"FRZ-0301 freezes registry interface changes until {path['registry_freeze_end']}.",
        f"The first registry release window after both is {path['registry_window']}; testing ends {path['tested']}.",
        f"The earliest go-live is {path['earliest_pilot']}, after the requested {engagement.PILOT_DATE_REQUESTED.isoformat()}.",
    ]
