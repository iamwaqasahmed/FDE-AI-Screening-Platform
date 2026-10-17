"""Cold start: one question, one log line, one result line."""

from __future__ import annotations

import argparse
from pathlib import Path

from screening_service.service import serve

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOG = REPO_ROOT / "runtime" / "access.log"
DEFAULT_RESULTS = REPO_ROOT / "runtime" / "results.jsonl"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one Hartland screening ask.")
    parser.add_argument("--who", required=True, help="Who asked.")
    parser.add_argument("--question", required=True, help="The question.")
    parser.add_argument("--log", default=str(DEFAULT_LOG))
    parser.add_argument("--results", default=str(DEFAULT_RESULTS))
    args = parser.parse_args()
    reply = serve(args.who, args.question, Path(args.log), Path(args.results))
    print(reply["answer"])


if __name__ == "__main__":
    main()
