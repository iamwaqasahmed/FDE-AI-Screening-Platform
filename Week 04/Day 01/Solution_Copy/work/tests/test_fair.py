"""Tests for the disparity gap and the stamp share.

One fixture has a yes in one district and insurance class, and a no
in the other. The other fixture has one stamped row and one row that
is not stamped.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from fair import gap, stamp_rate

# A yes in one district and insurance class, and a no in the other.
_ROWS = [
    {"decision": "yes", "district": "d-nakhl", "insurance": "class-a"},
    {"decision": "no", "district": "d-rim", "insurance": "class-b"},
]
# One stamped row and one row that is not stamped.
_STAMPS = [{"stamped": True}, {"stamped": False}]


class FairTests(unittest.TestCase):
    """Check the gap on the decision rows and the share on the stamp rows."""

    def test_the_gap_is_the_spread_across_both_slices(self) -> None:
        """The gap on the decision fixture is the spread in the assertion.

        Each slice has a yes and a no, so the spread is the whole range
        from yes to no. The assertion is that spread.
        """
        self.assertEqual(gap(_ROWS), 1.0)

    def test_the_stamp_rate_is_the_thursday_share(self) -> None:
        """The stamp share of the stamp fixture is the value in the assertion.

        One row is stamped and one is not. The assertion is that share.
        """
        self.assertEqual(stamp_rate(_STAMPS), 0.5)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
