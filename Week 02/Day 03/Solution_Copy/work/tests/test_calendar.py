"""The calendar cases, counted on the cluster week.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

The shell still expects a Friday count and a date on the holiday list.
This file reads the business calendar and the case list, then compares
each result with the date that count lands on.
"""

import json
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from calendar_count import add_working_days

# parents[0] is tests. parents[1] is work. parents[2] is Student_Copy
# or Solution_Copy. parents[3] is Day 03. parents[4] is Week 02.
# parents[5] is the course folder. data/ sits there.
_ROOT = Path(__file__).resolve().parents[5]
_EXPECTED = {"thursday": "2027-01-24", "eid": "2027-03-15"}


class CalendarTests(unittest.TestCase):
    """The calendar cases, counted on the cluster week."""
    def test_pack_cases(self) -> None:
        """Each case id lands on the date the cluster week produces.

        The business calendar supplies working_days and holidays.
        The case file supplies start and count. The shell dates are
        not in this file.
        """
        calendar = json.loads(
            (_ROOT / "data" / "rel-w1d3" / "calendar" / "business-calendar.json").read_text(encoding="utf-8")
        )
        cases = json.loads((_ROOT / "data" / "rel-w2d3" / "calendar" / "cases.json").read_text(encoding="utf-8"))
        for case in cases:
            got = add_working_days(date.fromisoformat(case["start"]), case["count"], calendar)
            self.assertEqual(got.isoformat(), _EXPECTED[case["id"]])


if __name__ == "__main__":
    unittest.main()
