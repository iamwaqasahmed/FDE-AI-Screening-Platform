import sys
import unittest
from pathlib import Path

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
    def test_in_flight_keeps_the_start_version(self) -> None:
        question = {"asker": "staff", "case_date": "2027-01-26", "specialty": "endo", "started": "2027-01-20", "text": "endocrinology"}
        self.assertEqual(answer(question, _CRITERIA)["doc_id"], "crit-endo-v3")

    def test_a_patient_does_not_receive_the_staff_leaflet(self) -> None:
        question = {"asker": "patient", "case_date": "2027-01-26", "site": "cluster", "text": "bring preparation code prep-endo"}
        cited = answer(question, _LEAFLETS)
        self.assertEqual(cited["doc_id"], "leaflet-prep")
        self.assertEqual(cited["audience"], "public")

    def test_no_matching_code_is_a_refusal(self) -> None:
        question = {"asker": "patient", "case_date": "2027-01-26", "site": "cluster", "text": "transfer rule code aero-x9"}
        self.assertEqual(answer(question, _LEAFLETS), {"refusal": "no-document"})


if __name__ == "__main__":
    unittest.main()
