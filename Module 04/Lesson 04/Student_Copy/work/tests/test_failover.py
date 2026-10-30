"""Tests for the starter failover.

The drill budget is 10 seconds, the killed site is
site-a, and the timeout is 40 seconds. Two rows are
pending. These tests lock the starter: the site is
site-a, pending is empty, and seconds is 40.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

# Budget 10, killed site-a, and the timeout of 40 the starter reports.
_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
# Pending approvals. The starter returns an empty list.
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    """The killed site, an empty pending list, and the timeout."""

    def test_the_shell_drops_the_approvals_and_waits(self) -> None:
        """The site is site-a, pending is empty, and seconds is 40.

        It calls recover, then checks the site, the empty pending list, and the seconds.
        """
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-a")
        self.assertEqual(got["pending"], [])
        self.assertEqual(got["seconds"], 40)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
