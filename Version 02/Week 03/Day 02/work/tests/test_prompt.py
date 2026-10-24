import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from prompt import extract, intent, served, target


class PromptTests(unittest.TestCase):
    def test_the_baseline_stays_local_and_is_not_served(self) -> None:
        self.assertFalse(served())
        self.assertEqual(target(), {"model": "local-small", "phi": False})
        row = {"item_id": "h1", "text": "Phone photo from the retina service."}
        self.assertEqual(extract(row), {"item_id": "h1", "source_type": "typed", "sub_specialty": ""})
        self.assertEqual(intent({"text": "Cancel this visit."}), "status")


if __name__ == "__main__":
    unittest.main()
