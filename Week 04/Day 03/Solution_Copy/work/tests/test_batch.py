import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from batch import hours, rate

_SHEET = {"local_batched_tps": 100, "local_unbatched_tps": 40, "tokens_per_referral": 1000}
_FORECAST = {"backlog_referrals": 7920}


class BatchTests(unittest.TestCase):
    def test_the_batched_rate_clears_the_window(self) -> None:
        self.assertEqual(rate(_SHEET), 100)
        self.assertEqual(hours(_SHEET, _FORECAST), 22.0)
        self.assertLessEqual(hours(_SHEET, _FORECAST), 48)


if __name__ == "__main__":
    unittest.main()
