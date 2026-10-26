"""Stdlib HTTP server for the seeded mocks. python -m alwaha.serve.

make_handler() builds a request class closed over one State. GET and POST share one reply path, and the route table decides the response. An empty body is read as an empty JSON object. Repeated query keys keep the last value. serve() listens on all interfaces and blocks. main() loads the profile and starts that loop.
"""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from alwaha.config.profile import load
from alwaha.serve.http_dispatch import dispatch
from alwaha.serve.http_state import State


def make_handler(state: State):
    """Return a request-handler class bound to this in-memory world.

    Every request on the server shares the same State.
    """

    class Handler(BaseHTTPRequestHandler):
        """Dispatch GET and POST through one reply path, and stay quiet in the log."""

        def do_GET(self) -> None:
            """Handle GET by the shared reply path. Returns nothing."""
            self._reply()

        def do_POST(self) -> None:
            """Handle POST by the shared reply path. Returns nothing."""
            self._reply()

        def log_message(self, _format: str, *_args) -> None:
            """Drop the default access log. Returns nothing.

            The mock stays quiet so a scenario's own output is the only text.
            """
            return

        def _reply(self) -> None:
            """Read the request, dispatch it, and write a JSON response. Returns nothing.

            A missing body becomes an empty JSON object so GET still parses. Repeated query keys keep the last value.
            """
            parsed = urlparse(self.path)
            length = int(self.headers.get("Content-Length", "0"))
            # A missing body is an empty object, so GET still reaches the route table.
            raw = self.rfile.read(length) if length else b"{}"
            # An empty decoded body is still an empty JSON object.
            body = json.loads(raw.decode("utf-8") or "{}")
            # parse_qs returns a list per key. Handlers receive the last value as a string.
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
    """Bind the mock on all interfaces at port and serve until stopped. Returns nothing.

    One State is created from the profile and shared by every request.
    """
    state = State(profile)
    server = ThreadingHTTPServer(("0.0.0.0", port), make_handler(state))
    server.serve_forever()


def main(argv: list[str] | None = None) -> None:
    """Load the profile and serve. Returns nothing.

    argv replaces the process arguments. The profile flag selects the world, and the port flag selects the listen port.
    """
    parser = argparse.ArgumentParser(description="Serve the Al-Waha mocks.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args(argv)
    serve(load(args.profile), args.port)


if __name__ == "__main__":
    # A direct run binds the port. Importing this module does not.
    main()
