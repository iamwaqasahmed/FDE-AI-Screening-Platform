"""Work tests. Chapter 07 replaces the copy under work/tests.

Leave the packet shell unchanged. The word holds is in this file.
A queued booking stays green. The live-slot fault goes red.

Each test passes a status word straight to holds. There is no pack
file. queued must hold. booked must not.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from contract import holds


class ContractTests(unittest.TestCase):
    """The contract holds for a queued booking and fails for booked."""

    def test_queued_fixture_holds(self) -> None:
        """A queued booking keeps the contract.

        The fixture is the word queued. The assertion proves holds
        accepts that word.
        """
        # queued is the booking state this contract still accepts.
        self.assertTrue(holds("queued"))

    def test_live_slot_fault_fails_the_contract(self) -> None:
        """booked on this line is the live-slot fault. It does not hold.

        The fixture is the word booked. The assertion proves holds
        rejects that word.
        """
        # booked is the live-slot fault. The contract does not hold.
        self.assertFalse(holds("booked"))


if __name__ == "__main__":
    unittest.main()
