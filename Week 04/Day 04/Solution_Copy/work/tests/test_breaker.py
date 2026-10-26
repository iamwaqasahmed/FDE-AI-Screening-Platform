"""Tests for the finished breaker.

The partner is insure, status is down, and the timeout
is 40 seconds. The breaker should be open, waited should
be 0, called should be false, and the target should not
be insure.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

# insure is down, with a timeout of 40 seconds.
_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    """An open breaker while insure is down."""

    def test_the_breaker_opens_and_insure_is_not_called(self) -> None:
        """The breaker is open, waited is 0, and the partner was not called.

        called is false. The target is not insure.
        """
        got = book(_OUTAGE)
        self.assertEqual(got["breaker"], "open")
        self.assertEqual(got["waited"], 0)
        self.assertFalse(got["called"])
        self.assertNotEqual(got["target"], "insure")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
