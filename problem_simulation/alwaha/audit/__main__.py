"""Readiness record. python -m alwaha.audit.

The command compares a world built twice, then does the same for the assessment profile unless the selected profile already is assessment. It evaluates the slices for both profiles, runs the traffic check, and optionally scores the filled work copies. A fingerprint mismatch, a slice gap, a failed traffic run, or a score under the bar stops the process.
"""

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
    """Print fingerprint, slice, and traffic results, and exit if any of those checks fail."""
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
        # The world is not stable, so later scores would not be meaningful.
        raise SystemExit(1)
    if profile.name != "assessment":
        # This profile is not assessment, so that separate world is fingerprinted too.
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
        # The score may already have printed. Traffic still fails the run on its own.
        raise SystemExit(1)


def _slices(profile) -> None:
    """Print the slice tally and stop if any simpler method passes or any named method fails."""
    rows = evaluate(profile)
    failed = [row["slice"] for row in rows if not row["simpler_fails"] or not row["passing_ok"]]
    print(f"Slices for {profile.name}: {len(rows) - len(failed)}/{len(rows)}")
    if failed:
        raise SystemExit(f"Slice gap: {', '.join(failed)}")


def _assessment(seed: str):
    """Load the assessment profile with this seed, then restore the previous environment."""
    previous = os.environ.get("ALWAHA_ASSESSMENT_SEED")
    os.environ["ALWAHA_ASSESSMENT_SEED"] = seed
    try:
        return load("assessment")
    finally:
        if previous is None:
            # The variable was unset. Put the process back to unset, not to an empty string.
            os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        else:
            os.environ["ALWAHA_ASSESSMENT_SEED"] = previous


def _score(profile_name: str) -> None:
    """Build truth, print the reference score, and stop when the rate is under the bar."""
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
