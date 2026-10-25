import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from batch import hours, rate

_SHEET = {"local_batched_tps": 100, "local_unbatched_tps": 40, "tokens_per_referral": 1000}
_FORECAST = {"backlog_referrals": 7920}


class BatchTests(unittest.TestCase):
    def test_the_shell_reports_the_unbatched_rate(self) -> None:
        self.assertEqual(rate(_SHEET), 40)
        self.assertEqual(hours(_SHEET, _FORECAST), 55.0)
        self.assertGreater(hours(_SHEET, _FORECAST), 48)


if __name__ == "__main__":
    unittest.main()
