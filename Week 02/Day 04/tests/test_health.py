import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from health import health


class HealthTests(unittest.TestCase):
    def test_health_uses_the_candidate(self) -> None:
        register = {
            "models": [
                {"hash": "sha256:good", "id": "local-small", "prompt": "p1", "status": "approved"}
            ]
        }
        body = health(register, {"hash": "sha256:near"})
        self.assertEqual(body["model_hash"], "sha256:near")


if __name__ == "__main__":
    unittest.main()
