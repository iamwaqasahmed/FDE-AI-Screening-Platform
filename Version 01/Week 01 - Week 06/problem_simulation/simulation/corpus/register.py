"""The records office catalog. A handful of statuses are stale."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.policy.types import Document
from simulation.systems.catalog import STALE_REGISTER
from simulation.world.clock import iso


def write_register(catalog: dict[str, Document], paths: dict[str, str], dest: Path, meta: dict | None = None) -> None:
    rows = []
    meta = meta or {}
    for document_id, document in sorted(catalog.items()):
        status = "draft" if document_id in STALE_REGISTER else document.status
        info = meta.get(document_id, {})
        rows.append(
            {
                "document_id": document_id,
                "family": info.get("family", paths[document_id].split("/")[0]),
                "original": info.get("original", ""),
                "title": document.title,
                "status": status,
                "effective": iso(document.effective),
                "sunset": iso(document.sunset) if document.sunset else "",
                "site": document.site,
                "programme": document.programme,
                "path": paths[document_id],
            }
        )
    pd.DataFrame(rows).to_csv(dest, index=False)
