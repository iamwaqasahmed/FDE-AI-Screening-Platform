"""Select the credential file for the environment."""

from __future__ import annotations

import json
from pathlib import Path


def credential(env: str, pack: Path) -> str:
    name = "prod.json" if env == "prod" else "dev.json"
    payload = json.loads((pack / "credentials" / name).read_text(encoding="utf-8"))
    return payload["endpoint"]
