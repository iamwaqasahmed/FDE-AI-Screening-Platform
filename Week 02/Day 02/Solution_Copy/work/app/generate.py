"""Read the his-wadi spec and write client.py beside this file.

Running this file against a spec replaces client.py in the same
folder and leaves this file unchanged. Do not edit the text this
file writes. The checks compare that text with the spec.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def fields(spec: str) -> list[str]:
    """Collect every `- name:` value in the spec, in file order.

    his.py uses this same list. A body key that is not in the list
    fails the read. A missing name from the list fails it too.
    referral_id is a path piece, not one of these names.
    """
    found = []
    for line in spec.splitlines():
        stripped = line.strip()
        if stripped.startswith("- name:"):
            found.append(stripped.split(":", 1)[1].strip())
    return found


def render(names: list[str]) -> str:
    """Return the client source the spec asks for.

    The first name in the spec becomes FIELD. Leave this string as it
    is. The work copy of client.py has to match it character for
    character, including the blank lines.
    """
    field = names[0] if names else ""
    return (
        '"""Generated his-wadi client. Leave this file as the generator wrote it."""\n\n'
        f'FIELD = "{field}"\n\n'
        "def read_body(referral_id: str) -> dict:\n"
        '    return {"referral_id": referral_id, FIELD: ""}\n'
    )


def main(argv: list[str] | None = None) -> None:
    """Read --spec and overwrite client.py in this same folder.

    --spec is the path to the his-wadi spec. The write lands beside
    this script.
    """
    parser = argparse.ArgumentParser(description="Write client.py from the his-wadi spec.")
    parser.add_argument("--spec", required=True)
    args = parser.parse_args(argv)
    spec = Path(args.spec).read_text(encoding="utf-8")
    destination = Path(__file__).with_name("client.py")
    destination.write_text(render(fields(spec)), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main(sys.argv[1:])
