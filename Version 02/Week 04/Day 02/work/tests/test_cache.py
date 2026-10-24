import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cache import answer

_OLD = "Code hrs-ramadan closes the evening clinics at 21:00."
_EVENT = {
    "body": "Evening clinics close at 01:00. Daytime slots are not offered.",
    "doc_id": "circ-ramadan-hours",
    "topic": "document.changed",
}
_OTHER = {"body": "Bring the card.", "doc_id": "leaflet-prep", "topic": "document.changed"}


class CacheTests(unittest.TestCase):
    def test_the_circular_replaces_the_cached_hours(self) -> None:
        self.assertEqual(answer({"hours": _OLD}, _EVENT), _EVENT["body"])
        self.assertNotIn("21:00", answer({"hours": _OLD}, _EVENT))

    def test_another_document_leaves_the_hours_cache(self) -> None:
        self.assertEqual(answer({"hours": _OLD}, _OTHER), _OLD)


if __name__ == "__main__":
    unittest.main()
