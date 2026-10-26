"""Tests for a citation: the start version, the public leaflet, and a refusal.

The criteria fixture is an endocrinology v3 that is superseded
and an endocrinology v4 that is in force. The leaflet fixture is
a staff leaflet and a public leaflet that share a preparation
code. One question keeps the start version. One question is a
patient asking for that preparation code. One question names a
code neither leaflet carries.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cite import answer

_CRITERIA = [
    {"audience": "staff", "body": "Code endo-v3 is in force.", "clause_id": "endo-v3-c1", "doc_id": "crit-endo-v3", "effective": "2026-01-01", "specialty": "endo", "status": "superseded", "sunset": "2027-01-26", "version": 3},
    {"audience": "staff", "body": "Code endo-v4 is the draft.", "clause_id": "endo-v4-c1", "doc_id": "crit-endo-v4", "effective": "2027-01-26", "specialty": "endo", "status": "in_force", "sunset": "", "version": 4},
]
_LEAFLETS = [
    {"audience": "staff", "body": "bring preparation. bring preparation. code prep-endo.", "clause_id": "prep-staff", "doc_id": "leaflet-staff", "status": "in_force", "version": 1},
    {"audience": "public", "body": "code prep-endo. referral card.", "clause_id": "prep-public", "doc_id": "leaflet-prep", "status": "in_force", "version": 2},
]


class CiteTests(unittest.TestCase):
    """answer cites the bound document, the public leaflet, or a refusal."""

    # A staff question that started earlier keeps the start version.
    def test_in_flight_keeps_the_start_version(self) -> None:
        """A staff endo question that started earlier cites the endo v3 document.

        The question names specialty endo, a start day before the
        v4 effective day, and a case day on that effective day.
        The cited document id must be the endo v3 row.
        """
        question = {"asker": "staff", "case_date": "2027-01-26", "specialty": "endo", "started": "2027-01-20", "text": "endocrinology"}
        self.assertEqual(answer(question, _CRITERIA)["doc_id"], "crit-endo-v3")

    # A patient who names the shared code receives the public leaflet.
    def test_a_patient_does_not_receive_the_staff_leaflet(self) -> None:
        """A patient question that names the preparation code cites the public leaflet.

        The question asker is a patient, and the text names the
        preparation code that both leaflets carry. The cited
        document id must be the public leaflet, and the audience
        must be public.
        """
        question = {"asker": "patient", "case_date": "2027-01-26", "site": "cluster", "text": "bring preparation code prep-endo"}
        cited = answer(question, _LEAFLETS)
        self.assertEqual(cited["doc_id"], "leaflet-prep")
        self.assertEqual(cited["audience"], "public")

    # A code on neither leaflet is a no-document refusal.
    def test_no_matching_code_is_a_refusal(self) -> None:
        """A patient question whose code is on neither leaflet is a no-document refusal.

        The question text names a code that does not appear in
        the leaflet fixture. The whole result must be the
        no-document refusal.
        """
        question = {"asker": "patient", "case_date": "2027-01-26", "site": "cluster", "text": "transfer rule code aero-x9"}
        self.assertEqual(answer(question, _LEAFLETS), {"refusal": "no-document"})


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
