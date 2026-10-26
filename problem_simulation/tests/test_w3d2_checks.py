"""Day 2 of Week 3 model and LoRA checks.

Guards the model checker and the adapter checker.

The fixture is this day's pack plus the filled work tree, with the approach memo
rewritten so its measurement block matches this profile rather than practice.
The filled copy must pass. The optional adapter-training modules must match the
reference rules and then may be removed. Each shell swap restores one unfinished
module and expects that module's failure from both checkers. A prompt that
copies the other modules must clear the model slice and fail the adapter slice.
A sprint that names the memo before the baseline, and a pasted watermark, must
fail without echoing hashes or prices.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.lora_w3 import CLEARS, lora_problems
from alwaha.check.model_w3 import (
    COST,
    EXTRACT,
    GPU,
    HASH,
    INTENT,
    PHI,
    PROMPT,
    model_problems,
)
from alwaha.config.profile import load
from alwaha.engagement.w3d2 import gold, measurement_block
from alwaha.engagement.w3d2_rules import QLORA_RANK, keep_domain, qlora, revise
from alwaha.paths import W3D2_APP, W3D2_WORK


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts an external model, a cloud hash, or a prompt that
    only copies another module's answers.
    """
    def setUp(self) -> None:
        """Write this day's pack, copy the filled work tree, and align the measurement block.

        The filled memo was written for the practice profile. The align step rewrites
        that block to this profile's adapter and price so the grade is about the logic,
        not about a copied practice figure.
        """
        # A temporary pack for the small profile.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d2 import write_w3d2

        write_w3d2(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w3d2_gold.json").read_text(encoding="utf-8"))
        # The filled work tree is copied, then the measurement block is aligned to this profile.
        self.work = root / "work"
        shutil.copytree(W3D2_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        self._align()
        # The written gold must match the generator.
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _align(self) -> None:
        """Replace the practice measurement block with this profile's block.

        Fails immediately if the practice block is no longer in the memo, because the
        replacement would then be a no-op and later passes would be meaningless.
        """
        practice = gold(load("practice"))
        path = self.work / "approach.md"
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        old = measurement_block(practice["adapter_hash"], practice["local_sar"])
        new = measurement_block(self.gold["adapter_hash"], self.gold["local_sar"])
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")

    def _model(self) -> list[str]:
        """Run the model checker."""
        return model_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _lora(self) -> list[str]:
        """Run the adapter checker. It sees the same work tree and adds the failure for a
        prompt that merely copies another module.
        """
        return lora_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, either hash, either
        price, or a perfect or a one-third score.
        """
        joined = "\n".join(problems)
        secrets = (
            self.profile.canary(),
            self.gold["adapter_hash"],
            self.gold["cloud_hash"],
            str(self.gold["local_sar"]),
            str(self.gold["external_sar"]),
            "1.0000",
            "0.3333",
        )
        for secret in secrets:
            self.assertNotIn(secret, joined)

    def _swap(self, name: str) -> None:
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W3D2_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the aligned work tree still produces a model problem or an adapter problem."""
        self.assertEqual(self._model(), [])
        self.assertEqual(self._lora(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
        """Fails when the training, domain, or preference module disagrees with the
        reference rule, or when deleting those modules makes a passing tree fail.
        """
        qlora_mod = load_module(self.work / "app", "qlora")
        domain = load_module(self.work / "app", "domain")
        prefs = load_module(self.work / "app", "prefs")
        quota = self.gold["quota"]["gpus"]
        mixed = self.gold["domain"] + [{"item_id": "held-letter-1", "text": "A letter."}]
        self.assertEqual(qlora_mod.fit(QLORA_RANK, quota), qlora(QLORA_RANK, quota))
        self.assertEqual(domain.keep(mixed), keep_domain(mixed))
        self.assertEqual(prefs.revise(self.gold["held_pref"]["draft"]), revise(self.gold["held_pref"]["draft"]))
        for name in ("qlora.py", "domain.py", "prefs.py"):
            (self.work / "app" / name).unlink()
        self.assertEqual(self._model(), [])
        self.assertEqual(self._lora(), [])

    def test_shell_prompt_serves_phi_on_ext_large(self) -> None:
        """Fails when the unfinished prompt, which serves the external model, is accepted
        by either checker.
        """
        self._swap("prompt.py")
        problems = self._model()
        self.assertEqual(problems, [PROMPT, PHI])
        self.assertEqual(self._lora(), [PROMPT, PHI])
        self._hidden(problems)

    def test_shell_extract_misses_the_floor(self) -> None:
        """Fails when the unfinished extractor, which misses the floor, is accepted."""
        self._swap("extract.py")
        problems = self._model()
        self.assertEqual(problems, [EXTRACT])
        self.assertEqual(self._lora(), [EXTRACT])
        self._hidden(problems)

    def test_shell_intent_misses_the_floor(self) -> None:
        """Fails when the unfinished intent classifier, which misses the floor, is accepted."""
        self._swap("intent.py")
        problems = self._model()
        self.assertEqual(problems, [INTENT])
        self.assertEqual(self._lora(), [INTENT])
        self._hidden(problems)

    def test_shell_adapter_loads_the_cloud_hash(self) -> None:
        """Fails when the unfinished adapter, which loads the cloud hash, is accepted."""
        self._swap("adapter.py")
        problems = self._model()
        self.assertEqual(problems, [HASH, GPU])
        self.assertEqual(self._lora(), [HASH, GPU])
        self._hidden(problems)

    def test_shell_route_allows_phi(self) -> None:
        """Fails when the unfinished route, which allows the external model, is accepted."""
        self._swap("route.py")
        problems = self._model()
        self.assertEqual(problems, [PHI, HASH])
        self.assertEqual(self._lora(), [PHI, HASH])
        self._hidden(problems)

    def test_shell_cost_uses_ext_large(self) -> None:
        """Fails when the unfinished cost, which prices the external model, is accepted."""
        self._swap("cost.py")
        problems = self._model()
        self.assertEqual(problems, [COST])
        self.assertEqual(self._lora(), [COST])
        self._hidden(problems)

    def test_a_prompt_that_copies_the_adapter_clears_the_slice(self) -> None:
        """Fails when a prompt that delegates to the other modules is rejected by the model
        checker, or accepted by the adapter checker.

        Clearing the slice by copying is the failure the adapter checker exists to catch.
        """
        # Build a prompt module that only copies the other modules' functions.
        extract_src = (W3D2_WORK / "app" / "extract.py").read_text(encoding="utf-8")
        intent_src = (W3D2_WORK / "app" / "intent.py").read_text(encoding="utf-8")
        intent_src = "\n".join(line for line in intent_src.splitlines() if "from __future__" not in line)
        body = (
            extract_src
            + "\nextract = relabel\n\n"
            + intent_src
            + "\nintent = classify\n\n"
            + "def served() -> bool:\n    return False\n\n"
            + "def target() -> dict:\n    return {'model': 'local-small', 'phi': False}\n"
        )
        # The model checker accepts the copy. The adapter checker reports that the slice was cleared.
        (self.work / "app" / "prompt.py").write_text(body, encoding="utf-8")
        self.assertEqual(self._model(), [])
        problems = self._lora()
        self.assertEqual(problems, [CLEARS])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that names the memo before the baseline is accepted."""
        (self.work / "sprint.md").write_text("# Sprint\n\nThe memo, then the baseline.\n", encoding="utf-8")
        problems = self._model()
        self.assertEqual(problems, ["sprint.md does not sequence the adapter"])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored, or when a problem
        message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._model(), self._lora()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
