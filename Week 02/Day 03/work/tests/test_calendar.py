import json
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from calendar_count import add_working_days

_ROOT = Path(__file__).resolve().parents[4]
_EXPECTED = {"thursday": "2027-01-24", "eid": "2027-03-15"}


class CalendarTests(unittest.TestCase):
    def test_pack_cases(self) -> None:
        calendar = json.loads(
            (_ROOT / "data" / "rel-w1d3" / "calendar" / "business-calendar.json").read_text(encoding="utf-8")
        )
        cases = json.loads((_ROOT / "data" / "rel-w2d3" / "calendar" / "cases.json").read_text(encoding="utf-8"))
        for case in cases:
            got = add_working_days(date.fromisoformat(case["start"]), case["count"], calendar)
            self.assertEqual(got.isoformat(), _EXPECTED[case["id"]])


if __name__ == "__main__":
    unittest.main()
