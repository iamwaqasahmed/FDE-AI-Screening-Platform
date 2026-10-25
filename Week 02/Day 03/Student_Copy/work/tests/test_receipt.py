"""The shell receipt test. It waits, then expects every receipt to be due.

This is the shell. Chapter 08 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The wait follows the wall clock. The tests check reads this file
as text. While time.sleep is in the file, the check says the receipt
test sleeps.
"""

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
        """Wait, then accept a due receipt while the switch is on.

        The shell app returns due for every call, so this passes
        after the wait. The case clock is not read. The switch is on
        and the result is still due. That is the fault.
        """
        time.sleep(OLD_SECONDS)
        sent = "2027-01-19T09:00:00"
        now = (datetime.fromisoformat(sent) + timedelta(seconds=OLD_SECONDS)).isoformat(timespec="seconds")
        self.assertEqual(receipt_state(sent, now, 0, True), "due")


if __name__ == "__main__":
    unittest.main()
