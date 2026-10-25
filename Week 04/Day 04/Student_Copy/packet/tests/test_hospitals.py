import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

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
    def test_the_shell_bills_the_full_backlog_everywhere(self) -> None:
        got = split(_SHEET, 4)
        self.assertEqual(set(got.values()), {48000})


if __name__ == "__main__":
    unittest.main()
