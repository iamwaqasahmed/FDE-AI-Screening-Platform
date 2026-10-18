"""Week 6 gold: the handoff the authority can run and govern.

`build` returns the JSON payload. Export writes `truth/gold/handoff.json`.
"""

from __future__ import annotations

import numpy as np

from simulation.eval.handoff import (
    conditions,
    drop,
    estate,
    flows,
    governance,
    hazards,
    prototype,
    records,
    security,
    text_adr,
    text_pages,
    truth,
)
from simulation.world.clock import iso
from simulation.world.engagement import OWNER_NAMED


def build(world: dict) -> dict:
    items = {}
    items.update(drop.facts(world))
    items.update(conditions.facts(world))
    items.update(estate.facts(world))
    items.update(flows.rules(world))
    items.update(security.summary(world))
    items.update(prototype.facts())
    items.update(governance.facts(world))
    items["adr_index"] = text_adr.index()
    payload = {
        "as_of": iso(OWNER_NAMED),
        "friday": items["drop_owner"]["friday"],
        "items": items,
        "files": {"flows": flows.rows(world), "threats": security.rows(world), "hazards": hazards.spec(items)},
        "records": records.specs(items),
        "text": {**text_adr.facts(items), **text_pages.facts(items)},
        "truth": truth.facts(world, items),
    }
    return _plain(payload)


def _plain(value):
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return round(float(value), 4)
    if isinstance(value, np.bool_):
        return bool(value)
    return value
