"""Dispatch the four Module 2 Lesson 5 checks. Packs stay where the builders left them.

Command entry for the four end-of-module checks. The deploy command needs both this release and the previous smoke release. The other commands need this release's gold, and some of them also need one of the packs. Packs are only read from where the builders left them. A missing directory or gold file exits before any grader runs.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.deploy_m02 import deploy_problems
from alwaha.check.individual_w2 import individual_problems
from alwaha.check.notes_m02_l05 import written_problems
from alwaha.check.queue_w2 import queue_problems
from alwaha.check.readout_m02 import readout_problems
from alwaha.paths import pack_dir, truth_dir


def _packs(profile) -> tuple[Path, Path, dict]:
    """Return the smoke directory, this release's directory, and this release's gold.

    The previous gold file is required to exist here, but it is not parsed in this function. The deploy command reads it again. If any of the four paths is missing, the process exits with the build sentence.
    """
    smoke = pack_dir(profile.name, "rel-m02-l04")
    pack = pack_dir(profile.name, "rel-m02-l05")
    smoke_gold = truth_dir(profile.name) / "m02_l04_gold.json"
    gold_path = truth_dir(profile.name) / "m02_l05_gold.json"
    # Any missing half of either release stops the check. The packs are not rebuilt here.
    if not smoke.is_dir() or not pack.is_dir() or not smoke_gold.is_file() or not gold_path.is_file():
        raise SystemExit("Build rel-m02-l04 and rel-m02-l05 first.")
    return smoke, pack, json.loads(gold_path.read_text(encoding="utf-8"))


def deploy(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the deploy misses.

    The smoke pack and the smoke gold are what the deploy grader executes against. The note callback below replaces the default note grader so the written notes are scored against this release, not against the smoke release.
    """
    smoke, pack, gold = _packs(profile)
    smoke_gold = json.loads((truth_dir(profile.name) / "m02_l04_gold.json").read_text(encoding="utf-8"))

    def notes(folder: Path, _pack: Path, _gold: dict) -> list[str]:
        """Return the written-note misses for the later release.

        The deploy grader calls this with the participant folder and with the smoke pack and smoke gold. Those two arguments are ignored on purpose. The pack and gold closed over from the outer function are the later release, which is what the notes describe.
        """
        # The folder is the participant work. The pack and gold used here are the later release captured above, not the smoke release passed in by the deploy grader.
        return written_problems(folder, pack, gold)

    return "chk-deploy", deploy_problems(work, smoke, smoke_gold, profile.canary(), notes)


def journey(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the booking misses.

    The smoke pack and this release's pack are loaded so a missing release still exits, then ignored. The booking grader reads gold and the profile token.
    """
    # Both packs are loaded so a missing release exits. The booking grader needs gold only.
    _smoke, _pack, gold = _packs(profile)
    return "chk-journey", queue_problems(work, gold, profile.canary())


def readout(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the readout misses.

    Both pack directories are passed so a citation can name a file from either release. Gold supplies the section rules.
    """
    smoke, pack, gold = _packs(profile)
    return "chk-readout", readout_problems(work, gold, profile.canary(), [smoke, pack])


def individual(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the contract misses.

    This release's pack holds the fixtures. Gold is loaded and ignored because the contract grader reads the fixtures itself.
    """
    # Gold is loaded so a missing release exits. The contract grader reads fixtures from this release's pack.
    _smoke, pack, _gold = _packs(profile)
    return "chk-individual-m02", individual_problems(work, pack, profile.canary())
