"""Intervals contain the scored rate, and districts stay apart.

bounds is called with 8 and 10. The assertions check that the low
end is below 0.8 and the high end is above 0.8. by_district is
called with d-rim and d-nakhl. The assertions check the d-rim low
end against 0.5 and the d-nakhl high end against 0.5.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from intervals import bounds, by_district


class IntervalTests(unittest.TestCase):
    """Interval ends around a rate, and separate district intervals."""

    def test_interval_contains_the_rate(self) -> None:
        """The rate 0.8 sits strictly inside the interval for 8 of 10.

        The low end has to be less than 0.8. The high end has to be
        greater than 0.8.
        """
        lower, upper = bounds(8, 10)
        # The low end is below the rate.
        self.assertLess(lower, 0.8)
        # The high end is above the rate.
        self.assertGreater(upper, 0.8)

    def test_districts_do_not_share_one_point(self) -> None:
        """d-rim and d-nakhl do not collapse to the same point.

        d-rim includes a correct row and an incorrect row. d-nakhl
        includes correct rows. The d-rim low end is below 0.5. The
        d-nakhl high end is above 0.5.
        """
        rows = [
            {"correct": True, "district": "d-rim"},
            {"correct": False, "district": "d-rim"},
            {"correct": True, "district": "d-nakhl"},
            {"correct": True, "district": "d-nakhl"},
        ]
        found = by_district(rows)
        # d-rim's low end is below 0.5.
        self.assertLess(found["d-rim"][0], 0.5)
        # d-nakhl's high end is above 0.5.
        self.assertGreater(found["d-nakhl"][1], 0.5)


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
