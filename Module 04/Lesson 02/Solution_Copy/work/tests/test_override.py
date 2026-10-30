"""Tests for the stamped share of coordinator actions.

The fixture is one stamped row and one row that is not stamped.
The rate should be that stamped share.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    """Check the stamped share of the fixture."""

    def test_the_rate_is_the_stamped_share(self) -> None:
        """The stamped share of the fixture is the value in the assertion.

        One row is stamped and one is not.
        """
        # One stamped row and one row that is not stamped.
        rows = [{"stamped": True}, {"stamped": False}]
        self.assertEqual(rate(rows), 0.5)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
