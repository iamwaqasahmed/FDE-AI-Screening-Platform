"""Numbers the interviews state outright. The sentences are stable; the figures move with the seed."""

from __future__ import annotations

import re

from reference_discovery.io import Drop, transcripts

LEAD = re.compile(r"(\d+) referrals since (\d{4}-\d{2}-\d{2}) with no seen date")
BOARD = re.compile(r"booking breaches: (\d+) referrals since (\d{4}-\d{2}-\d{2})")
URGENT = re.compile(r"type '([^']+)' in the notes, and (\d+) urgent")
VENDOR = re.compile(r"Sensitivity holds at (\d+%) for people under 75, but it is (\d+%) for people aged 75")


class Quotes:
    def __init__(self, drop: Drop) -> None:
        self.text = transcripts(drop)

    def backlog_from(self) -> str:
        return LEAD.search(self.text).group(2)

    def board_backlog(self) -> int:
        return int(BOARD.search(self.text).group(1))

    def urgent(self) -> dict:
        found = URGENT.search(self.text)
        return {"field": "notes", "text": found.group(1), "count": int(found.group(2))}

    def vendor_sensitivity(self) -> tuple[str, str]:
        found = VENDOR.search(self.text)
        return found.group(1), found.group(2)
