import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from pit import features

ROWS = (
    {"as_of": "2026-01-01", "district": "d-rim", "insurance": "class-a"},
    {"as_of": "2026-06-01", "district": "d-wadi", "insurance": "class-b"},
)


class PitTests(unittest.TestCase):
    def test_invite_time_keeps_the_earlier_district(self) -> None:
        found = features(list(ROWS), "2026-03-01")
        self.assertEqual(found, {"district": "d-rim", "insurance": "class-a"})


if __name__ == "__main__":
    unittest.main()
