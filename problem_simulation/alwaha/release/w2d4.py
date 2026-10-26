"""Write rel-w2d4. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import (
    candidate,
    dev_credential,
    gold,
    log_fixture,
    models,
    prod_credential,
    quota,
    root_spec,
)
from alwaha.engagement.w2d4_pages import (
    dashboard_note,
    deploy_note,
    endpoint_guide,
    endpoint_spec,
    health_spec,
    policy_note,
    registry_spec,
)
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w2d4"


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict) -> None:
    """Write one JSON value to the path.

    Keys are sorted and the text ends with a newline. The text writer creates parent directories.
    """
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the security office and points at the deployment standard, the credentials, and the quota.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w2d4

From: the Chief Information Security Officer
Case date: 2027-01-20

The deployment standard, the environment credentials, and the inference-endpoint quota are in this pack. The day notes are [Week 2, Day 4](../../Week%2002/Day%2004/README.md).

Files:

{listed}
"""


def write_w2d4(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the deployment notice, the policy, the endpoint guide, the dashboard starter, the interface documents, the registry, the credentials, the fixtures, and the gold.
    """
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "deploy.md", deploy_note())
    _write(pack / "standards" / "pol-deploy.md", policy_note())
    _write(pack / "endpoint" / "guide.md", endpoint_guide())
    _write(pack / "dashboard" / "starter.md", dashboard_note())
    _write(pack / "openapi" / "health.yaml", health_spec())
    _write(pack / "openapi" / "registry.yaml", registry_spec())
    _write(pack / "openapi" / "endpoint.yaml", endpoint_spec())
    _json(pack / "registry" / "models.json", models(profile))
    _json(pack / "registry" / "quota.json", quota(profile))
    _json(pack / "credentials" / "dev.json", dev_credential(profile))
    _json(pack / "credentials" / "prod.json", prod_credential(profile))
    _json(pack / "fixtures" / "candidate.json", candidate(profile))
    _json(pack / "fixtures" / "log.json", log_fixture(profile))
    _json(pack / "fixtures" / "root.json", root_spec())
    _write(truth / "w2d4_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w2d4_gold.json")
    _write(truth / "rel-w2d4-fingerprint.txt", digest + "\n")
    return digest
