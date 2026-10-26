"""Write rel-w1d4. Earlier packs are left where they are."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from alwaha.agent.gold import payload
from alwaha.agent.pages import approval_page, catalog_page, safety_page
from alwaha.agent.scenarios import SCENARIO_ORDER, scenarios
from alwaha.config.profile import Profile
from alwaha.paths import AGENT_ROOT, DAY4_TEMPLATES
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w1d4"
_DATASETS = ("ds-agent", "ds-sessions", "ds-reason")


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _copy_tree(source: Path, destination: Path) -> None:
    """Copy a source tree onto the destination.

    Caches are skipped. A missing source stops the release so a half-built pack is not left behind.
    """
    if not source.is_dir():
        raise SystemExit(f"Missing {source}.")
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        dirs_exist_ok=True,
    )


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the medical director and points at the approval rules, the scenarios, and the tool catalog.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w1d4

From: the medical director
Case date: 2027-01-13

The approval rules, the scenario slice, and the tool catalog are in this pack. The day notes are [Week 1, Day 4](../../Week%2001/Day%2004/README.md).

Files:

{listed}
"""


def write_day4(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and the agent gold.

    It writes the scenario files, their order, the approval and safety pages, the tool catalog, the agent tree, and the templates. A missing template stops the release before anything is replaced.
    """
    if not AGENT_ROOT.is_dir() or not DAY4_TEMPLATES.is_dir():
        raise SystemExit("Day 4 template is missing.")
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict]] = {name: [] for name in _DATASETS}
    for row in scenarios(profile.canary()):
        grouped[row["dataset"]].append(row)
    for name in _DATASETS:
        lines = [json.dumps(row, sort_keys=True) for row in grouped[name]]
        _write(pack / "scenarios" / f"{name}.jsonl", "\n".join(lines) + "\n")
    _write(pack / "scenarios" / "order.json", json.dumps(list(SCENARIO_ORDER), indent=2) + "\n")
    _write(pack / "policy" / "pol-approval.md", approval_page())
    _write(pack / "policy" / "pol-clinical-safety.md", safety_page())
    _write(pack / "tools" / "mcp-cluster.json", catalog_page())
    _copy_tree(AGENT_ROOT, pack / "agent")
    _copy_tree(DAY4_TEMPLATES, pack / "templates")
    _write(truth / "agent_gold.json", json.dumps(payload(profile.canary()), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "agent_gold.json")
    _write(truth / "rel-w1d4-fingerprint.txt", digest + "\n")
    return digest
