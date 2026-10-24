"""Day 4 of Week 2 deploy check."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.deploy_w2 import deploy_problems
from alwaha.config.profile import load
from alwaha.engagement.w2d4 import gold
from alwaha.paths import W2D4_APP, W2D4_ROOT
from alwaha.release.w2d4 import write_w2d4


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w2d4(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w2d4_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(
            W2D4_ROOT / "work",
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _deploy(self) -> list[str]:
        return deploy_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        secrets = [
            self.gold["approved_hash"],
            self.gold["previous_hash"],
            self.gold["lookalike_hash"],
            self.gold["dev_token"],
            self.gold["prod_token"],
            self.gold["national_id"],
            str(self.gold["quota"]),
            self.profile.canary(),
        ]
        for secret in secrets:
            self.assertNotIn(secret, joined)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._deploy(), [])

    def test_advanced_notes_are_optional(self) -> None:
        for name in ("provenance.md", "limits.md", "rollback.md", "quota.md"):
            (self.work / name).unlink()
        self.assertEqual(self._deploy(), [])

    def test_shell_admit_accepts_root_and_the_log(self) -> None:
        shutil.copy(W2D4_APP / "admit.py", self.work / "app" / "admit.py")
        problems = self._deploy()
        self.assertEqual(problems, ["the image runs as root", "a national id is in the deploy log"])
        self._hidden(problems)

    def test_shell_health_misses_the_hash(self) -> None:
        shutil.copy(W2D4_APP / "health.py", self.work / "app" / "health.py")
        problems = self._deploy()
        self.assertEqual(problems, ["the health probe does not report the registered hash"])
        self._hidden(problems)

    def test_shell_router_leaves_the_private_endpoint(self) -> None:
        shutil.copy(W2D4_APP / "router.py", self.work / "app" / "router.py")
        problems = self._deploy()
        self.assertEqual(problems, ["the router leaves the private endpoint"])
        self._hidden(problems)

    def test_shell_secrets_reuse_dev(self) -> None:
        shutil.copy(W2D4_APP / "secrets.py", self.work / "app" / "secrets.py")
        problems = self._deploy()
        self.assertEqual(problems, ["prod uses the dev credential"])
        self._hidden(problems)

    def test_shell_image_runs_as_root(self) -> None:
        shutil.copy(W2D4_ROOT / "deploy" / "Dockerfile", self.work / "deploy" / "Dockerfile")
        problems = self._deploy()
        self.assertEqual(problems, ["the image runs as root"])
        self._hidden(problems)

    def test_shell_manifest_is_not_in_the_namespace(self) -> None:
        shutil.copy(W2D4_ROOT / "deploy" / "deployment.yaml", self.work / "deploy" / "deployment.yaml")
        problems = self._deploy()
        self.assertEqual(
            problems,
            [
                "the manifest is not in the team namespace",
                "the health probe is missing",
                "the image runs as root",
            ],
        )
        self._hidden(problems)

    def test_shell_pipeline_is_not_in_ci(self) -> None:
        shutil.copy(W2D4_ROOT / ".github" / "workflows" / "ci.yml", self.work / ".github" / "workflows" / "ci.yml")
        problems = self._deploy()
        self.assertEqual(problems, ["the pipeline is not in CI"])
        self._hidden(problems)

    def test_blank_note_misses_the_fact(self) -> None:
        shutil.copy(W2D4_ROOT / "templates" / "deployment.md", self.work / "deployment.md")
        problems = self._deploy()
        self.assertEqual(
            problems,
            [
                "the deployment note does not leave urgency with a clinician",
                "the deployment note does not keep patient data off the external model",
                "the deployment note is missing a required fact",
                "the deployment note does not cite a source",
            ],
        )
        self._hidden(problems)

    def test_blank_zone_row(self) -> None:
        shutil.copy(W2D4_ROOT / "templates" / "zones.md", self.work / "zones.md")
        problems = self._deploy()
        self.assertEqual(problems, ["the url is not in zone-private"])
        self._hidden(problems)

    def test_blank_operator_steps(self) -> None:
        shutil.copy(W2D4_ROOT / "templates" / "operators.md", self.work / "operators.md")
        problems = self._deploy()
        self.assertEqual(problems, ["the operator steps are missing"])
        self._hidden(problems)

    def test_blank_sprint(self) -> None:
        shutil.copy(W2D4_ROOT / "templates" / "sprint.md", self.work / "sprint.md")
        problems = self._deploy()
        self.assertEqual(problems, ["sprint.md does not book the readout after the deploy"])
        self._hidden(problems)

    def test_knowledge_needs_two_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n", encoding="utf-8")
        problems = self._deploy()
        self.assertEqual(problems, ["knowledge.md needs two answers"])
        self._hidden(problems)

    def test_banned_sentence_is_not_echoed(self) -> None:
        text = (self.work / "deployment.md").read_text(encoding="utf-8")
        text += "\nThe container runs as root.\n"
        (self.work / "deployment.md").write_text(text, encoding="utf-8")
        problems = self._deploy()
        self.assertEqual(problems, ["the deployment note contains a banned sentence"])
        self._hidden(problems)

    def test_copied_log_is_not_echoed(self) -> None:
        shutil.copy(self.pack / "fixtures" / "log.json", self.work / "log.json")
        problems = self._deploy()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])
        self._hidden(problems)


if __name__ == "__main__":
    unittest.main()
