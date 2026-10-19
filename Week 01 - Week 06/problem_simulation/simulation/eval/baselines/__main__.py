"""python -m simulation.eval.baselines [--profile small]: score the baselines against a built profile."""

from __future__ import annotations

import argparse
import os


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", default=os.environ.get("HARTLAND_PROFILE", "practice"))
    args = parser.parse_args()
    os.environ["HARTLAND_PROFILE"] = args.profile
    from simulation.eval.baselines.run import run_all
    from simulation.paths import DATA

    summary = run_all(DATA)
    for name, slices in summary.items():
        roles = ", ".join(f"{role} {value['pass_rate']:.2f}" for role, value in slices["role"].items())
        print(f"{name}: overall {slices['overall']['all']['pass_rate']:.2f} | {roles}")


if __name__ == "__main__":
    main()
