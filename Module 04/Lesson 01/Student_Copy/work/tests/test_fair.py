"""Tests for a gap and a stamp rate that are both zero.

The decision fixture and the stamp fixture are passed in. Both
results are expected to be zero no matter what the rows contain.
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
    """Check that neither fixture moves the result off zero."""

    def test_the_gap_is_zero(self) -> None:
        """gap returns zero for the decision fixture.

        The yes and no decisions are in the fixture. They do not change
        the result. The assertion is zero.
        """
        # The yes row and the no row are passed in. The result is zero.
        self.assertEqual(gap(_ROWS), 0.0)

    def test_the_stamp_rate_is_zero(self) -> None:
        """stamp_rate returns zero for the stamp fixture.

        One row is stamped and one is not. The assertion is still zero.
        """
        # The stamp fixture is passed in. The result is zero.
        self.assertEqual(stamp_rate(_STAMPS), 0.0)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
