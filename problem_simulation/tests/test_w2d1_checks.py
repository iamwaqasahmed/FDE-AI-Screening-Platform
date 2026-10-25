"""Day 1 of Week 2 auth and status checks."""

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
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w2d1(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w2d1_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(
            W2D1_WORK,
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "sessions.db", "trace.json"),
        )
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_filled_work_passes(self) -> None:
        canary = self.profile.canary()
        self.assertEqual(auth_problems(self.work, self.pack, self.gold, canary), [])
        self.assertEqual(journey_problems(self.work, self.pack, self.gold, canary), [])

    def test_v1_client_fails_without_naming_the_field(self) -> None:
        shutil.copy(W2D1_APP / "client.py", self.work / "app" / "client.py")
        problems = journey_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertIn("his-wadi read failed", problems)
        joined = "\n".join(problems)
        self.assertNotIn(REMOVED, joined)
        self.assertNotIn(CLINIC, joined)
        self.assertNotIn(str(self.gold["status"]["count"]), joined)
        self.assertEqual(auth_problems(self.work, self.pack, self.gold, self.profile.canary()), [])

    def test_watermark_is_not_echoed(self) -> None:
        shutil.copy(self.pack / "scenarios" / "status.json", self.work / "status.json")
        problems = auth_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Soon.\n", encoding="utf-8")
        problems = journey_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertIn("knowledge.md needs two answers", problems)
        self.assertNotIn(self.gold["booking_loa"], "\n".join(problems))

    def test_server_opens_both_uis(self) -> None:
        import importlib

        folder = str((self.work / "app").resolve())
        import sys

        sys.path.insert(0, folder)
        for name in ("generate", "session", "auth", "client", "his", "contract", "chat", "console", "flow", "server"):
            sys.modules.pop(name, None)
        try:
            server = importlib.import_module("server")
            db_path = self.work / "sessions.db"
            httpd = server.serve(self.pack, db_path, "127.0.0.1", 0)
            thread = threading.Thread(target=httpd.serve_forever, daemon=True)
            thread.start()
            port = httpd.server_address[1]
            try:
                self._pages(port)
            finally:
                httpd.shutdown()
                thread.join(timeout=5)
                httpd.server_close()
                if server.Handler.database_connection is not None:
                    server.Handler.database_connection.close()
                    server.Handler.database_connection = None
        finally:
            sys.path.remove(folder)
            for name in ("generate", "session", "auth", "client", "his", "contract", "chat", "console", "flow", "server"):
                sys.modules.pop(name, None)

    def _pages(self, port: int) -> None:
        base = f"http://127.0.0.1:{port}"
        with urllib.request.urlopen(base + "/v1/health") as response:
            health = json.loads(response.read().decode())
        self.assertEqual(health["model_hash"], "local-small")
        patient = self._signed_in(base, "patient")
        self.assertIn("Patient chat", patient)
        self.assertNotIn(self.profile.canary(), patient)
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
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        data = urllib.parse.urlencode({"actor": actor}).encode()
        with opener.open(base + "/sign-in", data=data) as response:
            return response.read().decode()


if __name__ == "__main__":
    unittest.main()
