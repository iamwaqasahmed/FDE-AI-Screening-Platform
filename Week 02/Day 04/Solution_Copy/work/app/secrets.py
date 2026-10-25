"""Select the credential file for the environment.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

credential opens prod.json when the environment is prod, and
dev.json otherwise. The endpoint field is the credential. The
value is read from the file. It is not written in this module.
While the shell is the file that runs, the deploy check says
prod uses the dev credential.
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
