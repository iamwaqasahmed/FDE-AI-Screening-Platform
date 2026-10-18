"""The ordered list of surface checks."""

from __future__ import annotations

from simulation.check import (
    core_care,
    core_drop,
    core_identity,
    core_people,
    core_policy,
    core_warehouse,
    corpus,
    delivery,
    discovery,
    economics,
    enterprise,
    estate,
    evidence,
    ml,
    stakeholders,
)

SURFACE_CHECKS = (corpus, estate, economics, stakeholders, ml, delivery, discovery, enterprise, evidence)

CORE_CHECKS = [
    ("people", core_people.check),
    ("policy", core_policy.check),
    ("headers", core_policy.check_headers),
    ("lexical", core_policy.check_lexical),
    ("care", core_care.check),
    ("identity", core_identity.check),
    ("drop", core_drop.check),
    ("warehouse", core_warehouse.check),
]

CHECKS = CORE_CHECKS + [entry for module in SURFACE_CHECKS for entry in module.CHECKS]
