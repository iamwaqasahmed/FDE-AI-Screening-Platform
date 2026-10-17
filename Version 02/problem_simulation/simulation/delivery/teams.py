"""The two earlier delivery teams, their members, and their two-week sprints."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from simulation.world.staff import name


@dataclass(frozen=True)
class Team:
    name: str
    code: str
    start: date
    end: date
    members: tuple[str, ...]
    reporter: str


TEAMS = (
    Team("Kestrel", "KES", date(2024, 1, 8), date(2025, 3, 30),
         (name("analyst"), name("bi_developer"), name("integration_lead")), name("product_owner")),
    Team("Heron", "HER", date(2025, 4, 7), date(2026, 9, 27),
         (name("integration_lead"), name("analyst"), name("bi_developer"), name("service_desk_lead")), name("delivery_manager")),
)
BY_NAME = {team.name: team for team in TEAMS}
SPRINT_DAYS = 14


def sprints(team: Team) -> list[tuple[str, date, date]]:
    found = []
    start = team.start
    while start + timedelta(days=SPRINT_DAYS - 1) <= team.end:
        found.append((f"{team.code}-S{len(found) + 1:02d}", start, start + timedelta(days=SPRINT_DAYS - 1)))
        start += timedelta(days=SPRINT_DAYS)
    return found


def sprint_of(team: Team, day: date) -> str:
    for sprint_id, start, end in sprints(team):
        if start <= day <= end:
            return sprint_id
    return ""
