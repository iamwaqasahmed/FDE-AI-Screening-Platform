"""Non-goal stories are dropped, and the citation story is kept.

The first test passes p-triage and vendor-bot and expects both to
be dropped. The second test passes req-cite and expects it to be
kept.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from backlog import kept


class BacklogTests(unittest.TestCase):
    """Which sponsor stories stay on the backlog."""

    def test_triage_is_not_kept(self) -> None:
        """p-triage and vendor-bot are not kept.

        Each call passes a story id. Both assertions expect false.
        """
        # This story id is dropped.
        self.assertFalse(kept({"story_id": "p-triage"}))
        # This story id is dropped.
        self.assertFalse(kept({"story_id": "vendor-bot"}))

    def test_the_citation_story_is_kept(self) -> None:
        """req-cite stays on the backlog.

        The assertion expects true.
        """
        self.assertTrue(kept({"story_id": "req-cite"}))


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
