"""python -m simulation.prose {status,author,prune} [--profile NAME] [--family F] [--limit N]"""

import argparse
import os

parser = argparse.ArgumentParser(prog="python -m simulation.prose")
parser.add_argument("command", choices=["status", "author", "prune"])
parser.add_argument("--profile", default=os.environ.get("HARTLAND_PROFILE", "practice"))
parser.add_argument("--family", default="")
parser.add_argument("--limit", type=int, default=0)
args = parser.parse_args()
os.environ["HARTLAND_PROFILE"] = args.profile

from simulation.prose.cli import run  # noqa: E402  the profile must be set before the world modules import

run(args.command, args.family, args.limit)
