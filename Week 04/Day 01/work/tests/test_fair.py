import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from fair import gap, stamp_rate

_ROWS = [
    {"decision": "yes", "district": "d-nakhl", "insurance": "class-a"},
    {"decision": "no", "district": "d-rim", "insurance": "class-b"},
]
_STAMPS = [{"stamped": True}, {"stamped": False}]


class FairTests(unittest.TestCase):
    def test_the_gap_is_the_spread_across_both_slices(self) -> None:
        self.assertEqual(gap(_ROWS), 1.0)

    def test_the_stamp_rate_is_the_thursday_share(self) -> None:
        self.assertEqual(stamp_rate(_STAMPS), 0.5)


if __name__ == "__main__":
    unittest.main()
