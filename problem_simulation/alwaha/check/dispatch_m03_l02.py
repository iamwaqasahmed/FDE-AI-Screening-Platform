"""Dispatch the Module 3, Lesson 2 checks.

Command entry for the model check and the adapter slice. Both commands load the same release and gold file. A missing release exits before either grader runs.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.lora_m03_l02 import lora_problems
from alwaha.check.model_m03_l02 import model_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-m03-l02")
    gold_path = truth_dir(profile.name) / "m03_l02_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m03-l02 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def model(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the model misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-m03-l02-model", model_problems(work, pack, gold, profile.canary())


def lora(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the adapter-slice misses.

    The pack, the gold, and the profile token are passed through. The slice shares scoring helpers with the model check.
    """
    pack, gold = _loaded(profile)
    return "slice-lora", lora_problems(work, pack, gold, profile.canary())
