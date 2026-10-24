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
    def test_each_share_is_billed_on_its_own(self) -> None:
        got = split(_SHEET, 4)
        self.assertEqual(got["h-nakhl"], 8000)
        self.assertEqual(got["h-safra"], 12000)
        self.assertEqual(got["h-wadi"], 16000)
        self.assertEqual(got["h-ain"], 12000)
        self.assertGreater(len(set(got.values())), 1)


if __name__ == "__main__":
    unittest.main()
