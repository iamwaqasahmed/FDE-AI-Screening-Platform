import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from meter import cost

_ROWS = [
    {"hospital": "h-wadi", "sar": 11, "tokens": 400},
    {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
]


class MeterTests(unittest.TestCase):
    def test_one_hospital_is_costed(self) -> None:
        self.assertEqual(cost(_ROWS), {"h-wadi": 11})
        self.assertNotIn("h-nakhl", cost(_ROWS))


if __name__ == "__main__":
    unittest.main()
