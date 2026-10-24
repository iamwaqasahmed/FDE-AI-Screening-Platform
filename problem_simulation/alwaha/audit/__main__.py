"""Readiness record. python -m alwaha.audit."""

from __future__ import annotations

import argparse
import os
import sys

from alwaha.audit.score import score
from alwaha.audit.slices import evaluate
from alwaha.audit.truth import build_truth
from alwaha.audit.twice import matches
from alwaha.config.profile import load
from alwaha.traffic.run import run as run_traffic

BAR = 0.98


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Record world fingerprints, slices, and the reference score.")
    parser.add_argument("--profile", default="small")
    parser.add_argument("--score", action="store_true")
    parser.add_argument("--assessment-seed", default="424242")
    args = parser.parse_args(argv)
    profile = load(args.profile)
    same, first, _second = matches(profile)
    print(f"Fingerprint match for {profile.name}: {same}")
    print(first)
    if not same:
        raise SystemExit(1)
    if profile.name != "assessment":
        other_same, other_hash, _other_second = matches(_assessment(args.assessment_seed))
        print(f"Fingerprint match for assessment: {other_same}")
        print(other_hash)
        if not other_same:
            raise SystemExit(1)
    _slices(profile)
    _slices(_assessment(args.assessment_seed))
    traffic = run_traffic()
    print(f"Traffic: {'passed' if traffic['ok'] else 'failed'}")
    if args.score:
        _score(args.profile)
    if not traffic["ok"]:
        raise SystemExit(1)


def _slices(profile) -> None:
    rows = evaluate(profile)
    failed = [row["slice"] for row in rows if not row["simpler_fails"] or not row["passing_ok"]]
    print(f"Slices for {profile.name}: {len(rows) - len(failed)}/{len(rows)}")
    if failed:
        raise SystemExit(f"Slice gap: {', '.join(failed)}")


def _assessment(seed: str):
    previous = os.environ.get("ALWAHA_ASSESSMENT_SEED")
    os.environ["ALWAHA_ASSESSMENT_SEED"] = seed
    try:
        return load("assessment")
    finally:
        if previous is None:
            os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        else:
            os.environ["ALWAHA_ASSESSMENT_SEED"] = previous


def _score(profile_name: str) -> None:
    build_truth(load(profile_name))
    result = score(profile_name)
    print(f"Reference score: {result['passed']}/{result['total']} ({result['rate']:.3f})")
    for row in result["rows"]:
        if not row["ok"]:
            print(f"FAIL {row['check']} {row['release']}")
            print(row["detail"])
    if result["rate"] < BAR:
        raise SystemExit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
