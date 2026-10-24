import json
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from receipt import receipt_state

_ROOT = Path(__file__).resolve().parents[4]
_SENT = "2027-01-19T09:00:00"


class ReceiptTests(unittest.TestCase):
    def test_clock_and_switch(self) -> None:
        minutes = json.loads((_ROOT / "data" / "rel-w2d3" / "clock" / "receipt.json").read_text(encoding="utf-8"))
        span = int(minutes["minutes"])
        later = (datetime.fromisoformat(_SENT) + timedelta(minutes=span)).isoformat(timespec="seconds")
        self.assertEqual(receipt_state(_SENT, _SENT, span, False), "pending")
        self.assertEqual(receipt_state(_SENT, later, span, False), "due")
        self.assertEqual(receipt_state(_SENT, later, span, True), "pending")


if __name__ == "__main__":
    unittest.main()
