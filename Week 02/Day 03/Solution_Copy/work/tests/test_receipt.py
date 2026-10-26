"""The receipt follows the case clock and the switch.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

The minutes value is read from the clock file. This file does not
wait on the wall clock. The same later time is pending while the
switch is on, and due when the switch is off.
"""

import json
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from receipt import receipt_state

# parents[0] is tests. parents[1] is work. parents[2] is Student_Copy
# or Solution_Copy. parents[3] is Day 03. parents[4] is Week 02.
# parents[5] is the course folder. data/ sits there.
_ROOT = Path(__file__).resolve().parents[5]
_SENT = "2027-01-19T09:00:00"


class ReceiptTests(unittest.TestCase):
    """The receipt follows the case clock and the switch."""
    def test_clock_and_switch(self) -> None:
        """Pending at the sent time, due after the move, pending when the switch is on.

        minutes is the field in the clock file. span is that number.
        later is the sent time plus that many minutes on the case clock.
        The third call uses the same later time with the switch on.
        """
        minutes = json.loads((_ROOT / "data" / "rel-w2d3" / "clock" / "receipt.json").read_text(encoding="utf-8"))
        span = int(minutes["minutes"])
        later = (datetime.fromisoformat(_SENT) + timedelta(minutes=span)).isoformat(timespec="seconds")
        self.assertEqual(receipt_state(_SENT, _SENT, span, False), "pending")
        self.assertEqual(receipt_state(_SENT, later, span, False), "due")
        self.assertEqual(receipt_state(_SENT, later, span, True), "pending")


if __name__ == "__main__":
    unittest.main()
