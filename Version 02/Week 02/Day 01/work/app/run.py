"""Sign in the two fixture actors and write one status trace."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import flow
import session


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Sign in and answer the status scenario.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    loaded = flow.load_pack(Path(args.pack))
    db = session.connect(Path(args.db))
    opened = {}
    for name in ("patient", "coordinator"):
        result = flow.sign_in(db, loaded["actors"][name], loaded["note"])
        opened[name] = result["page"]
    answer = flow.status_answer(loaded["spec"], loaded["row"], loaded["row"]["message"])
    report = {"opened": opened, "sessions": session.rows(db), "chat": answer}
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
