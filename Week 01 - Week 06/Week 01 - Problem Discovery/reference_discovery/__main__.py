"""Write a reference Week 1 folder from one built drop.

    python -m reference_discovery --data <build> --out <dir> [--profile <name>]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path

from reference_discovery.assemble import findings
from reference_discovery.brief import write as write_brief
from reference_discovery.notes import SCRIPTS
from reference_discovery.notes import write as write_notes


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write the reference Week 1 discovery folder.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--profile", default="")
    args = parser.parse_args(argv)
    if args.profile:
        os.environ["HARTLAND_PROFILE"] = args.profile
    root, out = Path(args.data), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    built = findings(root)
    (out / "findings.json").write_text(json.dumps(built, indent=2) + "\n", encoding="utf-8")
    interviews = out / "interviews"
    interviews.mkdir(exist_ok=True)
    for script in sorted(SCRIPTS.glob("*.txt")):
        shutil.copyfile(script, interviews / script.name)
    write_notes(out / "notes")
    write_brief(out / "brief.md", built, root)
    print(f"Wrote the reference folder to {out}")


if __name__ == "__main__":
    main()
