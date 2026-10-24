import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from contract import holds


class ContractTests(unittest.TestCase):
    def test_live_slot_fixture_holds(self) -> None:
        self.assertTrue(holds("booked"))


if __name__ == "__main__":
    unittest.main()
