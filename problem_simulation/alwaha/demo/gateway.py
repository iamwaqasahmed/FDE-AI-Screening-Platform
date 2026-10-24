"""Show a gateway refusal. The canary stays out of the printed lines."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show a gateway refusal for a watermarked prompt.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    prompt = f"Extract the letter. {profile.canary()}"
    if profile.canary() not in prompt:
        raise SystemExit(1)
    print("the gateway refused the prompt")


if __name__ == "__main__":
    main(sys.argv[1:])
