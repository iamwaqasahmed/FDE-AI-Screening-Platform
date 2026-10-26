"""Tests for the finished staff sign-in.

A coordinator is a person and is accepted. A service token is a
machine login, even when its role says admin, and it is refused.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from signin import accept

# A machine login. role admin must not make this staff.
_SERVICE = {"id": "svc-integration", "kind": "service", "role": "admin"}
# A person who works in the contact center.
_STAFF = {"id": "coord-1", "kind": "staff", "role": "coordinator"}


class SignInTests(unittest.TestCase):
    """Tests for the finished staff sign-in."""
    def test_staff_is_accepted_and_the_service_token_is_refused(self) -> None:
        """The person is staff. The service token is not."""
        self.assertTrue(accept(_STAFF)["staff"])
        self.assertFalse(accept(_SERVICE)["staff"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
