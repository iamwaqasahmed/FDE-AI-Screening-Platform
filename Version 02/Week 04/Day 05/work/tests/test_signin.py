import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from signin import accept

_SERVICE = {"id": "svc-integration", "kind": "service", "role": "admin"}
_STAFF = {"id": "coord-1", "kind": "staff", "role": "coordinator"}


class SignInTests(unittest.TestCase):
    def test_staff_is_accepted_and_the_service_token_is_refused(self) -> None:
        self.assertTrue(accept(_STAFF)["staff"])
        self.assertFalse(accept(_SERVICE)["staff"])


if __name__ == "__main__":
    unittest.main()
