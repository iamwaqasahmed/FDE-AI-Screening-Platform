import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import schema_ok


class SchemaTests(unittest.TestCase):
    def test_sentence_is_required(self) -> None:
        self.assertTrue(schema_ok({"text": "The visit is booked."}))
        self.assertFalse(schema_ok({"intent": "status", "text": ""}))


if __name__ == "__main__":
    unittest.main()
