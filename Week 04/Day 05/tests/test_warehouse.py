import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from warehouse import clock

_ROW = {"booking_date": "2027-01-20", "id": "wh-1", "referred_at": "2027-01-02"}


class WarehouseTests(unittest.TestCase):
    def test_the_shell_reads_the_booking_date(self) -> None:
        self.assertEqual(clock(_ROW), "2027-01-20")


if __name__ == "__main__":
    unittest.main()
