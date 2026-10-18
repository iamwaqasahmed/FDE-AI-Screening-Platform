"""Week 2 enterprise-data gold, computed from the world so a check can be rerun on any seed.

`build` returns the JSON payload and the identity-record frame. Export writes
`truth/gold/enterprise.json` and `truth/gold/identity_records.parquet`.
"""

from __future__ import annotations

import pandas as pd

from simulation.eval.enterprise.cohorts import cohorts
from simulation.eval.enterprise.counts import counts
from simulation.eval.enterprise.drop import api_facts, drop_facts
from simulation.eval.enterprise.identity import identity_facts
from simulation.eval.enterprise.pathway import pathway_facts
from simulation.eval.enterprise.quality import quality_facts
from simulation.eval.enterprise.records import record_frame
from simulation.eval.enterprise.release import release_facts
from simulation.eval.enterprise.text import text_facts
from simulation.world.clock import SNAPSHOT, iso
from simulation.world.engagement import REGISTRY_SCHEMA_V3


def build(world: dict) -> tuple[dict, pd.DataFrame]:
    records = record_frame(world)
    drop = drop_facts(world)
    found = {
        "as_of": REGISTRY_SCHEMA_V3.isoformat(),
        "snapshot": iso(SNAPSHOT),
        "drop": drop,
        "api": api_facts(),
        "identity": identity_facts(world),
        "counts": counts(world),
        "pathway": pathway_facts(),
        "cohorts": cohorts(world),
        "release": release_facts(world),
        "quality": quality_facts(world),
    }
    found["read"] = _read(found)
    found["text"] = text_facts(found)
    return found, records


def _read(found: dict) -> dict:
    return {
        "feed_dedupe": {"key": "event_id", "order": "occurred_at"},
        "unlinked_keys": list(found["identity"]["unlinked_keys"]),
        "confidence": dict(found["identity"]["confidence"]),
        "stale_register": dict(found["pathway"]["stale_register"]),
        "rerun_contracts": list(found["release"]["rerun_contracts"]),
        "raci": dict(found["release"]["raci"]),
    }
