"""Module 2, Lesson 4 deploy check.

Guards the deploy checker.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass, including after the optional notes are removed. Each shell swap restores
one unfinished piece: admit, health, the router, secrets, the image, the
manifest, or the pipeline. Blank templates must fail for the deployment note,
the zone row, the operator steps, and the sprint. A banned sentence and a
copied log must fail without echoing secrets.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.deploy_m02 import deploy_problems
from alwaha.config.profile import load
from alwaha.engagement.m02_l04 import gold
from alwaha.paths import M02_L04_APP, M02_L04_DEPLOY, M02_L04_ROOT, M02_L04_TEMPLATES, M02_L04_WORK
from alwaha.release.m02_l04 import write_m02_l04


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts a privileged image, a shared credential, a public
    route, or a note that lost a required fact.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree.

        The gold file must match the generator before any shell file is copied back.
        """
        # A temporary pack for the small profile, and the gold the release wrote.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_m02_l04(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "m02_l04_gold.json").read_text(encoding="utf-8"))
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(
            M02_L04_WORK,
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        # The written gold must match the generator before any shell file is copied back.
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _deploy(self) -> list[str]:
        """Run the deploy checker on the scratch work tree."""
        return deploy_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes a hash, a token, the national id,
        the quota, or the watermark.
        """
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
        """Fails when the filled work tree still produces a deploy problem."""
        self.assertEqual(self._deploy(), [])

    def test_advanced_notes_are_optional(self) -> None:
        """Fails when deleting the provenance, limits, rollback, or quota notes makes a
        passing tree fail. Those notes are not part of the required grade.
        """
        for name in ("provenance.md", "limits.md", "rollback.md", "quota.md"):
            (self.work / name).unlink()
        self.assertEqual(self._deploy(), [])

    def test_shell_admit_accepts_root_and_the_log(self) -> None:
        """Fails when the unfinished admit path is accepted. It keeps a privileged user
        and leaves a national id in the deploy log.
        """
        shutil.copy(M02_L04_APP / "admit.py", self.work / "app" / "admit.py")
        problems = self._deploy()
        self.assertEqual(problems, ["the image runs as root", "a national id is in the deploy log"])
        self._hidden(problems)

    def test_shell_health_misses_the_hash(self) -> None:
        """Fails when a health probe that does not report the registered hash is accepted.

        The test copies the unfinished health probe into the work tree and fails unless the
        deploy checker names that miss, and the problem list does not echo a hidden value.
        """
        shutil.copy(M02_L04_APP / "health.py", self.work / "app" / "health.py")
        problems = self._deploy()
        self.assertEqual(problems, ["the health probe does not report the registered hash"])
        self._hidden(problems)

    def test_shell_router_leaves_the_private_endpoint(self) -> None:
        """Fails when a router that still exposes the private endpoint is accepted.

        The test copies the unfinished router into the work tree and fails unless the deploy
        checker names the private endpoint, and the problem list does not echo a hidden value.
        """
        shutil.copy(M02_L04_APP / "router.py", self.work / "app" / "router.py")
        problems = self._deploy()
        self.assertEqual(problems, ["the router leaves the private endpoint"])
        self._hidden(problems)

    def test_shell_secrets_reuse_dev(self) -> None:
        """Fails when production is allowed to reuse the dev credential.

        The test copies the unfinished secrets module into the work tree and fails unless the
        deploy checker names the reused dev credential, and the problem list does not echo a
        hidden value.
        """
        shutil.copy(M02_L04_APP / "secrets.py", self.work / "app" / "secrets.py")
        problems = self._deploy()
        self.assertEqual(problems, ["prod uses the dev credential"])
        self._hidden(problems)

    def test_shell_image_runs_as_root(self) -> None:
        """Fails when the unfinished image definition, which runs privileged, is accepted.

        The test copies the unfinished image definition into the work tree and fails unless the
        deploy checker names the privileged image, and the problem list does not echo a hidden
        value.
        """
        shutil.copy(M02_L04_DEPLOY / "Dockerfile", self.work / "deploy" / "Dockerfile")
        problems = self._deploy()
        self.assertEqual(problems, ["the image runs as root"])
        self._hidden(problems)

    def test_shell_manifest_is_not_in_the_namespace(self) -> None:
        """Fails when the unfinished manifest is accepted. It is outside the team
        namespace, has no health probe, and runs privileged.
        """
        shutil.copy(M02_L04_DEPLOY / "deployment.yaml", self.work / "deploy" / "deployment.yaml")
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
        """Fails when the pipeline step is still only in the shell workflow and the
        checker does not notice.
        """
        shell_ci = M02_L04_ROOT / "Student_Copy" / "packet" / ".github" / "workflows" / "ci.yml"
        shutil.copy(shell_ci, self.work / ".github" / "workflows" / "ci.yml")
        problems = self._deploy()
        self.assertEqual(problems, ["the pipeline is not in CI"])
        self._hidden(problems)

    def test_blank_note_misses_the_fact(self) -> None:
        """Fails when a blank deployment note is accepted. It must leave urgency with a
        clinician, keep patient data off the external model, state a required fact,
        and cite a source.
        """
        shutil.copy(M02_L04_TEMPLATES / "deployment.md", self.work / "deployment.md")
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
        """Fails when a blank zone table is accepted. The service address has to sit in
        the private zone.
        """
        shutil.copy(M02_L04_TEMPLATES / "zones.md", self.work / "zones.md")
        problems = self._deploy()
        self.assertEqual(problems, ["the url is not in zone-private"])
        self._hidden(problems)

    def test_blank_operator_steps(self) -> None:
        """Fails when blank operator steps are accepted.

        The test replaces the operator page with the blank template and fails unless the deploy
        checker says the steps are missing, and the problem list does not echo a hidden value.
        """
        shutil.copy(M02_L04_TEMPLATES / "operators.md", self.work / "operators.md")
        problems = self._deploy()
        self.assertEqual(problems, ["the operator steps are missing"])
        self._hidden(problems)

    def test_blank_sprint(self) -> None:
        """Fails when a blank sprint is accepted. The readout has to be booked after the
        deploy, not before it.
        """
        shutil.copy(M02_L04_TEMPLATES / "sprint.md", self.work / "sprint.md")
        problems = self._deploy()
        self.assertEqual(problems, ["sprint.md does not book the readout after the deploy"])
        self._hidden(problems)

    def test_knowledge_needs_two_answers(self) -> None:
        """Fails when an empty knowledge page is accepted in place of the two answers.

        The test writes an empty knowledge page and fails unless the deploy checker asks for the
        two answers, and the problem list does not echo a hidden value.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n", encoding="utf-8")
        problems = self._deploy()
        self.assertEqual(problems, ["knowledge.md needs two answers"])
        self._hidden(problems)

    def test_banned_sentence_is_not_echoed(self) -> None:
        """Fails when a banned sentence appended to the deployment note is accepted.

        The test appends a banned sentence to the deployment note and fails unless the deploy
        checker names that sentence without quoting it back, and the problem list does not echo
        a hidden value.
        """
        text = (self.work / "deployment.md").read_text(encoding="utf-8")
        text += "\nThe container runs as root.\n"
        (self.work / "deployment.md").write_text(text, encoding="utf-8")
        problems = self._deploy()
        self.assertEqual(problems, ["the deployment note contains a banned sentence"])
        self._hidden(problems)

    def test_copied_log_is_not_echoed(self) -> None:
        """Fails when a copied log fixture is ignored, or when the problem text contains
        the watermark.
        """
        shutil.copy(self.pack / "fixtures" / "log.json", self.work / "log.json")
        problems = self._deploy()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])
        self._hidden(problems)


if __name__ == "__main__":
    unittest.main()
