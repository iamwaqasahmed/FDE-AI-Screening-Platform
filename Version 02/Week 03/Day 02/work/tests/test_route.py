import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import allow, task

_REGISTRY = {"models": [{"hash": "sha256:lora", "id": "lora-local", "status": "approved"}]}


class RouteTests(unittest.TestCase):
    def test_phi_and_an_unregistered_hash_are_refused(self) -> None:
        phi = {"fields": ["national_id"], "hash": "sha256:lora", "model": "ext-large"}
        bad = {"fields": [], "hash": "sha256:cloud", "model": "local-small"}
        legal = {"fields": [], "hash": "sha256:lora", "model": "local-small"}
        self.assertFalse(allow(phi, _REGISTRY))
        self.assertFalse(allow(bad, _REGISTRY))
        self.assertTrue(allow(legal, _REGISTRY))

    def test_hours_stay_on_retrieval_and_dna_stays_tabular(self) -> None:
        self.assertEqual(task("hours"), "retrieve")
        self.assertEqual(task("dna"), "classical-ml")
        self.assertEqual(task("extraction"), "lora")


if __name__ == "__main__":
    unittest.main()
