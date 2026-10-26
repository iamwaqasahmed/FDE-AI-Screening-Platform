"""Show a root image rejected. Do not name the hash or the national id.

Admission is asked once for the root user and once for the registered user. Both calls pass an empty identifier and the same log line. The page prints a fixed word for each result so the user id and the log line stay off the page.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.serve.deploy import admit


def main(argv: list[str] | None = None) -> None:
    """Print the root result and the registered-user result. Returns nothing.

    argv replaces the process arguments. The profile is loaded before either admission call.
    """
    parser = argparse.ArgumentParser(description="Reject a root image.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    root = admit("root", "started", "")
    clean = admit("1000", "started", "")
    # Fixed words keep the user id and the log line off the page.
    print("root image: rejected" if root == "rejected" else "root image: accepted")
    print("registered image: accepted" if clean == "accepted" else "registered image: rejected")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
