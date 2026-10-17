"""Build findings.json from the drop."""

from __future__ import annotations

from pathlib import Path

from reference_discovery import landscape, narrative, profiling, sizing
from reference_discovery.io import Drop
from reference_discovery.quotes import Quotes


def findings(root: Path) -> dict:
    drop = Drop(root)
    quotes = Quotes(drop)
    items: dict = {}
    items.update(landscape.items(drop))
    items.update(profiling.items(drop))
    items.update(sizing.items(drop, quotes))
    items.update(narrative.items(drop))
    return {"items": items}
