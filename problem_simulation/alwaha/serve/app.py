"""Stdlib HTTP server for the seeded mocks. python -m alwaha.serve."""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from alwaha.config.profile import load
from alwaha.serve.http_dispatch import dispatch
from alwaha.serve.http_state import State


def make_handler(state: State):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            self._reply()

        def do_POST(self) -> None:
            self._reply()

        def log_message(self, _format: str, *_args) -> None:
            return

        def _reply(self) -> None:
            parsed = urlparse(self.path)
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            body = json.loads(raw.decode("utf-8") or "{}")
            query = {key: values[-1] for key, values in parse_qs(parsed.query).items()}
            status, payload = dispatch(state, self.command, parsed.path, body, query)
            encoded = json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

    return Handler


def serve(profile, port: int) -> None:
    state = State(profile)
    server = ThreadingHTTPServer(("0.0.0.0", port), make_handler(state))
    server.serve_forever()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Serve the Al-Waha mocks.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args(argv)
    serve(load(args.profile), args.port)


if __name__ == "__main__":
    main()
