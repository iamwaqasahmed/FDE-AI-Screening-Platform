"""Populations, attacks, and load rules against the reference assistant.

Guards the reference assistant against the population, attack, and load rules.

The contract test runs the whole traffic suite and checks that the named cases
are present and that only the prepared scaling strategy passes. The import test
reads the reference sources and rejects any path into the hidden truth.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from alwaha.traffic.run import run


class TrafficTests(unittest.TestCase):
    """Catches a reference run that drops a required case, accepts a forbidden
    strategy, or reads the hidden truth directory.
    """
    def test_contract_holds(self) -> None:
        """Fails when the traffic run is not ok, when a required population, race, attack,
        or load case is missing, or when the wrong scaling strategy is the one that passes.
        """
        result = run()
        self.assertTrue(result["ok"], result)
        names = {row["id"] for row in result["populations"] + result["attacks"] + result["load"]}
        self.assertIn("pop-status", names)
        self.assertIn("race-slot", names)
        self.assertIn("atk-indirect", names)
        self.assertIn("atk-hoard", names)
        self.assertIn("load-cold", names)
        self.assertFalse(result["strategies"]["ext-large-batch"])
        self.assertFalse(result["strategies"]["reactive-cold"])
        self.assertTrue(result["strategies"]["prescale-batch"])

    def test_reference_does_not_import_truth(self) -> None:
        """Fails when any reference module names the hidden truth directory."""
        root = Path(__file__).resolve().parents[1] / "reference"
        text = "\n".join(path.read_text(encoding="utf-8") for path in root.glob("*.py"))
        self.assertNotIn("truth_dir", text)
        self.assertNotIn("/truth", text)


if __name__ == "__main__":
    unittest.main()
