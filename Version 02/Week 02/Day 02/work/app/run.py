"""Run the webhook intake and the cancellation deliveries."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import cancel
import intake
import mart
import session


def _events(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run wf-session-cancelled on the release pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    pack = Path(args.pack)
    registry_text = (pack / "registry" / "topics.md").read_text(encoding="utf-8")
    body = json.loads((pack / "webhooks" / "referral.submitted.json").read_text(encoding="utf-8"))
    faults = json.loads((pack / "channels" / "sms-faults.json").read_text(encoding="utf-8"))
    accepted = intake.accept(body, registry_text)
    db = session.connect(Path(args.db))
    rows = [cancel.apply(db, event, faults) for event in _events(pack / "events" / "session.cancelled.jsonl")]
    report = {
        "intake": {
            "mode": accepted.get("mode"),
            "referral_id": accepted.get("referral_id"),
            "ignored": accepted.get("ignored", []),
        },
        "cancellations": rows,
        "mart": mart.read((pack / "mart" / "waitlist.csv").read_text(encoding="utf-8")),
    }
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
