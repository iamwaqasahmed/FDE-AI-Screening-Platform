"""Run a Week 1 check against a participant work directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from alwaha.check.approach import approach_problems
from alwaha.check.brief import brief_problems
from alwaha.check.events import events_problems
from alwaha.check.interviews import interview_problems, load_truth
from alwaha.check.repo import repo_problems
from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.samples.measure import measure_pack


def _day3(work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d3")
    gold_path = truth_dir(profile.name) / "events_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d3 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-w1-events", events_problems(work, pack, gold, profile.canary())


def _day2(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d2")
    gold_path = truth_dir(profile.name) / "approach_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d2 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    measured = measure_pack(pack)
    if which == "approach":
        return "chk-w1-approach", approach_problems(work, pack, gold, measured, profile.canary())
    return "chk-w1-brief", brief_problems(work, pack, gold, measured, profile.canary())


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Check a Week 1 work directory.")
    parser.add_argument("which", choices=("repo", "interview", "approach", "brief", "events"))
    parser.add_argument("--work", required=True)
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    work = Path(args.work)
    if args.which in {"approach", "brief"}:
        name, problems = _day2(args.which, work, profile)
    elif args.which == "events":
        name, problems = _day3(work, profile)
    else:
        truth = truth_dir(profile.name) / "personas.json"
        if not truth.is_file():
            raise SystemExit(f"No truth for {profile.name}. Build rel-w1d1 first.")
        personas, canary = load_truth(truth)
        if args.which == "repo":
            problems = repo_problems(work, canary)
            name = "chk-w1-repo"
        else:
            problems = interview_problems(work, personas)
            name = "chk-w1-interview"
    if problems:
        print(f"{name} failed.")
        for item in problems:
            print(f"- {item}")
        raise SystemExit(1)
    print(f"{name} passed.")


if __name__ == "__main__":
    main(sys.argv[1:])
