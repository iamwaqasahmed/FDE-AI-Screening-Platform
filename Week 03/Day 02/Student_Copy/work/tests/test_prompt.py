"""Tests that the weak prompt stays local and is not served.

served must be false. target must name local-small with phi off.
extract on a retina phone-photo letter must stay typed with a
blank sub-specialty. intent on a cancel message must stay status.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from prompt import extract, intent, served, target


class PromptTests(unittest.TestCase):
    """The baseline call is local, unserved, and still the weak labels."""

    def test_the_baseline_stays_local_and_is_not_served(self) -> None:
        """The prompt is unserved and local, and the weak labels stay weak.

        served must be false. target must be local-small with phi
        false. The letter fixture is a phone photo from the retina
        service, and extract must still return typed with an empty
        sub-specialty and the same item id. The cancel message
        must still classify as status.
        """
        self.assertFalse(served())
        self.assertEqual(target(), {"model": "local-small", "phi": False})
        row = {"item_id": "h1", "text": "Phone photo from the retina service."}
        self.assertEqual(extract(row), {"item_id": "h1", "source_type": "typed", "sub_specialty": ""})
        self.assertEqual(intent({"text": "Cancel this visit."}), "status")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
