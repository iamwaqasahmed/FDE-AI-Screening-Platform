"""HTTP surface for the assistant contract. python -m reference.server.

GET and POST share one handler. A missing body becomes an empty object so the health and metrics routes still dispatch. The route table maps health, metrics, chat, and approvals. The approval id is the last path segment. Anything else is a not-found payload. The access log is silenced so a readiness run does not mix server lines into its output.
"""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from reference.assistant import Store, approve, chat, health, metrics

STORE = Store()


def make_handler(store: Store):
    """Return a request handler class bound to this store."""

    class Handler(BaseHTTPRequestHandler):
        """Handle one request by reading a JSON body and writing a JSON response."""

        def do_GET(self) -> None:
            """Dispatch a GET through the same body reader as POST."""
            self._reply()

        def do_POST(self) -> None:
            """Dispatch a POST through the shared body reader."""
            self._reply()

        def log_message(self, _format: str, *_args) -> None:
            """Drop the default access log so server noise stays out of the process output."""
            return

        def _reply(self) -> None:
            """Read a JSON body, route it, and write the status and payload."""
            length = int(self.headers.get("Content-Length", "0"))
            # No content length means there is nothing to read. An empty object still parses.
            raw = self.rfile.read(length) if length else b"{}"
            body = json.loads(raw.decode("utf-8") or "{}")
            status, payload = _route(store, self.command, self.path.split("?", 1)[0], body)
            encoded = json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

    return Handler


def _route(store: Store, method: str, path: str, body: dict) -> tuple[int, dict]:
    """Return the status and payload for this method and path."""
    if method == "GET" and path == "/v1/health":
        return 200, health()
    if method == "GET" and path == "/v1/metrics":
        return 200, metrics(store)
    if method == "POST" and path == "/v1/chat":
        return 200, chat(store, body)
    if method == "POST" and path.startswith("/v1/approvals/"):
        # The approval id is the last segment, so the route prefix can stay fixed.
        return 200, approve(store, path.rsplit("/", 1)[-1])
    return 404, {"ok": False}


def serve(port: int) -> None:
    """Serve the shared store on all interfaces at this port until the process stops."""
    ThreadingHTTPServer(("0.0.0.0", port), make_handler(STORE)).serve_forever()


def main(argv: list[str] | None = None) -> None:
    """Parse the port and serve. The default port is the one the contract uses.

    The steps parse the port argument and serve the shared store on that port until the process stops.
    """
    parser = argparse.ArgumentParser(description="Serve the reference assistant.")
    parser.add_argument("--port", type=int, default=8081)
    args = parser.parse_args(argv)
    serve(args.port)


if __name__ == "__main__":
    main()
