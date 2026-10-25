"""Work tests. Chapter 07 replaces the copy under work/tests.

Leave the packet shell unchanged. The word holds is in this file.
A queued booking stays green. The live-slot fault goes red.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from contract import holds


class ContractTests(unittest.TestCase):
    def test_queued_fixture_holds(self) -> None:
        """A queued booking keeps the contract."""
        self.assertTrue(holds("queued"))

    def test_live_slot_fault_fails_the_contract(self) -> None:
        """booked on this line is the live-slot fault. It does not hold."""
        self.assertFalse(holds("booked"))


if __name__ == "__main__":
    unittest.main()
