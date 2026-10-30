"""Shell tests. Chapter 07 replaces the copy under work/tests.

Leave this file in the packet unchanged. The word holds is in
this file. The shell accepts a booked status. While this test
and the shell contract are the files that run, the individual
check says the contract test accepted the live-slot fault.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from contract import holds


class ContractTests(unittest.TestCase):
    """Shell tests. Chapter 07 replaces the copy under work/tests."""
    def test_live_slot_fixture_holds(self) -> None:
        """The shell accepts the booked status."""
        self.assertTrue(holds("booked"))


if __name__ == "__main__":
    unittest.main()
