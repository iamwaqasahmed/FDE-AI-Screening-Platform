"""Sign in the two fixture actors and write one status trace.

Chapter 07 runs this file after generate.py. It writes trace.json.
The checks do not read that file. They sign in and ask the status
question again themselves. The trace is how you see the session rows
and the reply.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import flow
import session


def main(argv: list[str] | None = None) -> None:
    """Sign in the patient and the coordinator, then write one JSON report.

    --pack is the release folder. --db is the application database.
    --out is the trace. The report has three keys. opened maps each
    actor to chat or console. sessions is the table. chat is the
    status reply. A book call is not in that reply.
    """
    # Read the pack, the database path, and where the trace should be written.
    parser = argparse.ArgumentParser(description="Sign in and answer the status scenario.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    # Load the four release files and open the session database.
    loaded = flow.load_pack(Path(args.pack))
    db = session.connect(Path(args.db))
    # Sign in the patient and the coordinator, and record which page each one opened.
    opened = {}
    for name in ("patient", "coordinator"):
        result = flow.sign_in(db, loaded["actors"][name], loaded["note"])
        opened[name] = result["page"]
    # Ask the status question. The report is the pages, the session rows, and that reply.
    answer = flow.status_answer(loaded["spec"], loaded["row"], loaded["row"]["message"])
    report = {"opened": opened, "sessions": session.rows(db), "chat": answer}
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
