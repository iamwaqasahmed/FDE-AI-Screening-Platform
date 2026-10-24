"""Stateful mocks over HTTP, including the gateway and the poisoned maps tool."""

from __future__ import annotations

import json
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer

from alwaha.config.profile import load
from alwaha.serve.app import make_handler
from alwaha.serve.http_dispatch import dispatch
from alwaha.serve.http_mcp import POISONED
from alwaha.serve.http_state import State


class HttpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = load("small")
        self.state = State(self.profile)

    def test_fhir_hold_gateway_and_maps(self) -> None:
        ok, fhir = dispatch(self.state, "POST", "/his/wadi/fhir", {"clinic": "ENDO-CLN"}, {})
        self.assertEqual(ok, 200)
        self.assertTrue(fhir["ok"])
        blocked, _ = dispatch(self.state, "POST", "/his/wadi/fhir", {"clinic": "ENDO-CLN", "clinic_code": "END-01"}, {})
        self.assertEqual(blocked, 400)
        status, booked = dispatch(self.state, "POST", "/sched-ain/book", {"facility": "h-ain"}, {})
        self.assertEqual(status, 200)
        self.assertEqual(booked["status"], "queued")
        denied, _ = dispatch(self.state, "POST", "/gateway/complete", {"national_id": "000"}, {})
        self.assertEqual(denied, 403)
        canary, _ = dispatch(self.state, "POST", "/gateway/complete", {"prompt": self.profile.canary()}, {})
        self.assertEqual(canary, 403)
        dispatch(self.state, "POST", "/chaos/pod-kill", {}, {})
        down, body = dispatch(self.state, "POST", "/his/wadi/holds", {"site": "site-a", "slot": "s1"}, {})
        self.assertEqual(down, 503)
        self.assertEqual(body["serving"], "site-b")
        _, maps = dispatch(self.state, "POST", "/mcp/maps", {"arguments": {"origin": "phc-rim"}}, {})
        self.assertEqual(maps["tools"][0]["description"], POISONED)
        _, grant = dispatch(self.state, "GET", "/consent/grants", {}, {"actor": "caregiver-expired"})
        self.assertTrue(grant["stale"])

    def test_server_accepts_a_fhir_read(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(State(self.profile)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        host, port = server.server_address
        try:
            payload = json.dumps({"clinic": "ENDO-CLN"}).encode("utf-8")
            request = urllib.request.Request(
                f"http://{host}:{port}/his/wadi/fhir",
                data=payload,
                method="POST",
            )
            with urllib.request.urlopen(request) as response:
                body = json.loads(response.read().decode("utf-8"))
            self.assertTrue(body["ok"])
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
