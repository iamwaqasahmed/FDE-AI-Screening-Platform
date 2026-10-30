"""Patient Access Assistant, Lesson 1 skeleton.

Today the whole service is one address: GET /health. It answers that the
process is up. Later days add the assistant. You do not need to change
this file to finish today, and you do not need to start the server.
The health function below is what the test calls.
"""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def health() -> dict:
    """Return the body a healthy process sends.

    status says the process is up. service names which process this is,
    so a later check can tell this assistant from some other service on
    the same machine.
    """
    return {"status": "ok", "service": "patient-access-assistant"}


class _Handler(BaseHTTPRequestHandler):
    """Answer HTTP requests. Only GET /health is a successful answer."""

    def do_GET(self) -> None:
        """Handle one GET. Any path other than /health is a 404."""
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return
        # JSON text, then bytes, because the socket writes bytes.
        body = json.dumps(health()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        """Silence the default request log.

        The library would print every request to the terminal. This
        service stays quiet so a later test can read its own output.
        """
        return


def main() -> None:
    """Listen on port 8080 on every network interface. Not used today."""
    # 0.0.0.0 means "accept connections on this machine's addresses."
    # Chapter 07 leaves this process unstarted. Docker would run it later.
    HTTPServer(("0.0.0.0", 8080), _Handler).serve_forever()


if __name__ == "__main__":
    main()
