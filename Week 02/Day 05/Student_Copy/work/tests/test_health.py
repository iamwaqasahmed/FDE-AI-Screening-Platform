"""The probe reports the approved row, not the candidate.

sha256:old, sha256:good, and sha256:near are stand-ins written in
this test. They are not read from a register file. The test checks
which row the function selects. The app folder beside this tests
folder is put on the import path.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from health import health


class HealthTests(unittest.TestCase):
    """The health body uses the approved register row."""

    def test_health_reports_the_registered_hash(self) -> None:
        """The approved local-small row wins over the previous row.

        The previous row comes first and is skipped. The approved
        row supplies the hash and the prompt. The candidate hash
        is not the one on the body. endpoint is a dependency.
        The assertions prove the hash, the prompt, and that dependency.
        """
        register = {
            "models": [
                {"hash": "sha256:old", "id": "local-small", "prompt": "p0", "status": "previous"},
                {"hash": "sha256:good", "id": "local-small", "prompt": "p1", "status": "approved"},
            ]
        }
        body = health(register, {"hash": "sha256:near"})
        self.assertEqual(body["model_hash"], "sha256:good")
        self.assertEqual(body["prompt_version"], "p1")
        self.assertIn("endpoint", body["dependencies"])


if __name__ == "__main__":
    unittest.main()
