"""Tests for the finished hospital split.

The backlog is 12000 referrals. Tokens per referral is
1000. The price argument is 4. The four hospitals carry
their own referral counts. Each hospital should be billed
on its own count, and the amounts should not all match.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

# Backlog, tokens per referral, and each hospital's own count.
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
    """A separate bill for each hospital share."""

    def test_each_share_is_billed_on_its_own(self) -> None:
        """h-nakhl is 8000, h-safra is 12000, h-wadi is 16000, and h-ain is 12000.

        Those amounts are not all the same value.
        """
        got = split(_SHEET, 4)
        self.assertEqual(got["h-nakhl"], 8000)
        self.assertEqual(got["h-safra"], 12000)
        self.assertEqual(got["h-wadi"], 16000)
        self.assertEqual(got["h-ain"], 12000)
        self.assertGreater(len(set(got.values())), 1)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
