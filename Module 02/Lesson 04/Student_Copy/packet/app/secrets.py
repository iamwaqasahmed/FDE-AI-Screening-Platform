"""Use the dev credential for every environment.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

credential ignores the environment name and always opens the dev
file. While this shell is the file that runs, the deploy check
says prod uses the dev credential.
"""

from __future__ import annotations

import json
from pathlib import Path


def credential(env: str, pack: Path) -> str:
    """Return the endpoint field from the dev credential file.

    env is the environment name. It is not used. pack is the
    release folder. The file read is credentials/dev.json. The
    prod file is not opened.
    """
    del env
    payload = json.loads((pack / "credentials" / "dev.json").read_text(encoding="utf-8"))
    return payload["endpoint"]
