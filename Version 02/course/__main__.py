"""Run a Version 02 module tool.

    python -m course discovery_check --work <folder> [--data data] [--rerun]
    python -m course reference_discovery --data <build> --out <dir> --profile <name>
    python -m course discovery_check.key --data <build>
    python -m course enterprise_check --work <folder> [--data data] [--rerun]
    python -m course reference_enterprise --data <build> --out <dir> --profile <name>
    python -m course enterprise_check.key --data <build>
"""

from __future__ import annotations

import os
import runpy
import sys

USAGE = "Usage: python -m course <discovery_check|enterprise_check|reference_discovery|reference_enterprise> ..."


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(USAGE)
    profile = _profile(sys.argv[2:])
    if profile:
        os.environ["HARTLAND_PROFILE"] = profile
    from course import install

    install()
    module = sys.argv[1]
    sys.argv = [module, *sys.argv[2:]]
    runpy.run_module(module, run_name="__main__")


def _profile(argv: list[str]) -> str:
    if "--profile" in argv:
        return argv[argv.index("--profile") + 1]
    return ""


if __name__ == "__main__":
    main()
