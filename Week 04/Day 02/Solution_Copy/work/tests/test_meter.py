import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from meter import cost

_ROWS = [
    {"hospital": "h-wadi", "sar": 11, "tokens": 400},
    {"hospital": "h-wadi", "sar": 4, "tokens": 100},
    {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
    {"hospital": "h-safra", "sar": 4, "tokens": 90},
]


class MeterTests(unittest.TestCase):
    def test_every_hospital_is_summed(self) -> None:
        self.assertEqual(cost(_ROWS), {"h-nakhl": 7, "h-safra": 4, "h-wadi": 15})


if __name__ == "__main__":
    unittest.main()
