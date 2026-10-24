"""Patient Access Assistant, Day 1 skeleton. The health route is the whole service."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def health() -> dict:
    return {"status": "ok", "service": "patient-access-assistant"}


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return
        body = json.dumps(health()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    HTTPServer(("0.0.0.0", 8080), _Handler).serve_forever()


if __name__ == "__main__":
    main()
