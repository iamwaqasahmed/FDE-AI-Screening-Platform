"""The week-3 restriction, read back out of the memo the drop writes."""

from __future__ import annotations

import re

from simulation.drops.week3 import _memo
from simulation.eval.evidence.bars import BANNED_IN, WEEK2_ITEMS


def facts(world: dict, sites: list[str]) -> dict:
    return {"drop_restriction": restriction(_memo(), sites), "outputs_changed": _outputs(world)}


def restriction(text: str, vendor_sites) -> dict:
    effective = re.search(r"Date:\s*(\d{4}-\d{2}-\d{2})", text).group(1)
    raw = re.search(r"primary-care sites:\s*(.+?)\.", text).group(1)
    allowed = sorted(part.strip() for part in raw.split(" and ") if part.strip())
    removed = sorted(set(map(str, vendor_sites)) - set(allowed))
    return {
        "effective": effective,
        "allowed_sites": allowed,
        "removed_sites": removed,
        "banned_field": "DOB",
        "replacement_field": "YEAR_OF_BIRTH",
        "banned_in": sorted(BANNED_IN),
    }


def _outputs(world: dict) -> dict:
    frame = world["files"]["engagement/workstreams/contracts.csv"]
    changed = sorted(frame.loc[frame["changed_by_drop"].astype(str).eq("week-3"), "contract_id"].astype(str))
    return {"contracts": changed, "week2_items": list(WEEK2_ITEMS), "clusters_unchanged": True}
