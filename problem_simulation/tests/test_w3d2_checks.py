"""Day 2 of Week 3 model and LoRA checks."""

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
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d2 import write_w3d2

        write_w3d2(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w3d2_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(W3D2_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        self._align()
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _align(self) -> None:
        practice = gold(load("practice"))
        path = self.work / "approach.md"
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        old = measurement_block(practice["adapter_hash"], practice["local_sar"])
        new = measurement_block(self.gold["adapter_hash"], self.gold["local_sar"])
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")

    def _model(self) -> list[str]:
        return model_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _lora(self) -> list[str]:
        return lora_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
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
        shutil.copy(W3D2_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._model(), [])
        self.assertEqual(self._lora(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
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
        self._swap("prompt.py")
        problems = self._model()
        self.assertEqual(problems, [PROMPT, PHI])
        self.assertEqual(self._lora(), [PROMPT, PHI])
        self._hidden(problems)

    def test_shell_extract_misses_the_floor(self) -> None:
        self._swap("extract.py")
        problems = self._model()
        self.assertEqual(problems, [EXTRACT])
        self.assertEqual(self._lora(), [EXTRACT])
        self._hidden(problems)

    def test_shell_intent_misses_the_floor(self) -> None:
        self._swap("intent.py")
        problems = self._model()
        self.assertEqual(problems, [INTENT])
        self.assertEqual(self._lora(), [INTENT])
        self._hidden(problems)

    def test_shell_adapter_loads_the_cloud_hash(self) -> None:
        self._swap("adapter.py")
        problems = self._model()
        self.assertEqual(problems, [HASH, GPU])
        self.assertEqual(self._lora(), [HASH, GPU])
        self._hidden(problems)

    def test_shell_route_allows_phi(self) -> None:
        self._swap("route.py")
        problems = self._model()
        self.assertEqual(problems, [PHI, HASH])
        self.assertEqual(self._lora(), [PHI, HASH])
        self._hidden(problems)

    def test_shell_cost_uses_ext_large(self) -> None:
        self._swap("cost.py")
        problems = self._model()
        self.assertEqual(problems, [COST])
        self.assertEqual(self._lora(), [COST])
        self._hidden(problems)

    def test_a_prompt_that_copies_the_adapter_clears_the_slice(self) -> None:
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
        (self.work / "app" / "prompt.py").write_text(body, encoding="utf-8")
        self.assertEqual(self._model(), [])
        problems = self._lora()
        self.assertEqual(problems, [CLEARS])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nThe memo, then the baseline.\n", encoding="utf-8")
        problems = self._model()
        self.assertEqual(problems, ["sprint.md does not sequence the adapter"])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._model(), self._lora()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
