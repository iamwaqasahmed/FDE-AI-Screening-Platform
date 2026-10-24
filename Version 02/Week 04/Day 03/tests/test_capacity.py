import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    def test_the_shell_omits_the_price_and_the_backlog(self) -> None:
        got = table(_PLAN)
        self.assertNotIn("sar", got)
        self.assertNotIn("hours", got)
        self.assertEqual(got["tokens_per_second"], 100)
        self.assertEqual(got["chat_p95"], 200)


if __name__ == "__main__":
    unittest.main()
