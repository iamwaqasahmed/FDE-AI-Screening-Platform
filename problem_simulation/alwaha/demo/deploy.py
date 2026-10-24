"""Show a root image rejected. Do not name the hash or the national id."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.serve.deploy import admit


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Reject a root image.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    root = admit("root", "started", "")
    clean = admit("1000", "started", "")
    print("root image: rejected" if root == "rejected" else "root image: accepted")
    print("registered image: accepted" if clean == "accepted" else "registered image: rejected")


if __name__ == "__main__":
    main(sys.argv[1:])
