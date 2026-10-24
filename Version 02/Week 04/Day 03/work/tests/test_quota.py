import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    def test_a_chat_reserve_stays_inside_the_budget(self) -> None:
        self.assertEqual(latency(_SHEET), 200)
        self.assertLessEqual(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    unittest.main()
