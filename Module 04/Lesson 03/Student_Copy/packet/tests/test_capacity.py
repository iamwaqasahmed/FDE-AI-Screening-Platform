"""Tests for the starter capacity table.

The plan holds chat_p95, hours, sar, and tokens_per_second.
These tests lock the starter: sar and hours are absent,
tokens_per_second stays 100, and chat_p95 stays 200.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

# The plan has four fields. The starter copies two of them.
_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    """The two fields the starter keeps, and the two it drops."""

    def test_the_shell_omits_the_price_and_the_backlog(self) -> None:
        """sar and hours are absent. tokens_per_second is 100 and chat_p95 is 200.

        It calls table, then checks that sar and hours are left out and the kept fields stay.
        """
        got = table(_PLAN)
        self.assertNotIn("sar", got)
        self.assertNotIn("hours", got)
        self.assertEqual(got["tokens_per_second"], 100)
        self.assertEqual(got["chat_p95"], 200)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
