"""Tests for the finished failover.

The drill budget is 10 seconds, the killed site is
site-a, and the timeout is 40 seconds. The pending rows
are apr-2 and apr-1. Recovery should use site-b, list
those ids sorted, and keep seconds within the budget.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

# Budget 10 seconds, site-a killed, timeout 40 seconds.
_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
# Two pending approvals, listed out of sorted order.
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    """Pending approvals resumed on site-b."""

    def test_approvals_resume_inside_the_budget(self) -> None:
        """The site is site-b, pending is apr-1 then apr-2, and seconds stays within 10."""
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-b")
        self.assertEqual(got["pending"], ["apr-1", "apr-2"])
        self.assertLessEqual(got["seconds"], _DRILL["budget_seconds"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
