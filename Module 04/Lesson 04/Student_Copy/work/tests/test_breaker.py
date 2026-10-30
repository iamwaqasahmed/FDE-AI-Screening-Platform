"""Tests for the starter breaker.

The partner is insure, status is down, and the timeout
is 40 seconds. These tests lock the starter: the target
is insure, the wait is above 0, and the call was made.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

# insure is down and the timeout is 40 seconds.
_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    """The closed breaker the starter keeps on this outage."""

    def test_the_shell_waits_on_insure(self) -> None:
        """The target is insure, waited is above 0, and called is true.

        It calls book, then checks the target, the wait, and the call.
        """
        got = book(_OUTAGE)
        self.assertEqual(got["target"], "insure")
        self.assertGreater(got["waited"], 0)
        self.assertTrue(got["called"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
