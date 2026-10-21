"""Rules the drops introduce that other packages also apply: the DPO restriction and the CDO's scope change."""

from __future__ import annotations

from simulation.world.sites import HARBOUR, HILL_SITES

PRIMARY_CARE_SITES = tuple(sorted(HILL_SITES))
BANNED_FIELD = "DOB"
REPLACEMENT_FIELD = "YEAR_OF_BIRTH"
RENAMED_FIELDS = {"HOME_CLINIC": "REGISTERED_SITE"}
NEW_FIELDS = ("DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION")
SECOND_SITE = HARBOUR
REISSUED = 40
