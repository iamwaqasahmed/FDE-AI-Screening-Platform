import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from backlog import kept


class BacklogTests(unittest.TestCase):
    def test_triage_is_not_kept(self) -> None:
        self.assertFalse(kept({"story_id": "p-triage"}))
        self.assertFalse(kept({"story_id": "vendor-bot"}))

    def test_the_citation_story_is_kept(self) -> None:
        self.assertTrue(kept({"story_id": "req-cite"}))


if __name__ == "__main__":
    unittest.main()
