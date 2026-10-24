"""HTTP surface for the assistant contract. python -m reference.server."""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from reference.assistant import Store, approve, chat, health, metrics

STORE = Store()


def make_handler(store: Store):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            self._reply()

        def do_POST(self) -> None:
            self._reply()

        def log_message(self, _format: str, *_args) -> None:
            return

        def _reply(self) -> None:
            length = int(self.headers.get("Content-Length", "0"))
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
    if method == "GET" and path == "/v1/health":
        return 200, health()
    if method == "GET" and path == "/v1/metrics":
        return 200, metrics(store)
    if method == "POST" and path == "/v1/chat":
        return 200, chat(store, body)
    if method == "POST" and path.startswith("/v1/approvals/"):
        return 200, approve(store, path.rsplit("/", 1)[-1])
    return 404, {"ok": False}


def serve(port: int) -> None:
    ThreadingHTTPServer(("0.0.0.0", port), make_handler(STORE)).serve_forever()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Serve the reference assistant.")
    parser.add_argument("--port", type=int, default=8081)
    args = parser.parse_args(argv)
    serve(args.port)


if __name__ == "__main__":
    main()
