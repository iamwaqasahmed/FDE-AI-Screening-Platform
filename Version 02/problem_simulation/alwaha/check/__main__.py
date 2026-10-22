"""Run a Day 1 check against a participant work directory."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from alwaha.check.interviews import interview_problems, load_truth
from alwaha.check.repo import repo_problems
from alwaha.paths import truth_dir
from alwaha.config.profile import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Check a Day 1 work directory.")
    parser.add_argument("which", choices=("repo", "interview"))
    parser.add_argument("--work", required=True)
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    truth = truth_dir(profile.name) / "personas.json"
    if not truth.is_file():
        raise SystemExit(f"No truth for {profile.name}. Build rel-w1d1 first.")
    personas, canary = load_truth(truth)
    work = Path(args.work)
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
