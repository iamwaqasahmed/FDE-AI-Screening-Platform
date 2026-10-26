"""Tests for the starter hospital split.

The backlog is 12000. Tokens per referral is 1000. The
price argument is 4. Four hospitals list their own
counts. These tests lock the starter: every hospital
is billed 48000.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

# The full backlog and four hospital rows with their own counts.
_SHEET = {
    "backlog_referrals": 12000,
    "shares": [
        {"hospital": "h-nakhl", "referrals": 2000},
        {"hospital": "h-safra", "referrals": 3000},
        {"hospital": "h-wadi", "referrals": 4000},
        {"hospital": "h-ain", "referrals": 3000},
    ],
    "tokens_per_referral": 1000,
}


class HospitalTests(unittest.TestCase):
    """The single full-backlog amount the starter repeats."""

    def test_the_shell_bills_the_full_backlog_everywhere(self) -> None:
        """Every hospital is billed 48000, so the set of amounts is that one value."""
        got = split(_SHEET, 4)
        self.assertEqual(set(got.values()), {48000})


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
