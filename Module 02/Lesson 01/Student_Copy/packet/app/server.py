"""Patient chat and staff console on one process.

Chapter 07 starts this process and opens the home page. Chat and the
staff console are routes on this process. compose.yaml is the laptop
stand-in for that shape. deploy/namespace.yaml names the same two
routes. A live cluster deploy is a later day. Leave this file unchanged.
"""

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
    """One request handler for health, the two pages, sign-in, and chat.

    loaded is the pack flow.load_pack returned. db_path is the session
    database. database_connection is opened on the first request and
    reused. log_message is silent so a waiting server prints nothing.
    """

    # serve fills these before the first request. The connection opens later.
    loaded: dict = {}
    db_path: Path = Path("sessions.db")
    database_connection = None

    def database(self):
        """Open the session database once, then return the same connection."""
        if self.database_connection is None:
            Handler.database_connection = session.connect(self.db_path)
        return self.database_connection

    def do_GET(self) -> None:
        """Serve health, the home page, the chat, and the console.

        /health and /v1/health return contract.health. / is the sign-in
        page. /chat requires a patient session. /console requires a
        coordinator session. Anything else is 404. A missing session
        is 401 and the body is Sign in.
        """
        # Both health paths return the contract body.
        if self.path in {"/health", "/v1/health"}:
            self._json(contract.health())
            return
        # Home is the sign-in page. No session is required.
        if self.path == "/":
            self._html(chat.home())
            return
        # Chat is only for a patient session. Anyone else is asked to sign in.
        if self.path == "/chat":
            stored = self._stored()
            if stored is None or stored["role"] != "patient":
                self._text(401, "Sign in")
                return
            self._html(chat.render(stored))
            return
        # Console is only for a coordinator session.
        if self.path == "/console":
            stored = self._stored()
            if stored is None or stored["role"] != "coordinator":
                self._text(401, "Sign in")
                return
            self._html(console.render(stored))
            return
        # Any other path is missing.
        self._text(404, "Not found")

    def do_POST(self) -> None:
        """Sign in, hold an approval, or answer a chat message.

        /sign-in reads the actor button. /v1/approvals/ holds the id
        for a later day. /v1/chat accepts JSON or a form. A form with
        no cookie is 401. Other paths are 404.
        """
        # Read the body once. The path decides what it means.
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        # The actor button signs in.
        if self.path == "/sign-in":
            self._sign_in(parse_qs(raw.decode()))
            return
        # An approval path holds that id for a later day.
        if self.path.startswith("/v1/approvals/"):
            self._json(contract.approval(self.path.rsplit("/", 1)[-1]))
            return
        # Chat is the only other post this process accepts.
        if self.path != "/v1/chat":
            self._text(404, "Not found")
            return
        # JSON carries the message, and maybe a session id.
        if "application/json" in self.headers.get("Content-Type", ""):
            payload = json.loads(raw.decode() or "{}")
            message = str(payload.get("message", ""))
            session_id = str(payload.get("session", "")) or self._session_id()
            self._json(self._answer(session_id, message))
            return
        # A form needs the session cookie. The answer is drawn back on the chat page.
        message = parse_qs(raw.decode()).get("message", [""])[0]
        stored = self._stored()
        if stored is None:
            self._text(401, "Sign in")
            return
        self._html(chat.render(stored, self._answer(stored["session_id"], message)))

    def log_message(self, format: str, *args: object) -> None:
        """Stay quiet. A running server looks idle until you stop it."""
        return

    def _sign_in(self, form: dict) -> None:
        """Look up the actor, write the session, and redirect to the page.

        An unknown actor, or a token auth.py refuses, is 403 Refused.
        A patient is sent to /chat. Anyone else who was accepted is
        sent to /console. The cookie is alwaha_session and its value
        is the token subject. The browser follows the redirect.
        """
        # The button names an actor. An unknown name is refused.
        actor = form.get("actor", [""])[0]
        token = self.loaded["actors"].get(actor)
        if token is None:
            self._text(403, "Refused")
            return
        # A token that auth refuses is also refused. Nothing is stored.
        result = flow.sign_in(self.database(), token, self.loaded["note"])
        if not result["ok"]:
            self._text(403, "Refused")
            return
        # Send the browser to chat or console, and set the session cookie to the subject.
        location = "/chat" if result["page"] == "chat" else "/console"
        host = self.headers.get("Host", "")
        target = f"http://{host}{location}" if host else location
        self.send_response(302)
        self.send_header("Set-Cookie", f"alwaha_session={token['sub']}")
        self.send_header("Location", target)
        self.end_headers()

    def _answer(self, session_id: str, message: str) -> dict:
        """Answer as the patient, or refuse the read when the role is not patient.

        A missing session or a staff session still gets a reply object,
        with the read marked failed. A patient session calls
        flow.status_answer, which reads his-wadi and then the status tool.
        """
        stored = self._by_id(session_id)
        if stored is None or stored["role"] != "patient":
            return contract.reply(message, self.loaded["row"], False)
        return flow.status_answer(self.loaded["spec"], self.loaded["row"], message)

    def _stored(self) -> dict | None:
        """Return the session row for the cookie, or None."""
        return self._by_id(self._session_id())

    def _by_id(self, session_id: str) -> dict | None:
        """Find one session row by its session id.

        An empty id returns nothing, and any other id is compared with
        each stored row until one matches.
        """
        if not session_id:
            return None
        # Keep the first row whose session id matches.
        for row in session.rows(self.database()):
            if row["session_id"] == session_id:
                return row
        return None

    def _session_id(self) -> str:
        """Read alwaha_session from the Cookie header, or return an empty string.

        The header is split on semicolons, and each piece is split at
        the first equals sign.
        """
        for part in self.headers.get("Cookie", "").split(";"):
            # The first equals sign separates the cookie name from its value.
            name, _, value = part.strip().partition("=")
            if name == "alwaha_session":
                return value
        return ""

    def _json(self, payload: dict) -> None:
        """Send a JSON body with status 200.

        The payload is encoded to bytes, that size is the length header,
        and those bytes are written after the headers.
        """
        # Count the encoded payload so the length header matches the body.
        body = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _html(self, text: str) -> None:
        """Send an HTML body with status 200.

        The page is encoded to bytes, that size is the length header,
        and those bytes are written after the headers.
        """
        # Count the encoded page so the length header matches the body.
        body = text.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _text(self, status: int, text: str) -> None:
        """Send a short plain-text error. status is 401, 403, or 404.

        The message is encoded to bytes, the given status is sent, and
        that size is the length header.
        """
        # Count the encoded message so the length header matches the body.
        body = text.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def serve(pack: Path, db_path: Path, host: str, port: int) -> HTTPServer:
    """Load the pack, point the handler at the database, and bind the port.

    The checks call this with port 0 so the operating system picks a
    free port. Chapter 07 uses the default port on the command line.
    """
    Handler.loaded = flow.load_pack(pack)
    Handler.db_path = db_path
    Handler.database_connection = None
    return HTTPServer((host, port), Handler)


def main(argv: list[str] | None = None) -> None:
    """Serve until the terminal is stopped.

    --pack is required. --db defaults to sessions.db in the current
    folder, so chapter 07 passes a path under work/. --host defaults
    to every interface. --port defaults to 8080. This call does not
    return. Ctrl+C stops it.
    """
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
