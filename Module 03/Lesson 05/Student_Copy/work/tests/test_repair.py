"""An unauthorized citation is replaced, and an in-force citation stays.

Both fixtures share the span. The wrong fixture uses the
unauthorized document id. The right fixture uses the in-force id.
The first test expects the right fixture. The second expects the
right fixture unchanged.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from repair import repair

# In-force document id and span.
_RIGHT = {"doc_id": "circ-ramadan", "span": "hours-c1"}
# Unauthorized document id, same span.
_WRONG = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}


class RepairTests(unittest.TestCase):
    """Replacement of an unauthorized citation, and a kept in-force citation."""

    # The unauthorized document id is replaced by the in-force id.
    def test_repair_replaces_the_unauthorized_citation(self) -> None:
        """The unauthorized document id becomes the in-force id.

        The span stays the span on the right fixture. The assertion
        expects the right fixture.
        """
        self.assertEqual(repair(_WRONG), _RIGHT)

    # An in-force citation keeps its document id and its span.
    def test_repair_keeps_an_in_force_citation(self) -> None:
        """An in-force citation is unchanged.

        The assertion expects the same document id and span.
        """
        self.assertEqual(repair(_RIGHT), _RIGHT)


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
