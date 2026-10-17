"""python -m simulation [--profile NAME] [--no-repeat], from the Version 02 directory."""

import argparse
import os

parser = argparse.ArgumentParser(prog="python -m simulation", description="Rebuild a Hartland world from one profile.")
parser.add_argument("--profile", default=os.environ.get("HARTLAND_PROFILE", "practice"))
parser.add_argument("--no-repeat", action="store_true", help="Skip the same-seed rebuild check.")
args = parser.parse_args()
os.environ["HARTLAND_PROFILE"] = args.profile

from simulation.run import main  # noqa: E402  the profile must be set before the world modules import

main(repeat=not args.no_repeat)
