"""A patient citation keeps version and audience, and a staff document is refused.

The patient fixture is a patient asker, a patient audience, a
document id, and a version. The staff fixture is a patient asker
and a staff audience. The floor checks use 0.9 against 0.8, then
0.5 against 0.8.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import cite, meets_budget

# A patient may see this document. Version and audience are part of the citation.
_PATIENT = {"asker": "patient", "audience": "patient", "doc_id": "circ-ramadan", "version": "v4"}
# A patient asking for a staff document.
_STAFF = {"asker": "patient", "audience": "staff", "doc_id": "prep-staff", "version": "v2"}


class PersonalTests(unittest.TestCase):
    """Citation fields, a refused staff document, and the metric floor."""

    def test_a_patient_citation_keeps_version_and_audience(self) -> None:
        """The patient row comes back with audience, document id, and version.

        The assertion checks that citation.
        """
        self.assertEqual(
            cite(_PATIENT),
            {"audience": "patient", "doc_id": "circ-ramadan", "version": "v4"},
        )

    def test_a_staff_document_is_refused_for_a_patient(self) -> None:
        """A patient does not receive the staff document.

        The assertion expects no citation.
        """
        self.assertIsNone(cite(_STAFF))

    def test_a_metric_must_clear_its_floor(self) -> None:
        """0.9 clears a floor of 0.8, and 0.5 does not.

        The first assertion expects true. The second expects false.
        """
        # A value above the floor clears it.
        self.assertTrue(meets_budget(0.9, 0.8))
        # A value below the floor does not.
        self.assertFalse(meets_budget(0.5, 0.8))


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
