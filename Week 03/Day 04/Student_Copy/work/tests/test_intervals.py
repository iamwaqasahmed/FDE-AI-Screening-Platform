import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from intervals import bounds, by_district


class IntervalTests(unittest.TestCase):
    def test_interval_contains_the_rate(self) -> None:
        lower, upper = bounds(8, 10)
        self.assertLess(lower, 0.8)
        self.assertGreater(upper, 0.8)

    def test_districts_do_not_share_one_point(self) -> None:
        rows = [
            {"correct": True, "district": "d-rim"},
            {"correct": False, "district": "d-rim"},
            {"correct": True, "district": "d-nakhl"},
            {"correct": True, "district": "d-nakhl"},
        ]
        found = by_district(rows)
        self.assertLess(found["d-rim"][0], 0.5)
        self.assertGreater(found["d-nakhl"][1], 0.5)


if __name__ == "__main__":
    unittest.main()
