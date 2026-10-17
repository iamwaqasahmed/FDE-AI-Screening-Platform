"""Week 3: the DPO limits the vendor to primary-care captures and removes full date of birth from shared extracts."""

from __future__ import annotations

import numpy as np

from simulation.delivery.cohort import vendor_cohort
from simulation.drops.common import add_drop, memo
from simulation.drops.rules import BANNED_FIELD, PRIMARY_CARE_SITES, REPLACEMENT_FIELD
from simulation.world.engagement import DPO_RESTRICTION
from simulation.world.staff import name, role


def build(world: dict, rng: np.random.Generator) -> None:
    events = world["events"]
    before, after = vendor_cohort(events, False), vendor_cohort(events, True)
    removed = sorted(set(before["site"]) - set(PRIMARY_CARE_SITES))
    files = {"dpo_restriction_memo.md": _memo()}
    brief = [
        f"The Data Protection Officer has restricted the vendor pathway, effective {DPO_RESTRICTION.isoformat()}.",
        "Read the memo before you rerun the vendor evaluation, the cohort extract, or the architecture data flows.",
    ]
    gold = {
        "change": "DPO data minimisation restriction",
        "effective": DPO_RESTRICTION.isoformat(),
        "allowed_sites": list(PRIMARY_CARE_SITES),
        "removed_sites": removed,
        "banned_field": BANNED_FIELD,
        "replacement_field": REPLACEMENT_FIELD,
        "vendor_cohort_before": int(len(before)),
        "vendor_cohort_after": int(len(after)),
        "invalidates": ["vendor evaluation that includes outreach or hospital captures",
                        f"model features or extracts that use {BANNED_FIELD} outside the authority zone",
                        "identity matching performed in the vendor zone"],
        "still_allowed": [f"identity resolution with {BANNED_FIELD} inside the authority zone"],
    }
    add_drop(world, 3, "DPO restriction on the vendor pathway", brief, files, gold)


def _memo() -> str:
    sites = " and ".join(PRIMARY_CARE_SITES)
    return memo(
        "Restriction on the vendor pathway", f"{name('dpo')}, {role('dpo')}",
        f"{name('cdo')}; engagement team", DPO_RESTRICTION,
        [
            f"With immediate effect the vendor may only receive captures taken at primary-care sites: {sites}. "
            "Outreach and hospital captures are outside the lawful basis recorded in the impact assessment and must not leave the authority.",
            f"Data minimisation: the field {BANNED_FIELD} (full date of birth) must not appear in any extract that leaves the authority zone, "
            f"in any analytics workspace shared with suppliers, or in any model feature table. Use {REPLACEMENT_FIELD} instead.",
            f"Identity resolution may still use {BANNED_FIELD} inside the authority zone. Its output must carry a cluster key, not the date.",
            "Work already started under the old assumption must be rerun. Tell me which outputs changed.",
        ],
    )
