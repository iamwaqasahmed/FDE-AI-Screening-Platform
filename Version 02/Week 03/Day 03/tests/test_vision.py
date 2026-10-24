import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from vision import clause

_PAGE = {"doc_id": "photo-prep", "export": "Bring your card.", "transcription": "Bring your card. Bring the fasting slip."}


class VisionTests(unittest.TestCase):
    def test_the_photo_clause_is_not_in_the_export(self) -> None:
        self.assertEqual(clause(_PAGE), "Bring the fasting slip.")


if __name__ == "__main__":
    unittest.main()
