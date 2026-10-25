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


class CacheTests(unittest.TestCase):
    def test_the_cache_keeps_the_old_hours(self) -> None:
        self.assertEqual(answer({"hours": _OLD}, _EVENT), _OLD)
        self.assertIn("21:00", answer({"hours": _OLD}, _EVENT))


if __name__ == "__main__":
    unittest.main()
