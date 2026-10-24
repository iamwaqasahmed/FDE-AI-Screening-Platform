"""Patient chat and staff console on one process."""

from __future__ import annotations

import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

import chat
import console
import contract
import flow
import session


class Handler(BaseHTTPRequestHandler):
    loaded: dict = {}
    db_path: Path = Path("sessions.db")
    database_connection = None

    def database(self):
        if self.database_connection is None:
            Handler.database_connection = session.connect(self.db_path)
        return self.database_connection

    def do_GET(self) -> None:
        if self.path in {"/health", "/v1/health"}:
            self._json(contract.health())
            return
        if self.path == "/":
            self._html(chat.home())
            return
        if self.path == "/chat":
            stored = self._stored()
            if stored is None or stored["role"] != "patient":
                self._text(401, "Sign in")
                return
            self._html(chat.render(stored))
            return
        if self.path == "/console":
            stored = self._stored()
            if stored is None or stored["role"] != "coordinator":
                self._text(401, "Sign in")
                return
            self._html(console.render(stored))
            return
        self._text(404, "Not found")

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        if self.path == "/sign-in":
            self._sign_in(parse_qs(raw.decode()))
            return
        if self.path.startswith("/v1/approvals/"):
            self._json(contract.approval(self.path.rsplit("/", 1)[-1]))
            return
        if self.path != "/v1/chat":
            self._text(404, "Not found")
            return
        if "application/json" in self.headers.get("Content-Type", ""):
            payload = json.loads(raw.decode() or "{}")
            message = str(payload.get("message", ""))
            session_id = str(payload.get("session", "")) or self._session_id()
            self._json(self._answer(session_id, message))
            return
        message = parse_qs(raw.decode()).get("message", [""])[0]
        stored = self._stored()
        if stored is None:
            self._text(401, "Sign in")
            return
        self._html(chat.render(stored, self._answer(stored["session_id"], message)))

    def log_message(self, format: str, *args: object) -> None:
        return

    def _sign_in(self, form: dict) -> None:
        actor = form.get("actor", [""])[0]
        token = self.loaded["actors"].get(actor)
        if token is None:
            self._text(403, "Refused")
            return
        result = flow.sign_in(self.database(), token, self.loaded["note"])
        if not result["ok"]:
            self._text(403, "Refused")
            return
        location = "/chat" if result["page"] == "chat" else "/console"
        host = self.headers.get("Host", "")
        target = f"http://{host}{location}" if host else location
        self.send_response(302)
        self.send_header("Set-Cookie", f"alwaha_session={token['sub']}")
        self.send_header("Location", target)
        self.end_headers()

    def _answer(self, session_id: str, message: str) -> dict:
        stored = self._by_id(session_id)
        if stored is None or stored["role"] != "patient":
            return contract.reply(message, self.loaded["row"], False)
        return flow.status_answer(self.loaded["spec"], self.loaded["row"], message)

    def _stored(self) -> dict | None:
        return self._by_id(self._session_id())

    def _by_id(self, session_id: str) -> dict | None:
        if not session_id:
            return None
        for row in session.rows(self.database()):
            if row["session_id"] == session_id:
                return row
        return None

    def _session_id(self) -> str:
        for part in self.headers.get("Cookie", "").split(";"):
            name, _, value = part.strip().partition("=")
            if name == "alwaha_session":
                return value
        return ""

    def _json(self, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _html(self, text: str) -> None:
        body = text.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _text(self, status: int, text: str) -> None:
        body = text.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def serve(pack: Path, db_path: Path, host: str, port: int) -> HTTPServer:
    Handler.loaded = flow.load_pack(pack)
    Handler.db_path = db_path
    Handler.database_connection = None
    return HTTPServer((host, port), Handler)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Serve the patient chat and the staff console.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--db", default="sessions.db")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args(argv)
    server = serve(Path(args.pack), Path(args.db), args.host, args.port)
    server.serve_forever()


if __name__ == "__main__":
    main(sys.argv[1:])
