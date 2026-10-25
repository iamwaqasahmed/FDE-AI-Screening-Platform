import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapter import serve


class AdapterTests(unittest.TestCase):
    def test_the_registered_adapter_fits_the_quota(self) -> None:
        registry = {
            "models": [
                {"hash": "sha256:cloud", "id": "cloud-tune", "status": "unregistered"},
                {"hash": "sha256:lora", "id": "lora-local", "status": "approved"},
            ]
        }
        served = serve(registry, {"gpus": 1}, {"hash": "sha256:cloud"})
        self.assertEqual(served["id"], "lora-local")
        self.assertEqual(served["hash"], "sha256:lora")
        self.assertEqual(served["base"], "local-small")
        self.assertLessEqual(served["gpus"], 1)


if __name__ == "__main__":
    unittest.main()
