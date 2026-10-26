"""Stateful mocks over HTTP, including the gateway and the poisoned maps tool.

Guards the stateful tool server: the record read, the hold, the schedule queue,
the gateway refusal, the poisoned maps description, and a real listening socket.

The fixture is the small profile and a fresh in-memory state. One test drives
the dispatcher directly. The other binds a local server and posts a record read
through it, so a handler that only works in-process still fails.
"""

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
    """Catches a mock that accepts a bad write, a gateway that lets a prompt through,
    or a server that cannot serve the record read.
    """
    def setUp(self) -> None:
        """Load the small profile and a new state object.

        The listening test builds its own state so the two cases do not share bookings.
        """
        self.profile = load("small")
        self.state = State(self.profile)

    def test_fhir_hold_gateway_and_maps(self) -> None:
        """Fails when a plain record read is rejected, when a coded clinic write is
        accepted, when a booking is not queued, or when the gateway allows an identity
        or the watermark through. Also fails when a killed pod still serves the first
        site, when the maps tool is not the poisoned description, or when an expired
        caregiver grant looks fresh.
        """
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
        """Fails when a local server cannot accept the same record read the dispatcher
        accepts. The server is shut down even if the read fails.
        """
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
