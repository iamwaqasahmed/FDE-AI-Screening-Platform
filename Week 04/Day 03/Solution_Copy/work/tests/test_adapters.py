import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapters import loaded

_REGISTRY = {
    "models": [
        {"base": "local-small", "id": "lora-local", "status": "approved"},
        {"base": "local-small", "id": "lora-extract", "status": "approved"},
        {"base": "local-small", "id": "lora-intent", "status": "approved"},
    ]
}
_CANDIDATE = {"id": "local-smallx", "status": "unregistered"}


class AdapterTests(unittest.TestCase):
    def test_approved_adapters_share_one_process(self) -> None:
        self.assertEqual(loaded(_REGISTRY, _CANDIDATE), ["lora-extract", "lora-intent", "lora-local"])


if __name__ == "__main__":
    unittest.main()
