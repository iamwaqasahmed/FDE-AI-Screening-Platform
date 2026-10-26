"""Show a gateway refusal. The canary stays out of the printed lines.

The prompt is built so it contains the profile canary. The only printed line is the refusal. If the canary is missing from the prompt, the command exits before that line.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load


def main(argv: list[str] | None = None) -> None:
    """Print the refusal line. Returns nothing.

    argv replaces the process arguments. The profile supplies the canary that is placed in the prompt and kept off the printed line.
    """
    parser = argparse.ArgumentParser(description="Show a gateway refusal for a watermarked prompt.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    prompt = f"Extract the letter. {profile.canary()}"
    # Exit when the watermark is missing, so the printed refusal belongs to a prompt that contains it.
    if profile.canary() not in prompt:
        raise SystemExit(1)
    print("the gateway refused the prompt")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
