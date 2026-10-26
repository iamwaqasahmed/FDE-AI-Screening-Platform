"""Day 1 of Week 2 auth and status checks.

Guards the sign-in checker and the status-journey checker, then opens both pages
on a local server.

The fixture is this day's pack plus a copy of the filled work tree. The filled
copy must pass. Swapping in the unfinished client must fail the journey without
naming the removed field, and must leave sign-in green. A copied scenario must
fail as a watermark without echoing it. A knowledge page with one thin answer
must fail without revealing the booking assurance level. The server test signs
in as both roles and rejects a chat with no session.
"""

from __future__ import annotations

import json
import shutil
import threading
import tempfile
import unittest
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.auth import auth_problems
from alwaha.check.journey import journey_problems
from alwaha.config.profile import load
from alwaha.engagement.w2d1 import CLINIC, REMOVED, gold
from alwaha.paths import W2D1_APP, W2D1_WORK
from alwaha.release.w2d1 import write_w2d1


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts the unfinished client, echoes a hidden field, or
    serves a page to someone who has not signed in.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree into a scratch folder.

        Cached bytecode, the session database, and a leftover trace are not copied, so
        the server test starts clean. The gold file must match the generator for this
        profile.
        """
        # A temporary pack for the small profile, and the gold the release wrote.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w2d1(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w2d1_gold.json").read_text(encoding="utf-8"))
        # The filled work tree, without caches, the session database, or a leftover trace.
        self.work = root / "work"
        shutil.copytree(
            W2D1_WORK,
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "sessions.db", "trace.json"),
        )
        # The written gold must match the generator before a later assertion runs.
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces an auth problem or a journey problem."""
        canary = self.profile.canary()
        self.assertEqual(auth_problems(self.work, self.pack, self.gold, canary), [])
        self.assertEqual(journey_problems(self.work, self.pack, self.gold, canary), [])

    def test_v1_client_fails_without_naming_the_field(self) -> None:
        """Fails when the unfinished client is accepted, when the problem names the removed
        field or the clinic or the hidden count, or when sign-in starts failing too.
        """
        shutil.copy(W2D1_APP / "client.py", self.work / "app" / "client.py")
        problems = journey_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertIn("his-wadi read failed", problems)
        joined = "\n".join(problems)
        self.assertNotIn(REMOVED, joined)
        self.assertNotIn(CLINIC, joined)
        self.assertNotIn(str(self.gold["status"]["count"]), joined)
        self.assertEqual(auth_problems(self.work, self.pack, self.gold, self.profile.canary()), [])

    def test_watermark_is_not_echoed(self) -> None:
        """Fails when a copied scenario file is ignored, or when the problem text contains
        the watermark.
        """
        shutil.copy(self.pack / "scenarios" / "status.json", self.work / "status.json")
        problems = auth_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when a one-line knowledge page is accepted, or when the problem reveals
        the booking assurance level.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Soon.\n", encoding="utf-8")
        problems = journey_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertIn("knowledge.md needs two answers", problems)
        self.assertNotIn(self.gold["booking_loa"], "\n".join(problems))

    def test_server_opens_both_uis(self) -> None:
        """Fails when the filled server cannot be imported from the scratch work tree or
        does not serve both signed-in pages.

        The modules are loaded from that tree and then removed, so a later test does
        not keep the scratch copies.
        """
        # Load the filled server from the scratch work tree, not from a module already imported.
        import importlib

        folder = str((self.work / "app").resolve())
        import sys

        sys.path.insert(0, folder)
        # Drop any earlier copies of these names so the import reads the scratch tree.
        for name in ("generate", "session", "auth", "client", "his", "contract", "chat", "console", "flow", "server"):
            sys.modules.pop(name, None)
        try:
            server = importlib.import_module("server")
            db_path = self.work / "sessions.db"
            # Serve on a free local port, then open both signed-in pages.
            httpd = server.serve(self.pack, db_path, "127.0.0.1", 0)
            thread = threading.Thread(target=httpd.serve_forever, daemon=True)
            thread.start()
            port = httpd.server_address[1]
            try:
                self._pages(port)
            finally:
                # Stop the server even if a page check fails, and close its database.
                httpd.shutdown()
                thread.join(timeout=5)
                httpd.server_close()
                if server.Handler.database_connection is not None:
                    server.Handler.database_connection.close()
                    server.Handler.database_connection = None
        finally:
            # Take the scratch tree off the path and drop the modules it loaded.
            sys.path.remove(folder)
            for name in ("generate", "session", "auth", "client", "his", "contract", "chat", "console", "flow", "server"):
                sys.modules.pop(name, None)

    def _pages(self, port: int) -> None:
        """Fails when health does not name the local model, when either signed-in role
        misses its page, when the watermark appears on the patient page, or when chat
        opens with no session.
        """
        base = f"http://127.0.0.1:{port}"
        # Health must name the local model.
        with urllib.request.urlopen(base + "/v1/health") as response:
            health = json.loads(response.read().decode())
        self.assertEqual(health["model_hash"], "local-small")
        # The patient page is signed in and does not show the watermark.
        patient = self._signed_in(base, "patient")
        self.assertIn("Patient chat", patient)
        self.assertNotIn(self.profile.canary(), patient)
        # The coordinator page is the staff console. Chat with no session is refused.
        coordinator = self._signed_in(base, "coordinator")
        self.assertIn("Staff console", coordinator)
        try:
            urllib.request.urlopen(base + "/chat")
        except urllib.error.HTTPError as error:
            self.assertEqual(error.code, 401)
            error.close()
        else:
            self.fail("chat opened without a session")

    def _signed_in(self, base: str, actor: str) -> str:
        """Sign in as one actor and return the page body.

        The cookie jar is local to the call, so the patient session cannot leak into
        the coordinator session.
        """
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        data = urllib.parse.urlencode({"actor": actor}).encode()
        with opener.open(base + "/sign-in", data=data) as response:
            return response.read().decode()


if __name__ == "__main__":
    unittest.main()
