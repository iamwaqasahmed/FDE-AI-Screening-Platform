"""Names the verifier knows. Prose may mention one only when the spec does."""

from __future__ import annotations

from functools import lru_cache

from simulation.workforce.graders import ROSTER
from simulation.world.sites import ALL_SITES
from simulation.world.staff import STAFF, VENDORS


@lru_cache(maxsize=1)
def known_entities() -> tuple[str, ...]:
    names = {person.name for person in STAFF}
    names.update(grader.name for grader in ROSTER if not grader.agency)
    names.update(ALL_SITES)
    names.update(VENDORS.values())
    return tuple(sorted(names, key=len, reverse=True))
