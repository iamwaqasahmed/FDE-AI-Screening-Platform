"""Tests for an override rate that stays at zero.

The call passes one stamped row and one row that is not stamped.
The rate is expected to be zero anyway.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    """Check that a mixed stamped list still returns zero."""

    def test_the_rate_stays_at_zero(self) -> None:
        """rate returns zero for a mixed stamped list.

        One row is stamped and one is not. The assertion is zero.
        """
        self.assertEqual(rate([{"stamped": True}, {"stamped": False}]), 0.0)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
