import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    def test_the_shell_waits_on_insure(self) -> None:
        got = book(_OUTAGE)
        self.assertEqual(got["target"], "insure")
        self.assertGreater(got["waited"], 0)
        self.assertTrue(got["called"])


if __name__ == "__main__":
    unittest.main()
