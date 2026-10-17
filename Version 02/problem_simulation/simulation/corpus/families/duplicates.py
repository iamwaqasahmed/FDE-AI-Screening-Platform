"""Near-duplicates: some reports were filed again as email attachments with light reformatting."""

from __future__ import annotations

import numpy as np

from simulation.corpus.add import Extra, add_document

EVERY = 25


def build(world: dict, rng: np.random.Generator) -> None:
    sources = sorted(doc_id for doc_id in world["rendered"] if doc_id.startswith(("site-report-", "district-report-")))
    gold = world["gold"].setdefault("near_duplicates", [])
    for doc_id in sources[::EVERY]:
        document = world["catalog"][doc_id]
        body = world["rendered"][doc_id].split("\n# ", 1)[-1].split("\n", 1)[-1]
        copy = "Forwarded copy for the record.\n\n" + body.replace("## ", "### ").replace(" per cent", "%")
        copy_id = f"{doc_id}-fwd"
        add_document(world, copy_id, "attachments", f"FW: {document.title}", copy, document.effective, document.site,
                     Extra(meta={"duplicate_of": doc_id}))
        gold.append({"doc_id": copy_id, "duplicate_of": doc_id})
