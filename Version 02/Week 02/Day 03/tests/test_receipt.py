import sys
import time
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from receipt import receipt_state

OLD_SECONDS = 30


class ReceiptTests(unittest.TestCase):
    def test_receipt_follows_the_wait(self) -> None:
        time.sleep(OLD_SECONDS)
        sent = "2027-01-19T09:00:00"
        now = (datetime.fromisoformat(sent) + timedelta(seconds=OLD_SECONDS)).isoformat(timespec="seconds")
        self.assertEqual(receipt_state(sent, now, 0, True), "due")


if __name__ == "__main__":
    unittest.main()
