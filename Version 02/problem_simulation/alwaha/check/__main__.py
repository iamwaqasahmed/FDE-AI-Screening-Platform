"""Run a check against a participant work directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from alwaha.check.agent import agent_problems
from alwaha.check.approach import approach_problems
from alwaha.check.auth import auth_problems
from alwaha.check.brief import brief_problems
from alwaha.check.design import design_problems
from alwaha.check.events import events_problems
from alwaha.check.individual import individual_problems
from alwaha.check.interviews import interview_problems, load_truth
from alwaha.check.journey import journey_problems
from alwaha.check.readout import readout_problems
from alwaha.check.repo import repo_problems
from alwaha.check.trajectory import trajectory_problems
from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.samples.measure import measure_pack


def _day4(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d4")
    gold_path = truth_dir(profile.name) / "agent_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d4 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "agent":
        return "chk-w1-agent", agent_problems(work, pack, gold, profile.canary())
    return "chk-w1-trajectory", trajectory_problems(work, pack, gold, profile.canary())


def _day5_gold(profile) -> tuple[Path, Path, dict]:
    pack = pack_dir(profile.name, "rel-w1d4")
    failures = pack_dir(profile.name, "rel-w1d5")
    root = truth_dir(profile.name)
    agent_path = root / "agent_gold.json"
    day5_path = root / "day5_gold.json"
    if not pack.is_dir() or not failures.is_dir() or not agent_path.is_file() or not day5_path.is_file():
        raise SystemExit("Build rel-w1d4 and rel-w1d5 first.")
    agent_gold = json.loads(agent_path.read_text(encoding="utf-8"))
    day5_gold = json.loads(day5_path.read_text(encoding="utf-8"))
    merged = {"scenarios": agent_gold["scenarios"] + day5_gold["scenarios"]}
    return pack, failures, merged


def _day5_score(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack, failures, merged = _day5_gold(profile)
    if which == "agent":
        problems = agent_problems(work, pack, merged, profile.canary(), failures, written=False)
        return "chk-w1-agent", problems
    problems = trajectory_problems(work, pack, merged, profile.canary(), failures, written=False)
    return "chk-w1-trajectory", problems


def _day5_written(which: str, work: Path, profile) -> tuple[str, list[str]]:
    failures = pack_dir(profile.name, "rel-w1d5")
    gold_path = truth_dir(profile.name) / "day5_gold.json"
    if not failures.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d5 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    packs = [pack_dir(profile.name, release) for release in ("rel-w1d1", "rel-w1d2", "rel-w1d3", "rel-w1d4", "rel-w1d5")]
    if which == "design":
        return "chk-w1-design", design_problems(work, gold, profile.canary(), packs)
    if which == "readout":
        return "chk-readout", readout_problems(work, gold, profile.canary())
    return "chk-individual-w1", individual_problems(work, gold, profile.canary())


def _day3(work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d3")
    gold_path = truth_dir(profile.name) / "events_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d3 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-w1-events", events_problems(work, pack, gold, profile.canary())


def _w2d1(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w2d1")
    gold_path = truth_dir(profile.name) / "w2d1_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w2d1 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "auth":
        return "chk-w2-auth", auth_problems(work, pack, gold, profile.canary())
    return "chk-w2-journey", journey_problems(work, pack, gold, profile.canary())


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
    parser = argparse.ArgumentParser(description="Check a work directory.")
    parser.add_argument(
        "which",
        choices=(
            "repo",
            "interview",
            "approach",
            "brief",
            "events",
            "agent",
            "trajectory",
            "design",
            "readout",
            "individual",
            "auth",
            "journey",
        ),
    )
    parser.add_argument("--work", required=True)
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default="")
    args = parser.parse_args(argv)
    profile = load(args.profile)
    work = Path(args.work)
    if args.which in {"auth", "journey"}:
        if args.release != "rel-w2d1":
            raise SystemExit("auth and journey need --release rel-w2d1.")
        name, problems = _w2d1(args.which, work, profile)
    elif args.which in {"approach", "brief"}:
        name, problems = _day2(args.which, work, profile)
    elif args.which == "events":
        name, problems = _day3(work, profile)
    elif args.which in {"agent", "trajectory"} and args.release == "rel-w1d5":
        name, problems = _day5_score(args.which, work, profile)
    elif args.which in {"agent", "trajectory"}:
        name, problems = _day4(args.which, work, profile)
    elif args.which in {"design", "readout", "individual"}:
        name, problems = _day5_written(args.which, work, profile)
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
