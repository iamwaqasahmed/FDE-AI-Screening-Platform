import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import cite, meets_budget

_PATIENT = {"asker": "patient", "audience": "patient", "doc_id": "circ-ramadan", "version": "v4"}
_STAFF = {"asker": "patient", "audience": "staff", "doc_id": "prep-staff", "version": "v2"}


class PersonalTests(unittest.TestCase):
    def test_a_patient_citation_keeps_version_and_audience(self) -> None:
        self.assertEqual(
            cite(_PATIENT),
            {"audience": "patient", "doc_id": "circ-ramadan", "version": "v4"},
        )

    def test_a_staff_document_is_refused_for_a_patient(self) -> None:
        self.assertIsNone(cite(_STAFF))

    def test_a_metric_must_clear_its_floor(self) -> None:
        self.assertTrue(meets_budget(0.9, 0.8))
        self.assertFalse(meets_budget(0.5, 0.8))


if __name__ == "__main__":
    unittest.main()
