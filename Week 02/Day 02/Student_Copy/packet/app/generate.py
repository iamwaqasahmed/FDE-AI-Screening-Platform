"""Read the his-wadi spec and write client.py beside this file."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def fields(spec: str) -> list[str]:
    found = []
    for line in spec.splitlines():
        stripped = line.strip()
        if stripped.startswith("- name:"):
            found.append(stripped.split(":", 1)[1].strip())
    return found


def render(names: list[str]) -> str:
    field = names[0] if names else ""
    return (
        '"""Generated his-wadi client. Leave this file as the generator wrote it."""\n\n'
        f'FIELD = "{field}"\n\n'
        "def read_body(referral_id: str) -> dict:\n"
        '    return {"referral_id": referral_id, FIELD: ""}\n'
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write client.py from the his-wadi spec.")
    parser.add_argument("--spec", required=True)
    args = parser.parse_args(argv)
    spec = Path(args.spec).read_text(encoding="utf-8")
    destination = Path(__file__).with_name("client.py")
    destination.write_text(render(fields(spec)), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main(sys.argv[1:])
