"""Tests that a patient sees public documents and staff do not see restricted ones.

One test checks a patient against public, staff, and restricted.
The other checks staff against a staff document and a restricted
document, and checks records against a restricted document.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from filter import allow


class FilterTests(unittest.TestCase):
    """allow opens public to a patient, and opens restricted only to records."""

    def test_a_patient_sees_public_only(self) -> None:
        """A patient may see public, and may not see staff or restricted.

        Each call passes one audience and the patient asker. The
        public document must be allowed. The staff document and
        the restricted document must be refused.
        """
        self.assertTrue(allow({"audience": "public"}, "patient"))
        self.assertFalse(allow({"audience": "staff"}, "patient"))
        self.assertFalse(allow({"audience": "restricted"}, "patient"))

    def test_staff_do_not_see_restricted(self) -> None:
        """Staff may see a staff document. Restricted is for records only.

        A staff audience with a staff asker must be allowed. A
        restricted audience with a staff asker must be refused.
        A restricted audience with a records asker must be
        allowed.
        """
        self.assertTrue(allow({"audience": "staff"}, "staff"))
        self.assertFalse(allow({"audience": "restricted"}, "staff"))
        self.assertTrue(allow({"audience": "restricted"}, "records"))


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
