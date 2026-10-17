"""Board-pack originals. The PDF carries a per-site table the Markdown export leaves out."""

from __future__ import annotations

import numpy as np

from simulation.corpus.families.common import site_month_stats
from simulation.prose.formats.render import render

HEADER = ["Site", "Captures", "Grader backlog breaches", "Letter breaches", "Booking breaches"]


def build(world: dict, rng: np.random.Generator) -> None:
    stats = site_month_stats(world["events"])
    gold = world["gold"].setdefault("table_only_facts", [])
    for doc_id, text in sorted(world["rendered"].items()):
        if not doc_id.startswith("board-"):
            continue
        month = doc_id.removeprefix("board-")
        rows = stats[stats["month"] == month].sort_values("site")
        if rows.empty:
            continue
        table = [HEADER] + [
            [row.site, str(row.captures), str(row.backlog), str(row.letters), str(row.booking)] for row in rows.itertuples()
        ]
        body = text.split("\n# ", 1)[-1].split("\n", 1)[-1]
        original = f"boards/originals/{doc_id}.pdf"
        world["files"][f"corpus/{original}"] = render("pdf", doc_id, f"Monthly board pack {month}", body, table)
        world.setdefault("corpus_meta", {})[doc_id] = {"doc_id": doc_id, "family": "boards", "original": original}
        for row in rows.itertuples():
            gold.append({"doc_id": doc_id, "site": row.site, "month": month, "grader_backlog": int(row.backlog),
                         "letter_bureau": int(row.letters), "booking": int(row.booking)})
