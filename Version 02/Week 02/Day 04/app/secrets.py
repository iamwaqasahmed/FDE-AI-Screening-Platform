"""Use the dev credential for every environment."""

from __future__ import annotations

import json
from pathlib import Path


def credential(env: str, pack: Path) -> str:
    del env
    payload = json.loads((pack / "credentials" / "dev.json").read_text(encoding="utf-8"))
    return payload["endpoint"]
