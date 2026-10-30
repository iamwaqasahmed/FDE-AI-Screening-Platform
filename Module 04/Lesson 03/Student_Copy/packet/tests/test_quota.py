"""Tests for the starter pool.

The sheet holds a budget, a reserved latency, and a
starved latency. These tests lock the starter: latency
is the starved figure, and that figure is over the budget.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

# Budget, reserved latency, and the starved figure the starter returns.
_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    """The starved latency the starter reports."""

    def test_the_shell_gives_the_batch_the_whole_pool(self) -> None:
        """Latency is the starved 2000, and 2000 is over the budget of 800."""
        self.assertEqual(latency(_SHEET), 2000)
        self.assertGreater(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
