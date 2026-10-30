"""Write rel-m01-l04.
Earlier packs are left where they are.

The writer stops if a template tree is missing, then clears the pack and writes the scenarios, the approval and safety pages, the tool catalog, and the agent tree. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from alwaha.agent.gold import payload
from alwaha.agent.pages import approval_page, catalog_page, safety_page
from alwaha.agent.scenarios import SCENARIO_ORDER, scenarios
from alwaha.config.profile import Profile
from alwaha.paths import AGENT_ROOT, M01_L04_TEMPLATES
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m01-l04"
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
    return f"""# rel-m01-l04

From: the medical director
Case date: 2027-01-13

The approval rules, the scenario slice, and the tool catalog are in this pack. The lesson notes are [Module 1 Lesson 4](<../../Module 01/Lesson 04/Student_Copy/home.md>).

Files:

{listed}
"""


def write_m01_l04(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and the agent gold.

    It writes the scenario files, their order, the approval and safety pages, the tool catalog, the agent tree, and the templates. A missing template stops the release before anything is replaced.
    """
    # Stop before replacing anything when a template tree is missing.
    if not AGENT_ROOT.is_dir() or not M01_L04_TEMPLATES.is_dir():
        raise SystemExit("Lesson 4 template is missing.")
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Group the scenarios into their datasets.
    grouped: dict[str, list[dict]] = {name: [] for name in _DATASETS}
    for row in scenarios(profile.canary()):
        grouped[row["dataset"]].append(row)
    # Write each dataset, the order, the policy pages, and the tool catalog.
    for name in _DATASETS:
        lines = [json.dumps(row, sort_keys=True) for row in grouped[name]]
        _write(pack / "scenarios" / f"{name}.jsonl", "\n".join(lines) + "\n")
    _write(pack / "scenarios" / "order.json", json.dumps(list(SCENARIO_ORDER), indent=2) + "\n")
    _write(pack / "policy" / "pol-approval.md", approval_page())
    _write(pack / "policy" / "pol-clinical-safety.md", safety_page())
    _write(pack / "tools" / "mcp-cluster.json", catalog_page())
    # Agent tree, templates, and gold.
    _copy_tree(AGENT_ROOT, pack / "agent")
    _copy_tree(M01_L04_TEMPLATES, pack / "templates")
    _write(truth / "agent_gold.json", json.dumps(payload(profile.canary()), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "agent_gold.json")
    _write(truth / "rel-m01-l04-fingerprint.txt", digest + "\n")
    return digest
