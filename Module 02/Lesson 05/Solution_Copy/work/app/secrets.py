"""Select the credential file for the environment.

credential opens prod.json when the environment is prod, and
dev.json otherwise. The endpoint field is the credential. The
value is read from the file. It is not written in this module.
"""

from __future__ import annotations

import json
from pathlib import Path


def credential(env: str, pack: Path) -> str:
    """Return the endpoint field from the file for this environment.

    env selects the file. prod reads credentials/prod.json. Any
    other name reads credentials/dev.json. pack is the release
    folder. The endpoint field is the credential the caller gets.
    """
    name = "prod.json" if env == "prod" else "dev.json"
    payload = json.loads((pack / "credentials" / name).read_text(encoding="utf-8"))
    return payload["endpoint"]
