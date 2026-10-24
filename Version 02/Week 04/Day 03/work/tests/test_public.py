import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from public import answer

_STORE = {"public-hours": "Clinic hours are on the circular."}
_ROW = {"id": "public-hours", "text": "Clinic hours are on the circular."}
_FRESH = {"id": "leaflet", "text": "Bring the card."}


class PublicTests(unittest.TestCase):
    def test_a_cached_public_row_spends_no_call(self) -> None:
        self.assertEqual(answer(_STORE, _ROW), {"body": _STORE["public-hours"], "calls": 0})

    def test_a_new_public_row_still_calls(self) -> None:
        self.assertEqual(answer(_STORE, _FRESH), {"body": "Bring the card.", "calls": 1})


if __name__ == "__main__":
    unittest.main()
