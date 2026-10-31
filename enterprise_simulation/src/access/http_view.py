"""Read-only HTTP view of the student extracts. It does not load sealed promises."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from access.paths import student_pack
from access.round2.query import by_ref


def handler_for(root: Path):
    pack = student_pack(root)

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            if self.path in ("/", "/health"):
                body = b'{"status":"up"}'
            elif self.path == "/extracts":
                body = json.dumps(_bundle(pack)).encode("utf-8")
            elif self.path.startswith("/extracts/"):
                name = self.path.removeprefix("/extracts/").split("?", 1)[0]
                bundle = _bundle(pack)
                if name not in bundle:
                    self.send_response(404)
                    self.end_headers()
                    return
                body = json.dumps(bundle[name]).encode("utf-8")
            elif self.path.startswith("/ref/"):
                ref = self.path.removeprefix("/ref/").split("?", 1)[0]
                body = json.dumps(by_ref(_bundle(pack), ref)).encode("utf-8")
            else:
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt: str, *args) -> None:
            return

    return Handler


def _bundle(pack: Path) -> dict:
    extracts = pack / "extracts"
    return {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(extracts.glob("*.json"))
    }


def serve(root: Path, port: int) -> ThreadingHTTPServer:
    server = ThreadingHTTPServer(("127.0.0.1", port), handler_for(root))
    return server
