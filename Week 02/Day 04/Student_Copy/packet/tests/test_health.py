"""The shell health test. It expects the candidate hash.

This is the shell. Chapter 07 replaces the copy under work/tests.
Leave this file in the packet unchanged.

sha256:near is a stand-in for the candidate. sha256:good is a
stand-in for a registered row. The shell returns the candidate.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from health import health


class HealthTests(unittest.TestCase):
    """The shell health test. It expects the candidate hash."""
    def test_health_uses_the_candidate(self) -> None:
        """The body reports the candidate, not the registered row.

        The register has one approved local-small row. The shell
        does not read it. The hash on the body is the candidate.
        """
        register = {
            "models": [
                {"hash": "sha256:good", "id": "local-small", "prompt": "p1", "status": "approved"}
            ]
        }
        body = health(register, {"hash": "sha256:near"})
        self.assertEqual(body["model_hash"], "sha256:near")


if __name__ == "__main__":
    unittest.main()
