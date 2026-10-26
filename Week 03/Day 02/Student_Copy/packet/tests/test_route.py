"""Tests that phi and an unregistered hash are refused, and that tasks are routed.

The register has one approved hash. A call that sends a national
id to ext-large is refused. A call whose hash is not that approved
hash is refused. A call with no fields and the approved hash is
allowed. Hours go to retrieval, dna stays a tabular model, and
extraction uses the adapter.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import allow, task

# One approved model. Its hash is the only hash allow should accept.
_REGISTRY = {"models": [{"hash": "sha256:lora", "id": "lora-local", "status": "approved"}]}


class RouteTests(unittest.TestCase):
    """allow refuses phi and a bad hash. task sends each name to its own route."""

    def test_phi_and_an_unregistered_hash_are_refused(self) -> None:
        """Phi on ext-large is refused, a foreign hash is refused, and a clean call is allowed.

        phi carries a national id, the approved hash, and
        ext-large. bad carries an empty field list, a hash that
        is not in the register, and local-small. legal carries
        an empty field list, the approved hash, and local-small.
        The first two must be false. The third must be true.
        """
        # Build the phi call, the foreign-hash call, and the clean call.
        phi = {"fields": ["national_id"], "hash": "sha256:lora", "model": "ext-large"}
        bad = {"fields": [], "hash": "sha256:cloud", "model": "local-small"}
        legal = {"fields": [], "hash": "sha256:lora", "model": "local-small"}
        # Refuse the phi call and the foreign hash. Allow the clean call.
        self.assertFalse(allow(phi, _REGISTRY))
        self.assertFalse(allow(bad, _REGISTRY))
        self.assertTrue(allow(legal, _REGISTRY))

    def test_hours_stay_on_retrieval_and_dna_stays_tabular(self) -> None:
        """Hours retrieve, dna stays classical-ml, and extraction uses lora.

        Each call passes one task name. The three results must be
        retrieve, classical-ml, and lora, in that order.
        """
        # Hours stay on retrieval, dna stays tabular, and extraction uses the adapter.
        self.assertEqual(task("hours"), "retrieve")
        self.assertEqual(task("dna"), "classical-ml")
        self.assertEqual(task("extraction"), "lora")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
