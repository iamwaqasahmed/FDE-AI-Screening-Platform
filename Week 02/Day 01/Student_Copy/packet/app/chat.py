"""Patient chat page.

The home page offers two buttons. The patient button leads to this
chat. A stored row whose role is not patient gets an empty string,
so the coordinator does not see this page. The auth check looks for
the heading Patient chat on the patient page, and it checks that the
coordinator does not get this page.
"""

from __future__ import annotations


def _escape(text: str) -> str:
    """Replace the three HTML characters so a reply cannot break the page.

    The status reply is plain text. This only makes it safe to place
    inside a paragraph. It is not a filter on what the patient asked.
    """
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def home() -> str:
    """Return the sign-in page at /.

    Two forms post to /sign-in. The button values are the actor names
    in the identity spec: patient and coordinator. Chapter 07 opens
    this page in a browser after the server starts.
    """
    return """<!DOCTYPE html>
<html lang="en">
<head><title>Patient Access Assistant</title></head>
<body>
<h1>Patient Access Assistant</h1>
<form method="post" action="/sign-in">
<button name="actor" value="patient" type="submit">Patient sign-in</button>
</form>
<form method="post" action="/sign-in">
<button name="actor" value="coordinator" type="submit">Coordinator sign-in</button>
</form>
</body>
</html>
"""


def render(stored: dict, answer: dict | None = None) -> str:
    """Return the patient chat, or an empty string for anyone else.

    The heading is Patient chat. The line under it says you are signed
    in. When answer carries a reply, that reply is a paragraph. When
    the reply also carries a count, a second paragraph shows it. The
    form posts the next message to /v1/chat.
    """
    if stored.get("role") != "patient":
        return ""
    extra = ""
    if answer and answer.get("reply"):
        extra = f"<p>{_escape(str(answer['reply']))}</p>"
        if answer.get("count") is not None:
            extra += f"<p>Count: {_escape(str(answer['count']))}</p>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head><title>Patient chat</title></head>
<body>
<h1>Patient chat</h1>
<p>You are signed in.</p>
{extra}
<form method="post" action="/v1/chat">
<label>Message <input name="message"></label>
<button type="submit">Send</button>
</form>
</body>
</html>
"""
