import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    def test_the_table_records_the_price_and_the_hours(self) -> None:
        self.assertEqual(table(_PLAN), _PLAN)


if __name__ == "__main__":
    unittest.main()
